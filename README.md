# Vernam-Cipher-Program
* A lightweight, command-line Python application that demonstrates symmetric encryption and decryption using the Vernam Cipher algorithm via bitwise XOR operations.

## Features
* Encrypt Messages: Converts plaintext into ciphertext using a user-provided key.
* Decrypt Messages: Reverses the XOR encryption to recover the original plaintext using the exact encryption key.
* Built-in Guide: Includes an interactive description explaining how the Vernam cipher works and the rules required to keep it mathematically unbreakable.

## Requirements
* Python 3.x (No external libraries required)

## Usage
* Clone or download ```vernam cipher.py```.
  
* Run the script in your terminal:
```python "vernam cipher.py"```

Follow the on-screen menu prompts:
*  1 — Encrypt a message
*  2 — Decrypt a message
*  3 — View program description and cipher theory
*  4 — Quit the program

## Important Notes
* Key Length: Your key must be at least the same length (in characters) as the message you are encrypting.
* True Randomness: For a Vernam cipher to be truly secure, the key must be completely random, shared securely in person, and destroyed immediately after use.
* Character Encoding: Because XOR operations on ASCII characters can produce non-printable control characters, copying and pasting ciphertext directly into some terminals may behave unexpectedly depending on your console's encoding.
