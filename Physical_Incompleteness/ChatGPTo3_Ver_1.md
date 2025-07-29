### Physical Inconsistency Theorem

*Any formal system Σ that (i) is powerful enough to encode self-reference and (ii) is implemented in a physical substrate with a finite information-capacity bound κ<sub>max</sub> must, on pain of violating that bound, eventually enter a state in which distinct syntactic objects share the **same** physical state.  Because the mapping “formula → physical realisation” ceases to be injective, Σ can no longer preserve the rule that contradictory strings occupy disjoint states; hence its **physical** realisation becomes inconsistent.*

---

### 1 Physical preliminaries

| Symbol           | Meaning                                                                                                   | Source                               |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| κ<sub>max</sub>  | maximum bits per Planck-volume the substrate can stably hold                                              |                                      |
| I<sub>max</sub>  | absolute bit budget of the device:  I<sub>max</sub> = min $\displaystyle\frac{E}{k_{B}T\ln2},\;κ_{\max}V$ | energy/entropy bound + Landauer cost |
| c<sub>comp</sub> | fastest possible irreversible bit-ops s<sup>-1</sup>                                                      |                                      |

---

### 2 Formal preliminaries

*Σ* is a first-order theory with Gödel numbering **gn**(·).
Let *W* := { all well-formed strings of Σ }.  Because Σ is recursively enumerable, |*W*| = ℵ<sub>0</sub> (countably infinite).

A **coding function**
$ϕ:\; W\;→\;{\cal P}$
assigns each string a distinct physical micro-state in the device’s state-set *𝒫* of size 2<sup>I<sub>max</sub></sup>.

---

### 3 Key lemmas

**Lemma 1 (Representation bound).**
|𝒫| = 2<sup>I<sub>max</sub></sup>.
If |*W*| > |𝒫| then ϕ cannot be injective (pigeon-hole principle).

**Lemma 2 (Self-referential overflow).**
Because Σ is Gödel-complete for syntax, there exists an *overflow sentence*
$Ω_N :=$ “*The code of this sentence is ≥ N*”.
Taking N > 2<sup>I<sub>max</sub></sup> forces **gn**(Ω<sub>N</sub>) to need more than I<sub>max</sub> bits, so ϕ(Ω<sub>N</sub>) is **undefined**.

**Lemma 3 (Collision of opposites).**
Choose any pair of strings (φ, ¬φ) whose Gödel numbers both exceed 2<sup>I<sub>max</sub></sup>.
Because ϕ is non-injective, there exist φ ≠ ψ with ϕ(φ) = ϕ(ψ).  In particular we can arrange ϕ(φ) = ϕ(¬φ).

---

### 4 Proof of the theorem

1. **Finite carrier.**
   I<sub>max</sub> bits are all that can be stored without violating the energy-information inequality.

2. **Surplus syntax.**
   Since |*W*| = ℵ<sub>0</sub> > 2<sup>I<sub>max</sub></sup>, Lemma 1 applies: ϕ cannot remain injective once Σ attempts to enumerate beyond 2<sup>I<sub>max</sub></sup> distinct strings.

3. **Undefined code.**
   The sentence Ω<sub>N</sub> of Lemma 2 refers to a Gödel number that physically cannot be encoded; yet Ω<sub>N</sub> is a legitimate string of Σ.
   Σ therefore contains well-formed sentences for which **no** physical state exists, contradicting the requirement that every theorem have a realisation.

4. **State collision.**
   By Lemma 3 the same physical micro-state simultaneously realises φ and ¬φ.  Observation of that state would **verify both** propositions, violating the principle that a consistent theory never derives a formula together with its negation.

5. **Conclusion.**
   Hence a physically realised Σ with unbounded syntax but bounded information capacity is forced into a situation where contradictory strings occupy the identical physical configuration.  The *formal* calculus may still be logically consistent, but its **physical instantiation is not**—it cannot preserve “distinct theorems → distinct states”.  We say the system has entered **physical inconsistency**.

---

### 5 Metasystem transition (resolution)

The framework therefore demands what Chapter 1 calls a *metasystem transition*: introduce new degrees of freedom (expand V or E) **or** drop sentences so that |*W*| ≤ 2<sup>I<sub>max</sub></sup> again.  Absent such a transition, continued operation inevitably violates the conservation laws and c<sub>comp</sub> bound that underwrite the device’s own physics, making stable computation impossible.

---

### 6 Relation to other bounds

* **Bekenstein-style language entropy.**  Treating each token as an information quantum saturates the same κ<sub>max</sub> bound derived for physical systems.
* **Speed limit.**  Even if capacity were increased, the enumeration needed to keep ϕ injective cannot outrun c<sub>comp</sub>, so overflow recurs in time rather than space.

---

### 7 Take-away

> **Consistency is not just a logical property; it is a physical privilege.**
> A self-referential system that tries to speak more bits than its body can bear is forced, by pure pigeon-hole arithmetic plus Landauer-Bekenstein physics, to compress logically incompatible statements into the same hardware state—thereby turning logical soundness into *physical* inconsistency.
