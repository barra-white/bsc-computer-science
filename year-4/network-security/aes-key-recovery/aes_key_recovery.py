from Crypto.Cipher import AES
import binascii
from itertools import product

# AES decryption function
def aes_decrypt(key_hex, ciphertext):
    key_bytes = binascii.unhexlify(key_hex)
    cipher = AES.new(key_bytes, AES.MODE_ECB)  # Assuming ECB mode is used
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data

# Function to brute-force missing 'X' bits in the key
def brute_force_key(partial_key, ciphertext):
    # Find positions of 'X' in the partial key
    missing_positions = [i for i, c in enumerate(partial_key) if c == 'X']
    
    # Define hex characters to replace 'X' with
    hex_chars = '0123456789ABCDEF'
    
    # Generate all possible combinations for missing positions
    for bits in product(hex_chars, repeat=len(missing_positions)):
        trial_key = list(partial_key)
        
        # Replace 'X' with the current combination of bits
        for i, bit in zip(missing_positions, bits):
            trial_key[i] = bit
        trial_key = ''.join(trial_key)
        
        # Try to decrypt with this trial key
        try:
            decrypted_data = aes_decrypt(trial_key, ciphertext)
            # Check if the decrypted data looks valid (you can add additional checks here)
            if is_valid_decryption(decrypted_data):
                return trial_key, decrypted_data
        except Exception as e:
            continue
    
    return None, None

# Helper function to validate the decryption (e.g., check if it decodes to UTF-8 text)
def is_valid_decryption(decrypted_data):
    try:
        decrypted_text = decrypted_data.decode('utf-8')
        if decrypted_text:  # If we got valid text
            return True
    except UnicodeDecodeError:
        pass
    return False

# Main function to start brute-forcing
def main():
    # The partial AES key with 'X' representing missing bits
    partial_key = "BECBXXACXXDBAEDBEEACFCFBCADEFAFF"
    
    # Path to the encrypted AES file (adjust according to your directory structure)
    aes_file_path = "9.aes"

    
    # Read the AES-encrypted file
    with open(aes_file_path, 'rb') as f:
        ciphertext = f.read()
    
    # Start brute-forcing the AES key
    recovered_key, decrypted_data = brute_force_key(partial_key, ciphertext)
    
    if recovered_key:
        print(f"Recovered AES Key: {recovered_key}")
        with open("decrypted_output.txt", "wb") as output_file:
            output_file.write(decrypted_data)
        print(f"Decrypted Data: {decrypted_data.decode('utf-8', 'ignore')}")
    else:
        print("Failed to recover the key.")

if __name__ == '__main__':
    main()
