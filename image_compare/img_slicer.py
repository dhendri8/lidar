import cv2


def crop_image(path):

    img = cv2.imread(path)
    height, width, channels = img.shape

    cropped_img = img[100:200, 0:width]

    filename = path.split("/")[-1]
    newpath = ("smaller_sample_images/" + filename)
    cv2.imwrite(newpath, cropped_img)


crop_image("sample_images/2019-04-05T19-05-43.jpg")
crop_image("sample_images/2019-04-05T19-05-49.jpg")