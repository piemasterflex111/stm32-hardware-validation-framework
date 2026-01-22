# Interview Pitches — Hardware Test / Validation / Test Automation

This file contains the **exact pitches to say**, mapped to real interview moments.  
Do not improvise. Pick the right one and stop when finished.

---

## 1) Recruiter Opener — 10–15 seconds (DEFAULT)

**Use when:**  
“Tell me about yourself.”

> I’m a hardware test and validation engineer with aerospace and defense experience, strongest in assembly-side test execution—fixtures and harness interfaces, power and comms bring-up, and bench debug. At Terran Orbital I supported battery module testing including a 16-channel flashing and telemetry fixture and helped qualify electrical test stations to reduce false fails.

Stop.

---

## 2) Hiring Manager Background — 60–90 seconds

**Use when:**  
“Walk me through your background.”

> I started in embedded hardware roles doing bring-up, flashing, and bench debug, and I wrote small Python utilities to make those workflows repeatable.  
>  
> Then I moved into defense electronics qualification at Mercury, running MIL-STD-810 testing and driving failure investigations to closure with documented corrective actions.  
>  
> At Terran Orbital I focused on assembly-side test execution and validation support for battery modules and power subsystems—fixtures and harness interfaces, power and comms bring-up, and evidence-based debugging. A key example was supporting a 16-channel flashing and telemetry fixture with controlled power and RS-422, and validating harness mapping end-to-end while partnering with software to scale execution.  
>  
> In my lead role I built more of the supporting infrastructure—telemetry logging, clearer pass/fail criteria, and traceability so failures were faster to diagnose.  
>  
> Outside of work, I’m building a small Python test runner that produces per-serial results and evidence, and I’m extending it with basic instrument control and CAN log capture.

Stop. Let them drill.

---

## 3) Anchor Project Pitch — 60 seconds (CORE TECHNICAL STORY)

**Use when:**  
“Tell me about a project you worked on.”  
“Walk me through a test system.”

> One of my core projects was supporting and validating a 16-channel flashing and telemetry fixture for battery modules. The problem was scaling channel count without turning failures into guesswork.  
>  
> My ownership was assembly-side test execution and validation. I worked the fixture and harness interfaces, power distribution, and RS-422 comms bring-up, and I validated pinouts and continuity end-to-end so software could scale execution without introducing new failure modes.  
>  
> When issues came up, I isolated station versus DUT first—power and current behavior, comms consistency, then controlled swaps across channels or known-good units—so we didn’t chase false failures. Because operators ran the station, I also pushed for simple setup checks and clear evidence capture.  
>  
> The result was a station that scaled from 8 to 16 channels while staying repeatable and debuggable on the assembly line.

Stop.

---

## 4) Debugging Pitch — 30–45 seconds

**Use when:**  
“How do you debug hardware issues?”  
“What do you do when a test fails?”

> I isolate station versus DUT first. I start with power rails and current draw to confirm the unit is alive, then check the physical comms layer and instrument state. After that I do controlled swaps—known-good unit, channel, or cable—to see what the failure follows. I rely on evidence before changing anything so fixes are targeted, not guesswork.

Stop.

---

## 5) Automation Credibility Pitch — 30 seconds

**Use when:**  
“What automation have you done in Python?”  
“How do you approach test automation?”

> I use Python to make tests repeatable and the data trustworthy. My focus is per-serial execution, explicit limits for pass/fail, and structured results with evidence so reruns don’t contaminate data. I separate hardware I/O, test logic, and logging so tests stay maintainable as stations evolve.

Stop.

---

## 6) Scope Honesty Clarifier — 10 seconds (ONLY IF ASKED)

**Use when:**  
“Did you own final acceptance?”  
“Were you the ATE owner?”

> My ownership was assembly-side test execution and validation support. Final module acceptance before spacecraft integration was owned by a different team.

Stop. Do not justify.

---

## 7) Manufacturing Pivot Pitch — 15–20 seconds (ONLY FOR MFG ROLES)

**Use when:**  
Interviewing for Manufacturing / NPI / Production roles.

> I’m a manufacturing engineer in aerospace and defense focused on high-voltage battery module production. I’ve owned end-to-end build flow—process definition, fixtures and tooling, work instructions, and production readiness—and I supported assembly-side testing to prevent defects from moving downstream.

Stop.

---

## Decision Rule (memorize)

- **Recruiter screen** → Pitch #1  
- **Hiring manager background** → Pitch #2  
- **Technical deep dive** → Pitch #3, then #4  
- **Automation questions** → Pitch #5  
- **Scope challenge** → Pitch #6  
- **Manufacturing roles only** → Pitch #7

Do not blend pitches. Do not extend unless asked.
