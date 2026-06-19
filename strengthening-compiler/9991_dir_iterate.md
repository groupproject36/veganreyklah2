# 9991 — Dir.iterate: name invariants and exhaustion state

**Target:** `rye/lib/std/Io/Dir.zig` — `Iterator.next`
**Parity:** 13/13 GREEN

---

## What we state

`Iterator.next` wraps `Reader.next`. The `Reader` filters `.` and `..` internally — every entry it returns is a real directory entry. That means the two classes of return are well-defined:

- **non-null**: a real entry whose name the OS accepted and stored
- **null**: the directory is exhausted and the reader has settled into `.finished`

Pass 9991 makes both classes explicit with postcondition assertions.

### The strengthened function

```zig
pub fn next(it: *Iterator, io: Io) Error!?Entry {
    it.reader.buffer = &it.reader_buffer;
    const result = try it.reader.next(io);
    // Postcondition: every returned entry has a non-empty name within the OS
    // limit; null means the directory is exhausted and the reader is finished.
    if (result) |entry| {
        assert(entry.name.len > 0);               // every directory entry has a name
        assert(entry.name.len <= max_name_bytes);  // the name fits the OS limit
    } else {
        assert(it.reader.state == .finished);      // null means iteration is complete
    }
    return result;
}
```

### Assertions and their authority

| Assertion | Kind | Authority |
|-----------|------|-----------|
| `entry.name.len > 0` | postcondition | POSIX: `d_name` is never the empty string |
| `entry.name.len <= max_name_bytes` | postcondition | `max_name_bytes` mirrors `NAME_MAX`; the OS already enforced this |
| `it.reader.state == .finished` | postcondition | `Reader.next` settles to `.finished` before returning null |

All three state facts the kernel already enforces — we surface them so callers can read them at a glance and so a future regression in the reader triggers an assertion rather than silent misbehavior.

---

## Parity test

`rye/tests/dir_iterate_test.rye` — `pub fn main(init: std.process.Init) !u8`

Creates `/tmp/rye_dir_iterate_test` with one known file (`rye_seed.txt`), iterates, confirms name invariants hold, confirms the second call returns null and `reader.state == .finished`, then cleans up.

Deterministic by construction: exactly one entry, no ordering uncertainty.

Output (both baseline and Rye std):
```
rye: Dir.iterate assertions confirmed (name invariants, exhaustion state).
```
Exit code: 0.

---

## Corpus after this pass

13 programs. All GREEN.

`dir_iterate_test fs_boundary_test mem_diff_test sha3_256_test sha3_256_boundary_test sha3_512_test sha3_boundary_test version_test call_paths_test ed25519_sign_test x25519_agree_test aead_seal_test sealed_message_test`

---

## Position in the stack

| Pass | Subject |
|------|---------|
| 9999 | Manifesto |
| 9998 | SHA3-512 |
| 9997 | Keccak generic |
| 9996 | SHA3-512 boundary |
| 9995 | Ed25519 + X25519 + AEAD |
| 9994 | SHA3-256 |
| 9993 | mem diff primitives |
| 9992 | std.Io.Dir filesystem boundary |
| **9991** | **Dir.iterate name invariants + exhaustion state** |

The four-pass strengthening frontier (9994–9991) is now complete. Mantra seed may begin.
