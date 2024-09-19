#!/usr/bin/python3
import string 

# This code aims to a cipher text with the word thats is n-position from the word to cipher
letters = string.ascii_letters
number = string.digits
special_char = string.punctuation

char = letters + special_char + number #reference characters for the cipher 
plain_txt = input("Enter text to cipher:\n> ")

blk_list = list()                
key_list = list()
key = int(input("Enter the number for the shift: "))                             # Primary key of the cipher text
blk_pos = list()
key_pos = list()

cipher_txt = ""
shift_list = list()  
shift_pos = list()  

for word in plain_txt.split():      # splits phrase to cipher per letter in a word
    blk_list.append(word) 

for i in range(len(blk_list)):      # creates the cipher key word, each word is key position away from the text to cipher
    key_list.append([])
    key_list[i] = blk_list[(i + key) % len(blk_list)] # creates the key number of shifts
    for l in key_list[i]:                                       # this loop check if the word to cipher with is equal length to the word to cipher with 
        if len(key_list[i]) < len(blk_list[i]):      # if the word to cipher with is shorter, add single letter of same word until its equal to the word to cipher too
            key_list[i] += key_list[i] * (len(blk_list[i]))
        elif len(key_list[i]) > len(blk_list[i]):   #if the word to cipher with is longer, shorten it the equal the word to cipher too.
            key_list.insert(i,key_list[i][:len(blk_list[i])]) 
            key_list.pop(i+1)
        else:
            break

lst = list()
for j in range(len(blk_list)):
    blk_pos.append([])
    key_pos.append([])
    for k in blk_list[j]:
        pos = char.index(k)
        blk_pos[j].append(pos)
    for l in key_list[j]:
        pos = char.index(l)
        key_pos[j].append(pos)

for q in range(len(blk_pos)):
    shift_pos.append([])
    for w in range(len(blk_pos[q])):
        cipher_pos = (blk_pos[q][w] + key_pos[q][w]) % len(char)
        shift_pos[q].append(cipher_pos)
        cipher_txt += char[cipher_pos]
    shift_list.append(cipher_txt) 
    cipher_txt = ""                     # clear the variable so that a new variable can be saved

print("\n")
print(" ".join(shift_list))

print("\nDo you want to decipher the cipher text: Y or N ", end="")
choice = input().upper()

if choice == "Y":
    decipher_txt = ""
    deshift_list = list()   
    for r in range(len(blk_pos)):
        for t in range(len(blk_pos[r])):
            decipher_pos = (shift_pos[r][t] - key_pos[r][t]) % len(char)
            decipher_txt += char[decipher_pos]
        deshift_list.append(decipher_txt) 
        decipher_txt = "" 
    print("\n")
    print(" ".join(deshift_list))
else:
    print("Ok GoodBye....")
