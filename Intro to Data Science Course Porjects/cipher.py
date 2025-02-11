def cipher(text):
    if isinstance(text, str):
        encryption = text.strip()
        encryption = list(encryption)
    else:
        return "wrong text"
    
    process = []
    
    for char in encryption:
        if char.isupper():
           shifted = ((ord(char) - ord('A') + 20) % 26) + ord('A')
        else:
            shifted = ((ord(char) - ord('a') + 20) % 26) + ord('a')
        process.append(chr(shifted))
    
    decrypted = ''.join(process)
    return decrypted
    
    

print(cipher("XIA"))
        
        
        
        
        
for i in range(20):
    
    if (i % 3 == 0)and (i % 5 == 0):
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
       print(i) 
        
        
    