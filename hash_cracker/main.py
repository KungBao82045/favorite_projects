def cyber_security1(Red, Cyan, Yellow, White, Green, Purple):
    import hashlib
    import time

    print(f"\n\n\nRunning, {Green}Hash Cracker.{White}!")
    print(f"Created By{Yellow} Jacky{White}")
    print(f'''\nv1.2 {Cyan}- You can now use other hashes like SHA1, SHA224 ect.
    - Program will no longer give you double warning when you choose to iterate
    - Program will now send an error if you type improperly{White}''')

    flag = 0
    hash_types = ("MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512")
    
    hash_enter = str(input(f"\n[*] Select Hash Type({Cyan}MD5{White}, {Red}SHA1{White}, {Yellow}SHA224{White}, SHA256, {Green}SHA384{White}, {Purple}SHA512{White}): ")).upper()
    
    if hash_enter not in hash_types:
        quit(f"[{Cyan}-{White}] Cannot start. Make sure to type the hash properly")

    pass_hash = input(f"\n{White}[{Cyan}*{White}] Enter Hash: ")

    if len(pass_hash) != 32 and hash_enter == "MD5":
        print(f"[{Cyan}-{White}]{Red} MD5 must contain 32 letters!{White}")
        quit(0)
    
    elif len(pass_hash) != 40 and hash_enter == "SHA1":
        print(f"[{Cyan}-{White}]{Red} SHA1 must contain 40 letters!{White}")
        quit(0)
    
    elif len(pass_hash) != 56 and hash_enter == "SHA224":
        print(f"[{Cyan}-{White}]{Red} SHA224 must contain 56 letters!{White}")
        quit(0)
    
    elif len(pass_hash) != 64 and hash_enter == "SHA256":
        print(f"[{Cyan}-{White}]{Red} SHA256 must contain 64 letters!{White}")
        quit(0)
    
    elif len(pass_hash) != 96 and hash_enter == "SHA384":
        print(f"[{Cyan}-{White}]{Red} SHA384 must contain 96 letters!{White}")
        quit(0)
    
    elif len(pass_hash) != 128 and hash_enter == "SHA512":
        print(f"[{Cyan}-{White}]{Red} SHA512 must contain 128 letters!{White}")
        quit(0)

    Wordlist = input(f"[{Cyan}*{White}] Enter File Name: ")

    try:
        pass_file = open(Wordlist, "r")

    except:

        quit(f"\n[{Cyan}-{White}]{Red} File Not Found:{White} %s" % Wordlist)

#    choice = input(f'[{Cyan}*{White}] (Y/N)Would You Like To See Iteration?({Yellow}WARNING: Iteration Can Slower The Process{White}): ')
#
#    if choice.lower() == "y" or choice.lower() == "yes":
#
#        print("\nIterating!"); flag = 1; time.sleep(3)
#
#    elif choice.lower() == 'n' or choice.lower() == "no":
#
#        print("\nInitiating. Please Wait While Jacky Is Searching For Matching Hash. Go Grab Some Coffee Or Something!")
#
#    else:
#
#        quit(f'{Red}ERROR: Couldn\'t Initiate The Code. Exiting...')
    #print(f"\n[{Cyan}*{White}]I Am Now Searching For Matching Hash. Go Grab Some Coffee Or Something!")
    flag = 1

    start = time.perf_counter()
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        try:
            if hash_enter == "MD5":
                digest = hashlib.md5(enc_wrd.strip()).hexdigest()
            elif hash_enter == "SHA1":
                digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
            elif hash_enter == "SHA224":
                digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
            elif hash_enter == "SHA256":
                digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
            elif hash_enter == "SHA384":
                digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
            elif hash_enter == "SHA512":
                digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
            else:
                raise ValueError("ERROR: Couldn't Go To The Next Step. Exiting")
        except Exception as v_E:
            print(v_E)

        if flag == 1:
            print(pass_hash); print(digest); print(word)

        if digest == pass_hash:
            finish = time.perf_counter()
            print(f"\n------------------------------------------")
            print(f"\n    -- MATCHING HASH FOUND -- ")
            print(f"\n[{Cyan}*{White}] {hash_enter} hash used: " + pass_hash)
            print(f"[{Cyan}*{White}] Wordlist used: " + Wordlist)
            print(f"[{Cyan}*{White}] Elapsed TIme: {round(finish-start)} second(s)")
            print(f"\n[{Cyan}!!{White}]{Green} Original String: %s{White}" % word)
            print(f"{White}------------------------------------------")
            break

    else:
        finish = time.perf_counter()
        print("\n------------------------------------------")
        print(f"\n[{Cyan}*{White}] {hash_enter} hash used: {White}%s" % pass_hash)
        print(f"[{Cyan}*{White}] Elapsed TIme: {round(finish-start)} second(s)")
        print(f"[{Cyan}-{White}]{Red} No Match Found In {White}%s" % Wordlist)
        print(f"\n{White}------------------------------------------")

cyber_security1(Red='\033[91m', Cyan='\033[96m', Yellow='\033[93m', White='\033[0m', Green='\033[92m', Purple = '\033[95m')
