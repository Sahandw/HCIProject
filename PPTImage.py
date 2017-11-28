from PIL import Image, ImageTk
class PPTImage:
    def __init__(self , fileName):
        imageOrg = Image.open(fileName)
        imageOrg = imageOrg.resize((450, 400) , Image.ANTIALIAS)
        self.original = ImageTk.PhotoImage(imageOrg)


        imagePreview = Image.open(fileName)
        imagePreview = imagePreview.resize((100,100) , Image.ANTIALIAS)
        self.preview = ImageTk.PhotoImage(imagePreview)

