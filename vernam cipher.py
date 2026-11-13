def mainmenu():
    print("--------------")
    print("The Vernam Cipher Menu")
    print("1 to encrypt a message.")
    print("2 to decrypt a message.")
    print("3 to see the description of this program.")
    print("4 to quit the program.")
    option = int(input("Please enter your chosen option from the list above. "))
    if option == 1:
        print("Encrypt a message selected.")
        option1()
    elif option == 2:
        keyquestion = input("Do you have the key to decrypt the message? Without a key, your message cannot be decrypted ever. ")
        if keyquestion == "yes":
            print("Decrypt a message selected.")
            option2()
        elif keyquestion == "no":
            print("Message cannot be decrypted without a key.")
            mainmenu()
        else:
            print("Invalid response. Returning to main menu.")
            mainmenu()
    elif option == 3:
        print("Description of the program selected.")
        option3()
    elif option == 4:
        print("Quit the program selected. Goodbye!")
        exit()
    else:
        print("Invalid choice. Returning to main menu.")
        mainmenu()

def vernam_cipher(plaintext, key):
    # Convert strings to bytes
    plaintext_bytes = plaintext.encode()
    key_bytes = key.encode()

    ciphertext_bytes = bytearray()
    for p, k in zip(plaintext_bytes, key_bytes):
        ciphertext_bytes.append(p ^ k)

    return ciphertext_bytes.decode()

def vernam_decipher(ciphertext, key):
    """
    Reverses a Vernam cipher encryption using the provided key.
    """
    ciphertext_bytes = ciphertext.encode()
    key_bytes = key.encode()
    plaintext_bytes = bytearray()

    for c, k in zip(ciphertext_bytes, key_bytes):
        plaintext_bytes.append(c ^ k)

    return plaintext_bytes.decode()


def option1():
    key = input("Please enter your key. Ensure that the key is at least the same length as the plaintext you will enter. ")
    plaintext = input("Please enter the plaintext. ")
    ciphertext = vernam_cipher(plaintext, key)
    print(ciphertext)
    mainmenu()

def option2():
    key_input = input("Please enter the key used to encrypt the original message. ")
    ciphertext_input = input("Please enter the ciphertext originally generated. ")
    deciphered_text = vernam_decipher(ciphertext_input, key_input)
    print(deciphered_text)
    mainmenu()

def option3():
    print("Description of the Program:")
    print("---------------------------")
    print("This program can do four tasks.")
    print("1 - Encrypt plaintext to ciphertext using an input of a key from the user (has to be truly random to be worth vernam ciphering) and the original plaintext")
    print("2 - Decrypt ciphertext to plaintext using an input of the key (usually destroyed afterwards) used to encrypt the original plaintext")
    print("3 - Tell the user about the program and how it functions.")
    print("4 - Exit Python and therefore quit the program.")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("NOTICES FROM THE CREATOR:")
    print("Option 1 requires a key made up by the user in order to carry out encryption on the ciphertext and must the same number of characters or more in length as the plaintext.")
    print("Option 2 requires the original key used to encrypt the message to be able to decrypt the message or the program will not be able to undo the encryption.")
    print("Option 3 does not require any special functions, it's literally just printing stuff. I get it it's boring.")
    print("Option 4 will close the program unless you specifically click on the Cancel button in the IDE to show that you don't want to quit.")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("What actually is a vernam cipher?")
    print("According to Physics Maths Tutors 1.3.1 notes for OCR A Level Computer Science, a vernam cipher is a form of encryption which is unbreakable.")
    print("The Vernam cipher makes use of a one-time pad also known as a key that must be a truly random sequence with the same length or greater than the plaintext.")
    print("The key must also be shared in-person by hand, independently of the message and must be destroyed after use in either encryption or decryption, hence why warnings are usually displayed to destroy the one-time pad after use.")
    print("Encryption and decryption of the message is performed bit by bit using an exclusive or (XOR) operation with the shared key.")
    print("This is what makes the vernam cipher so unbreakable and how without the key the message can never be interpreted even if intercepted when encrypted.")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("THIS PROGRAM HAS BEEN WRITTEN BY NICEABCD.INC AND ALL COPYRIGHT GOES TO THE RESPECTED CREATOR. Created by NiceABCD on 24th April 2025.")
    mainmenu()

mainmenu()


