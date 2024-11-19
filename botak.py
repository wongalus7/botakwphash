#!/usr/bin/env python3

import sys
import os
import platform
from passlib.hash import phpass

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def banner():
    green_lime = "\033[92m"
    print(green_lime + """
  ^    ^    ^    ^    ^       ^    ^       ^    ^    ^    ^    ^  
 /B\  /o\  /t\  /a\  /k\     /W\  /P\     /H\  /a\  /s\  /h\  /!\ 
<___><___><___><___><___>   <___><___>   <___><___><___><___><___>
             Mass MD5 WordPress Hash Bruteforce!
""")

clear_screen()
banner()

hashes_file_path = input("List WordPress Hash: ")
wordlist_path = "wordlist.txt"

successful_cracks = []

spin_chars = "|/-\\"

def wphashbrute(hash, total_words):
    try:
        with open(wordlist_path) as f:
            words = f.read().strip().splitlines()
            total_words = len(words)  # Total number of words in wordlist
            
        for index, pwd in enumerate(words):
            spinner = spin_chars[index % len(spin_chars)]  # Spinner animation character
            sys.stdout.write(f"\r\033[92m{hash}  {spinner}  Attempting word {index + 1}/{total_words}\033[0m")
            sys.stdout.flush()

            if phpass.verify(pwd, hash):
                print(f"\n\033[92mWordPress (PHPass) | Password found: {pwd}\033[0m")
                successful_cracks.append((hash, pwd))
                return True
            
    except IOError:
        print("Could not open your wordlist, try again.")
    except ValueError:
        print("WordPress (PHPass) | Invalid hash")
    except Exception as e:
        print(f"Error: {e}")
    return False

def gaskanah():
    try:
        with open(hashes_file_path) as hashes:
            hashes = hashes.read().strip().splitlines()
            total_hashes = len(hashes)
            
            for hash in hashes:
                hash = hash.strip()
                wphashbrute(hash, total_hashes)
            
    except IOError:
        print("Could not open your hashes file, try again.")
    except Exception as e:
        print(f"Error processing hashes: {e}")
    
    if successful_cracks:
        print("\nSuccessfully cracked passwords:")
        for hash, pwd in successful_cracks:
            print(f"\033[92mHash: {hash} | Password: {pwd}\033[0m")
    
    sys.exit(0)

gaskanah()
