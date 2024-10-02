def get_k_s():
  in_str = input("\nEnter your setup key: ")
  alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
  k_s = ""
  for i in in_str:
    if alphabet.count(i.upper()) > 0:
      k_s += i.upper()
  return k_s

def get_k_r():
  in_str = input("\nEnter your rotation key, with each rotation separated by a space: ")
  in_str = in_str.replace("’", "'")
  valid = ["U","U\'","D","D\'","R","R\'","L","L\'","F","F\'","B","B\'"]
  k_r = in_str.split()
  return k_r
  
def main():
  import cryptosystem as cs
  k_s = get_k_s()
  k_r = get_k_r()
  
  while True:
    choice = input("\nEnter 'quit' to stop.\nYour options are: encrypt, decrypt, newkeys, or quit.\nWhat would you like to do? ")
    if choice.lower() == 'quit':
      break

    if choice.lower() == 'encrypt':
      ptext = input("\nEnter the plaintext you want to encrypt: ")
      cipher = cs.Cipher(k_s, k_r)
      print("\nCiphertext:\n", cipher.encrypt(ptext), "\n\n")
    elif choice.lower() == 'decrypt':
      ctext = input("\nEnter the ciphertext you want to decrypt: ")
      cipher = cs.Cipher(k_s, k_r)
      print("\nPlaintext:\n", cipher.decrypt(ctext), "\n\n")
    elif choice.lower() == 'newkeys':
      k_s = get_k_s()
      k_r = get_k_r()

if __name__ == "__main__":
  main()
