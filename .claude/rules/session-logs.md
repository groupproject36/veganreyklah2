# Session Logs

At the end of **every** response — before finishing the turn — write a session log to `session-logs/`. The log captures the step-by-step reasoning followed before and during any prose writing, repository update, or code implementation, together with the changes made. It is a record kept for years.

## Filename

`<countdown>_<YYYYMMDD>-<HHMMSS>.md`, where the date and time are taken from the user's prompt (e.g. `99999_20260619-072600.md`).

The countdown prefix starts at `99999` and **decreases by one** for each new log — next `99998`, then `99997`, and so on — so the folder sorts newest-first under plain alphabetical order. To choose the next number, take the lowest prefix already in `session-logs/` and subtract one.

## Contents

- The step-by-step **thinking trace** and reasoning followed during the response.
- **Observations** about the changes, and any decisions or trade-offs taken.
- A list of the **files** created, modified, or deleted, each with a one-line why.

## Spirit

Write it plainly and honestly, in Radiant Style, so a future self or another agent can follow the work home. Commit the log alongside the changes it records.
