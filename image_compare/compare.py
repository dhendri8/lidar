# import the necessary packages
from func_timeout import func_set_timeout, func_timeout, FunctionTimedOut
import numpy as np
import cv2

image1 = cv2.imread("sample_images/2019-04-05T19-05-43.jpg")
image2 = cv2.imread("sample_images/2019-04-05T19-05-49.jpg")

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

@func_set_timeout(1)
def compare_images():
	count=0
	while True: 
		image1 = cv2.imread("smaller_sample_images/2019-04-05T19-05-43.jpg")
		image2 = cv2.imread("smaller_sample_images/2019-04-05T19-05-49.jpg")

		print (mse(image1, image2))
		count += 1
		print (count)
		
try: 
	compare_images()
except:
	print("all done")
