# clipassman (Console Smart Password Manager CLI) <sup>v2.0.1</sup>

---

> **Command-line smart password manager** implementing deterministic password generation - passwords are never stored, only regenerated when needed.

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassman?label=pypi%20downloads)](https://pypi.org/project/clipassman/)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassman)](https://pepy.tech/projects/clipassman)
[![PyPI Weekly Downloads](https://static.pepy.tech/badge/clipassman/week)](https://pepy.tech/projects/clipassman)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassman)
[![GitHub release](https://img.shields.io/github/v/release/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/)
[![PyPI version](https://img.shields.io/pypi/v/clipassman)](https://pypi.org/project/clipassman)
[![GitHub license](https://img.shields.io/github/license/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)
[![PyPI format](https://img.shields.io/pypi/format/clipassman)](https://pypi.org/project/clipassman)

## 🖥️ Console Smart Password Manager CLI

Cross-platform command-line interface for managing password metadata using deterministic password generation.

> **Powered by** [smartpasslib v2.0.0](https://github.com/smartlegionlab/smartpasslib) - The core library for deterministic password generation

### ⚠️ **BREAKING CHANGES in v2.0.1**

**WARNING:** This version introduces breaking changes:
- All passwords generated with v1.x are now **INVALID**
- **Login parameter removed** - now uses only secret phrase and description
- You must create **NEW** passwords using your secret phrases
- Simplified API - only secret phrase required

---

## 📦 Installation

### Standard Installation
```bash
pip install clipassman
```

### For Systems with Package Conflicts
```bash
pip install clipassman --break-system-packages
```

### Manual Installation
```bash
# Clone and install from source
git clone https://github.com/smartlegionlab/clipassman.git
cd clipassman
pip install -e .
```

---

## 🚀 Quick Start

### Interactive Mode (Recommended)
```bash
clipassman
```
Launches the interactive terminal interface.

### Store Password Metadata
```bash
# Launch interactive mode to add password
clipassman
# Then choose option 1: Add Password
```

### Generate Password When Needed
```bash
# Launch interactive mode
clipassman
# Choose option 2: Get/Delete Password
# Select your password entry and enter secret phrase
```

---

## 🎯 Key Features

### Deterministic Password Generation
- **Same secret** → **Same password** every time
- Passwords are **mathematical functions** of your secret phrase
- No password database to breach

### Security by Design
- **No password storage** - generated on-demand
- **Local processing** - all operations on your machine
- **Public key verification** - proof of secret knowledge without revealing it
- **No internet connection required**

### User-Friendly Interface
- **Interactive terminal UI** with clear menus
- **Password strength customization** (4-100 characters)
- **Descriptive service names** for easy identification
- **Clear feedback** and error messages

---

## ⚙️ How It Works

**Traditional Password Managers:**
- Store encrypted passwords
- Require master password decryption
- Risk of data breaches

**clipassman v2.0.1:**
1. **You provide**: Description + Secret phrase
2. **System generates**: Public key (hash of secret)
3. **System stores**: Only description, length, and public key
4. **When needed**: Enter secret → Password regenerated

### Creating a Password:
```
1. Choose "Add Password"
2. Enter description (e.g., "GitHub Account")
3. Enter secret phrase (never leaves your terminal)
4. Set password length (4-100 characters)
5. Password is generated and displayed
```

### Retrieving a Password:
```
1. Choose "Get/Delete Password"
2. Select password entry from list
3. Enter your secret phrase
4. Password is regenerated identically
```

---

## 🔄 Smart Password Ecosystem

This CLI manager is part of a comprehensive suite of applications built on deterministic password technology:

### 🛠️ Console Applications
- [**CLI Smart Password Generator**](https://github.com/smartlegionlab/clipassgen/) - Smart passwords generator
- **CLI Smart Password Manager** (this tool) - Smart Password manager

### 🖥️ Desktop Applications
- [**Desktop Smart Password Manager**](https://github.com/smartlegionlab/smart-password-manager-desktop) - Graphical interface

### 🌐 Web Applications
- [**Web Smart Password Manager**](https://github.com/smartlegionlab/smart-password-manager) - Browser-based interface

### 💡 Core Technology
- [**SmartPassLib v2.0.0**](https://github.com/smartlegionlab/smartpasslib) - Core password generation library

---

## 🛡️ Security Features

### What Makes It Secure:
- **No Password Storage** - Passwords exist only when generated
- **Deterministic Generation** - Same inputs → same output, every time
- **Local Processing** - No data leaves your computer
- **Verification Without Storage** - Public keys verify secret knowledge
- **Open Source** - Transparent codebase for security verification

### Data Privacy:
- All data stored locally in `~/.cases.json`
- No internet connectivity required
- No telemetry or data collection
- No cloud synchronization

---

## 📋 Migration from v1.x

### Important Notes:
- **v2.0.1 is NOT backward compatible** with v1.x
- **All v1.x passwords are invalid** in v2.0.1
- **You must recreate all passwords** using your secret phrases

### Migration Steps:
1. **Backup** any critical passwords from v1.x
2. **Install** v2.0.1 fresh
3. **Delete** old `~/.cases.json` file
4. **Launch** clipassman v2.0.1
5. **Recreate** all passwords using your secret phrases
6. **Update** all service credentials with new passwords

### Why the Breaking Changes?
- Simplified API (removed login parameter)
- Improved cryptographic algorithms
- Better security model
- Cleaner codebase

---

## 🐛 Troubleshooting

### Common Issues:

**"Module not found" errors:**
```bash
# Reinstall with pip
pip install --force-reinstall clipassman

# Check Python version (requires 3.7+)
python --version
```

**Password generation fails:**
- Ensure secret phrase is entered correctly
- Check Caps Lock and keyboard layout
- Verify password length is between 4-100 characters

### Getting Help:
1. Check [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
2. Review the [smartpasslib documentation](https://github.com/smartlegionlab/smartpasslib)
3. Create a new issue with details of your problem

---

## 📜 License

**BSD 3-Clause License**

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

## 🔗 Links & Resources

- **GitHub Repository**: [clipassman](https://github.com/smartlegionlab/clipassman)
- **Core Library**: [smartpasslib](https://github.com/smartlegionlab/smartpasslib)
- **Issues & Support**: [GitHub Issues](https://github.com/smartlegionlab/clipassman/issues)
- **PyPI Package**: [clipassman on PyPI](https://pypi.org/project/clipassman/)
- **Pointer-Based Security Paradigm**: [Paper](https://doi.org/10.5281/zenodo.17204738)
- **Local Data Regeneration Paradigm**: [Paper](https://doi.org/10.5281/zenodo.17264327)

---

**Note**: Always keep backup copies of your secret phrases. If you lose your secret phrase, you cannot regenerate your passwords. The system only stores verification data, not the secrets themselves.

**Warning**: Upgrading from v1.x requires recreating all passwords. Plan your migration accordingly.

![CLI Interface](https://github.com/smartlegionlab/clipassman/raw/master/data/images/clipassman.png)
