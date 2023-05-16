import random

def Encoding():
    message=input("enter your message for Encoding:->\n ")
    choice1=["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        '!','@','#','$','%','^','&','*','-','+','=','~']
    choice2=['1','2','3','4','5','6','7','8','9',]
    key=""
    for i in range (0,40):
        if i%3==0:
            key=key+random.choice(choice2)
        else:
            key=key+random.choice(choice1)
    key_heart=key[::2][::3][1]
    print(key_heart)
    encrypted1=""
    for alp in message:
        ascii_value=chr(ord(alp)+int(key_heart))
        # print(ascii_value) 
        encrypted1=encrypted1+ascii_value

    binary_encrypted = bin(int.from_bytes(encrypted1.encode(), 'big'))[2:]
    print("Your Message :-",binary_encrypted)
    print("your Encryption key :-",key)



def Decrypt():
    encoded_message=input('Enter Binary message for decrypting:->')
    print();print()
    inputed_key=input('Enter Encryption key :->')
    encode_binary_message=int(encoded_message, 2).to_bytes((len(encoded_message) + 7) // 8,'big').decode()
    print(encode_binary_message)
    key_heart_for_decode=inputed_key[::2][::3][1]
    decoded_ascii=""
    for alp1 in encode_binary_message:
        ascii_decode=chr(int(ord(alp1)-int(key_heart_for_decode)))
        decoded_ascii=decoded_ascii+ascii_decode

    print('your decoded message is :- \n \t',decoded_ascii)



while True:
    option=input('select a option :-\n \t 1:- Encode \n \t 2:- Decode \n \t 3:- Quit  \n :->')
    if(option == "1"):
        Encoding()
    elif(option == "2"):
        Decrypt()
    elif(option=="3"):
        break
    else:
        print('Error !\n \tEnter a valid key :)\n\n\n')