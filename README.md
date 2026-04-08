# CLIPassMan (Console Smart Password Manager) <sup>v2.2.2</sup>

---

**Terminal-based smart password manager with deterministic password generation. Generate, manage, and retrieve passwords without storing them - all from your command line.**

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

## **Core Principles:**

- **Zero-Password Storage**: No passwords are ever stored or transmitted
- **Deterministic Regeneration**: Passwords are recreated identically from your secret phrase
- **Metadata Management**: Store only descriptions and verification keys
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

**Key Features:**
- **No Password Database**: Eliminates password storage completely
- **Interactive Terminal UI**: Clean, centered text with visual framing
- **Public Key Verification**: Verify secret knowledge without exposure
- **List View**: See all your password metadata in clear lists
- **Export/Import**: Backup and restore functionality with timestamped files
- **Bulk Operations**: Clear all passwords with double confirmation
- **Secure Hidden Input**: Hidden secret phrase entry via getpass
- **No Dependencies**: Only Python standard library + smartpasslib
- **Server Ready**: Perfect for headless systems and remote management

**Security Model:**
- **Proof of Knowledge**: Verify you know a secret without storing it
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

Powered by **[smartpasslib v2.2.0+](https://github.com/smartlegionlab/smartpasslib)** - The core library for deterministic password generation.

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret phrase.

**What's NOT stored**:
- Your secret phrase
- The actual password
- Any reversible password data

**What IS stored** (in `~/.config/smart_password_manager/passwords.json`):
- Public verification key (hash of secret)
- Service description
- Password length parameter

**Export format**: Same JSON structure, can be backed up and restored across different machines running the same software version.

**Security model**: Proof of secret knowledge without secret storage or password transmission.

---

## File Locations

Starting from v2.2.2, configuration files are stored in:

| Platform | Configuration Path |
|----------|-------------------|
| Linux | `~/.config/smart_password_manager/passwords.json` |
| macOS | `~/.config/smart_password_manager/passwords.json` |
| Windows | `C:\Users\Username\.config\smart_password_manager\passwords.json` |

**Automatic Migration**:
- Old `~/.cases.json` files are automatically migrated on first run
- Original file is backed up as `~/.cases.json.bak`
- Migration is one-time and non-destructive
- All your existing passwords are preserved

---

## What's New in v2.2.2

### Import/Export Functionality

- **Export passwords**: Save your password metadata to JSON file with timestamp
- **Import passwords**: Restore from previously exported files
- **Format options**: Choose between pretty or minified JSON
- **Metadata inclusion**: Optional timestamp and version info in export
- **Safe import**: Merges with existing data, never overwrites existing entries
- **Import preview**: See export metadata before confirming
- **Statistics**: Clear feedback on added/skipped/invalid entries
- **Filename suggestions**: Auto-generated timestamps prevent overwrites

### Configuration Migration

- **New config location**: Now uses `~/.config/smart_password_manager/passwords.json`
- **Automatic migration**: Old `~/.cases.json` files are auto-migrated on first run
- **Cross-platform paths**: Works on Linux, macOS, and Windows
- **Safe backup**: Original file preserved as `.cases.json.bak`

### Improved Terminal UI

- **New menu option**: Export/Import in main menu (option 3)
- **Better feedback**: Clear statistics after import
- **Format selection**: Choose JSON format during export
- **Filename suggestions**: Auto-generated timestamps
- **Consistent visual styling** throughout the application

### Security Improvements

- **Stronger public key verification** using enhanced cryptographic methods
- **Better input validation** with clear error messages
- **Duplicate detection** - prevents creating multiple entries with same secret
- **Case-sensitive secrets** with clear user warnings

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
pip install clipassman

# For systems with package conflicts
pip install clipassman --break-system-packages

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
4. Enter your secret phrase (never shared or stored)
5. Confirm your secret phrase
6. Set password length (4-100 characters)
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
pip install smartpasslib>=2.2.0
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

## Core Components

### Terminal Interface Features

**Main Menu:**
```
********************************************************************************
********************** Smart Password Manager CLI v2.2.2 ***********************
******************************* Version: v2.2.2 ********************************
------------------------ Main Menu | Total passwords: 0 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action:

```

**Password Creation:**
- Description input with validation
- Secret phrase entry with confirmation
- Password length selection (4-100 characters)
- Public key generation and display
- Generated password display

**Password Retrieval:**
- Numbered list of password entries
- Secret phrase entry via getpass (hidden)
- Public key verification
- Password regeneration

**Export/Import Interface:**
```
------------------------ Export/Import Menu ------------------------
1: Export passwords to file
2: Import passwords from file
0: ← Back to Main Menu
Choose an action:
```

### Security Implementation

**Public Key System:**
```python
# Generate public key from secret
public_key = SmartPasswordMaster.generate_public_key(secret)

# Verify secret without exposing it
is_valid = SmartPasswordMaster.check_public_key(secret, public_key)

# Generate password deterministically
password = SmartPasswordMaster.generate_smart_password(secret, length)
```

**Input Security:**
- Hidden secret input via `getpass.getpass()`
- Case-sensitive secret validation
- Duplicate detection prevention
- Input sanitization and validation

---

## Advanced Usage

### Password Management Strategy

**For Multiple Accounts:**
```bash
Description Examples:
- GitHub Personal Account
- Work Email - Office 365
- Social Media - Twitter
- Cloud Storage - Dropbox

Length Strategy:
- Critical accounts: 20-24 characters
- Important accounts: 16-20 characters
- General accounts: 12-16 characters
- Temporary accounts: 8-12 characters
```

### Secret Phrase Management

**Best Practices:**
1. **Unique per service** - Different secret for each account type
2. **Memorable but complex** - Phrases you can remember but others can't guess
3. **Case-sensitive** - v2.2.2 enforces exact case matching
4. **No digital storage** - Keep only in memory or physical backup
5. **Backup plan** - Physical written backup in secure location
6. **Export regularly** - Backup metadata after adding new passwords

**Example Secret Phrases:**
```
Good: "MyFavoriteCoffeeShop@2025#Boston"
Good: "PurpleElephantsDanceInMoonlight42"
Avoid: "password123", "letmein", "123456"
```

### Backup Strategy

**Recommended workflow:**
1. Export metadata after adding new passwords
2. Store exports in secure, encrypted location
3. Keep exports across different machines for synchronization
4. Test import on a separate machine before relying on backups
5. Use timestamped exports to maintain version history

---

## Ecosystem Integration

### Part of Smart Password Suite

**Core Technology:**
- **[smartpasslib](https://github.com/smartlegionlab/smartpasslib)** - Core password generation library

**Desktop Application:**
- **[Desktop Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager-desktop)** - Graphical interface with edit capabilities

**Other CLI Tools:**
- **[CLI Smart Password Generator](https://github.com/smartlegionlab/clipassgen/)** - Terminal-based password generation only

**Web Interface:**
- **[Web Smart Password Manager](https://github.com/smartlegionlab/smart-password-manager)** - Browser-based access

### Data Compatibility
- Uses same `~/.config/smart_password_manager/passwords.json` format as desktop manager
- Export files compatible across all ecosystem tools
- Consistent cryptographic operations across platforms
- Can share password metadata between CLI and desktop versions

### Comparison with Desktop Version

**CLI Advantages:**
- No GUI dependencies
- Works on servers and headless systems
- Faster for keyboard-centric users
- Scriptable and automatable
- Lower resource usage

**Desktop Advantages:**
- Graphical interface with table view
- Edit functionality for metadata
- Copy to clipboard with one click
- Better visual feedback
- Mouse support
- Context menu for quick actions

---

## License

**[BSD 3-Clause License](LICENSE)**

Copyright (c) 2026, Alexander Suvorov

---

## Support

- **CLI Manager Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline help (option 5) and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

## Security Warnings

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + length) = identical output (password)
4. **Single point of failure**: Secret phrase is the sole authentication factor for all passwords
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use

### Export/Import Security Notes

- Export files contain ONLY metadata (public keys, descriptions, lengths)
- No passwords or secret phrases are ever exported
- Export files are plain JSON - store them securely
- Treat exported metadata as sensitive information
- Timestamped exports help maintain backup history

---

**Version**: 2.2.2 | [**Author**](https://smartlegionlab.ru): [Alexander Suvorov](https://alexander-suvorov.ru)

---

## Terminal Interface Examples

![clipassman](https://github.com/smartlegionlab/clipassman/blob/master/data/images/clipassman.png)

### Main Interface
```
********************************************************************************
********************** Smart Password Manager CLI v2.2.2 ***********************
******************************* Version: v2.2.2 ********************************
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

IMPORTANT: Your secret phrase:
• Is case-sensitive
• Should be memorable but secure
• Will generate the same password every time
• Is never stored - only the hash is saved

Enter secret phrase (hidden): 
Confirm secret phrase (hidden): 
Enter password length (4-100): 16
--------------------------------------------------------------------------------
✓ Password metadata added successfully!
Description: Account 1
Length: 16 characters
Public Key: d8295cdc1a8e3094...bb4b558bf7d70b4b
--------------------------- Your generated password: ---------------------------
wcJjBKIhsgV%!6Iq
--------------------------------------------------------------------------------

Press Enter to continue... 
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 3
------------------------------ Export/Import Menu ------------------------------
1: Export passwords to file
2: Import passwords from file
0: ← Back to Main Menu
Choose an action: 1
------------------------------- Export Passwords -------------------------------
Total passwords: 1
Default filename: passwords_export_20260218_124959.json
Enter filename (or press Enter for default): 

Export format:
1: Pretty JSON (readable, with indentation)
2: Minified JSON (smaller size)
Choose format (1/2): 1
Include export metadata (timestamp, version)? (y/n): y
--------------------------------------------------------------------------------
✓ Successfully exported 1 passwords to:
  passwords_export_20260218_124959.json

Press Enter to continue... 
------------------------------ Export/Import Menu ------------------------------
1: Export passwords to file
2: Import passwords from file
0: ← Back to Main Menu
Choose an action: 2
------------------------------- Import Passwords -------------------------------
Current passwords: 1
Enter filename to import: /home/user/passwords_export_20260218_124959.json

Export metadata:
  Date: 2026-02-18T12:50:18.597439
  App version: 2.2.2
  Passwords in file: 1

Found 1 passwords in file

Proceed with import? (y/n): y
--------------------------------------------------------------------------------
✓ Import completed:
  • Added: 0 new passwords
  • Skipped (already exist): 1

Press Enter to continue... 
------------------------------ Export/Import Menu ------------------------------
1: Export passwords to file
2: Import passwords from file
0: ← Back to Main Menu
Choose an action: 0
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Export/Import Passwords
4: Clear All Passwords
5: Help
0: Exit
Choose an action: 5
------------------------------------- Help -------------------------------------

        CLIPASSMAN v2.2.2 - Console Smart Password Manager

        HOW IT WORKS:
        1. Provide a secret phrase
        2. System generates a public key from the secret
        3. Password is generated deterministically
        4. Same secret + same length = same password every time

        To retrieve a password:
        1. Enter the same secret phrase
        2. Password is regenerated identically

        SECURITY NOTES:
        • Passwords are NEVER stored anywhere
        • Case-sensitive secret phrases
        • Lost secret phrase = permanently lost passwords
        • Public key can be stored for verification
        
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