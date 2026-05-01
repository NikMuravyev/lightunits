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
        # Existing models
        "en": "en_core_web_sm",  # English (12MB)
        "ru": "ru_core_news_sm",  # Russian (43MB)
        "de": "de_core_news_sm",  # German (14MB)
        "pl": "pl_core_news_sm",  # Polish (15MB)
        "fi": "fi_core_news_sm",  # Finnish (13MB)
        "fr": "fr_core_news_sm",  # French (16MB)
        "es": "es_core_news_sm",  # Spanish (13MB)
        "it": "it_core_news_sm",  # Italian (14MB)
        "pt": "pt_core_news_sm",  # Portuguese (13MB)
        "nl": "nl_core_news_sm",  # Dutch (13MB)
        "zh": "zh_core_web_sm",  # Chinese (14MB)
        "ja": "ja_core_news_sm",  # Japanese (17MB)
        "da": "da_core_news_sm",  # Danish (13MB)
        "sv": "sv_core_news_sm",  # Swedish (13MB)
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
    Read examples from a CSV file.
    Each line of the first column is treated as a separate example.
    Returns a list of examples.
    """
    examples = []

    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found!")
        return examples

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # Skip header if it exists (optional - you might want to make this configurable)
            # next(reader, None)  # Uncomment if your CSV has a header row

            for row in reader:
                if row and row[0].strip():  # Check if first column exists and is not empty
                    examples.append(row[0].strip())

        print(f"Successfully read {len(examples)} examples from '{csv_file_path}'")

    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return examples


def analyze_dependencies(examples, query_word, language="en"):
    """
    Analyze both incoming and outgoing dependencies for a specific word across examples
    Returns a dictionary with dependency statistics
    """
    nlp = load_model(language)
    stats = defaultdict(lambda: {"count": 0, "examples": []})

    for sentence in examples:
        doc = nlp(sentence)
        for token in doc:
            # Case-insensitive matching
            if token.text.lower() == query_word.lower():
                # Collect outgoing dependencies (query word -> children)
                for child in token.children:
                    # Exclude punctuation dependencies
                    if child.dep_ == "punct":
                        continue

                    dep_type = f"OUT: {child.dep_}"
                    stats[dep_type]["count"] += 1

                    # Store example child (limit to 3 per dependency type)
                    if len(stats[dep_type]["examples"]) < 3:
                        example = f"{token.text} → {child.text}"
                        stats[dep_type]["examples"].append(example)

                # Collect incoming dependencies (head -> query word)
                if token.head != token:  # Skip if query word is the root
                    dep_type = f"IN: {token.dep_}"
                    stats[dep_type]["count"] += 1

                    # Store example (limit to 3 per dependency type)
                    if len(stats[dep_type]["examples"]) < 3:
                        example = f"{token.head.text} → {token.text}"
                        stats[dep_type]["examples"].append(example)

    return dict(stats)


def print_dependency_stats(stats, query_word):
    """Print dependency statistics in a table format"""
    if not stats:
        print(f"\nNo dependencies found for '{query_word}' in the examples")
        return

    # Prepare table data
    table_data = []
    for dep_type, data in sorted(stats.items()):
        examples = ", ".join(data["examples"])
        table_data.append([dep_type, data["count"], examples])

    # Print table
    print(f"\nDependency Statistics for '{query_word}':")
    print(tabulate(
        table_data,
        headers=["Dependency Type (Direction)", "Count", "Example Relations"],
        tablefmt="grid",
        numalign="center",
        stralign="left"
    ))

    # Print summary
    total = sum(item["count"] for item in stats.values())
    unique = len(stats)
    print(f"\nTotal dependencies: {total} | Unique types: {unique}")


def export_combined_dependency_table_to_csv(all_dependency_data, filename):
    """Export combined dependency table data to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Example_ID', 'Sentence', 'Token', 'Direction', 'Child', 'Dependency Type'])
        # Write data
        for row in all_dependency_data:
            writer.writerow(row)
    print(f"Combined dependency table exported to: {filename}")


def export_dependency_stats_to_csv(stats_data, query_word, filename):
    """Export dependency statistics to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Dependency Type (Direction)', 'Count', 'Example Relations'])
        # Write data
        for dep_type, data in sorted(stats_data.items()):
            examples = ", ".join(data["examples"])
            writer.writerow([dep_type, data["count"], examples])
    print(f"Dependency statistics for '{query_word}' exported to: {filename}")


def process_examples_with_analysis(examples, language="en", query_words=None, output_dir="dependency_visualizations"):
    """Process examples with dependency analysis for specific words"""
    nlp = load_model(language)
    os.makedirs(output_dir, exist_ok=True)

    # Create CSV directory
    csv_dir = "dependency_csv_exports"
    os.makedirs(csv_dir, exist_ok=True)

    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Combined data for all examples
    all_dependency_data = []

    # Process each example
    for i, sentence in enumerate(examples):
        print(f"\n{'=' * 50}")
        print(f"PROCESSING EXAMPLE {i + 1} ({language.upper()}): {sentence}")
        print(f"{'=' * 50}")

        doc = nlp(sentence)

        # Enhanced dependency table showing only outgoing dependencies
        print("\nOUTGOING DEPENDENCIES TABLE:")
        print(f"{'Token':<15}{'→':<5}{'Child':<15}{'Dependency Type':<20}")
        print("-" * 55)

        # Track which dependencies we've already shown to avoid duplicates within this example
        shown_dependencies = set()

        for token in doc:
            # Show only outgoing dependencies (token -> children)
            for child in token.children:
                if child.dep_ != "punct":  # Exclude punctuation
                    dependency_key = f"{token.text}_{child.text}_{child.dep_}"
                    if dependency_key not in shown_dependencies:
                        print(f"{token.text:<15}{'→':<5}{child.text:<15}{child.dep_:<20}")
                        # Add to combined CSV data with example info
                        all_dependency_data.append([i + 1, sentence, token.text, '→', child.text, child.dep_])
                        shown_dependencies.add(dependency_key)

        # Original basic dependencies (unchanged)
        print("\nBASIC DEPENDENCIES:")
        print(f"{'Token':<15}{'Dependency':<12}{'Head':<15}Children")
        print("-" * 45)
        for token in doc:
            children = ", ".join([child.text for child in token.children])
            print(f"{token.text:<15}{token.dep_:<12}{token.head.text:<15}{children}")

        # Tree structure
        print("\nTREE STRUCTURE:")
        root = build_dependency_tree(doc)
        print_tree(root)

        # Visualization
        output_file = os.path.join(output_dir, f"dependency_{language}_{i + 1}.html")
        visualize_dependencies(doc, output_file)
        print(f"\nVisualization saved to: {output_file}")

    # Export combined dependency table to CSV
    if all_dependency_data:
        combined_csv_filename = os.path.join(csv_dir, f"combined_dependency_table_{language}_{timestamp}.csv")
        export_combined_dependency_table_to_csv(all_dependency_data, combined_csv_filename)

        # Print summary of combined table
        print(f"\n{'=' * 60}")
        print(f"COMBINED DEPENDENCY TABLE SUMMARY")
        print(f"{'=' * 60}")
        print(f"Total dependencies across all examples: {len(all_dependency_data)}")
        print(f"Unique dependency types: {len(set(row[5] for row in all_dependency_data))}")

        # Show a preview of the combined data
        print(f"\nFirst 10 dependencies in combined table:")
        preview_headers = ['Example_ID', 'Token', '→', 'Child', 'Dependency Type']
        preview_data = [[row[0], row[2], row[3], row[4], row[5]] for row in all_dependency_data[:10]]
        print(tabulate(preview_data, headers=preview_headers, tablefmt="grid"))

    # Dependency analysis for query words (shows both incoming and outgoing)
    if query_words:
        print("\n\n" + "=" * 60)
        print("DEPENDENCY ANALYSIS FOR QUERY WORDS")
        print("=" * 60)

        for word in query_words:
            stats = analyze_dependencies(examples, word, language)
            print_dependency_stats(stats, word)

            # Export dependency statistics to CSV
            stats_filename = os.path.join(csv_dir, f"dependency_stats_{language}_{word}_{timestamp}.csv")
            export_dependency_stats_to_csv(stats, word, stats_filename)

    return csv_dir


# Main execution
if __name__ == "__main__":
    # Configuration
    LANGUAGE = "ru"  # Change to "ru" for Russian
    OUTPUT_DIR = "dependency_visualizations"
    QUERY_WORDS = ["компания", "песни"]  # Words to analyze
    CSV_FILE_PATH = "examples.csv"  # Path to your CSV file

    # Read examples from CSV file
    examples = read_examples_from_csv(CSV_FILE_PATH)

    if not examples:
        print("No examples found! Using default examples instead.")
        # Fallback to default examples if CSV is empty or not found
        examples = [
            "Наша дружная компания шла по улице и пела песни",
            "Компания производит качественные товары для дома",
            "В этой компании работают хорошие специалисты"
        ]

    # Process examples with analysis
    csv_export_dir = process_examples_with_analysis(
        examples,
        language=LANGUAGE,
        query_words=QUERY_WORDS,
        output_dir=OUTPUT_DIR
    )

    print(f"\nProcessing complete!")
    print(f"Open HTML files in browser to view visualizations.")
    print(f"CSV files exported to: {csv_export_dir}")