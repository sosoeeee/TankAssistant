import win32gui
import cv2
import pytesseract
import numpy as np


def findTitle(window_title):
    """
    查找指定标题窗口句柄
    @param window_title: 标题名
    @return: 窗口句柄
    """
    hWndList = []
    # 函数功能：该函数枚举所有屏幕上的顶层窗口，办法是先将句柄传给每一个窗口，然后再传送给应用程序定义的回调函数。
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    for hwnd in hWndList:
        # 函数功能：该函数获得指定窗口所属的类的类名。
        # clsname = win32gui.GetClassName(hwnd)
        # 函数功能：该函数将指定窗口的标题条文本（如果存在）拷贝到一个缓存区内
        title = win32gui.GetWindowText(hwnd)
        print(title)
        print('------------------------')
        if title == window_title:
            print("标题：", title, "句柄：", hwnd)
            print('------------------------')
            return hwnd
    return -1


# 细化函数，输入需要细化的图片（经过二值化处理的图片）和映射矩阵array
# 这个函数将根据算法，运算出中心点的对应值
def Thin(image, array):
    h, w = image.shape
    iThin = image

    for i in range(h):
        for j in range(w):
            if image[i, j] == 0:
                a = [1] * 9
                for k in range(3):
                    for l in range(3):
                        # 如果3*3矩阵的点不在边界且这些值为零，也就是黑色的点
                        if -1 < (i - 1 + k) < h and -1 < (j - 1 + l) < w and iThin[i - 1 + k, j - 1 + l] == 0:
                            a[k * 3 + l] = 0
                sum = a[0] * 1 + a[1] * 2 + a[2] * 4 + a[3] * 8 + a[5] * 16 + a[6] * 32 + a[7] * 64 + a[8] * 128
                iThin[i, j] = array[sum] * 255
    return iThin


# 映射表
array = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
         1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
         1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
         1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
         0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
         1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
         1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]


def img_resize(image):
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 200
    height_new = 150
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new


testImg = cv2.imread('test.jpg')
y = testImg.shape[0]
x = testImg.shape[1]
testImg = testImg[7:25, 42:68]
testImg = cv2.GaussianBlur(testImg, (3, 3), 0)
testImg = img_resize(testImg)
gray = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((9, 9), np.uint8)
erode = ~cv2.erode(~binary, kernel, 1000000)
cv2.imshow('test', erode)
cv2.waitKey(1000)
# iThin_2 = Thin(~binary.copy(), array)
# cv2.imshow('test', iThin_2)
# cv2.waitKey(5000)
config = r'--oem 3 --psm 6 outputbase digits'
string = pytesseract.image_to_string(erode, lang='eng', config=config)
print(string)
