# Anchor Project Pitch — 16-Channel Flashing & Telemetry Fixture

## 60-Second Anchor Pitch (use verbatim)

> One of my core projects was supporting and validating a 16-channel flashing and telemetry fixture for battery modules. The problem was that the existing setup didn’t scale cleanly—when channel count increased, failures became harder to isolate and trust.  
>  
> My ownership was on the assembly-side test execution and validation. I worked on the fixture and harness interfaces, power distribution, and RS-422 comms bring-up, and I validated pinouts and continuity end-to-end so software could scale execution without introducing new failure modes.  
>  
> From a validation standpoint, I focused on setup sanity checks before power, clean port-to-harness mapping, and capturing evidence when things failed so we could quickly tell fixture issues from unit issues. I partnered closely with software as they scaled execution from 8 to 16 channels to make sure the hardware side stayed stable.  
>  
> The result was a station that scaled channel count while remaining repeatable and debuggable, and it was used reliably on the assembly line instead of constantly needing manual intervention.

Stop.

---

## Common Follow-Ups (answer in 1–2 sentences)

### What were the top failure modes?
> Most issues came down to harness or grounding problems and occasional comms instability. Validating pinouts and continuity early—before power-up—eliminated a lot of false failures.

### How did you know it was fixture vs DUT?
> I checked power behavior and comms consistency first, then swapped known-good units or channels and reviewed evidence logs to see whether the failure followed the unit or the setup.

### What did you own vs others?
> I owned assembly-side test execution, fixture and harness validation, and failure isolation. Final acceptance criteria and spacecraft-level testing lived with a different team.

---

## Notes
- Keep it to ~60 seconds unless asked to go deeper.
- Use concrete nouns (fixture, harness, RS-422, power).
- Don’t add outcomes unless they’re true and specific.
