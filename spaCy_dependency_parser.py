import spacy
from spacy import displacy
import os
import subprocess
from collections import defaultdict
from tabulate import tabulate
import csv
from datetime import datetime


class DependencyNode:
    """Class representing a node in the dependency tree"""

    def __init__(self, token):
        self.token = token
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def build_dependency_tree(doc):
    """Build a tree structure from spaCy's dependency parse"""
    nodes = {token: DependencyNode(token) for token in doc}

    for token in doc:
        if token.head != token:  # Skip root pointing to itself
            nodes[token.head].add_child(nodes[token])

    root = [node for node in nodes.values() if node.token.head == node.token][0]
    return root


def print_tree(node, level=0):
    """Print the tree structure in text format"""
    indent = "    " * level
    print(f"{indent}{node.token.text} ({node.token.dep_})")
    for child in sorted(node.children, key=lambda x: x.token.i):
        print_tree(child, level + 1)


def visualize_dependencies(doc, output_file):
    """Visualize dependencies and save as HTML file"""
    html = displacy.render(doc, style="dep", page=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)


def load_model(language):
    """Load spaCy model with automatic download if missing"""
    models = {
        "en": "en_core_web_sm",
        "ru": "ru_core_news_sm",
        "de": "de_core_news_sm",
        "pl": "pl_core_news_sm",
        "fi": "fi_core_news_sm",
        "fr": "fr_core_news_sm",
        "es": "es_core_news_sm",
        "it": "it_core_news_sm",
        "pt": "pt_core_news_sm",
        "nl": "nl_core_news_sm",
        "zh": "zh_core_web_sm",
        "ja": "ja_core_news_sm",
        "da": "da_core_news_sm",
        "sv": "sv_core_news_sm",
    }

    model_name = models.get(language, "en_core_web_sm")

    try:
        return spacy.load(model_name)
    except OSError:
        print(f"Downloading {language} language model...")
        subprocess.run(["python", "-m", "spacy", "download", model_name])
        return spacy.load(model_name)


def read_examples_from_csv(csv_file_path):
    """
    Read examples from a CSV file with two columns:
    - first column: example number (n)
    - second column: sentence (Full context)
    Returns two lists: ids and sentences.
    """
    ids = []
    sentences = []

    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found!")
        return ids, sentences

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # Uncomment the next line if your CSV has a header row
            # next(reader, None)

            for row in reader:
                if len(row) >= 2 and row[0].strip() and row[1].strip():
                    # Try to convert n to int, keep as string if fails
                    try:
                        n = int(row[0].strip())
                    except ValueError:
                        n = row[0].strip()
                    sentence = row[1].strip()
                    ids.append(n)
                    sentences.append(sentence)

        print(f"Successfully read {len(sentences)} examples from '{csv_file_path}'")

    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return ids, sentences


def analyze_dependencies(examples, query_word, language="en"):
    """
    Analyze both incoming and outgoing dependencies for a specific word across examples.
    Uses lemma matching to catch inflected forms.
    Returns a dictionary with dependency statistics.
    """
    nlp = load_model(language)
    stats = defaultdict(lambda: {"count": 0, "examples": []})

    for sentence in examples:
        doc = nlp(sentence)
        for token in doc:
            # Match by lemma (case-insensitive) to catch all grammatical forms
            if token.lemma_.lower() == query_word.lower():
                # Outgoing dependencies (query word -> children)
                for child in token.children:
                    if child.dep_ == "punct":
                        continue
                    dep_type = f"OUT: {child.dep_}"
                    stats[dep_type]["count"] += 1
                    example = f"{token.text} → {child.text}"
                    stats[dep_type]["examples"].append(example)

                # Incoming dependencies (head -> query word)
                if token.head != token:
                    dep_type = f"IN: {token.dep_}"
                    stats[dep_type]["count"] += 1
                    # FIX: use token.head.text, not undefined 'child'
                    example = f"{token.head.text} → {token.text}"
                    stats[dep_type]["examples"].append(example)

    return dict(stats)


def print_dependency_stats(stats, query_word):
    """Print dependency statistics in a table format"""
    if not stats:
        print(f"\nNo dependencies found for '{query_word}' in the examples")
        return

    table_data = []
    for dep_type, data in sorted(stats.items()):
        examples = ", ".join(data["examples"])
        table_data.append([dep_type, data["count"], examples])

    print(f"\nDependency Statistics for '{query_word}':")
    print(tabulate(
        table_data,
        headers=["Dependency Type (Direction)", "Count", "Example Relations"],
        tablefmt="grid",
        numalign="center",
        stralign="left"
    ))

    total = sum(item["count"] for item in stats.values())
    unique = len(stats)
    print(f"\nTotal dependencies: {total} | Unique types: {unique}")


def export_combined_dependency_table_to_csv(all_dependency_data, filename):
    """Export combined dependency table data to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Example_ID', 'Sentence', 'Token', 'Direction', 'Child', 'Dependency Type'])
        for row in all_dependency_data:
            writer.writerow(row)
    print(f"Combined dependency table exported to: {filename}")


def export_dependency_stats_to_csv(stats_data, query_word, filename):
    """Export dependency statistics to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dependency Type (Direction)', 'Count', 'Example Relations'])
        for dep_type, data in sorted(stats_data.items()):
            examples = ", ".join(data["examples"])
            writer.writerow([dep_type, data["count"], examples])
    print(f"Dependency statistics for '{query_word}' exported to: {filename}")

def export_all_dependency_occurrences(ids, sentences, query_word, language, filename):
    """
    Export every dependency occurrence for the query word (no aggregation, one row per occurrence).
    Uses lemma matching.
    """
    nlp = load_model(language)
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'Sentence', 'Word', 'Direction',
                         'Related_Word', 'Dependency_Type', 'Position_Word',
                         'Position_Related', 'Is_Root'])
        for n, sentence in zip(ids, sentences):
            doc = nlp(sentence)
            for token in doc:
                if token.lemma_.lower() == query_word.lower():
                    # Outgoing
                    for child in token.children:
                        if child.dep_ == "punct":
                            continue
                        writer.writerow([n, sentence, token.text, 'OUT',
                                         child.text, child.dep_, token.i, child.i,
                                         token.head == token])   # <-- FIXED
                    # Incoming
                    if token.head != token:
                        writer.writerow([n, sentence, token.text, 'IN',
                                         token.head.text, token.dep_, token.i, token.head.i,
                                         False])   # not root by definition
    print(f"All occurrences for '{query_word}' exported to: {filename}")

def export_incoming_heads(ids, sentences, query_word, language, filename):
    """
    Export for each input example (n) a row with:
    - n: original example number
    - Head: semicolon-separated list of head words (incoming dependencies)
    - DepType: semicolon-separated list of dependency types
    If no incoming head exists for the query word in that sentence, both Head and DepType are empty.
    """
    nlp = load_model(language)
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'Head', 'DepType'])
        for n, sentence in zip(ids, sentences):
            doc = nlp(sentence)
            heads = []
            dep_types = []
            for token in doc:
                if token.lemma_.lower() == query_word.lower():
                    if token.head != token:  # has incoming dependency
                        heads.append(token.head.text)
                        dep_types.append(token.dep_)
            # Write one row per sentence, joining multiple heads/deps with '; '
            writer.writerow([n, '; '.join(heads), '; '.join(dep_types)])
    print(f"Incoming heads for '{query_word}' exported to: {filename}")

def process_examples_with_analysis(ids, sentences, language="en", query_words=None, output_dir="dependency_visualizations"):
    """Process examples with dependency analysis for specific words."""
    nlp = load_model(language)
    os.makedirs(output_dir, exist_ok=True)

    csv_dir = "dependency_csv_exports"
    os.makedirs(csv_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    all_dependency_data = []

    # Process each sentence
    for idx, sentence in enumerate(sentences):
        print(f"\n{'=' * 50}")
        print(f"PROCESSING EXAMPLE {idx + 1} ({language.upper()}): {sentence}")
        print(f"{'=' * 50}")

        doc = nlp(sentence)

        # Outgoing dependencies table (console)
        print("\nOUTGOING DEPENDENCIES TABLE:")
        print(f"{'Token':<15}{'→':<5}{'Child':<15}{'Dependency Type':<20}")
        print("-" * 55)

        shown_dependencies = set()
        for token in doc:
            for child in token.children:
                if child.dep_ != "punct":
                    dependency_key = f"{token.text}_{child.text}_{child.dep_}"
                    if dependency_key not in shown_dependencies:
                        print(f"{token.text:<15}{'→':<5}{child.text:<15}{child.dep_:<20}")
                        all_dependency_data.append([idx + 1, sentence, token.text, '→', child.text, child.dep_])
                        shown_dependencies.add(dependency_key)

        # Basic dependencies (console)
        print("\nBASIC DEPENDENCIES:")
        print(f"{'Token':<15}{'Dependency':<12}{'Head':<15}Children")
        print("-" * 45)
        for token in doc:
            children = ", ".join([child.text for child in token.children])
            print(f"{token.text:<15}{token.dep_:<12}{token.head.text:<15}{children}")

        # Tree structure (console)
        print("\nTREE STRUCTURE:")
        root = build_dependency_tree(doc)
        print_tree(root)

        # HTML visualization
        output_file = os.path.join(output_dir, f"dependency_{language}_{idx + 1}.html")
        visualize_dependencies(doc, output_file)
        print(f"\nVisualization saved to: {output_file}")

    # Export combined dependency table
    if all_dependency_data:
        combined_csv_filename = os.path.join(csv_dir, f"combined_dependency_table_{language}_{timestamp}.csv")
        export_combined_dependency_table_to_csv(all_dependency_data, combined_csv_filename)

        print(f"\n{'=' * 60}")
        print(f"COMBINED DEPENDENCY TABLE SUMMARY")
        print(f"{'=' * 60}")
        print(f"Total dependencies across all examples: {len(all_dependency_data)}")
        print(f"Unique dependency types: {len(set(row[5] for row in all_dependency_data))}")

        print(f"\nFirst 10 dependencies in combined table:")
        preview_headers = ['Example_ID', 'Token', '→', 'Child', 'Dependency Type']
        preview_data = [[row[0], row[2], row[3], row[4], row[5]] for row in all_dependency_data[:10]]
        print(tabulate(preview_data, headers=preview_headers, tablefmt="grid"))

    # Dependency analysis for query words
    if query_words:
        print("\n\n" + "=" * 60)
        print("DEPENDENCY ANALYSIS FOR QUERY WORDS")
        print("=" * 60)

        for word in query_words:
            stats = analyze_dependencies(sentences, word, language)
            print_dependency_stats(stats, word)

            stats_filename = os.path.join(csv_dir, f"dependency_stats_{language}_{word}_{timestamp}.csv")
            export_dependency_stats_to_csv(stats, word, stats_filename)

            full_filename = os.path.join(csv_dir, f"full_occurrences_{language}_{word}_{timestamp}.csv")
            export_all_dependency_occurrences(ids, sentences, word, language, full_filename)

            # NEW: export incoming heads
            heads_filename = os.path.join(csv_dir, f"incoming_heads_{language}_{word}_{timestamp}.csv")
            export_incoming_heads(ids, sentences, word, language, heads_filename)

    return csv_dir


# Main execution
if __name__ == "__main__":
    # Configuration
    LANGUAGE = "ru"                     # Change to your language code
    OUTPUT_DIR = "dependency_visualizations"
    QUERY_WORDS = ["компания"]          # Word to analyse (lemma form)
    CSV_FILE_PATH = "/home/yenotmur/Dropbox/TypConstr/Comitative/komp_full.csv"  # Your two-column CSV

    # Read examples from CSV
    ids, sentences = read_examples_from_csv(CSV_FILE_PATH)

    if not sentences:
        print("No examples found! Using default examples instead.")
        ids = list(range(1, 4))
        sentences = [
            "Наша дружная компания шла по улице и пела песни",
            "Компания производит качественные товары для дома",
            "В этой компании работают хорошие специалисты"
        ]

    # Process examples
    csv_export_dir = process_examples_with_analysis(
        ids, sentences,
        language=LANGUAGE,
        query_words=QUERY_WORDS,
        output_dir=OUTPUT_DIR
    )

    print(f"\nProcessing complete!")
    print(f"Open HTML files in browser to view visualizations.")
    print(f"CSV files exported to: {csv_export_dir}")