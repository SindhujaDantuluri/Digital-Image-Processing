import cv2
import numpy as np

angle = -45
shear = 0.5
translation = 5

type_border = cv2.BORDER_CONSTANT
color_border = (255, 255, 255)

img = cv2.imread('ch.jpeg')
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)

cos_part = np.abs(M[0, 0])
sin_part = np.abs(M[0, 1])

new_cols = int((rows * sin_part) + (cols * cos_part)) 
new_rows = int((rows * cos_part) + (cols * sin_part))

new_cols += (shear*new_cols)
new_rows += (shear*new_rows)

up_down = int((new_rows-rows)/2)
left_right = int((new_cols-cols)/2)

final_image = cv2.copyMakeBorder(img, up_down, up_down,left_right,left_right,type_border, value = color_border)
rows,cols = final_image.shape[:2]

M_rot = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
translat_center_x = -(shear*cols)/2
translat_center_y = -(shear*rows)/2

M = M_rot + np.float64([[0,shear,translation + translat_center_x], [shear,0,translation + translat_center_y]])
final_image  = cv2.warpAffine(final_image , M, (cols,rows),borderMode = type_border, borderValue = color_border)

cv2.imshow("Unsheared Image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()