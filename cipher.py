def get_k_s():
  in_str = input("\nEnter your setup key: ")
  alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
  k_s = ""
  for i in in_str:
    if alphabet.count(i.upper()) > 0:
      k_s += i.upper()
  return k_s

def get_k_r():
  in_str = input("\nEnter your rotation key, separated by spaces: ")
  valid = ["U","U\'","D","D\'","R","R\'","L","L\'","F","F\'","B","B\'"]
  #k_r = list(map(str, input().split()))
  ctr = 0
  while ctr < len(in_str):
    new_str = in_str[ctr].upper()
    if(ctr+1 < len(in_str) and (in_str[ctr+1] == "\'" or in_str[ctr+1] == "’")):
      in_str += "\'"
      ctr += 1
    ctr += 1
    try:
      valid.index(new_str)
      k_r.append(new_str)
    except ValueError:
      raise Exception("Error: k_r must contain ONLY \"U\", \"U'\", \"D\", \"D'\", \"F\", \"F'\", \"B\", \"B'\", \"L\", \"L'\", \"R\", \"R'\"")
  print(k_r)
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
      print("\nCiphertext: \n", cipher.encrypt(ptext), "\n\n")
    elif choice.lower() == 'decrypt':
      ctext = input("\nEnter the ciphertext you want to decrypt: ")
      cipher = cs.Cipher(k_s, k_r)
      print("\nPlaintext: \n", cipher.decrypt(ctext), "\n\n")
    elif choice.lower() == 'newkeys':
      k_s = get_k_s()
      k_r = get_k_r()

if __name__ == "__main__":
  main()
