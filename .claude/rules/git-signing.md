# Git Commit Signing

All commits MUST be GPG-signed. The global config already sets `commit.gpgsign=true` and names the signing key. Never bypass this:

- Never use `--no-gpg-sign` or `-c commit.gpgsign=false`
- Never skip hooks with `--no-verify`
- If a commit fails due to GPG, investigate and fix — do not disable signing

After pushing, remind the user to upload their public GPG key to GitHub and Codeberg if commits show as "Unverified" on those platforms.

Push to all four remotes when the user asks:
- `origin` (Codeberg veganreyklah2)
- `github` (GitHub veganreyklah2)
- `gp36-codeberg` (Codeberg groupproject36)
- `gp36-github` (GitHub groupproject36)
