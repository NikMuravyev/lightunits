---
tags:
  - cxg
Type: overview
---
**Overview**  
Even after more than seven decades of modern syntactic research, many core phenomena remain analytically recalcitrant. This report surveys ten grand challenges that still resist fully satisfactory solutions and asks, for each one, whether (and how) it has been explored in Construction-Grammar (CxG) frameworks. The survey brings together findings from formal syntax, typology, psycholinguistics, computational linguistics and usage-based research, highlighting convergences and remaining gaps. A comparative matrix at the end provides a quick reference to CxG coverage.

## The Landscape of Syntax Challenges

Numerous review papers and white-books have catalogued “grand challenges” for linguistic theory: integrating theories and levels[1](https://faculty.washington.edu/ebender/papers/GrandChallenge.pdf), managing cross-linguistic diversity[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10234276/), coping with data scale[3](https://www.frontiersin.org/research-topics/7957/theoretical-syntax-at-the-crossroads-big-data-citizen-science-and-crowdsourcing), and modeling cognitive constraints[4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7500530/). When we zero in on narrow syntax, ten problem clusters dominate current debate (Table 1).

| #   | Challenge                         | Why It Remains Hard                                           | Key Sources                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --- | --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Long-Distance Dependencies (LDDs) | Unbounded filler–gap chains, island constraints               | 26[5](https://www.cambridge.org/core/books/subjects-and-universal-grammar/longdistance-dependencies/D5EBFA03B707C0944C5D2413FD300B99) 36[6](https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6) 79[7](https://brill.com/previewpdf/display/book/9781849500104/B9781849500104-s015.xml) |
| 2   | Ellipsis & Gapping                | Recovering silent structure, parallelism constraints          | 56[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf) 63[9](https://aclanthology.org/Y16-2028.pdf) 71[10](https://aclanthology.org/N18-1105.pdf)                                                                                                                                                                                                                                                                                                |
| 3   | Coordination                      | Non-constituent coordination, Coordinate Structure Constraint | 57[11](https://proceedings.hpsg.xyz/article/view/580/644) 68[12](https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf) 61[13](https://babel.ucsc.edu/~hank/wilder_coordination_atb_ellipsis.pdf)                                                                                                                                                                                               |
| 4   | Free Word Order                   | Scrambling, discourse-driven linearization                    | 29[14](https://journal.fi/finjol/article/view/153157/98672) 48[15](https://iclc2019.site/wp-content/uploads/abstracts/construction/ICLC-15_paper_472.pdf) 72[16](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf)                                                                                                                                                                                                                                |
| 5   | Argument-Structure Alternations   | Verb–syntax mismatches, productivity limits                   | 25[17](https://core.ac.uk/download/pdf/53183524.pdf) 35[18](https://www.cse.iitk.ac.in/users/amit/books/goldberg-1995-constructions-construction-grammar.html) 67[19](https://www.degruyter.com/document/doi/10.1075/slcs.195.04ros/html)                                                                                                                                                                                                                    |
| 6   | Structural Ambiguity              | Multiple parses, probabilistic disambiguation                 | 88[20](https://www.cs.utexas.edu/~dnp/frege/subsection-178.html) 96[4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7500530/)                                                                                                                                                                                                                                                                                                                                    |

The next sections examine each challenge in detail, then evaluate CxG contributions.

## Long-Distance Dependencies

#### Why They Matter

Wh-movement, topicalization, relativization, and raising all exhibit constituents that appear to move arbitrarily far, yet remain interpretable at their trace sites. Traditional accounts rely on filler–gap licensing and island constraints; however, they struggle to predict cross-linguistic variation in extraction domains[5](https://www.cambridge.org/core/books/subjects-and-universal-grammar/longdistance-dependencies/D5EBFA03B707C0944C5D2413FD300B99).

#### Construction-Grammar Approaches

1. **Fluid Construction Grammar (FCG)** offers an account where LDDs “emerge as a side-effect” of interacting constructions rather than being hard-wired filler–gap pairs; no traces are required[6](https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6).
2. **Rely-On Construction Networks** reframe dependency chains as networks of partial form–meaning correspondences, allowing multiple “linking routes” without transformations[19](https://www.degruyter.com/document/doi/10.1075/slcs.195.04ros/html).

#### Evaluation

CxG provides elegant alternatives to the filler–gap mechanism and offers computational implementations (FCG parsers handle LDDs bidirectionally[6](https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6)). Yet a comprehensive typology of islands inside CxG is still lacking.

## Ellipsis, Gapping and Other Void Phenomena

#### The Challenge

Constructions like VP-ellipsis, sluicing, stripping, and gapping delete large chunks of syntax while preserving meaning.[10](https://aclanthology.org/N18-1105.pdf) Theories must explain what is deleted, how it is recovered, and why certain deletions are impossible.

#### Construction-Grammar Work

- **Goldberg & Perek’s Ellipsis Family**: CxG treats each ellipsis pattern as a distinct construction pairing surface remnants with interpretation rules[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf)[29](https://www.semanticscholar.org/paper/Ellipsis-in-Construction-Grammar-Goldberg-Perek/5031181cfab57cdd43f0aa0bf95864ae0943a430).
- **Gapping in QUD-based HPSG–CxG Hybrids**: Park recasts gapping as resolving a Question-Under-Discussion, avoiding purely syntactic accounts[9](https://aclanthology.org/Y16-2028.pdf).

#### Strengths & Gaps

The usage-based view captures cross-construction similarities (economy, discourse givenness)[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf); however, formal coverage of languages with rich voice morphology remains under-developed.

## Coordination & Non-Constituent Coordination

#### Persistent Problems

- Non-constituent coordination (“John gave _ and Mary lent _ a book”).
- Coordinate Structure Constraint violations (e.g., Across-The-Board extraction).
- Interaction with gapping and ellipsis[13](https://babel.ucsc.edu/~hank/wilder_coordination_atb_ellipsis.pdf).

#### CxG Contributions

- **Incremental Updating Model**: Kempen models coordination as “appropriateness repairs” that incrementally update shared structure[12](https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf).
- **Domain-General Coordination Schema**: Wetta proposes surface-oriented, constructional rules that treat coordination as licenses over linear domains rather than hierarchical trees[16](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf).
- **Coordination Templates in FCG** capture languages with polysyndeton, asyndeton, and WITH-type coordinators in a single formalism[30](https://courses.washington.edu/ling567/2005/Coordination.pdf).

#### Remaining Issues

While CxG excels at modeling language-specific “coordination constructions,” systematic cross-linguistic constraints such as _same-category_ effects require further unification.

## Free Word Order and Information-Structure Driven Reordering

#### Analytical Barriers

Languages such as Warlpiri or Finnish permit near-arbitrary constituent permutations. Traditional phrase-structure accounts multiply movement rules; dependency grammars lose clear heads.

#### Construction-Grammar Innovations

- **Ordering Constructions**: Kuningas & Leino propose that each information-structural order (Topic–Comment, Focus–Background, etc.) is a separate construction specifying both linearization and discourse function[14](https://journal.fi/finjol/article/view/153157/98672)[31](https://journal.fi/finjol/article/download/153157/98672).
- **Surface-Oriented Flat Constructions**: Wetta replaces deep trees with flat, linear constructions that directly encode order and information-structure cues[16](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf).
- **FCG’s Flexible Linearization** handles free-order languages by competition among constructions without global syntactic movement[15](https://iclc2019.site/wp-content/uploads/abstracts/construction/ICLC-15_paper_472.pdf).

#### Assessment

CxG explains discourse-conditioned word order variation elegantly, but quantitative typological validation across dozens of free-order languages is still pending.

## Argument-Structure Alternations and Verb–Syntax Mismatches

#### The Dilemma

Verbs often appear in syntactic frames that deviate from their “core” argument structure (e.g., _spray/load_ alternation). Projectionist views struggle with productivity and idiomaticity.

#### The CxG Answer

- **Argument-Structure Constructions (ASC)**: Goldberg treats patterns like Ditransitive, Caused-Motion, and Resultative as form–meaning pairings independent of particular verbs[18](https://www.cse.iitk.ac.in/users/amit/books/goldberg-1995-constructions-construction-grammar.html)[17](https://core.ac.uk/download/pdf/53183524.pdf).
- **Design Patterns in FCG** explicitly separate verb semantics from ASC linking rules, operationalizing ASC learning in computational agents[32](https://csl.sony.fr/publication/a-design-pattern-for-argument-structure-constructions/).

#### Successes & Open Questions

CxG has reshaped the field’s view of alternations and productivity. Challenges remain in modeling gradience between verb-specific and fully schematic constructions, especially in low-resource languages.

## Structural Ambiguity and Parsing Complexity

#### The Issue

Ambiguities in attachment (_I saw the man with the telescope_), coordination, and modifier scope burden both human and machine parsers[20](https://www.cs.utexas.edu/~dnp/frege/subsection-178.html)[4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7500530/).

#### CxG Perspectives

- Constructions supply **strong probabilistic cues** (lexical, semantic, discourse) that guide ambiguity resolution in usage[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf).
- Surface-flat CxG reduces spurious parses by avoiding unseen deep structures[16](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf).
- Computational models using CxG constraints achieve competitive parsing accuracies while maintaining interpretability[33](https://aclanthology.org/W06-3510.pdf).

#### Limitations

NP-hardness results for transformational grammars[26](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=114128595e8950a4fd095564b7f61c6afee80ebe) do not automatically lift for CxG; empirical efficiency studies on large corpora are still sparse.


## Comparative Matrix: Which Challenges Have CxG Accounts?

| Challenge                       | Core CxG Literature                                                                                                                                                                                                                                                         | Coverage Status     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Long-Distance Dependencies      | FCG emergent LDDs[6](https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6)                              | **Partial**         |
| Ellipsis & Gapping              | Ellipsis family[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf) [29](https://www.semanticscholar.org/paper/Ellipsis-in-Construction-Grammar-Goldberg-Perek/5031181cfab57cdd43f0aa0bf95864ae0943a430); QUD-gapping[9](https://aclanthology.org/Y16-2028.pdf) | **Substantial**     |
| Coordination                    | Update model[12](https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf); Surface templates[30](https://courses.washington.edu/ling567/2005/Coordination.pdf)                                                   | **Growing**         |
| Free Word Order                 | Ordering constructions[14](https://journal.fi/finjol/article/view/153157/98672); flat CxG[16](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf)                                                                                                                  | **Advanced**        |
| Argument-Structure Alternations | ASC theory[18](https://www.cse.iitk.ac.in/users/amit/books/goldberg-1995-constructions-construction-grammar.html)[17](https://core.ac.uk/download/pdf/53183524.pdf)                                                                                                         | **Mature**          |
| Structural Ambiguity            | Probabilistic cues[8](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf); parsing templates[33](https://aclanthology.org/W06-3510.pdf)                                                                                                                            | **Early**           |


## Implications and Future Work

1. **Bridging Formalism and Usage**: CxG’s meaning-centric stance sheds new light on recalcitrant phenomena like gapping and LDDs, but needs tighter formal semantics for typological generalization.
2. **Scaling Up**: Automated construction detection and probabilistic weighting are essential for applying CxG to big data; collaboration with NLP researchers is crucial[28](https://aclanthology.org/2025.naacl-long.177.pdf)[3](https://www.frontiersin.org/research-topics/7957/theoretical-syntax-at-the-crossroads-big-data-citizen-science-and-crowdsourcing).
3. **Typological Systematics**: Creating an open database of cross-linguistic constructional correspondences would advance both CxG and classical typology.
4. **Cognitive Plausibility**: Incremental updating models of coordination and LDD parsing offer promising psycholinguistic alignments[12](https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf); experimental validation remains a fertile ground.
5. **Complexity Metrics**: Integrating construction frequency, network connectivity, and processing cost could yield more insightful measures than current bit-complexity counts[24](https://www.academia.edu/52378740/Complexity_in_Language_A_Multifaceted_Phenomenon).

## Concluding Remark

Construction Grammar has already reshaped approaches to some of syntax’s toughest puzzles, most notably argument-structure alternations, ellipsis, and information-structure-driven word order. Yet the program is far from complete. Integrating formal rigor, typological breadth, big-data methods, and cognitive evidence will be essential for CxG to tackle the remaining grand challenges in natural-language syntax.

1. [https://faculty.washington.edu/ebender/papers/GrandChallenge.pdf](https://faculty.washington.edu/ebender/papers/GrandChallenge.pdf)
2. [https://pmc.ncbi.nlm.nih.gov/articles/PMC10234276/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10234276/)
3. [https://www.frontiersin.org/research-topics/7957/theoretical-syntax-at-the-crossroads-big-data-citizen-science-and-crowdsourcing](https://www.frontiersin.org/research-topics/7957/theoretical-syntax-at-the-crossroads-big-data-citizen-science-and-crowdsourcing)
4. [https://pmc.ncbi.nlm.nih.gov/articles/PMC7500530/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7500530/)
5. [https://www.cambridge.org/core/books/subjects-and-universal-grammar/longdistance-dependencies/D5EBFA03B707C0944C5D2413FD300B99](https://www.cambridge.org/core/books/subjects-and-universal-grammar/longdistance-dependencies/D5EBFA03B707C0944C5D2413FD300B99)
6. [https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6](https://www.cambridge.org/core/journals/language-and-cognition/article/abs/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6)
7. [https://brill.com/previewpdf/display/book/9781849500104/B9781849500104-s015.xml](https://brill.com/previewpdf/display/book/9781849500104/B9781849500104-s015.xml)
8. [http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf](http://www.fperek.net/pdfs/GoldbergPerekTA-ellipsis-CxG.pdf)
9. [https://aclanthology.org/Y16-2028.pdf](https://aclanthology.org/Y16-2028.pdf)
10. [https://aclanthology.org/N18-1105.pdf](https://aclanthology.org/N18-1105.pdf)
11. [https://proceedings.hpsg.xyz/article/view/580/644](https://proceedings.hpsg.xyz/article/view/580/644)
12. [https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf](https://pure.mpg.de/pubman/item/item_67023_8/component/file_67024/Kempen_Clausal_coordination_Linguistics_2009.pdf)
13. [https://babel.ucsc.edu/~hank/wilder_coordination_atb_ellipsis.pdf](https://babel.ucsc.edu/~hank/wilder_coordination_atb_ellipsis.pdf)
14. [https://journal.fi/finjol/article/view/153157/98672](https://journal.fi/finjol/article/view/153157/98672)
15. [https://iclc2019.site/wp-content/uploads/abstracts/construction/ICLC-15_paper_472.pdf](https://iclc2019.site/wp-content/uploads/abstracts/construction/ICLC-15_paper_472.pdf)
16. [http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf](http://www.acsu.buffalo.edu/~rchaves/wetta_dissertation.pdf)
17. [https://core.ac.uk/download/pdf/53183524.pdf](https://core.ac.uk/download/pdf/53183524.pdf)
18. [https://www.cse.iitk.ac.in/users/amit/books/goldberg-1995-constructions-construction-grammar.html](https://www.cse.iitk.ac.in/users/amit/books/goldberg-1995-constructions-construction-grammar.html)
19. [https://www.degruyter.com/document/doi/10.1075/slcs.195.04ros/html](https://www.degruyter.com/document/doi/10.1075/slcs.195.04ros/html)
20. [https://www.cs.utexas.edu/~dnp/frege/subsection-178.html](https://www.cs.utexas.edu/~dnp/frege/subsection-178.html)
21. [https://www.cambridgescholars.com/resources/pdfs/978-1-5275-6747-4-sample.pdf](https://www.cambridgescholars.com/resources/pdfs/978-1-5275-6747-4-sample.pdf)
22. [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.02002/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.02002/full)
23. [https://pmc.ncbi.nlm.nih.gov/articles/PMC9205392/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9205392/)
24. [https://www.academia.edu/52378740/Complexity_in_Language_A_Multifaceted_Phenomenon](https://www.academia.edu/52378740/Complexity_in_Language_A_Multifaceted_Phenomenon)
25. [https://www.cambridge.org/us/universitypress/subjects/languages-linguistics/evolution-language/complexity-language-developmental-and-evolutionary-perspectives?format=PB&isbn=9781107686625](https://www.cambridge.org/us/universitypress/subjects/languages-linguistics/evolution-language/complexity-language-developmental-and-evolutionary-perspectives?format=PB&isbn=9781107686625)
26. [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=114128595e8950a4fd095564b7f61c6afee80ebe](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=114128595e8950a4fd095564b7f61c6afee80ebe)
27. [https://www.let.rug.nl/~vannoord/alp/proposal/node5.html](https://www.let.rug.nl/~vannoord/alp/proposal/node5.html)
28. [https://aclanthology.org/2025.naacl-long.177.pdf](https://aclanthology.org/2025.naacl-long.177.pdf)
29. [https://www.semanticscholar.org/paper/Ellipsis-in-Construction-Grammar-Goldberg-Perek/5031181cfab57cdd43f0aa0bf95864ae0943a430](https://www.semanticscholar.org/paper/Ellipsis-in-Construction-Grammar-Goldberg-Perek/5031181cfab57cdd43f0aa0bf95864ae0943a430)
30. [https://courses.washington.edu/ling567/2005/Coordination.pdf](https://courses.washington.edu/ling567/2005/Coordination.pdf)
31. [https://journal.fi/finjol/article/download/153157/98672](https://journal.fi/finjol/article/download/153157/98672)
32. [https://csl.sony.fr/publication/a-design-pattern-for-argument-structure-constructions/](https://csl.sony.fr/publication/a-design-pattern-for-argument-structure-constructions/)
33. [https://aclanthology.org/W06-3510.pdf](https://aclanthology.org/W06-3510.pdf)
34. [https://stacks.stanford.edu/file/druid:rf717ks1306/rf717ks1306.pdf](https://stacks.stanford.edu/file/druid:rf717ks1306/rf717ks1306.pdf)
35. [https://en.wikipedia.org/wiki/Fluid_construction_grammar](https://en.wikipedia.org/wiki/Fluid_construction_grammar)
36. [https://linguistics.ucsc.edu/research/publications/chung/problembook.pdf](https://linguistics.ucsc.edu/research/publications/chung/problembook.pdf)
37. [https://netnut.io/syntax-error/](https://netnut.io/syntax-error/)
38. [https://www.univ-orleans.fr/lifo/Members/duchier/teaching/OzNLP/node49.html](https://www.univ-orleans.fr/lifo/Members/duchier/teaching/OzNLP/node49.html)
39. [https://mjsshonline.com/index.php/journal/article/download/2/1](https://mjsshonline.com/index.php/journal/article/download/2/1)
40. [https://www.cambridge.org/core/books/abs/computational-linguistics/syntax-analysis/2B6220E2EE873738543EB7F7835D6A0A](https://www.cambridge.org/core/books/abs/computational-linguistics/syntax-analysis/2B6220E2EE873738543EB7F7835D6A0A)
41. [https://www.reddit.com/r/asklinguistics/comments/r7rpza/syntax_hard/](https://www.reddit.com/r/asklinguistics/comments/r7rpza/syntax_hard/)
42. [https://www.clarin.ac.uk/article/key-research-challenges](https://www.clarin.ac.uk/article/key-research-challenges)
43. [https://arxiv.org/html/2402.01641](https://arxiv.org/html/2402.01641)
44. [https://rrg.caset.buffalo.edu/rrg/RVVCosubChallengesreprint.pdf](https://rrg.caset.buffalo.edu/rrg/RVVCosubChallengesreprint.pdf)
45. [https://botpenguin.com/glossary/syntax-analysis](https://botpenguin.com/glossary/syntax-analysis)
46. [https://computinged.wordpress.com/2012/01/04/the-syntax-problems-in-high-school-cs/](https://computinged.wordpress.com/2012/01/04/the-syntax-problems-in-high-school-cs/)
47. [https://uhra.herts.ac.uk/id/eprint/12728/1/101970.pdf](https://uhra.herts.ac.uk/id/eprint/12728/1/101970.pdf)
48. [https://www.cs.toronto.edu/~niu/teaching/csc485/L3_Syntax.pdf](https://www.cs.toronto.edu/~niu/teaching/csc485/L3_Syntax.pdf)
49. [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3fd3f44f0b014d4cd23a161f5a37ecfbd877a260](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3fd3f44f0b014d4cd23a161f5a37ecfbd877a260)
50. [https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5469](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5469)
51. [https://www.phon.ox.ac.uk/jpierrehumbert/publications/SBE_Challenge_Labphon.pdf](https://www.phon.ox.ac.uk/jpierrehumbert/publications/SBE_Challenge_Labphon.pdf)
52. [https://www.geeksforgeeks.org/machine-learning/syntax-tree-natural-language-processing/](https://www.geeksforgeeks.org/machine-learning/syntax-tree-natural-language-processing/)
53. [https://www.cambridge.org/core/journals/language-and-cognition/article/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6](https://www.cambridge.org/core/journals/language-and-cognition/article/longdistance-dependencies-without-fillergaps-a-cognitivefunctional-alternative-in-fluid-construction-grammar/9CE9B4C98BD6585E6B9B2A04A650D3D6)
54. [https://www.youtube.com/watch?v=Ih0iMW3tJaE](https://www.youtube.com/watch?v=Ih0iMW3tJaE)
55. [https://www.thoughtco.com/what-is-coordination-grammar-1689931](https://www.thoughtco.com/what-is-coordination-grammar-1689931)
56. [https://dl.acm.org/doi/pdf/10.3115/976973.977008](https://dl.acm.org/doi/pdf/10.3115/976973.977008)
57. [https://www.grammarbook.com/blog/clauses-sentences/elliptical-sentence-constructions/](https://www.grammarbook.com/blog/clauses-sentences/elliptical-sentence-constructions/)
58. [https://opentextbc.ca/advancedenglish/chapter/coordination-and-subordination/](https://opentextbc.ca/advancedenglish/chapter/coordination-and-subordination/)
59. [https://bond-lab.github.io/Theories-of-Grammar/pdf/lec-11-ldd.pdf](https://bond-lab.github.io/Theories-of-Grammar/pdf/lec-11-ldd.pdf)
60. [https://en.wikipedia.org/wiki/Ellipsis_(grammar)](https://en.wikipedia.org/wiki/Ellipsis_\(grammar\))
61. [https://en.wikipedia.org/wiki/Coordination_(linguistics)](https://en.wikipedia.org/wiki/Coordination_\(linguistics\))
62. [https://www.reddit.com/r/conlangs/comments/u5io4y/is_free_word_order_all_its_cracked_up_to_be/](https://www.reddit.com/r/conlangs/comments/u5io4y/is_free_word_order_all_its_cracked_up_to_be/)
63. [https://en.wikipedia.org/wiki/Ellipsis_(linguistics)](https://en.wikipedia.org/wiki/Ellipsis_\(linguistics\))
64. [https://www.let.rug.nl/~hendriks/papers/coordination.pdf](https://www.let.rug.nl/~hendriks/papers/coordination.pdf)
65. [https://www.academia.edu/68713388/Word_Orders_and_Construction_Grammar](https://www.academia.edu/68713388/Word_Orders_and_Construction_Grammar)
66. [https://books.google.com/books/about/Constructions.html?id=HzmGM0qCKtIC](https://books.google.com/books/about/Constructions.html?id=HzmGM0qCKtIC)
67. [https://linguistics.stackexchange.com/questions/27457/what-constitutes-a-long-distance-dependency-and-how-can-it-be-quantified](https://linguistics.stackexchange.com/questions/27457/what-constitutes-a-long-distance-dependency-and-how-can-it-be-quantified)
68. [https://en.wikipedia.org/wiki/Gapping](https://en.wikipedia.org/wiki/Gapping)
69. [https://www.glossa-journal.org/article/id/9639/](https://www.glossa-journal.org/article/id/9639/)
70. [https://linguistics.ucla.edu/people/Kracht/courses/case_046_gapp.htm](https://linguistics.ucla.edu/people/Kracht/courses/case_046_gapp.htm)
71. [https://www.cambridge.org/core/journals/journal-of-linguistics/article/aggressively-nondlinked-construction-and-ellipsis-a-direct-interpretation-approach/C92D413574503A1D36B8F849A1CA9C23](https://www.cambridge.org/core/journals/journal-of-linguistics/article/aggressively-nondlinked-construction-and-ellipsis-a-direct-interpretation-approach/C92D413574503A1D36B8F849A1CA9C23)
72. [http://courses.washington.edu/ling567/2005/lab8.html](http://courses.washington.edu/ling567/2005/lab8.html)
73. [https://pmc.ncbi.nlm.nih.gov/articles/PMC7162722/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7162722/)
74. [https://journals.sagepub.com/doi/pdf/10.1177/17470218241280567?download=true](https://journals.sagepub.com/doi/pdf/10.1177/17470218241280567?download=true)
75. [https://aclanthology.org/1988.tmi-1.2.pdf](https://aclanthology.org/1988.tmi-1.2.pdf)
76. [https://pubmed.ncbi.nlm.nih.gov/31952450/](https://pubmed.ncbi.nlm.nih.gov/31952450/)
77. [https://aclanthology.org/O14-1013.pdf](https://aclanthology.org/O14-1013.pdf)
78. [https://www.sprachforschung.uni-wuppertal.de/fileadmin/linguistik/rathert/Kolloquien/WS12_13/Constructions__complexity_and_word_order_variation__Wuppertal_.pdf](https://www.sprachforschung.uni-wuppertal.de/fileadmin/linguistik/rathert/Kolloquien/WS12_13/Constructions__complexity_and_word_order_variation__Wuppertal_.pdf)
79. [https://ai.vub.ac.be/sites/default/files/iccg04-interpretation.pdf](https://ai.vub.ac.be/sites/default/files/iccg04-interpretation.pdf)
80. [https://en.wikipedia.org/wiki/Goldberg%E2%80%93Coxeter_construction](https://en.wikipedia.org/wiki/Goldberg%E2%80%93Coxeter_construction)
81. [https://aclanthology.org/2020.emnlp-main.218.pdf](https://aclanthology.org/2020.emnlp-main.218.pdf)
82. [https://aclanthology.org/E06-2008.pdf](https://aclanthology.org/E06-2008.pdf)
83. [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=7b14b96316cc9272455b97e52bfc23bd2cbbfe8b](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=7b14b96316cc9272455b97e52bfc23bd2cbbfe8b)
84. [https://www.numberanalytics.com/blog/linguistics-gapping-in-depth-analysis](https://www.numberanalytics.com/blog/linguistics-gapping-in-depth-analysis)
85. [https://webofproceedings.org/proceedings_series/ESSP/ICLAHD%202019/HD1220049.pdf](https://webofproceedings.org/proceedings_series/ESSP/ICLAHD%202019/HD1220049.pdf)
86. [https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/a-starting-point-word-order/](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/a-starting-point-word-order/)
87. [https://pure.mpg.de/rest/items/item_67023_8/component/file_67024/content](https://pure.mpg.de/rest/items/item_67023_8/component/file_67024/content)
88. [https://aclanthology.org/C90-3056.pdf](https://aclanthology.org/C90-3056.pdf)
89. [https://adele.scholar.princeton.edu/publications/ellipsis-construction-grammar-oxford-handbook-ellipsis](https://adele.scholar.princeton.edu/publications/ellipsis-construction-grammar-oxford-handbook-ellipsis)
90. [https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/23F840830E987630A523C7DD2DC7DD22/9780511997587not_p231-245_CBO.pdf/notes.pdf](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/23F840830E987630A523C7DD2DC7DD22/9780511997587not_p231-245_CBO.pdf/notes.pdf)
91. [https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011516-034008;jsessionid=hS_BHWEjZGWsp9bcb7LiamL0ZSIBtDyd5kwFSOa0.annurevlive-10-241-10-100](https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011516-034008;jsessionid=hS_BHWEjZGWsp9bcb7LiamL0ZSIBtDyd5kwFSOa0.annurevlive-10-241-10-100)
92. [https://studiapsypaed.com/wp-content/uploads/2021/09/2-2010-12.pdf](https://studiapsypaed.com/wp-content/uploads/2021/09/2-2010-12.pdf)
93. [https://arxiv.org/html/2412.04497v2](https://arxiv.org/html/2412.04497v2)
94. [https://cyberleninka.ru/article/n/the-challenges-and-opportunities-of-using-digital-technologies-in-linguistics-education](https://cyberleninka.ru/article/n/the-challenges-and-opportunities-of-using-digital-technologies-in-linguistics-education)
95. [https://en.wikipedia.org/wiki/Syntactic_ambiguity](https://en.wikipedia.org/wiki/Syntactic_ambiguity)
96. [https://www.degruyter.com/document/doi/10.1515/lingvan-2022-0133/html?lang=en&srsltid=AfmBOop6G9Qg5i2_DTvlttKsUiTKWthXSi8qI3_OP1BEXzlKdQ8qwG15](https://www.degruyter.com/document/doi/10.1515/lingvan-2022-0133/html?lang=en&srsltid=AfmBOop6G9Qg5i2_DTvlttKsUiTKWthXSi8qI3_OP1BEXzlKdQ8qwG15)
97. [https://homepages.inf.ed.ac.uk/steedman/tl/tlnotes01handout.pdf](https://homepages.inf.ed.ac.uk/steedman/tl/tlnotes01handout.pdf)
98. [https://en.wikipedia.org/wiki/Syntactic_parsing_(computational_linguistics)](https://en.wikipedia.org/wiki/Syntactic_parsing_\(computational_linguistics\))