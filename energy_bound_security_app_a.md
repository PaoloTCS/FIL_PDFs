# Appendix A — Formal Security Lemma for Gödel‑Tile Puzzles
*(Supplement to “Energy‑Bound Security” briefing)*

---
## A.1  Threat Model

- **Adversary** `Adv_B` is any probabilistic polynomial‑time (PPT) Turing machine whose **irreversible bit‑operation budget** is bounded above by `B`.
- `Adv_B` may possess arbitrary quantum co‑processors, but any *classical* bit it measures or erases counts toward the same Landauer budget.
- The **ciphertext family** `Γ_B` is parameterised by a diagonal sentence `G_B` constructed for budget `B` as defined by Theorem 3.16.

> **Goal:** Show that *distinguishing* `Γ_B` from a random bit‑string is infeasible for `Adv_B` unless it violates the incompleteness bound.

---
## A.2  Cipher Construction Recap

1. Compute `G_B ≔ “¬□≤B G_B”` in a meta‑system with budget `≫ B`.
2. Derive one‑time pad `P = Hash(G_B ∥ nonce)`.
3. Ciphertext `Γ_B = (nonce, C)` where `C = K ⊕ P` and `K` is the session key.

*Verification* is trivial: recompute `G_B, P` once (budget `≈ log B`) and XOR.

---
## A.3  Indistinguishability Lemma

**Lemma A.1 (Gödel‑Tile IND).**
For any PPT adversary `Adv_B` limited to `≤ B` irreversible ops,

\[\Pr[Adv_B(Γ_B) = 1] \;\le\; \Pr[Adv_B(U_{|Γ_B|}) = 1] + \varepsilon(λ)\]

where \(U_{|Γ_B|}\) is a uniform random string of the same length and \(\varepsilon(λ)\) is negligible in the security parameter `λ`.

### Proof Sketch
1. `Adv_B` can distinguish `Γ_B` from random **iff** it recovers \(P\) with non‑negligible advantage.
2. Recovering \(P = Hash(G_B ∥ nonce)\) requires knowledge of \(G_B\) (pre‑image resistance of the hash family).  
3. **To output \(G_B\) or its hash, `Adv_B` must decide `G_B`**, i.e. produce a proof of either `G_B` or `¬G_B`.
4. By Theorem 3.16, no machine operating within budget `B` can decide `G_B`.
5. Therefore `Adv_B`’s distinguishing advantage reduces to the random oracle advantage, which is negligible. ∎

---
## A.4  Concrete Parameter Example

| Budget shell | `B` (irreversible ops) | Landauer heat @ 300 K (J) | Tile size (bits) | Hash length (bits) | Attack energy cost (J) |
|--------------|------------------------|---------------------------|------------------|---------------------|-------------------------|
| S₃ | 3×10³⁸ | 9×10¹⁷ | 64 | 256 | ≥ 1×10¹⁸ |

Even an exaFLOP data‑centre at 250 MW would require \> 25 GWh (≈5 days at full capacity) to reach `B`—and must still overcome hash pre‑image hardness.

---
## A.5  Discussion of Quantum Attackers

- Grover search reduces *step count* by √; defender compensates by doubling `B`.
- Hash pre‑image remains quantum‑resistant when chosen from SHA‑3 family with ≥256‑bit output.
- Measurement collapses every qubit used in key extraction ⇒ same Landauer heat per classical bit.

---
## A.6  Open Questions

1. **Side‑channel minimisation**: ensure hash and XOR steps leak no partial info before full pad reconstruction.
2. **Adaptive budget escalations**: dynamic puzzles that re‑randomise `G_B` if defender senses attacker heat output increasing.

---
*End of Appendix A*

