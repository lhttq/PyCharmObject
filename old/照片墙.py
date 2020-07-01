from PIL import Image
import os,sys

mw = 100
ms = 20

msize = mw*ms
toImage = Image.new('RGBA',(2000,2000))

for y in range(1,21):
	for x in range(1,21):
		try:
			fromImage = Image.open(r"C:/Users/Administrator/Desktop/love/ta/%s.jpg" %str(ms*(y-1)+x))
			fromImage = fromImage.resize((100,100),Image.ANTIALIAS)
			toImage.paste(fromImage,((x-1)*mw,(y-1)*mw))
		except IOError:
			pass
toImage.show()
toImage.save('C:/Users/Administrator/Desktop/ta.jpg')
