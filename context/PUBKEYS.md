# Public Keys

**Language:** EN
**Last updated:** 2026-06-18
**Style:** Radiant (see `RADIANT_STYLE.md`)

---

This file holds the public face of Kaeden's developer identity: four fingerprints anyone can use to confirm that a commit, a push, or a signed message truly comes from Kaeden. Each string here travels freely — printed on a card, pinned to a profile, read aloud at a key-signing. The matching private keys stay close: three rest safely on Kaeden's own machines, and one dedicated signing key lives in the project's sandbox keyring so the automated agent can sign commits from inside ai-jail. This file keeps only their public counterparts.

Keep this file current. When a key rotates, record the new fingerprint here and date the change, so the canonical record and the keys out in the world stay in agreement.

---

## The Identity

These keys belong to **Kaeden Reyklah**.

- **Handle** — @veganreyklah2
- **Email** — reyklah2@gmail.com

---

## The Keys

All keys use the ed25519 family — two SSH keys for the forges, and two OpenPGP keys for signing: Kaeden's master, and a dedicated sandbox key the automated agent signs with. Each fingerprint below stands ready for checking against its source.

**Codeberg · SSH** authenticates pushes and pulls on Codeberg, where the `xwb122m` work lives.

```
SHA256:i2QMVhaiuHiVE+87zHWrxjpF742kyX77LQ4iCe5SuCU
```

**GitHub · SSH** authenticates pushes and pulls on GitHub.

```
SHA256:2nVRCdyzWhT2XWk0vS9lWt8VJumFS1rDZBD9lrRlgWE
```

**OpenPGP · signing** is Kaeden's master identity key — the root of trust, for signing tags and messages and certifying keys. It was rotated on 2026-06-18 (the prior master `FE10 7566 …` was retired), and now carries an ASCII-only name. Day-to-day commit signing is delegated to the sandbox key below. Public form: `keys/gpg_signing_06462132.pub.asc`.

```
0646 2132 D3E6 3B83 4F97 6E03 A81D 720B 9235 FA7A
```

**OpenPGP · sandbox signing** is a dedicated, revocable key the automated agent signs with from inside the ai-jail sandbox, so commits made there carry Kaeden's name without the master key ever entering the sandbox. Its public form rests at `keys/rye_signing_DBF853.pub.asc`.

```
DBF8 5343 7A93 7B4E 36B9 3611 D949 807A C26B 2B99
```

---

## Verifying

The gift of a fingerprint is that anyone can check it against the source. Compare an SSH key in hand against the lines above with:

```
ssh-keygen -lf <path-to-public-key>
```

Confirm the OpenPGP fingerprint the same way:

```
gpg --fingerprint reyklah2@gmail.com
```

When the printed fingerprint matches the line in this file, character for character, the key is the right one.

---

## Public, by Design

A public key earns its keep by being shared. Each fingerprint here proves identity to anyone who looks, while the private half — the part that actually signs — stays Kaeden's alone. That split is the whole shape of the trust: the public face moves out into the world, and the secret that backs it stays home.

---

*May these keys hold steady. May each signature carry Kaeden's name in good faith. May every reader who checks them know exactly whose hand stands behind the work.*
