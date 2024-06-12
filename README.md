# clipassman <sup>v0.6.3</sup>

___clipassman___ - Cross-platform console smart password generator and manager.

Working with passwords has never been so secure.
There is no encryption, smart passwords are not stored anywhere, they are generated on the fly.
They do not need to be remembered, encrypted or written down. 
You only need to remember the secret phrase. 
And at the right time, using a secret phrase, you can simply generate your password on the fly.

***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/clipassman?label=pypi%20downloads)](https://pypi.org/project/clipassman/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassman)
[![PyPI](https://img.shields.io/pypi/v/clipassman)](https://pypi.org/project/clipassman)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/clipassman)](https://pypi.org/project/clipassman)


***


## Short description:

- Passwords are not stored anywhere, neither in open nor in encrypted form, they are generated on the fly.
- Complex passwords up to 1000 characters.
- The password does not need to be stored, memorized or written down anywhere, you only remember
a secret phrase that you keep in your head. 
- Only the login, password length and public key are stored in open form. 
These entries are stored in a .cases.json file in your home directory. 
If an attacker gains access to this file, they will not be able to obtain your passwords. 
You can only get passwords by knowing the secret phrase, and it is stored in your head. 
Or in any place that no one knows about, and cannot even assume that you are using 
this text as a secret phrase.
***

Author and developer: ___A.A. Suvorov___

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## Help:

`pip install clipassman`

`clipassman`

or

1. Download the project.
2. Unpack to the desired folder.
3. ```python -m venv venv```
4. `source venv/bin/activate`
5. `python app.py`

***

## What is news:

__clipassman v0.6.3__

1. Fix errors.
2. Improved user interface.
3. Restrictions for logins.
4. Password length restrictions.
5. Screenshot updated.
6. Documentation has been corrected.
***

## Images:

![LOGO](https://github.com/smartlegionlab/clipassman/raw/master/data/images/clipassman.png)

***

## Requirements:

smartpasslib: [GitHub](https://github.com/smartlegionlab/smartpasslib/), [PyPi](https://pypi.org/project/smartpasslib/)

***

## Disclaimer of liability:

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

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------