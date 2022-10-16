# -----------------------------------------------Encode md5 hash-------------------------------------------
class Encode_md5:
    def E_md5(self):
        while True:
            try:
                import hashlib
                text = input("[+]Enter your text you want to Convert md5hash:> ")
                hash = hashlib.md5(text.encode())
                md5_hash = hash.hexdigest()
                print("Your md5 hash is:> ", md5_hash)
            except:
                print("please get some help!!")
EncMsg=Encode_md5()
EncMsg.E_md5()