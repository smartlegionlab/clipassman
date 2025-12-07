# CLIPassMan (Console Smart Password Manager) <sup>v2.1.3</sup>

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

---

## **🔐 Core Principles:**

- 🔐 **Zero-Password Storage**: No passwords are ever stored or transmitted
- 🔑 **Deterministic Regeneration**: Passwords are recreated identically from your secret phrase
- 📝 **Metadata Management**: Store only descriptions and verification keys
- 💻 **Terminal Processing**: All cryptographic operations happen in your CLI
- 🔄 **On-Demand Discovery**: Passwords exist only when you generate them

**What You Can Do:**
1. **Create Smart Passwords**: Generate deterministic passwords from secret phrases
2. **Store Metadata Securely**: Keep password descriptions and lengths without storing passwords
3. **Regenerate Passwords**: Recreate passwords anytime using your secret phrase
4. **Manage Services**: Organize passwords for different accounts and services
5. **Secure Terminal Input**: Hidden secret phrase entry with getpass
6. **Verify Secrets**: Prove knowledge of secrets without exposing them
7. **Cross-Platform Management**: Works on any system with Python
8. **No GUI Dependencies**: Pure terminal interface for servers and remote systems

**Key Features:**
- ✅ **No Password Database**: Eliminates password storage completely
- ✅ **Interactive Terminal UI**: Clean, centered text with visual framing
- ✅ **Public Key Verification**: Verify secret knowledge without exposure
- ✅ **List View**: See all your password metadata in clear lists
- ✅ **Bulk Operations**: Clear all passwords with double confirmation
- ✅ **Secure Hidden Input**: Hidden secret phrase entry via getpass
- ✅ **No Dependencies**: Only Python standard library + smartpasslib
- ✅ **Server Ready**: Perfect for headless systems and remote management

**Security Model:**
- **Proof of Knowledge**: Verify you know a secret without storing it
- **Deterministic Security**: Same secret + length = same password, always
- **Metadata Separation**: Non-sensitive data stored separately from verification
- **Local Processing**: No data leaves your computer
- **No Recovery Backdoors**: Lost secret = permanently lost access (by design)

---

## ⚠️ Critical Notice

**BEFORE USING THIS SOFTWARE, READ THE COMPLETE LEGAL DISCLAIMER BELOW**

[View Legal Disclaimer & Liability Waiver](#-legal-disclaimer)

*Usage of this software constitutes acceptance of all terms and conditions.*

---

## 📚 Research Paradigms & Publications

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural Shift from Data Protection to Data Non-Existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological Shift from Data Transmission to Synchronous State Discovery

---

## 🔬 Technical Foundation

Powered by **[smartpasslib v2.1.0+](https://github.com/smartlegionlab/smartpasslib)** - The core library for deterministic password generation.

**Key principle**: Instead of storing passwords, you store verification metadata. The actual password is regenerated on-demand from your secret phrase.

**What's NOT stored**:
- Your secret phrase
- The actual password
- Any reversible password data

**What IS stored** (in `~/.cases.json`):
- Public verification key (hash of secret)
- Service description
- Password length parameter

**Security model**: Proof of secret knowledge without secret storage or password transmission.

---

## 🆕 What's New in v2.1.3

### ⚠️ **BREAKING CHANGES WARNING**

**CRITICAL**: v2.1.3 is **NOT** backward compatible with v1.x. All passwords generated with v1.x are now **INVALID**. You must recreate all passwords using your secret phrases.

### Major Improvements:

**Simplified Architecture:**
- **Login parameter removed** - now uses only secret phrase and description
- **Streamlined API** - single authentication factor (secret phrase)
- **Cleaner codebase** - reduced complexity and better maintainability

**Enhanced Terminal Interface:**
- **SmartPrinter class** for beautiful centered and framed text output
- **Better visual hierarchy** with consistent symbol borders
- **Improved menu layouts** for clearer navigation
- **Automatic terminal width detection** for perfect centering

**Security Improvements:**
- **Stronger public key verification** using enhanced cryptographic methods
- **Better input validation** with clear error messages
- **Duplicate detection** - prevents creating multiple entries with same secret
- **Case-sensitive secrets** with clear user warnings

**User Experience:**
- **Clear migration warnings** with step-by-step instructions
- **Interactive confirmation dialogs** for destructive operations
- **Better help system** with comprehensive documentation
- **Password list numbering** for easy selection

### Breaking Changes:

**Compatibility:**
- **NOT compatible** with v1.x password generation
- Requires **smartpasslib v2.1.0+**
- **All v1.x passwords must be recreated**
- **Login parameter completely removed**

**Migration Required:**
```bash
# Important: Backup old passwords before migration
# Step 1: Recover passwords using v1.x if needed
# Step 2: Delete old ~/.cases.json file
# Step 3: Install clipassman v2.1.3
# Step 4: Recreate all passwords with your secret phrases
# Step 5: Update all account credentials
```

### New Features:

**Terminal UI Enhancements:**
```python
# Centered text output with custom symbols
# Framed text for important messages
# Automatic terminal width detection
# Consistent visual styling throughout
```

**Security Features:**
- Duplicate secret phrase detection
- Public key display (first and last 16 characters)
- Clear case-sensitivity warnings
- Input validation with helpful error messages

**Management Features:**
- Total password count display in main menu
- Individual password deletion with confirmation
- Bulk clear operation with double confirmation
- Password list with descriptions and lengths

### Key Improvements:

1. **Simplified Workflow** - No login parameter needed
2. **Better Terminal UI** - Professional-looking output
3. **Enhanced Security** - Stronger verification methods
4. **Clearer Migration** - Step-by-step upgrade path
5. **Improved Error Handling** - User-friendly messages

---

## 📦 Installation & Quick Start

### Prerequisites
- **Python 3.7+** required
- **pip** for package management

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

## 🚀 Quick Usage Guide

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

### Managing Passwords
```bash
# Main menu options:
1: Add Password          # Create new password
2: Get/Delete Password   # Retrieve or remove password
3: Clear All Passwords   # Remove all entries (double confirmation)
4: Help                  # View documentation
0: Exit                  # Quit application
```

### Deleting Passwords
1. Select option **2: Get/Delete Password**
2. Choose password entry
3. Select **2: Delete entry**
4. Confirm deletion with 'y'
5. Only metadata removed - password can be recreated with secret

---

## 📦 Windows Standalone Executable

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
3. **IMPORTANT:** Check ✅ "Add Python to PATH"
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

```

#### Step 6: Build Executable
```cmd
# Build single .exe file
pyinstaller --onefile --console --name "clipassman.exe" --additional-hooks-dir=. app.py

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

## 🏗️ Core Components

### Terminal Interface Features

**Main Menu:**
```
********************************************************************************
********************** Smart Password Manager CLI v2.1.3 ***********************
******************************* Version: v2.1.3 ********************************
------------------------ Main Menu | Total passwords: 0 ------------------------
1: Add Password
2: Get/Delete Password
3: Clear All Passwords
4: Help
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

## 💡 Advanced Usage

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
3. **Case-sensitive** - v2.1.3 enforces exact case matching
4. **No digital storage** - Keep only in memory or physical backup
5. **Backup plan** - Physical written backup in secure location

**Example Secret Phrases:**
```
Good: "MyFavoriteCoffeeShop@2025#Boston"
Good: "PurpleElephantsDanceInMoonlight42"
Avoid: "password123", "letmein", "123456"
```

---

## 🔧 Ecosystem Integration

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
- Uses same `~/.cases.json` format as desktop manager
- Compatible metadata with smartpasslib ecosystem
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

---

## 📜 License

**[BSD 3-Clause License](LICENSE)**

Copyright (c) 2025, Alexander Suvorov

```
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## 🆘 Support

- **CLI Manager Issues**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **Core Library Issues**: [smartpasslib Issues](https://github.com/smartlegionlab/smartpasslib/issues)
- **Documentation**: Inline help (option 4) and this README

**Note**: Always test password generation with non-essential accounts first. Implementation security depends on proper usage.

---

## ⚠️ Security Warnings

**Version Incompatibility**: v2.1.3 passwords are incompatible with v1.x.
Never mix secret phrases across different versions.

### Secret Phrase Security

**Your secret phrase is the cryptographic master key**

1. **Permanent data loss**: Lost secret phrase = irreversible loss of all derived passwords
2. **No recovery mechanisms**: No password recovery, no secret reset, no administrative override
3. **Deterministic generation**: Identical input (secret + length) = identical output (password)
4. **Single point of failure**: Secret phrase is the sole authentication factor for all passwords
5. **Secure storage required**: Digital storage of secret phrases is prohibited

**Critical**: Test password regeneration with non-essential accounts before production use

---

## 📄 Legal Disclaimer

**COMPLETE AND ABSOLUTE RELEASE FROM ALL LIABILITY**

**SOFTWARE PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.**

The copyright holder, contributors, and any associated parties **EXPLICITLY DISCLAIM AND DENY ALL RESPONSIBILITY AND LIABILITY** for:

1. **ANY AND ALL DATA LOSS**: Complete or partial loss of passwords, accounts, credentials, cryptographic keys, or any data whatsoever
2. **ANY AND ALL SECURITY INCIDENTS**: Unauthorized access, data breaches, account compromises, theft, or exposure of sensitive information
3. **ANY AND ALL FINANCIAL LOSSES**: Direct, indirect, incidental, special, consequential, or punitive damages of any kind
4. **ANY AND ALL OPERATIONAL DISRUPTIONS**: Service interruptions, account lockouts, authentication failures, or denial of service
5. **ANY AND ALL IMPLEMENTATION ISSUES**: Bugs, errors, vulnerabilities, misconfigurations, or incorrect usage
6. **ANY AND ALL LEGAL OR REGULATORY CONSEQUENCES**: Violations of laws, regulations, compliance requirements, or terms of service
7. **ANY AND ALL PERSONAL OR BUSINESS DAMAGES**: Reputational harm, business interruption, loss of revenue, or any other damages
8. **ANY AND ALL THIRD-PARTY CLAIMS**: Claims made by any other parties affected by software usage

**USER ACCEPTS FULL AND UNCONDITIONAL RESPONSIBILITY**

By installing, accessing, or using this software in any manner, you irrevocably agree that:

- You assume **ALL** risks associated with software usage
- You bear **SOLE** responsibility for secret phrase management and security
- You accept **COMPLETE** responsibility for all testing and validation
- You are **EXCLUSIVELY** liable for compliance with all applicable laws
- You accept **TOTAL** responsibility for any and all consequences
- You **PERMANENTLY AND IRREVOCABLY** waive, release, and discharge all claims against the copyright holder, contributors, distributors, and any associated entities

**NO WARRANTY OF ANY KIND**

This software comes with **ABSOLUTELY NO GUARANTEES** regarding:
- Security effectiveness or cryptographic strength
- Reliability or availability
- Fitness for any particular purpose
- Accuracy or correctness
- Freedom from defects or vulnerabilities

**NOT A SECURITY PRODUCT OR SERVICE**

This is experimental software. It is not:
- Security consultation or advice
- A certified cryptographic product
- A guaranteed security solution
- Professional security software
- Endorsed by any security authority

**FINAL AND BINDING AGREEMENT**

Usage of this software constitutes your **FULL AND UNCONDITIONAL ACCEPTANCE** of this disclaimer. If you do not accept **ALL** terms and conditions, **DO NOT USE THE SOFTWARE.**

**BY PROCEEDING, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DISCLAIMER IN ITS ENTIRETY, UNDERSTAND ITS TERMS COMPLETELY, AND ACCEPT THEM WITHOUT RESERVATION OR EXCEPTION.**

---

**Version**: 2.1.3 | [**Author**](https://smartlegionlab.ru): [Alexander Suvorov](https://alexander-suvorov.ru)

---

**Note**: This is v2.1.3. If migrating from v1.x, all passwords must be regenerated with new secret phrases.

---

## Terminal Interface Examples

![clipassman](https://github.com/smartlegionlab/clipassman/blob/master/data/images/clipassman.png)

### Main Interface
```
********************************************************************************
********************** Smart Password Manager CLI v2.1.3 ***********************
******************************* Version: v2.1.3 ********************************
------------------------ Main Menu | Total passwords: 0 ------------------------
1: Add Password
2: Get/Delete Password
3: Clear All Passwords
4: Help
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
3: Clear All Passwords
4: Help
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
wcJjBKIhsgV%!6Iq
--------------------------------------------------------------------------------

Press Enter to continue... 
-------------------------------- Password List: --------------------------------
1. Account 1 (16 chars)
0. ← Back
Select entry: 0
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Clear All Passwords
4: Help
0: Exit
Choose an action: 4
------------------------------------- Help -------------------------------------

        CLIPASSMAN v2.1.3 - Console Smart Password Manager

        BREAKING CHANGES WARNING:
        • Login parameter completely removed
        • Now uses ONLY secret phrase
        • All v1.x passwords are INVALID
        • Old password metadata cannot be migrated

        MIGRATION REQUIRED:
        If you have old passwords from v1.x:
        1. Recover them using v1.x version
        2. Generate new ones here with your secret phrases
        3. Update all accounts with new passwords
        4. Securely delete old password records

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
        
        print(f"For more information, visit the project page on GitHub: https://github.com/smartlegionlab/clipassman")
        
----------------------------------------------------------------------
Complete documentation: https://github.com/smartlegionlab/smartpasslib
----------------------------------------------------------------------
--------------------------------------------------------------------------------

Press Enter to continue... 
------------------------ Main Menu | Total passwords: 1 ------------------------
1: Add Password
2: Get/Delete Password
3: Clear All Passwords
4: Help
0: Exit
Choose an action: 0
----------------- https://github.com/smartlegionlab/clipassman -----------------
--------------------- Copyright © 2025, Alexander Suvorov ----------------------
================================================================================
```
