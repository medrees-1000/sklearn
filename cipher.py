def cipher(text):
    if isinstance(text, str):
        encryption = text.strip()
        encryption = list(encryption)
    else:
        return "wrong text"
    
    process = []
    
    for char in encryption:
        if char.isupper():
           shifted = ((ord(char) - ord('A') + 3) % 26) + ord('A')
        else:
            shifted = ((ord(char) - ord('a') + 3) % 26) + ord('a')
        process.append(chr(shifted))
    
    decrypted = ''.join(process)
    return decrypted
    
    

print(cipher("XIR"))
        
    
    
        
        
    