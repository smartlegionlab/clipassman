# clipassman <sup>v0.6.2</sup>

___clipassman___ - Cross-platform console smart password generator and manager.

Working with passwords has never been so secure. 
No encryption, smart passwords are not stored anywhere, they are generated on the fly.
They do not need to be memorized or written down. You only need to remember the secret phrase.

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

***

## What is news:

__clipassman v0.6.2__

Fix errors.

***

## Images:

![LOGO](https://github.com/smartlegionlab/clipassman/raw/master/data/images/clipassman.png)

***

# Description:

___clipassman___ - Cross-platform console smart password generator and manager.

- Passwords are not stored anywhere, neither in open nor in encrypted form, they are generated on the fly.
- Complex passwords up to 1000 characters.
- The password does not need to be stored, memorized or written down anywhere, you only remember
a secret phrase that you keep in your head. 
 
The utility allows you to store and generate complex cryptographic passwords on the fly.
Passwords are not stored in either plaintext or encrypted form. They are not stored anywhere at all,
and are always in the calculated state, but you can only get them by knowing the secret phrase,
which will be stored in your head (I'm sure the most reliable place! Moreover, 
it is not realistic to store complex long passwords in your head!
but the secret phrase, very easy!). 
 
You will create smart passwords using your username (or any word that will be stored in clear text),
the length of the password (no matter how long the password from will always be the same, 
specifying the length you just count the required number of characters from the available ones (4-1000)), 
as well as the secret phrase.
 
A secret phrase is like your password to access a password. It will be stored in your head,
and it will be required when generating a new password, 
as well as each time your password is requested. 
You can use the same secret phrase to generate different passwords using different usernames,
in this case, the passwords will be different.
After all, the main meaning is that the pair: login and secret phrase,
they will always return the same password!
 
That's why you basically don't need your metadata file. 
It is created only for convenience, and faster access to passwords.
You can get your password from any device at any time using this utility, 
and your password pair: login + secret phrase.
Regardless of the system or device , you will receive your password. 
This is convenient for securely storing, retrieving, and recovering your passwords.
 
You need to keep your secret phrase secret. 
If an attacker finds out your username and secret phrase,
it will easily generate your password. But still, it's almost impossible. 
After all, read your secret phrase he can't get out of your head.

You don't have to use real logins. Login in our case is simply the name of your case, 
under which the case will be stored in the manager, 
for further password generation on the fly. 
It will also be used in the process of generating a smart password, 
so it is important, but can be stored in clear text.

A file will be created on your system, in your home folder. 
It will store open data: 1. Login. 2. Password length. 3. 
Public key for each case. Having stolen this data, the attacker will in any case 
not be able to obtain your smart passwords, 
since they can only be obtained by knowing the secret phrase, and it is stored in your head.

---

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