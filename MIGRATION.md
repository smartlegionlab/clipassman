# Migration Guide: v2.x.x to v3.x.x

## ⚠️ Breaking Change Notice

**CLIPassMan v3.x.x is NOT backward compatible with v2.x.x**

Passwords generated with older versions cannot be regenerated using v3.x.x due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**v3.x.x introduces fundamental improvements:**

- **Cross-platform determinism** — same passwords as Python, Go, Kotlin, JS, C#
- **Decentralized by design** — no central servers, no cloud dependency
- **Stronger cryptographic algorithm** — based on SHA-256
- **Better cross-platform consistency** — identical results across all platforms

---

## What changed:

- Core algorithm now uses **SHA-256** instead of previous methods
- Same secret + same length = same password across all platforms
- Old passwords **cannot be regenerated** with new version

---

## Migration Steps

### Step 1: Install old version to retrieve existing passwords

```bash
pip install clipassman==2.2.2
```

### Step 2: Retrieve existing passwords

For each entry, generate the actual password using your secret phrase with the old version. Keep these passwords accessible during migration.

### Step 3: Upgrade to v3.x.x

```bash
pip install --upgrade clipassman
```

### Step 4: Generate new passwords

Using the **same secret phrases and lengths**, generate new passwords with the new version.

### Step 5: Update your services

Replace old passwords with newly generated ones on each website/service.

### Step 6: Verify

- Log in using new passwords
- Confirm regeneration works (same secret → same password)

---

## Important Notes

- **No automatic migration** — manual regeneration required for each password
- **Your secret phrases remain the same** — only generated passwords change
- Old passwords are not compatible with new version
- Test with non-essential accounts first

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)

