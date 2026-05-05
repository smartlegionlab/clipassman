# Migration Guide: Previous versions to v4.0.0

> **📌 Version Note:** CLIPassMan v4.0.0 uses smartpasslib v4.0.0, which introduces breaking changes from all previous versions. All smartpasslib implementations (Python, C#, JS, Go, Kotlin) now share the same algorithm.

## ⚠️ Breaking Change Notice

**CLIPassMan v4.0.0 is NOT backward compatible with previous versions (v2.x.x, v3.x.x)**

Passwords generated with older versions cannot be regenerated using v4.0.0 due to fundamental changes in the deterministic generation algorithm.

---

## Why the change?

**CLIPassMan v4.0.0 (smartpasslib v4.0.0) introduces fundamental improvements:**

- **Dynamic iteration counts** — deterministic steps vary per secret (15-30 for private, 45-60 for public)
- **Expanded character set** — Google-compatible symbols (26 special chars + A-Z + a-z + 0-9)
- **Enhanced key derivation** — salt separation for public/private keys ("private"/"public")
- **Unified length validation** — password length must be 12-100 characters (was 12-1000)
- **Input validation** — secret phrases must be at least 12 characters (enforced)
- **Maximum security** — no secret exposure in logs or iterations

---

## What changed:

| Aspect                 | Previous versions      | v4.0.0                                |
|------------------------|------------------------|---------------------------------------|
| Private key iterations | Fixed 30               | Dynamic 15-30                         |
| Public key iterations  | Fixed 60               | Dynamic 45-60                         |
| Key derivation salt    | None                   | "private"/"public"                    |
| Character set          | `abc...!@#$&*-_`       | `!@#$%^&*()_+-=[]{};:,.<>?/A-Za-z0-9` |
| Password max length    | 1000                   | 100                                   |
| Secret validation      | Min 4 chars            | Min 12 chars (enforced)               |
| Secret in iterations   | Yes (exposed)          | No (secure)                           |

---

## Metadata File Compatibility

**The old `passwords.json` file is NOT compatible with v4.0.0**

Public keys stored in previous versions cannot be used with v4.0.0 because:
- Iteration counts changed from fixed 60 to dynamic 45-60
- Salt "public" was added to key derivation

**Result:** Old entries will load but secret verification will fail. Passwords cannot be regenerated.

---

## Migration Steps

The migration process is the SAME for all previous versions (v2.x.x, v3.x.x):

### Step 1: Retrieve existing passwords using old version

Before upgrading, retrieve all actual passwords from your current version:

```bash
# Using your current version
clipassman
# Select option 2, then 1 for each password entry
```

**Save all retrieved passwords** in a safe place.

### Step 2: Backup old metadata file

The old metadata file is located at:
- Linux: `~/.config/smart_password_manager/passwords.json`

Copy this file to a safe location (e.g., `passwords.json.bak`).

### Step 3: Upgrade to v4.0.0

```bash
pip install --upgrade clipassman
```

### Step 4: Remove old metadata file

The old metadata file must be removed or moved away from the default location. v4.0.0 will create a new empty file on first run.

### Step 5: Re-add entries

Launch clipassman v4.0.0 and add all entries again using the **same secret phrases and lengths** as before.

### Step 6: Update services

Replace old passwords (from Step 1) with newly generated ones on each website/service.

### Step 7: Verify

Log in using new passwords. Confirm regeneration works (same secret → same password).

---

## Important Notes

- **No automatic migration** — manual password regeneration required
- **Metadata file is NOT compatible** — old entries cannot be used
- **Old passwords still work** on services until you change them
- **Your secret phrases remain the same**
- **Secret phrases shorter than 12 characters will now be rejected**
- **Password lengths between 101 and 1000 will now be rejected**
- **Generated passwords will be DIFFERENT** — all services need updates
- Test with non-essential accounts first

---

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)

---

