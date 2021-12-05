# OpenCVでwatermark表示
import cv2

# Read and Show Image
img = cv2.imread('images/sample.JPG')
watermark = cv2.imread("images/logo.PNG")

# Resize Watermark Image
wm_scale = 40
wm_width = int(watermark.shape[1] * wm_scale/100)
wm_height = int(watermark.shape[0] * wm_scale/100)
wm_dim = (wm_width, wm_height)
resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

# Center: x,y coordinates
h_img, w_img, _ = img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

# Get the Rectangular Region of interest (ROI) and name it ‘roi’.
roi = img[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result

# Where to Save, Name the Watermarked Image
filename = 'images/watermarked_sample.jpg'
cv2.imwrite(filename, img)

cv2.imshow("Resized Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
