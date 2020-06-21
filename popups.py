import random

color = ["red","black","black","red","black"]
images = ["alert1.png", "alert2.png", "alert3.png","alert4.png","alert5.png"]

for i in range(1,101):
	fh = open("popup"+str(i)+".html", "w+")
	sel = random.randint(0,4)
	fh.write("<html>\n<head>\n<title>ALERT</title>\n<body style=\"background-color:{0};\">\n<script>\n".format(color[sel]))
	height = random.randint(400,800)
	width = random.randint(400,800)
	x = random.randint(100,1600)
	y = random.randint(100,1600)
	fh.write("var windowObjectReference = window.open('popup{4}.html','_blank','height={0},width={1}').moveTo({2},{3});\n".format(height,width,x,y,i+1))
	fh.write("</script>\n")
	if width < height:
		fh.write("<img src=\"{0}\" style=\"width: {1};\">\n</body>\n</html>".format(images[sel],width))
	else:
		fh.write("<img src=\"{0}\" style=\"height: {1};\">\n</body>\n</html>".format(images[sel],height))
	fh.close()

i = 101
fh = open("popup"+str(i)+".html", "w+")
fh.write("<html>\n<head>\n<title>ALERT</title>\n<body style=\"background-color:{0};\">\n<script>\n".format("black"))
fh.write("var windowObjectReference = window.open('popup{4}.html','_blank','height={0},width={1}').moveTo({2},{3});\n".format(500,600,800,200,i+1))
fh.write("</script>\n")
fh.write("</body>\n</html>\n")
fh.close()

i = 102
fh = open("popup"+str(i)+".html", "w+")
fh.write("<html>\n<head>\n<title>ALERT</title>\n<body>\n<h1>")
fh.write("You've been Hacked</h1>\n")
fh.write("<img src=\"{0}\">\n</body>\n</html>".format("alert6.jpeg"))
fh.write("</body>\n</html>\n")
fh.close()
