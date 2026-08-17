# AES Key Recovery

Lab Assessment — Network Security, Year 4, BSc Computer Science.

Recovers a partially-redacted AES key. A Vigenère-encrypted key (`key_v.txt`, puzzle `case_v.txt`) is decrypted to reveal an AES key with several bits masked as `X`; the script then brute-forces the missing hex nibbles against a target ciphertext until the output decodes to valid text.

## Files

| File | Description |
|------|-------------|
| `aes_key_recovery.py` | Brute-forces the masked AES key and decrypts the ciphertext |
| `case_v.txt` | Vigenère ciphertext (puzzle input) |
| `key_v.txt` | Vigenère-encrypted AES key (puzzle input) |

## Usage

```bash
pip install -r requirements.txt
python3 aes_key_recovery.py
```

Place the target `.aes` ciphertext alongside the script (referenced as `9.aes`).
