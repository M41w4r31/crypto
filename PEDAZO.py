if messageNumber == '1':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[0])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())

if messageNumber == '2':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[1])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())

if messageNumber == '3':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[2])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())

if messageNumber == '4':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[3])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())

if messageNumber == '5':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[4])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())

if messageNumber == '6':
    # First let us encrypt secret message
    encrypted = encrypt(congratulationsMesagges[5])
    print(encrypted)

    key = encrypted['key']
    print (key)

    decrypted = decrypt(encrypted , key).decode()
    print (decrypted)


    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()

# ENCRYPT
    msg =key.encode()   
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    aesrsa = binascii.hexlify(encrypted).decode()
    print (aesrsa)
# DECRYPT
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted:', decrypted.decode())
