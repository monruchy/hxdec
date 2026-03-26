import argparse
import sys


def xor_hex_decode(hex_data: str, key: str) -> str:
    """Decode hex string with XOR key"""
    result = []

    for i in range(0, len(hex_data), 2):
        try:
            byte = int(hex_data[i:i+2], 16)
        except ValueError:
            raise ValueError(f"Invalid hex at position {i}")

        key_char = ord(key[(i // 2) % len(key)])
        decoded_char = chr(byte ^ key_char)
        result.append(decoded_char)

    return "".join(result)


def main():
    parser = argparse.ArgumentParser(
        description="🔓 Decode XOR + HEX obfuscated PowerShell payload"
    )

    parser.add_argument(
        "-d", "--data",
        help="Hex encoded string",
        required=True
    )

    parser.add_argument(
        "-k", "--key",
        help="XOR key (default: IflNgl)",
        default="IflNgl"
    )

    parser.add_argument(
        "-o", "--output",
        help="Save decoded output to file"
    )

    args = parser.parse_args()

    try:
        decoded = xor_hex_decode(args.data, args.key)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    print("\n=== DECODED OUTPUT ===\n")
    print(decoded)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(decoded)
        print(f"\n[+] Saved to {args.output}")


if __name__ == "__main__":
    main()