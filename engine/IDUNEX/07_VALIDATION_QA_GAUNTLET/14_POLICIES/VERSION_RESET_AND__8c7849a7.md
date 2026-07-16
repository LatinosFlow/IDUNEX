# Version Reset and No Legacy Trace Policy

A regenerated baseline may read previous packages as sources, but runtime files must be re-emitted under the current official version.

Rules:
1. No legacy package names in active runtime.
2. No concrete project names in the motor.
3. No concrete subject/model names in the motor.
4. Previous examples are either removed or transformed into neutral placeholders.
5. Manifests are regenerated after all content changes.
6. ZIP hash is external because internal self-hash would alter the archive.

Failure blocks release.
