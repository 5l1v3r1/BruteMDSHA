from hashlib import md5

class MD5:
    def __init__(self):
        self.hash = ""
        self.count = 0
        self.decryptHash = ""
        self.decryptValue = False

    def encrypt(self, hashh):
        self.hash = hashh
        print(f"[+] Hash gerada = {hashh} => {md5(hashh.encode()).hexdigest()}")

    def decrypt(self, hashh, encoding="ascii"):
        for x in open("wordlist/rockyou.txt", "r", encoding="ISO-8859-1").readlines():
            file = str(x.replace("\n", ""))

            if hashh == md5(file.encode()).hexdigest():
                self.hash = md5(file.encode()).hexdigest()
                self.decryptValue = True
                self.decryptHash = file

                return print(f"\n[+] HASH ENCONTRADA > {hashh} = {file}")
            elif hashh != md5(file.encode()).hexdigest():
                self.decryptValue = False
                print(f"[*] Não encontrada < {hashh} = {file}")

            self.count += 1

        if self.decryptValue is True:
            print(f"\n[+] Hash encontrada: {self.hash} => {self.decryptHash}")
        else:
            print(f"\n[!] Não econtrei essa Hash na minha wordlist padrão.")