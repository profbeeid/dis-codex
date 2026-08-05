# Validation report

Engine unit tests: 10/10 passed.  
Ten-minute mechanics fixture: passed; it included a wait, a private note hidden from chair view, unfinished drafting, a directive, a revision request, and a delayed consequence.  
Private information: actor secrets were not passed to other fixed-role agents.  
Outcome authority: actors proposed actions; the orchestrator resolved world consequences.  
Session continuity: Session 2 actors received the locked Session 1 terminal state.

This is an exploratory lean calibration, not a protocol-valid registered baseline. To minimize tokens, each fixed-role agent returned a sequence of decisions for an entire session in one invocation; the scheduler therefore did not independently re-invoke each actor at every eligibility time. Pass B used three compact aggregate agent calls rather than isolated calls for all 21 roles. The results are sufficient for deck sizing and dais-load diagnosis, but should not be used to estimate fine-grained silence, timing, or model-to-model behavioral variance.

