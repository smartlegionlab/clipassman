# CLIPassMan (Console Smart Password Manager) <sup>v3.0.3</sup>

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
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/clipassman?style=social)](https://github.com/smartlegionlab/clipassman/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/clipassman?style=social)](https://github.com/smartlegionlab/clipassman/network/members)

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/clipassman/blob/master/DISCLAIMER.md)

---

## 🔄 Breaking Change (v3.x.x)

> **⚠️ This release uses [smartpasslib](https://github.com/smartlegionlab/smartpasslib) v3.x.x, which is NOT backward compatible with v2.x.x**

Passwords created with v2.x.x or earlier **cannot be regenerated** using v3.x.x.

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

Powered by **[smartpasslib](https://github.com/smartlegionlab/smartpasslib) v3.x.x+** — The core library for deterministic password generation.

**Key derivation (same as Python/JS/Kotlin/Go/C# versions):**

| Key Type    | Iterations | Purpose                                               |
|-------------|------------|-------------------------------------------------------|
| Private Key | 30         | Password generation (never stored, never transmitted) |
| Public Key  | 60         | Verification (stored locally)                         |

**Character Set:** `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&*-_`

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

**Export format**: Same JSON structure, but v3.x.x exports are **incompatible** with older versions. Always note which version created the export.

---

## File Locations

Starting from v3.x.x, configuration files are stored in:

| Platform | Configuration Path                                                |
|----------|-------------------------------------------------------------------|
| Linux    | `~/.config/smart_password_manager/passwords.json`                 |
| macOS    | `~/.config/smart_password_manager/passwords.json`                 |
| Windows  | `C:\Users\Username\.config\smart_password_manager\passwords.json` |

**Automatic Migration**:
- Old `~/.cases.json` files are automatically migrated on first run
- Original file is backed up as `~/.cases.json.bak`
- Migration is one-time and non-destructive
- All your existing passwords are preserved

---

## Installation & Quick Start

### Prerequisites
- **Python 3.7+** required
- **pip** for package management

### Quick Run from Repository

```bash
# Clone and run in one go
git clone https://github.com/smartlegionlab/clipassman.git
cd clipassman
python clipassman/clipassman.py
```

### Quick Installation
```bash
# Install from PyPI
pip install clipassman==3.0.3

# For systems with package conflicts
pip install clipassman==3.0.3 --break-system-packages

# Verify installation
clipassman
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
8. Success message with filename and password count

### Importing Passwords
1. Launch `clipassman`
2. Select option **3: Export/Import Passwords**
3. Select **2: Import passwords from file**
4. Enter filename to import
5. Review export metadata if present (date, version, count)
6. Confirm import (y/n)
7. See statistics of added/skipped/invalid entries
8. Table automatically refreshes with new passwords

### Deleting Passwords
1. Select option **2: Get/Delete Password**
2. Choose password entry
3. Select **2: Delete entry**
4. Confirm deletion with 'y'
5. Only metadata removed - password can be recreated with secret

### Clearing All Passwords
1. Select option **4: Clear All Passwords**
2. First confirmation with 'y'
3. Type 'DELETE ALL' to confirm
4. All password entries are removed

### Managing Passwords
```bash
# Main menu options:
1: Add Password          # Create new password
2: Get/Delete Password   # Retrieve or remove password
3: Export/Import         # Backup or restore password metadata
4: Clear All Passwords   # Remove all entries (double confirmation)
5: Help                  # View documentation
0: Exit                  # Quit application
```

---

## Windows Standalone Executable

### Creating a Single-File *.exe

Build a standalone `clipassman.exe` that runs without Python installation:

#### Step 1: Get the Project Files
1. **Download project ZIP:**
   - Go to: https://github.com/smartlegionlab/clipassman
   - Click green "Code" button
   - Select "Download ZIP"
   - Extract to: `C:\clipassman-master`

#### Step 2: Install Python
1. Download Python installer from: https://python.org/downloads/
2. Run installer
3. **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"

#### Step 3: Open Command Prompt
1. Press `Win + R`
2. Type `cmd`, press Enter
3. Navigate to project folder:
   ```cmd
   cd C:\clipassman-master
   ```

#### Step 4: Create Virtual Environment
```cmd
# Create virtual environment
python -m venv venv

# Activate it (IMPORTANT!)
.\venv\Scripts\activate

# You should see (venv) in your command prompt
```

#### Step 5: Install Dependencies
```cmd
# Install PyInstaller in virtual environment
pip install pyinstaller
pip install smartpasslib==3.0.0
```

#### Step 6: Build Executable
```cmd
# Build single .exe file
pyinstaller --onefile --console --name "clipassman.exe" clipassman/clipassman.py

# Wait for build to complete (1-2 minutes)
```

#### Step 7: Find and Use
**Location:** `C:\clipassman-master\dist\clipassman.exe`

**Create desktop shortcut:**
1. Open `C:\clipassman-master\dist\` folder
2. Right-click `clipassman.exe`
3. Select "Create shortcut"
4. Drag shortcut to desktop
5. Rename shortcut to "CLIPassMan"
6. Double-click to start

**What you get:**
- Single file: `clipassman.exe` (~10MB)
- No Python required to run
- Works on any Windows 10/11 PC
- Can be copied to USB drive

---

## Security Requirements

### Secret Phrase
- **Minimum 12 characters** (enforced)
- Case-sensitive
- Use mix of: uppercase, lowercase, numbers, symbols, emoji, or Cyrillic
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
❌ Same as description           — never use the same value as password description
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
| v2.2.2 and below | v2.x.x       | ❌ Deprecated/Unsupported | Must migrate to v3.x.x |
| v3.x.x+          | v3.x.x       | ✅ Current                | N/A                    |

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
- Weak secrets like "password123" or "qwerty" will be rejected
- Use a mix of: uppercase, lowercase, numbers, symbols, emoji, or Cyrillic
- A 12-character secret with diverse character types provides **practical brute-force immunity**

**Remember:** The app cannot recover your secret phrase. If you lose it, all passwords are permanently lost.

### Export/Import Security Notes

- Export files contain ONLY metadata (public keys, descriptions, lengths)
- No passwords or secret phrases are ever exported
- Export files are plain JSON - store them securely
- Treat exported metadata as sensitive information
- Timestamped exports help maintain backup history

---

## Terminal Interface Examples

![clipassman](https://github.com/smartlegionlab/clipassman/blob/master/data/images/clipassman.png)

### Main Interface
```
********************************************************************************
********************** Smart Password Manager CLI v3.0.3 ***********************
******************************* Version: v3.0.3 ********************************
------------------------ Main Menu | Total passwords: 0 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 1
---------------------------- Add new smart password ----------------------------
-------------------------------------------------------------------
Enter a descriptive name for this password (e.g., "GitHub Account")
-------------------------------------------------------------------
Description: Account 1

IMPORTANT: Your secret phrase (minimum 12 characters):
• Is case-sensitive
• Should be memorable but secure
• Will generate the same password every time
• Is never stored - only the hash is saved

Good examples: 'MyCat🐱Hippo2026' or 'P@ssw0rd!LongSecret'
Bad examples: 'password123', 'qwerty', 'mysecret'

Enter secret phrase (hidden): 
Confirm secret phrase (hidden): 
Enter password length (12-100, recommended 16-24): 16
--------------------------------------------------------------------------------
✓ Password metadata added successfully!
Description: Account 1
Length: 16 characters
Public Key: 9e279e242cbfd802...2d1d6c79c3dfa348
--------------------------- Your generated password: ---------------------------
lklkVJxrHffoT@5E
--------------------------------------------------------------------------------

Press Enter to continue... 
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 2
-------------------------------- Password List: --------------------------------
1. Account 1 (16 chars)
0. ← Back
Select entry: 1
--------------------------------------------------------------------------------
Selected: Account 1
Length: 16 characters
1: Get password
2: Delete entry
0: ← Back
Select action: 1
--------------------------- Retrieve Smart Password ----------------------------
Description: Account 1
Length: 16 characters
Enter secret phrase (hidden): 
----------------------------- Generated Password: ------------------------------
lklkVJxrHffoT@5E
--------------------------------------------------------------------------------

Press Enter to continue... 
--------------------------------------------------------------------------------
Selected: Account 1
Length: 16 characters
1: Get password
2: Delete entry
0: ← Back
Select action: 0
-------------------------------- Password List: --------------------------------
1. Account 1 (16 chars)
0. ← Back
Select entry: 0
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 5
------------------------------------- Help -------------------------------------


    CLIPASSMAN v3.0.3 - Console Smart Password Manager

    DECENTRALIZED BY DESIGN:
    • No cloud, no database, no trust required
    • Your secrets never leave your device
    • There is no "forgot password" button — you are in complete control
    • Metadata can be synced via any channel (USB, cloud, even paper)

    HOW IT WORKS:
    1. Provide a secret phrase (minimum 12 characters)
    2. System generates a public key from the secret
    3. Password is generated deterministically
    4. Same secret + same length = same password across all platforms

    To retrieve a password:
    1. Enter the same secret phrase
    2. Password is regenerated identically

    SECURITY NOTES:
    • Passwords are NEVER stored anywhere
    • Secret phrases must be at least 12 characters
    • Case-sensitive secret phrases
    • Lost secret phrase = permanently lost passwords
    • Public key can be stored for verification

    CROSS-PLATFORM COMPATIBILITY:
    Same secret + same length = identical passwords on:
    • Python (Desktop, CLI)
    • C# (Desktop, CLI)
    • Web, Android, and all smartpasslib implementations

    For more information, visit the project page on GitHub: https://github.com/smartlegionlab/clipassman

    
----------------------------------------------------------------------
Complete documentation: https://github.com/smartlegionlab/smartpasslib
----------------------------------------------------------------------
--------------------------------------------------------------------------------

Press Enter to continue... 
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 0
----------------- https://github.com/smartlegionlab/clipassman -----------------
--------------------- Copyright © 2026, Alexander Suvorov ----------------------
================================================================================


```

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)**

Copyright (©) 2026, Alexander Suvorov

## Support

- **CLI Manager Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline help (option 5) and this [README](https://github.com/smartlegionlab/clipassman/blob/master/README.md)

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

