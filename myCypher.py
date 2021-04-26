import sys

def encrypt(text,s):
  result = ""
   # transverse the plain text
  for i in range(len(text)):
    char = text[i]
      # Encrypt uppercase characters in plain text
      
    if (char.isupper()):
        result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
    else:
        result += chr((ord(char) + s - 97) % 26 + 97)
  return result

if __name__ == '__main__':
  #check the above function
  s = sys.argv[1]
  filename = sys.argv[2]
  outputfile = sys.argv[3]
  with open(filename, "r+") as file1:
    text = file1.read()
  print('Number of arguments:', len(sys.argv), 'arguments.')
  print('Argument List:', str(sys.argv))
  print("Plain Text : ", text)
  print("Shift pattern : ",s)
  output = encrypt(text.upper(),int(s))
  print(output)
  f = open(outputfile, "w")
  f.write(output)
  f.close()