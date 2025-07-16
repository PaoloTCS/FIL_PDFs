The Nibbler Algorithm and Primes-of-Primes: A Framework for Recursive Knowledge Discovery
Version: 1.0 (Chapter Draft)
Author: A Synthesis of work by Paolo Pignatelli and Gemini 2.5 Pro
Status: Internal R&D Document for the FIL Project
Abstract
This chapter introduces a novel computational framework for discovering and structuring knowledge from undifferentiated information substrates. At its core are two synergistic constructs: the Nibbler Algorithm, a recursive graph-building engine, and the Primes-of-Primes (PoP) Operator, a number-theoretic system for generating unique, hierarchical identifiers. We demonstrate how Nibbler recursively transforms raw data into a directed semantic graph, using a process analogous to a dynamically growing transformer architecture. The challenge of maintaining identity and traceability through infinite recursion is solved by the PoP operator, which provides a "lossy breadcrumb trail" for every emergent pattern. This framework is explicitly designed to operate within the constraints of Physical Incompleteness (PI), using bounded recursion and lossy compression to manage exponential complexity. We will explore the algorithm's formal definitions, its deep theoretical ties to Gödel's incompleteness, group theory, and its practical application in building scalable knowledge systems.
1. The Fundamental Challenge: From Information Chaos to Structured Knowledge
In many complex domains—from analyzing large language model embeddings to interpreting experimental sensor data—we are faced with a deluge of undifferentiated information. This primordial substrate, which we term the Fundamental Language Field (FL Field), is rich in potential but lacks inherent structure. The primary challenge is to develop a process that can, without prohibitive computational cost or brittle assumptions, incrementally discover stable patterns, build relationships between them, and organize them into a coherent, hierarchical knowledge structure.
Existing methods often fail at scale. Full-graph operations are computationally explosive, while purely local methods fail to capture emergent, higher-order structures. The Nibbler framework was conceived to bridge this gap, providing a physically-grounded, scalable, and self-organizing approach to knowledge discovery.
2. The Nibbler Algorithm: A Recursive Graph Constructor
The Nibbler algorithm is not merely a tool for analyzing graphs; it is a process that builds a graph from a more primitive source. Its design is governed by three core principles.
2.1. Core Principles
Directed Graphs as the Substrate of Knowledge: Nibbler operates on and produces a directed graph G = (V, E, w), where nodes V represent recognized patterns, and directed edges E represent relationships of composition, causality, or derivation. Directionality is crucial for modeling the flow of information from simple to complex.
Recursion as the Engine of Discovery: The algorithm is fundamentally recursive. It identifies a self-consistent subgraph, abstracts it into a new, single "meta-node," and then is capable of applying itself to a collection of these new meta-nodes. This recursive self-application is what allows it to build structures of arbitrary complexity.
Self-Compression as the Key to Scalability: Left unchecked, recursive pattern generation would lead to an exponential explosion in complexity. Nibbler's core innovation is that its primary operation—the abstraction of a subgraph into a meta-node—is an act of compression. It uses itself to manage the complexity it creates.
2.2. The Algorithmic Cycle
Nibbler operates in a continuous, multi-level cycle:
Observe: It scans the information substrate (either the initial FL Field or an existing graph level) to identify candidate patterns.
Recognize: It applies a kernel function to validate these patterns, assessing their stability, energy, and semantic coherence against the local context.
Compress (Nibble): Stable, coherent collections of nodes (e.g., dense subgraphs or "cliques") are identified and abstracted into new, higher-level meta-nodes.
Recurse: The algorithm is then applied to the new level of meta-nodes, repeating the cycle to discover patterns-of-patterns.
2.3. Formal Definitions
Directed Graph G=(V,E,w): The evolving knowledge structure.
Nibble Operator N(G, θ, level): A recursive function that takes a graph G and parameters θ at a given level and returns a compressed version of the graph.
Kernel k_N(o): A function that scores an observation o, typically a blend of a discovery kernel k_D (measuring novelty/contrast) and a pattern kernel k_P (measuring internal consistency/low entropy).
Recursion Trigger η: A complexity threshold. If a discovered subgraph S has a complexity C(S) > η, the Nibbler operator is called recursively on S.
2.4. The Transformer Analogy
The Nibbler architecture is deeply analogous to a Transformer, but one that builds its own layers dynamically.
Transformer Component	Nibbler Analogy
Input Tokens	Primordial observations from the FL Field.
Stacked Layers	The recursive levels of the Nibbler hierarchy. Each recursion adds a new "layer" of abstraction.
Self-Attention Mechanism	The recognition kernel k_N, which weighs the importance of nodes/patterns based on their relationship to the local context.
Multi-Head Attention	The separate processing of different types of subgraphs, such as dense cliques (local, associative patterns) and directed flows (causal, sequential patterns).
Positional Encoding	A unique identifier for each node that encodes its history and position. This is the crucial role filled by the Primes-of-Primes operator.
Dimensionality Reduction	The self-compression mechanism, where a complex subgraph is mapped to a single meta-node.
3. The Identity Problem and the Prime Encoding Solution
The concept of compressing a subgraph into a "meta-node" presents a critical challenge: the identity problem. How can a compressed meta-node retain information about its constituent parts without defeating the purpose of compression by storing its entire history?
An initial solution is Prime Encoding. By assigning a unique prime number to each primordial pattern, a composite meta-node can be identified by the product of its constituents' primes. Thanks to the Fundamental Theorem of Arithmetic, this product can be uniquely factored, making the node's composition perfectly decomposable.
However, as recursion deepens, these products can grow astronomically large. A more dynamic, scalable, and hierarchically aware system is needed.
4. Primes-of-Primes (PoP): A Dynamic Framework for Hierarchical Tagging
The Primes-of-Primes (PoP) operator provides this advanced system. It is a recursive function that generates a sparse, ordered, and infinitely scalable hierarchy of identifiers.
4.1. Formal Definition of the PoP Operator
Let p_n be the n-th prime number (e.g., p_1=2, p_2=3). The PoP operator P^(k)(n) is defined as:
Base Case (k=1): P^(1)(n) = p_n
Recursive Step (k > 1): P^(k+1)(n) = p_{P^(k)(n)}
This operator "primes the index" repeatedly, creating a tower of primes. For example, P^(3)(2) is calculated as:
P^(1)(2) = p_2 = 3
P^(2)(2) = p_{P^(1)(2)} = p_3 = 5
P^(3)(2) = p_{P^(2)(2)} = p_5 = 11
4.2. The PoP Trail: A Recursive Tagging System
We use the PoP operator not to generate a single ID, but to create a PoP Trail—a sequence of numbers that acts as a unique, hierarchical address for every pattern discovered by Nibbler.
A pattern's tag is represented as Symbol_{trail}, where the trail is a list of integers encoding its recursive lineage.
Level 0: A primordial pattern observed at index n is given the symbol S and a trail [n].
Level 1 Recursion: When Nibbler recurses on this pattern, the new pattern gets the trail [n, P^(1)(n)].
Level 2 Recursion: The next level of recursion appends P^(2)(n), yielding the trail [n, P^(1)(n), P^(2)(n)].
This trail is a "lossy breadcrumb," providing a complete, decomposable history of the pattern's origin.
4.3. Branching and State Reset
When the algorithm branches (e.g., by identifying two separate cliques at the same level), a new symbol (S → T) is introduced to signify a new lineage, and its trail starts anew. This prevents trails from becoming monolithic and allows the knowledge graph to grow as a tree of recursive discoveries.
5. The Integrated Nibbler-PoP Algorithm
Marrying the Nibbler procedure with PoP trails creates a robust, traceable, and scalable system.
5.1. Unified Pseudocode
Generated pseudo
procedure NIBBLER(G, θ, level, base_symbol, base_index):
    trail = [base_index] # Initialize trail for this recursive call

    while not STOP_CONDITION(...):
        # 1. Observe, Recognize, and Extract patterns as before
        ...
        
        # 2. Assign PoP Trail Tags to new patterns
        for each new_pattern P discovered from parent_pattern:
            parent_trail = parent_pattern.trail
            new_subscript = P^(level)(parent_trail[0]) # Apply PoP to base index
            
            # Append and potentially trim the trail
            new_trail = APPEND_AND_TRIM(parent_trail, new_subscript)
            P.tag = base_symbol + "_{" + new_trail + "}"

        # 3. Identify subgraphs S (cliques, flows) for the next recursive step
        S = SELECT_SUBGRAPH(F, G, θ)
        
        # 4. Check for Recursion Trigger
        if RECURSION_TRIGGER(S, trail) == True:
            # Branch: Get a new symbol and reset base index for the recursive call
            new_symbol = GET_NEXT_SYMBOL(base_symbol)
            for sub_component in S:
                # Recursive call with a new lineage
                NIBBLER(sub_component, θ, level + 1, new_symbol, sub_component.index)
        
        # 5. Compress S into a meta-node and update G
        ...
Use code with caution.
Pseudo
5.2. Worked Example
Level 0: Nibbler observes a primordial pattern, the 5th one seen. It is tagged S_[5].
Level 1: It recurses on this pattern. The resulting structure is tagged S_[5, 11] because P^(1)(5) = p_5 = 11.
Level 2: It recurses again. The new pattern is tagged S_[5, 11, 31] because P^(2)(5) = p_{11} = 31.
Branching: At this level, two distinct cliques C1 and C2 are found.
The recursive call on C1 introduces a new symbol T. Its first pattern is tagged T_[...].
The recursive call on C2 introduces symbol U. Its first pattern is tagged U_[...].
The tags S_[5, 11, 31], T_[...], and U_[...] now exist as nodes in the graph, each with a complete, traceable history.
6. Managing Infinite Growth: Physical Incompleteness and Bounded Recursion
A purely mathematical recursion would lead to trails of infinite length and PoP values of incomprehensible size. This is where the framework's grounding in Physical Incompleteness (PI) becomes essential. The PI theorem posits that any finite, physical system has observational and computational limits—an "information horizon."
The Nibbler-PoP framework respects this constraint not as a limitation, but as a core design feature.
6.1. Lossy Compression as a PI-Compliant Mechanism
When a PoP value in a trail exceeds a predefined size threshold (e.g., what can be stored in a 64-bit integer), it cannot be stored exactly. Instead, it is lossily compressed.
Method: A common method is logarithmic compression (e.g., storing floor(log2(p)) instead of p). This preserves scale and order while capping the storage size.
Justification: Under PI, high-level abstractions do not require primordial precision. The fact that a pattern emerged from a deep and complex recursion is more important than the exact prime number that represents it.
6.2. FIFO Trimming of PoP Trails
Similarly, the trail itself cannot grow infinitely long. We apply a First-In, First-Out (FIFO) Trimming strategy.
Method: The trail is treated as a fixed-size queue. When a new subscript is added to a full trail, the oldest subscript is dropped or approximated.
Justification: This prioritizes recent, more relevant information. The "ancient history" of a pattern is less critical to its current interactions than its immediate parentage. The trimmed parts can still be approximated, providing a fuzzy but useful historical context.
7. Deeper Connections and Theoretical Extensions
The Nibbler-PoP framework resonates with deep concepts in logic, mathematics, and science.
7.1. The Gödel Omega Chain Analogy
There is a profound parallel between PoP trails and the ω-chains in Gödel's incompleteness theorems.
Gödel's System: Starts with a formal system T (like arithmetic), and creates an infinite hierarchy T, T + Con(T), T + Con(T + Con(T)), etc., where Con(T) is a statement of T's own consistency. Each level transcends the one below it.
Nibbler's System: Starts with base patterns (our T) and recursively generates new levels of meta-patterns that encapsulate the structure ("consistency") of the level below.
The Parallel: The PoP trail is a concrete enumeration of this recursive ascent. The act of trimming the trail is analogous to the fact that no finite system can ever complete the infinite ω-chain—it must operate within a bounded, incomplete prefix.
7.2. Group-Theoretic Structures
The tagged nodes in the Nibbler graph can be seen as elements of algebraic structures.
Cliques: Subgraphs with high interconnectivity can be treated as commutative groups, where the group operation on two nodes is the product of their PoP tags (since order doesn't matter).
Flows: Directed, sequential paths can be treated as non-commutative semigroups, where the order of operations (concatenation of trails) is critical.
This opens the door to using the tools of abstract algebra to analyze the structure of the generated knowledge graph.
8. Conclusion and Future Work
The Nibbler algorithm, enhanced with the Primes-of-Primes tagging system, represents a robust and scalable framework for autonomous knowledge discovery. It uniquely balances theoretical elegance with practical constraints by integrating number theory, recursive computation, and the physical reality of incomplete information. It provides a path from undifferentiated data to a structured, traceable, and self-compressing knowledge graph.
Open questions for future research include:
What are the optimal strategies for lossy compression? Is logarithmic scaling always preferable to hashing or other methods?
How should trails be merged when branches of the graph recombine?
Can the group-theoretic properties of the graph be used to predict its evolution or identify higher-order symmetries?
Can the framework be extended to handle temporal or dynamic data, where the graph itself is constantly changing?
Appendix: Table of P^(k)(n) for n ≤ 100, k ≤ 3
(This table illustrates the rapid but structured growth of the PoP operator, demonstrating its utility in creating a sparse set of identifiers.)
n	P^1(n)	P^2(n)	P^3(n)
1	2	3	5
2	3	5	11
3	5	11	31
4	7	17	59
5	11	31	127
...	...	...	...
100	541	3911	36887
(The full table as previously generated would be included here.)