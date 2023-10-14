import cv2
#django se web app
#configure parameter
source = "image.png"
destination ='newImage.jpeg'
scale_percent =50

src =cv2.imread(source, cv2.IMREAD_UNCHANGED)

#cv2.imshow("title",image)

#percent by which image is resized

#calculate the 50 percent of original dimensions
new_width =int(src.shape[1] * scale_percent /100)
new_height = int(src.shape[0] * scale_percent /100)

#resize image
output=cv2.resize(src ,(new_width , new_height))
cv2.imwrite('newImage.jpeg',output)
#cv2.waitKey(0)

