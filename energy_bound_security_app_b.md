# Appendix B — Reference Tables and Conversion Charts
*(Supplement to “Energy‑Bound Security” briefing)*

---
## B.1  Landauer Cost vs. Temperature

| Temperature (K) | `k_B T ln 2` (J per bit erase) | Ops per joule (`1 / cost`) |
|-----------------|---------------------------------|----------------------------|
| 1 K  | 9.6×10⁻²³ | 1.0×10²² |
| 4 K  | 3.8×10⁻²² | 2.6×10²¹ |
| 20 K | 1.9×10⁻²¹ | 5.3×10²⁰ |
| 77 K (LN₂) | 7.3×10⁻²¹ | 1.4×10²⁰ |
| 300 K | 2.9×10⁻²¹ | 3.4×10¹⁹ |
| 350 K (shipboard warm) | 3.4×10⁻²¹ | 2.9×10¹⁹ |

**Note:** Attacker benefits little from extreme cryogenics; heat extraction overhead cancels gains.

---
## B.2  Joules ↔ Irreversible Operations Conversion (300 K)

| Energy Budget (J) | Equivalent bit‑ops `B` |
|-------------------|-------------------------|
| 1 kJ | 3.4×10²¹ |
| 1 MJ | 3.4×10²⁴ |
| 1 GJ | 3.4×10²⁷ |
| 1 TJ | 3.4×10³⁰ |
| 1 PJ | 3.4×10³³ |

---
## B.3  Sample Tile Parameters

| Defender capability | Max attacker budget tolerated (`B`) | Tile size (bits) | Defender compute budget (`≈10B`) | Suggested hash output (bits) |
|---------------------|--------------------------------------|------------------|-----------------|------------------------------|
| Forward FOB (diesel, 5 MW) | 10³³ | 48 | 10³⁴ | 192 |
| Carrier group (nuclear, 100 MW) | 10³⁵ | 60 | 10³⁶ | 256 |
| CONUS DC (250 MW) | 10³⁶ | 64 | 10³⁷ | 256 |
| National lab (1 GW) | 10³⁸ | 72 | 10³⁹ | 384 |

Tile size chooses the Gödel sentence bit‑length; hash length ≥ 4× tile size for collision resistance.

---
## B.4  Grid and Reactor Benchmarks

| Facility / Platform | Typical electric output | Run‑time to supply 1 GJ | Ops (300 K) achievable |
|---------------------|-------------------------|-------------------------|-----------------------|
| Household circuit | 5 kW | 2 days | 3.4×10²⁷ |
| Google nuclear PPA site | 300 MW | 55 min | 1×10³¹ |
| Virginia‑class reactor | 200 MW | 1.4 h | 7×10³⁰ |
| Large‑scale SMR farm | 1 GW | 17 min | 3.4×10³¹ |

---
## B.5  Heat‑Signature Detection Thresholds

Assuming 50 % cooling efficiency and 300 K exhaust:

| Dissipated heat (J) | Average power over 30 days | Thermal signature (°C above ambient) at 1 km² facility |
|---------------------|---------------------------|------------------------------------------------------|
| 10¹⁶ (2.8 GWh) | 3.8 MW | +25 °C |
| 10¹⁷ | 38 MW | +60 °C |
| 10¹⁸ | 380 MW | +130 °C (visible in IR) |
| 10¹⁹ | 3.8 GW | Industrial‑scale plume |

---
*End of Appendix B*

