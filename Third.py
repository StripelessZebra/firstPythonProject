import urllib.request

def imageDownloadMethod(name):
    fileName = "firsImage.jpg"
    urllib.request.urlretrieve(name, fileName)

imageDownloadMethod("http://bravecto.buydogheartwormmedicine.com/wp-content/uploads/2017/04/11.jpg")
