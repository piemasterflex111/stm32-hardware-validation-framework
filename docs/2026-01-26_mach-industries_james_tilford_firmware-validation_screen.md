# Interview Coaching Log — Mach Industries (James Tilford) — Phone Screen Prep

- **Date:** 2026-01-22
- **Candidate:** Payam Adloo
- **Interviewer:** James Tilford — Principal Embedded Consultant
- **Target Role:** Firmware Validation Engineer (adjacent: Embedded Test / HW-FW Validation / HIL Test)
- **Session Type:** 30-minute first-call screen simulation + coaching
- **Goal:** Produce “strong hire” signal: ownership, HW/FW debug, automation rigor, clear communication

---

## Context Assumptions (Mach / James)

- Mach moves fast. HW + embedded systems. Ownership is expected.
- James is senior/technical. Probes fundamentals and “did you actually do it.”
- If answers are fuzzy or unquantified → likely reject.

---

## Candidate Baseline (conservative claims)

- **Experience:** 8 years total engineering; ~5 years manufacturing/test/validation-heavy
- **Strengths:** HW/FW/test boundary, bring-up, fixtures/harness interfaces, power+comms sequencing, bench debug, root-cause
- **Tools comfort:** scope, DMM, basic logic analyzer, bench PSU, reflashing, logs, triage
- **Software:** Python tools for logging, analysis, evidence, repeatable pass/fail checks
- **Weaker areas:** deep firmware development, deep protocol depth, FAANG-level formal frameworks
- **Known gap:** EE fundamentals under pressure (example: resistor divider)

---

## Interview Simulation Structure (planned)

1) 60-second opener (fit for Mach + role)  
2) 3–4 deep dives on one anchor project (validation + automation)  
3) Fundamentals check (embedded + EE basics)  
4) Debug scenario (HW/FW boundary)  
5) Test strategy scenario (regression + coverage + reliability)  
6) Close: candidate questions + next steps

---

## Q/A Log + Coaching

### Q1 — Opener
**James:** “Alright Payam. Quick intro. Tell me about yourself and why Mach.”

**Payam (actual):**
- Electrical + manufacturing test engineer background
- HW/FW/test boundary: bring-up, validation, production issues
- Worked with EE + firmware teams at system level
- Leaning into firmware validation + test automation

**Coach Grade:** **WEAK PASS**

**Missing:**
- No concrete outcomes, scale, artifacts
- No “why Mach” tied to speed/ownership/rigor
- Not enough proof in 60 seconds

**Better answer (recommended):**
- Mention: bring-up ownership, fixtures/harness, reflashing/logs, Python pass/fail + evidence
- Tie to Mach: fast HW iteration + need validation rigor and ownership

**Trap follow-up expected:**
- “Give me one concrete example. What behavior did you validate and what did you personally build/own?”

---

### Q2 — Anchor example selection
**James (trap):** “Give me one concrete example… what did you validate and what did you build/own?”

**Payam (actual):**
- Gatekeeper RF system module with FSK
- Each new firmware build: verify features, run test cases, document

**Coach Grade:** **WEAK PASS**

**Missing:**
- Still vague: stimulus/measurement/limits/tools/bug found
- Sounds like manual QA unless quantified and structured

**Trap follow-up expected:**
- “Pick one test case. Stimulus, measurement, pass/fail limits, tools.”

---

### Q3 — Test case drill-down
**James:** “Pick one test case. Stimulus, measurement, limits, tools.”

**Payam (actual):**
- Shopping cart wheel system: MCU + magnetometer + accelerometer
- Hall effect for wheel rotation count
- No Bluetooth (dead reckoning to conserve battery)
- Signals: 8 kHz and 2.4 GHz
- Used beacon dongle
- UART via PuTTY @115200; sent MAC address commands
- Updated FW via command; verified by packets sent/received

**Coach Grade:** **WEAK PASS** (good detail; too long; still missing crisp limits)

**What to tighten:**
- State ONE test in first sentence
- Add limits (or explicitly say limits were defined but not recalled)
- Clarify reproducibility and evidence artifacts

**Trap follow-up expected:**
- “How did you detect packet loss/corruption and make it reproducible across builds?”

---

### Q4 — Rigor / reproducibility check
**James (trap):** “How exactly did you log, detect loss/corruption, and make it reproducible?”

**Payam (actual):**
- Logged terminal window
- Verified packet count
- Detected issues if expected sum not sent
- Reported to firmware engineer
- Needed clean RF environment (avoid other transmitters)

**Coach Grade:** **FAIL**

**Reason:**
- Sounds manual and non-deterministic
- No parsing, no structured artifacts, no flake controls
- “No other signals nearby” is not a reproducibility strategy

**Better answer (recommended):**
- Save UART output to file with timestamps + build ID + test ID
- Detect via sequence gaps / checksum/CRC / timing violations
- Environment controls documented; classify failures (DUT vs INFRA)

**Trap follow-up expected:**
- “If I asked you to automate this regression, what would you build first, and what would you keep manual initially?”

---

### Q5 — Automation design question
**James:** “What would you automate first? What stays manual initially?”

**Payam (actual):**
- Build infrastructure in layers
- Capture fw version, module ID, timestamp, test case, station details
- Capture results/evidence/failure modes
- Manual packet counts initially to validate infrastructure correctness

**Coach Grade:** **WEAK PASS**

**Missing:**
- Concrete first deliverable: CLI runner + folder outputs + parsing checks
- Explicit pass/fail logic and flake controls
- Clear “what stays manual” rationale (stimulus reliability)

**Trap follow-up expected:**
- “What files do you save per run and what does a FW engineer get in 2 minutes?”

---

### Q6 — Artifact structure / traceability
**James:** “Exactly what artifacts per run? What does FW get in 2 minutes?”

**Payam (actual):**
- CLI inputs: fw_version, dut_sn, test_id
- Creates folder per SN + per run
- `metadata.json`, `results.csv`, `report.md`, `evidence/` with per-test txt
- Repo layout: `src/ results/ docs/ configs/ data/ tools`
- Firmware engineer uses `report.md` and `results.csv`

**Coach Grade:** **PASS**

**Enhancements:**
- Call out raw UART / packet capture logs explicitly
- `metadata.json` should include: build hash, tool versions, station ID, instrument IDs
- Make the 2-minute flow explicit (report → results → raw evidence)

**Next question queued by coach:**
- EE fundamentals: resistor divider formula + loading effect
  - (Not answered in this session)

---

## Strong Material Identified (use in the real call)

### A) Anchor recent proof (recommended to lead with)
**Mini ATE-style validation runner**
- Per-serial and per-run isolation
- Evidence package per execution:
  - `metadata.json` for traceability
  - raw `results.csv` source of truth
  - auto `report.md` for humans
  - deterministic evidence files tied to TEST-IDs
- Design choice: reruns never overwrite history; run ID in folders not filenames

### B) What still must be added to sound “strong hire”
- Quantified limits (or acknowledge limits existed without guessing numbers)
- One closed-loop regression story: detected → isolated → outcome
- Flake control strategy: timeouts, retries, classify INFRA vs DUT, s
