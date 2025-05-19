"""
Amalgam

@author: RDxR10
"""


from Crypto.Util.number import isPrime, bytes_to_long
import random

class Amalgam:
    def __init__(self, bits=128):
        self.p = self._generate_prime(bits)
        self.g = 2  
        self.x = random.randint(2, self.p-2) 
        self.h = pow(self.g, self.x, self.p)
        
    def _generate_prime(self, bits):
        while True:
            s_f = 1
            for prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
                s_f *= prime
            k = random.getrandbits(bits - s_f.bit_length())
            p = k * s_f + 1
            
            if isPrime(p) and p.bit_length() == bits:
                return p
    
    def encrypt(self, m):
        y = random.randint(2, self.p-2)
        c1 = pow(self.g, y, self.p)
        s = pow(self.h, y, self.p)
        c2 = (m * s) % self.p
        return (c1, c2)
    
    def get_public_params(self):
        return (self.p, self.g, self.h)


def run_server():
    prob = Amalgam()
    flag = b"REDACTED"
    flag_ = bytes_to_long(flag)
    flag_enc = prob.encrypt(flag_)
    print(f"p = {prob.p}")
    print(f"g = {prob.g}")
    print(f"h = {prob.h}")
    print(f"Encrypted flag: {flag_enc}")

    while True:
        try:
            print("\n1. Encrypt a message")
            print("2. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                m = int(input("Enter message as integer: "))
                if m == flag_:
                    print("Nice try!")
                    continue
                
                enc = prob.encrypt(m)
                print(f"Encrypted Message: {enc}")
                
            elif choice == "2":
                break
                
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    run_server()