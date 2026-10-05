# Logan-Eberwein-RH-Weil-Window

Companion repository for the paper **"The truncated Weil quadratic form: inertia, visibility, structural measurements, and no-go theorems for the Riemann Hypothesis"** by Logan Eberwein (Independent Researcher, ORCID 0009-0004-5650-9313).

This is not a proof of the Riemann Hypothesis. The paper records structural results, no-go theorems, numerical laws and negative results about the truncated (window) Weil quadratic form, and the outcome of a year-long research program. The Lean 4 sources for the SR/Rees matrix program (paper §12) live in the separate repository [Logan-Eberwein-RH-Research](https://github.com/loganeberwein6/Logan-Eberwein-RH-Research).

## Contents

| folder | contents |
| --- | --- |
| `paper/` | the paper (PDF) |
| `code/weil_window/` | high-precision (python-flint arb) Weil-window computations for §1–§8 |
| `code/section11/` | the four §11 computations (Eisenstein, Nyman–Beurling, large deviations, Davenport–Heilbronn) |
| `code/exploratory/` | every exploratory script from the working sessions, kept for provenance (not all are cited in the paper) |
| `data/` | zeta zeros, Davenport–Heilbronn zeros, ζ sampled on the critical line |
| `outputs/` | logs of reruns of the cited computations |
| `supplementary/OPERATOR_SUMMARY.md` | the full operator-candidate ledger (297 candidates, 124 cycles) cited in §12.12 |

## Section-by-section map

| paper section | script(s) | notes |
| --- | --- | --- |
| §1 reference values | `code/weil_window/weilhp.py`, `val.py`, `ref.py` | 2N+1 scalar-functional assembly; outputs in `outputs/s1_*.txt` |
| §2 inertia identity (numerics) | `code/exploratory/it14.py`, `it15.py`, `fib.py` | double precision; uses `sig.py`/`sem.py` |
| §3 ground state = W⁻¹·cosh | `code/weil_window/ccm.py` | 600-bit arb |
| §4 kernel K(γ,γ) = 1 | `code/weil_window/kdiag.py` | |
| §5 visibility δ*(L,T), band edge, exact pair | `code/weil_window/run.py`, `edge.py`, `exact.py` | |
| §6 accuracy law | `code/weil_window/ccm2.py` | uses `data/zeros.pkl` |
| §7.2 height-dependent criterion | `code/weil_window/suff.py`, `exact72.py`, `conv72.py` | exact sinh form and basis check |
| §8.1–8.2 locality | `code/weil_window/local.py`, `local2.py` | double precision, N = 40 |
| §8.3 function field | `code/weil_window/ff.py` | output in `outputs/s8_3_function_field.txt` |
| §8.4 renormalized margin, planted crash | `code/weil_window/flow.py`, `crash.py` | |
| §8.6 prime-weight sensitivity / §9.4 | `code/weil_window/pos.py` | |
| §9 negative results (dictionary) | `code/exploratory/it5.py`–`it12b.py` | |
| §11.1 Eisenstein +1 law | `code/section11/gk.py` | exact rational arithmetic |
| §11.2 Nyman–Beurling floors | `code/section11/zsamp.py` → `cyc.py`, `dual.py`, `rat.py` | `zsamp.py` writes `data/zline_*.npy` (about 12 min) |
| §11.3 large deviations | `code/section11/ld.py`, `core11.py` | |
| §11.4 Davenport–Heilbronn | `code/section11/dh.py` → `dhnu.py`, `mono.py` | `dh.py` writes `data/dh_zeros.npy` (about 20 min) |

Scripts were written for a working directory containing their data files; copy the needed files from `data/` next to the script (or adjust the paths) before running.

## Environment

Python 3.12 with the packages in `requirements.txt`. High-precision runs use python-flint 0.9.0 (arb) and mpmath.

## Status of results

Numerical results are high-precision computations in truncated bases and are not interval-certified. The paper labels each result as theorem, numerical, heuristic, negative or retracted, and lists open problems in §14.

## Citation

See `CITATION.cff`.
