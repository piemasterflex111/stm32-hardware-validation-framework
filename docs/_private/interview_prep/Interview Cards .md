# Interview Cards (VS Code)

Rule: Read the **Prompt**. Speak the **Say** out loud. Stop when done.
Do not add extra sentences unless asked.

---

## Card 1 — Recruiter Opener (10–15s)
**Prompt:** “Tell me about yourself.”

**Say:**
I’m a hardware test and validation engineer with aerospace and defense experience, strongest in assembly-side test execution—fixtures and harness interfaces, power and comms bring-up, and bench debug. At Terran Orbital I supported battery module testing including a 16-channel flashing and telemetry fixture and helped qualify electrical test stations to reduce false fails.

---

## Card 2 — Anchor Project (60s)
**Prompt:** “Tell me about a project you worked on.” / “Walk me through a test system.”

**Say:**
One of my core projects was supporting and validating a 16-channel flashing and telemetry fixture for battery modules. The problem was scaling channel count without turning failures into guesswork.

My ownership was assembly-side test execution and validation. I worked the fixture and harness interfaces, power distribution, and RS-422 comms bring-up, and I validated pinouts and continuity end-to-end so software could scale execution without introducing new failure modes.

When issues came up, I isolated station versus DUT first—power and current behavior, comms consistency, then controlled swaps across channels or known-good units—so we didn’t chase false failures. Because operators ran the station, I pushed for simple setup checks and clear evidence capture.

The station scaled from 8 to 16 channels and stayed repeatable and debuggable on the assembly line.

---

## Card 3 — Debug Method (30–45s)
**Prompt:** “How do you debug hardware issues?” / “What do you do when a test fails?”

**Say:**
I isolate station versus DUT first. I start with power rails and current draw to confirm the unit is alive, then check the physical comms layer and instrument state. After that I do controlled swaps—known-good unit, channel, or cable—to see what the failure follows. I rely on evidence before changing anything so fixes are targeted, not guesswork.

---

## Card 4 — Scope Clarifier (10s)
**Prompt:** “Did you own final acceptance?” / “Were you the ATE owner?”

**Say:**
My ownership was assembly-side test execution and validation support. Final module acceptance before spacecraft integration was owned by a different team.

---

## Card 5 — Manufacturing Opener (15–20s) [Only if screening for mfg roles]
**Prompt:** “Tell me about yourself.” (Manufacturing roles)

**Say:**
I’m a manufacturing engineer in aerospace and defense focused on high-voltage battery module production. I’ve owned end-to-end build flow—process definition, fixtures and tooling, work instructions, and production readiness—and I supported assembly-side testing to prevent defects from moving downstream.


## Card 6 — Automation Proof (20–30s)
**Prompt:** “What automation have you done in Python?” / “How do you approach test automation?”

**Say:**
I use Python to make tests repeatable and the data trustworthy. I structure runs per serial number, capture measured values against explicit limits, and write results plus evidence so reruns don’t contaminate data. I keep hardware I/O, test logic, and logging separate so it stays maintainable as the station evolves.

## Card 7 — Why This Role (10–15s)
**Prompt:** “Why are you looking?” / “Why this role?”

**Say:**
I’m looking for a role where test and validation is the core—owning fixtures, instrumentation, automation, and debug with the electrical and firmware teams. That’s where I’ve been strongest and where I want deeper ownership.

# Anchor Project — Follow-Up Q&A (Card 2)

## Follow-Up 1: “What were the main failure modes?”

**Say (1 sentence):**  
Most issues came down to harness or grounding problems and occasional comms instability, which we caught early by validating pinouts and continuity before power-up.

Stop.

---

## Follow-Up 2: “How did you know it was the station versus the DUT?”

**Say (1 sentence):**  
I isolated station versus DUT by checking power behavior and comms consistency first, then doing controlled swaps with known-good units or channels to see what the failure followed.

Stop.

---

## Follow-Up 3: “What did you personally own versus other teams?”

**Say (1 sentence):**  
I owned assembly-side test execution, fixture and harness validation, and failure isolation, while final acceptance criteria and spacecraft-level testing were owned by a different team.

Stop.

# Anchor Project — Hard Follow-Ups (Senior HM Level)

## Q1 Hard Follow-Up: “What checks did you add to reduce false fails?”
**Say (1 sentence):**  
I pushed for simple preflight checks—continuity/short checks, port-to-channel mapping verification, and a known-good baseline run—so setup issues were caught before we blamed the DUT.

Stop.

---

## Q2 Hard Follow-Up: “What did you measure, with what tools, before swapping anything?”
**Say (1 sentence):**  
Before swapping, I verified rail voltages and current draw with a DMM/supply readback and confirmed comms at the physical layer, so the swap test was a last step, not the first guess.

Stop.

---

## Q3 Hard Follow-Up: “If you owned it end-to-end, what would you change in the design?”
**Say (1 sentence):**  
I’d formalize station self-checks and evidence capture—automated harness validation, clearer failure codes, and a repeatable bring-up sequence—so operators can’t accidentally create ambiguous failures.

Stop.



----------------------------------------
1) Make a 10-minute daily drill (do this for 3 days)

Record on your phone. One take each.

Recruiter opener (Card 1) — 15s

Anchor project (Card 2) — 60s

Follow-ups — answer these 3 in one sentence each (no extra words):

main failure modes

station vs DUT

what you owned

Hard follow-ups — same thing: one sentence each.

Rule: if you talk past the sentence, you restart.

2) Build “interview cards” in VS Code (simple, fast)

Create interview_cards.md with only:

Card 1 (15s)

Card 2 (60s)

Follow-ups (3) + Hard follow-ups (3)

Nothing else. You want tiny and retrievable.

3) Run a live mock with me

When you’re ready, paste:
“Start recruiter screen. Cut me off if I ramble.”
I’ll ask the questions in order and force tight re-answers.