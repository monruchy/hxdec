# hxdec

🔓 Hex XOR Decoder for analyzing obfuscated scripts (e.g. PowerShell malware loaders)

## Features
- Decode HEX + XOR encoded strings
- Custom XOR key support
- Output to file
- Safe (no code execution)

## Usage

```bash
python hxdec.py -d "<hex_data>" -k "<key>"

Example

python hxdec.py -d "6d07163d..." -k "IflNgl" -o output.ps1

Why hxdec?

Many malicious scripts use simple XOR + HEX obfuscation to hide payloads.
hxdec helps security researchers quickly reveal the real code safely.

Disclaimer

This tool is for educational and malware analysis purposes only.
Do not use it for malicious activities.