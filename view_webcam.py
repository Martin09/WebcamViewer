import cv2

def rotate_image(img, angle):
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

cv2.namedWindow("MBE Cam!")
vc = cv2.VideoCapture(0)

# Set resolution
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    frame = rotate_image(frame, 180)
else:
    rval = False

while rval:
    cv2.imshow("MBE Cam!", frame)
    rval, frame = vc.read()
    frame = rotate_image(frame, 180)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("MBE Cam!")
