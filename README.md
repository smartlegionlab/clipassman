# CLIPassMan (Console Smart Password Manager) <sup>v4.0.0</sup>

---

**Console Smart Password Manager - Terminal-based smart password manager with deterministic password generation. Generate, manage, and retrieve passwords without storing them - all from your command line.**

**Decentralized by Design**: Unlike traditional password managers that store encrypted vaults on central servers, 
Smart Password Manager stores nothing. Your secrets never leave your device. Passwords are regenerated on-demand — 
**no cloud, no database, no trust required**.

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassman?label=pypi%20downloads)](https://pypi.org/project/clipassman/)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassman)](https://pepy.tech/projects/clipassman)
[![PyPI Weekly Downloads](https://static.pepy.tech/badge/clipassman/week)](https://pepy.tech/projects/clipassman)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassman)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/)
[![PyPI version](https://img.shields.io/pypi/v/clipassman)](https://pypi.org/project/clipassman)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)
[![PyPI format](https://img.shields.io/pypi/format/clipassman)](https://pypi.org/project/clipassman)
![Platform](https://img.shields.io/badge/platform-linux-lightgrey)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/clipassman?style=social)](https://github.com/smartlegionlab/clipassman/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/clipassman?style=social)](https://github.com/smartlegionlab/clipassman/network/members)

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/clipassman/blob/master/DISCLAIMER.md)

---

## 🔄 Breaking Change (v4.0.0)

> **⚠️ This release uses [smartpasslib](https://github.com/smartlegionlab/smartpasslib) v4.0.0, which is NOT backward compatible with v2.x.x or v3.x.x**

Smart passwords created with older versions **cannot be regenerated** using v4.0.0.

📖 **Full migration instructions** → see [MIGRATION.md](https://github.com/smartlegionlab/clipassman/blob/master/MIGRATION.md)

---

## Core Principles

- **Zero-Storage Security**: No passwords or secret phrases are ever stored or transmitted
- **Decentralized Architecture**: No central servers, no cloud dependency, no third-party trust required
- **Deterministic Regeneration**: Passwords are recreated identically from your secret phrase
- **Metadata Only**: Store only descriptions and verification keys
- **Terminal Processing**: All cryptographic operations happen in your CLI
- **On-Demand Discovery**: Passwords exist only when you generate them

**What You Can Do:**
1. **Create Smart Passwords**: Generate deterministic passwords from secret phrases
2. **Store Metadata Securely**: Keep password descriptions and lengths without storing passwords
3. **Regenerate Passwords**: Recreate passwords anytime using your secret phrase
4. **Manage Services**: Organize passwords for different accounts and services
5. **Secure Terminal Input**: Hidden secret phrase entry with getpass
6. **Verify Secrets**: Prove knowledge of secrets without exposing them
7. **Export/Import**: Backup and restore your password metadata
8. **Cross-Platform Management**: Works on any system with Python
9. **No GUI Dependencies**: Pure terminal interface for servers and remote systems

## Key Features

- **Decentralized & Serverless**: No central database, no cloud lock-in, complete user sovereignty
- **No Password Database**: Eliminates password storage completely
- **Interactive Terminal UI**: Clean, centered text with visual framing
- **Public Key Verification**: Verify secret knowledge without exposure
- **List View**: See all your password metadata in clear lists
- **Export/Import**: Backup and restore functionality with timestamped files
- **Bulk Operations**: Clear all passwords with double confirmation
- **Secure Hidden Input**: Hidden secret phrase entry via getpass
- **No Dependencies**: Only Python standard library + smartpasslib
- **Server Ready**: Perfect for headless systems and remote management

## Security Model

- **Proof of Knowledge**: Public keys verify secrets without exposing them
- **Decentralized Trust**: No third party needed — you control your secrets completely
- **Deterministic Security**: Same secret + length = same password, always
- **Metadata Separation**: Non-sensitive data stored separately from verification
- **Local Processing**: No data leaves your computer
- **No Recovery Backdoors**: Lost secret = permanently lost access (by design)

---

## Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## Technical Foundation

Powered by **[smartpasslib](https://github.com/smartlegionlab/smartpasslib) v4.0.0+** — The core library for deterministic password generation.

**Key derivation (same as Python/JS/Kotlin/Go/C# versions v4.0.0):**

| Key Type    | Iterations              | Purpose                                               |
|-------------|-------------------------|-------------------------------------------------------|
| Private Key | 15-30 (dynamic)         | Password generation (never stored, never transmitted) |
| Public Key  | 45-60 (dynamic)         | Verification (stored locally)                         |

**Character Set (Google-compatible):**
```
!@#$%^&*()_+-=[]{};:,.<>?/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz
```

**Validation Rules:**
- Secret phrase: minimum 12 characters
- Password length: 12-100 characters

**Decentralized Architecture**:
- No central authority required
- Metadata can be synced via any channel
- Your security depends only on your secret phrase
- Works offline — no internet connection required

**What's NOT stored**:
- Your secret phrase
- The actual password
- Any reversible password data

**What IS stored** (in `~/.config/smart_password_manager/passwords.json`):
- Public verification key (hash of secret)
- Service description
- Password length parameter

---

## File Locations

Configuration files are stored in:

| Platform | Configuration Path                                                |
|----------|-------------------------------------------------------------------|
| Linux    | `~/.config/smart_password_manager/passwords.json`                 |

**Legacy Migration**:
- Old `~/.cases.json` files from v1.x.x/v2.x.x/v3.x.x are **NOT compatible** with v4.0.0
- Public keys in old files use different derivation (fixed iterations, no salt)
- These files will **not** be migrated automatically
- If you have existing metadata, you need to recreate entries manually
- Keep old file as backup: `~/.cases.json.v3.bak`
- See [MIGRATION.md](MIGRATION.md) for detailed instructions

---

## Installation & Quick Start

### Prerequisites
- **Python 3.7+** required
- **pip** for package management

### Quick Installation
```bash
# Install from PyPI
pip install clipassman==4.0.0

# For systems with package conflicts
pip install clipassman==4.0.0 --break-system-packages

# Verify installation
clipassman
```

### Quick Run from Repository

```bash
# Clone and run in one go
git clone https://github.com/smartlegionlab/clipassman.git
cd clipassman
python app.py
```

### Manual Installation
```bash
# Clone repository
git clone https://github.com/smartlegionlab/clipassman.git
cd clipassman

# Install in development mode
pip install -e .

# Or install from local source
pip install .
```

---

## Quick Usage Guide

### Launching the Application
```bash
# Start interactive terminal interface
clipassman

# Or if installed locally
python -m clipassman.clipassman
```

### Creating Your First Password
1. Launch `clipassman`
2. Select option **1: Add Password**
3. Enter service description (e.g., "GitHub Account")
4. Enter your secret phrase (minimum 12 characters, never stored)
   - Good examples: `"MyStrongSecretPhrase2026!"` or `"P@ssw0rd!LongSecret"`
5. Confirm your secret phrase
6. Set password length (12-100 characters, 16-24 recommended)
7. Password is generated and displayed
8. Save it securely (not stored by system)

### Retrieving a Password
1. Launch `clipassman`
2. Select option **2: Get/Delete Password**
3. Choose password entry from numbered list
4. Select **1: Get password**
5. Enter your secret phrase (hidden input)
6. Password regenerates identically

### Exporting Passwords
1. Launch `clipassman`
2. Select option **3: Export/Import Passwords**
3. Select **1: Export passwords to file**
4. Choose filename (or press Enter for auto-generated with timestamp)
5. Select format (1: pretty JSON, 2: minified JSON)
6. Choose whether to include metadata (y/n)
7. File is saved with all your password metadata

### Importing Passwords
1. Launch `clipassman`
2. Select option **3: Export/Import Passwords**
3. Select **2: Import passwords from file**
4. Enter filename to import
5. Review export metadata if present
6. Confirm import (y/n)
7. See statistics of added/skipped/invalid entries

### Deleting Passwords
1. Select option **2: Get/Delete Password**
2. Choose password entry
3. Select **2: Delete entry**
4. Confirm deletion with 'y'

### Clearing All Passwords
1. Select option **4: Clear All Passwords**
2. First confirmation with 'y'
3. Type 'DELETE ALL' to confirm

---

## Security Requirements

### Secret Phrase
- **Minimum 12 characters** (enforced)
- Case-sensitive
- Use mix of: uppercase, lowercase, numbers, symbols
- Never store digitally
- **NEVER use your password description as secret phrase**

### Strong Secret Examples
```
✅ "MyStrongSecretPhrase2026!"   — mixed case + numbers + symbols
✅ "P@ssw0rd!LongSecret"         — special chars + numbers + length
✅ "КотБегемот2026НаДиете"       — Cyrillic + numbers
```

### Weak Secret Examples (avoid)
```
❌ "GitHub Account"              — using description as secret (weak!)
❌ "password"                    — dictionary word, too short
❌ "1234567890"                  — only digits, too short
❌ "qwerty123"                   — keyboard pattern
```

### Decentralized Nature

**There is no "forgot password" button.** This is by design:

- No central server can reset your passwords
- No support team can recover your access
- Your secret phrase is the ONLY key

**This is the price of true decentralization** — you are completely in control.

## Cross-Platform Compatibility

CLIPassMan produces **identical passwords** to:

| Platform         | Application                                                                               |
|------------------|-------------------------------------------------------------------------------------------|
| Desktop Python   | [Desktop Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)       |
| Desktop C#       | [Desktop C# Manager](https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop) |
| CLI C#           | [CLI Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli)       |
| CLI Generator C# | [CLI Generator (C#)](https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli)   |
| Web              | [Web Manager](https://github.com/smartlegionlab/smart-password-manager-web)               |
| Android          | [Android Manager](https://github.com/smartlegionlab/smart-password-manager-android)       |
| Python Core      | [smartpasslib](https://github.com/smartlegionlab/smartpasslib)                            |
| Go Core          | [smartpasslib-go](https://github.com/smartlegionlab/smartpasslib-go)                      |
| Kotlin Core      | [smartpasslib-kotlin](https://github.com/smartlegionlab/smartpasslib-kotlin)              |
| JS Core          | [smartpasslib-js](https://github.com/smartlegionlab/smartpasslib-js)                      |
| C# Core          | [smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp)              |

## Ecosystem

**Core Libraries:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Python
- **[smartpasslib-js](https://github.com/smartlegionlab/smartpasslib-js)** - JavaScript
- **[smartpasslib-kotlin](https://github.com/smartlegionlab/smartpasslib-kotlin)** - Kotlin
- **[smartpasslib-go](https://github.com/smartlegionlab/smartpasslib-go)** - Go
- **[smartpasslib-csharp](https://github.com/smartlegionlab/smartpasslib-csharp)** - C#

**CLI Applications:**
- **[CLI Smart Password Manager (Python)](https://github.com/smartlegionlab/clipassman)** (this)
- **[CLI Smart Password Generator (Python)](https://github.com/smartlegionlab/clipassgen)**
- **[CLI Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli)**
- **[CLI Smart Password Generator (C#)](https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli)**

**Desktop Applications:**
- **[Desktop Smart Password Manager (Python)](https://github.com/smartlegionlab/smart-password-manager-desktop)**
- **[Desktop Smart Password Manager (C#)](https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop)**

**Other:**
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-web)**
- **[Android Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-android)**

## Version History

| Version          | smartpasslib | Status                   | Migration Required     |
|------------------|--------------|--------------------------|------------------------|
| v2.x.x and below | v2.x.x       | ❌ Deprecated/Unsupported | Must migrate to v4.x.x |
| v3.x.x           | v3.x.x       | ❌ Deprecated/Unsupported | Must migrate to v4.x.x |
| **v4.0.0+**      | **v4.0.0+**  | ✅ Current                | N/A                    |

## Security Warnings

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + length) = identical output (password)
4. **Single point of failure**: Secret phrase is the sole authentication factor for all passwords
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use

### Secret Phrase Strength

**The security of your passwords depends entirely on your secret phrase.**

- **Minimum 12 characters** is enforced by the application
- Short secrets (under 12 chars) are **automatically rejected**
- Use a mix of: uppercase, lowercase, numbers, symbols
- A 12-character secret with diverse character types provides **practical brute-force immunity**

**Remember:** The app cannot recover your secret phrase. If you lose it, all passwords are permanently lost.

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)**

Copyright (©) 2026, Alexander Suvorov

## Support

- **CLI Manager Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline help (option 5) and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

