Dimensional Formalism and Disambiguation in Semantic Interfaces

Author: Paolo PignatelliDate: 2025‑07‑19 (rev‑A)

1 · Conceptual Foundation – Dimensions as Additive Constraints

“Where shall we meet in New York?”Answer: 6th Avenue · 45th Street · Apartment 6B · 3 PM.

Each attribute (avenue, street, apartment, time) removes ambiguity. We therefore define:

Disambiguating Dimension – Any attribute, latent factor, or degree‑of‑freedom along which an entity can be compared, filtered, or separated from peers. Adding a new dimension reduces semantic entropy, even if that dimension is purely mathematical or conceptual.

Principle of Contextual Dimensionality – The dimensionality of an object is always defined relative to the universe (reference set) in which it is embedded. Conceptually, you refine along orthogonal axes until uncertainty collapses to a single micro‑state; equivalently, entropy is driven to unity—complete, unique distinguishability within that universe.

2 · Orthogonality and Hierarchies of Dimension Sets

Orthogonality gauges informational independence. A family  is strictly orthogonal when


In practice we encounter hierarchies of orthogonality:

Tier‑0 orthogonality – Empirically independent (e.g., pixel‑hue vs. audio‑frequency).

Tier‑1 orthogonality – Independent after a shared transform (e.g., optic‑flow vs. melodic‑contour after time alignment).

Tier‑2 orthogonality – Independent only in an abstract latent manifold (e.g., intent vs. emotion after an encoder).

These tiers form a lattice where parent nodes represent coarse independent sets and children represent finer sub‑dimensions.

3 · Dimensional Disambiguation in an Immersive UI

In the spherical interface all candidate screens start maximally ambiguous. Each active dimension slices the candidate set until a unique node remains. Typical classes are:

Class

Examples

Purpose

Spatial



Global layout

Visual

Color, edge style

Topic / affect

Auditory

Fundamental‑freq, ADSR motif

Context cue

Behavioral

Gaze vector, gesture type

Relevance weight

Abstract Latent

Sentiment, topic embedding

Semantic intent

Ontological

Axiomatic truth status, necessity

Logical filtering

4 · Dimension–Entropy Reduction Law

Let  be the initial entropy over a candidate set . Activating dimension  yields . After  dimensions:

Resolution succeeds once .If dimensions are not strictly orthogonal, the effective gain is  with  the redundancy coefficient.

5 · Taxonomy of Dimension Sub‑Spaces

We generalize beyond the human sensorium. The global set

collects four orthogonal super‑spaces:

Empirical () – Raw sensor data (not limited to five senses: could include LIDAR, neutrino flux, qubit phase, etc.).

Constructed () – Algorithmic aggregates or transforms (e.g., optic‑flow, mel‑spectrogram, wavelet coefficients).

Semantic () – Learned abstractions and latent embeddings (topic vectors, user intent, emotional valence).

Ontological () – Formal or metaphysical attributes (truth modalities, necessity/possibility, causal potency).

5.1 Representative Dimensions

Super‑Space

Example Dimensions

Symbol

Notes



Photon flux, EM‑phase, muon count



Measurable via instrument



Optical flow, MFCC vector, graph centrality



Derived numerically



Sentiment score, intent embedding



Learned via model



Logical truth value, necessity degree



Abstract / modal

6 · Granularity and Refinement Operators

A dimension may itself possess granularity:

Atomic granularity – Boolean or categorical (e.g., truth: ).

Discrete graded – Few ordered bins (e.g., sentiment: negative → neutral → positive).

Continuous – Arbitrarily fine (e.g., wavelength in nm).

Refinement operator  maps a coarse dimension  to a finer subdivision :

where mutual information satisfies .

Granularity interacts with orthogonality: excessive refinement may introduce correlation with other dimensions, raising . The system therefore searches for a Pareto‑front between entropy reduction and dimensional redundancy.

7 · Tensor Products Across Super‑Spaces

Cross‑modal meaning often arises by combining heterogeneous dimensions. Formally, for super‑spaces :


Basis element  binds attributes at arbitrarily different ontological levels (e.g., necessity  × melodic contour ).Interaction kernels  promote salient pairings and prune the exponential basis.

8 · Operational Guidelines

Designing Dimension Pools – Start coarse with one orthogonal set per super‑space. Add refined sub‑dimensions only when entropy budget demands.

Dynamic Pool Pruning – Periodically compute redundancy coefficients  and retire low‑value dimensions.

UI Mapping – Expose empirical sliders (e.g., wavelength) and ontological toggles (e.g., ‘mandatory’ vs. ‘optional’ attribute) for power users.

9 · Future Work

Automated Orthogonality Discovery – Use ICA/PCA or information‑geometric methods to learn orthogonal latent axes beyond human intuition.

Meta‑Dimensional Reasoning – Treat granularity itself as a tuneable dimension; implement zoom‑in/out gestures that refine or coalesce dimensions on demand.

Causal‑Tensor Extensions – Augment tensor products with directed edges encoding cause→effect, enabling predictive filtering across .

Next‑Step Prompt – “Demonstrate an adaptive refinement algorithm that balances entropy gain against redundancy when adding new ontological dimensions.”

