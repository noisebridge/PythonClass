# Hands-on Cryptography in Python - Noisebridge Python Class


We'll discuss the basics of cryptography. We'll briefly survey standard tools, best practices, and some "hacks".  Then we'll break our own rules and implement Diffie Helman. 

Speaker: Blake Griffith 


* Wiki Entry [https://noisebridge.net/wiki/Pyclass](https://noisebridge.net/wiki/Pyclass)
* Lessons [https://github.com/PyClass/PyClassLessons/tree/master/course](https://github.com/PyClass/PyClassLessons/tree/master/course)

* **PDF Notes download** the handwritten notes here (warning these are incompete) [noisebridge-python-cryptography-2017_01-30.pdf](noisebridge-python-cryptography-2017_01-30)

![Notes](images/notes_screenshot.png)

## Code


~~~~
def rand_int(nbytes):
    return int.from_bytes(os.urandom(nbytes), byteorder='little')
 
def rand_less_than(upper_bound):
    while True:
        r = rand_int(((upper_bound).bit_length() + 7) // 8)
        if r < upper_bound:
            return r
 
def is_prime(p):
    for _ in range(5):
        a = rand_less_than(p)
        if not pow(a, p - 1, p) == 1:
            return False
    return True
 
def choose_parameters():
    while True:
        modulus = rand_int(1024 // 8)
        if is_prime(modulus):
            break
    base = rand_less_than(modulus)
    return base, modulus
 
class Peep:
    def __init__(self, base, modulus):
        self.base = base
        self.modulus = modulus
        self.private = rand_less_than(modulus)
        self.public = pow(base, self.private, modulus)
 
    def send(self):
        return self.public
 
    def receive(self, B):
        self.shared_secret = pow(B, self.private, self.modulus)
 
if __name__ == '__main__':
    base, modulus = choose_parameters()
    alice = Peep(base, modulus)
    bob = Peep(base, modulus)
 
    A = alice.send()
    B = bob.send()
 
    alice.receive(B)
    bob.receive(A)
 
    assert alice.shared_secret == bob.shared_secret
    ~~~~