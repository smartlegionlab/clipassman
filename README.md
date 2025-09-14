# clipassman <sup>v0.7.7</sup>

___clipassman___ - Cross-platform console Smart Password manager and generator.

Working with passwords has never been so secure.
There is no encryption, smart passwords are not stored anywhere, they are generated on the fly.
They do not need to be remembered, encrypted or written down. 
You only need to remember the secret phrase. 
And at the right time, using a secret phrase, you can simply generate your password on the fly.

***

[![PyPI Downloads](https://static.pepy.tech/badge/clipassman)](https://pepy.tech/projects/clipassman)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassman/month)](https://pepy.tech/projects/clipassman)
[![PyPI Downloads](https://static.pepy.tech/badge/clipassman/week)](https://pepy.tech/projects/clipassman)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/clipassman)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/)
[![PyPI](https://img.shields.io/pypi/v/clipassman)](https://pypi.org/project/clipassman)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/clipassman)](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/clipassman)](https://pypi.org/project/clipassman)


***


## Short description:

___clipassman___ - Cross-platform console Smart Password manager and generator.

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

- Library for creating smart password generators and managers: [smartpasslib](https://github.com/smartlegionlab/smartpasslib/)
- Console Smart Password Generator: [clipassgen](https://github.com/smartlegionlab/clipassgen/)

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

On some systems, when running the command `pip install clipassman` an error occurs, you can solve it like this 

`pip install clipassman --break-system-packages`

`clipassman`

or

1. Download the project.
2. Unpack to the desired folder.
3. `python app.py`

***

## Images:

![LOGO](https://github.com/smartlegionlab/clipassman/raw/master/data/images/clipassman.png)

***

## 📜 License & Disclaimer

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.

- You are free to use, modify, and distribute this software.
- **However, if you modify this software and run it as a hosted service (e.g., a web app), you MUST make the full source code of your modified version available to your users under the same license.**
- The full license text can be found in the [LICENSE](https://github.com/smartlegionlab/clipassman/blob/master/LICENSE) file.

### ⚠️ Important Disclaimer

> **THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
>
> *(This is a summary of the full disclaimer, which is legally binding and located in sections 15 and 16 of the AGPLv3 license).*

For commercial use that is not compatible with the AGPLv3 terms (e.g., including this software in a proprietary product without disclosing the source code), a **commercial license** is required. Please contact me at [smartlegiondev@gmail.com](mailto:smartlegiondev@gmail.com) to discuss terms.