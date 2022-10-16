# --------------------------------------------------Convert any link to a QRcode------------------
class LinkImg:
    def link_img(self):
        import qrcode
        link=input("[+]enter your link you want to convert:> ")
        img=qrcode.make(link)
        img.save("qrcode.jpg")
        print("\n[***]---Your img was create and store in folder please check.-------")
