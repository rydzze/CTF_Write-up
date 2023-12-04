import os
import random
import threading
import time

banner = """I think that my hash function should be free of collisions.
However, if you prove me wrong by finding collisions, I'll reward you with a flag.
Good luck!
"""

with open("flag.txt", "r") as f:
    flag = f.read().strip()

max_rounds = 30
time_limit = 10
s_charset = [chr(i) for i in range(33, 127)]
s_min_len = 32
s_max_len = 64

def die(timeout):
    time.sleep(timeout)
    print("\n\nTime is up!")
    os._exit(0)

def simpleHashFunction(pt):
    mod = 2**128
    mult = 31107660549029995755035237740128219709
    cur = 281483737825725237143369797025428684609
    for c in pt:
        cur = ((cur + ord(c)) * mult) % mod
    ct = ""
    for i in range(16):
        ct = hex(cur % 256)[2:].zfill(2) + ct
        cur >>= 8
    return ct

def generateRandomString(length, charset):
    return ''.join([random.choice(charset) for i in range(length)])

def main():
    thr = threading.Thread(target=die, args=(time_limit,))
    thr.start()

    random.seed(time.time())
    print(banner)
    print(
        "You will have",
        time_limit,
        "seconds to solve",
        max_rounds,
        "tests. Good luck!\n",
    )

    for rnd in range(max_rounds):
        print(f"ROUND {rnd+1}/{max_rounds}:")

        s = generateRandomString(random.randrange(s_min_len, s_max_len + 1), s_charset)
        hsh = simpleHashFunction(s)
        print("s =", s)
        print("hash =", hsh)
        print("> ", end="")

        try:
            raw_user_input = input()
            if len(raw_user_input) > 1024:
                print("Please keep your string to <= 1024 characters, exiting!")
                os._exit(0)

            if raw_user_input == s:
                print("Your string cannot be the same as my string, exiting!")
                os._exit(0)

            for ch in raw_user_input:
                if ch not in s_charset:
                    print(f"Your string can only contain characters in the charset {s_charset}, exiting!")
                    os._exit(0)

            user_hsh = simpleHashFunction(raw_user_input)
            if hsh != user_hsh:
                print(f"Your hash, {user_hsh}, does not match my hash, exiting!")
                os._exit(0)
        except:
            print("Unable to parse your input, exiting!")
            os._exit(0)

        print("Collision Found!\n")

    print("Congrats! Here's the flag:", flag)

if __name__ == "__main__":
    main()
