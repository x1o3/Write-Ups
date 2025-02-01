from sympy import mod_inverse
import math

class PaillierDecryption:
    def __init__(self, n, g, lambda_, mu):
        self.n = n
        self.g = g 
        self.lambda_ = lambda_ 
        self.mu = mu

    def L(self, x):
        return (x - 1) // self.n

    def decrypt(self, ciphertext):
        n_square = self.n * self.n
        u = pow(ciphertext, self.lambda_, n_square)
        l_u = self.L(u)
        m = (l_u * self.mu) % self.n
        return m
    
n = 7706350080509933960915731475157042386819671015219471730180600096244041619157664652904817532724395035921591766213569126357832044793897396453188463203180479  # Public key n
p = 67900214844112219555506702373451026839323873323112297627106747938936601518641

q  = n//p
g = n + 1
lambda_ = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
mu = mod_inverse(lambda_, n)
ciphertext = 3200582589046258776155111823678284049720921208421907625678046048235090972062311394465840930987801830150074095472397448894824955433581146581756394990759693485024784752393021623403780900596295902851666159728976310042295438662890462140529728898204884475396206982517133180218657638227721832459756090360135861134
decryption = PaillierDecryption(n, g, lambda_, mu)
decrypted_message = decryption.decrypt(ciphertext)
print(f"Decrypted message: {decrypted_message}")
