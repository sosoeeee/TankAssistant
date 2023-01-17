import win32gui
import cv2
import pytesseract
import numpy as np
import re


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


def imgResize(image):
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 400
    height_new = 300
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new[50:390, :]


def findArrow(image):
    image = image[7:26, 74:95]
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binaryImg = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    height, width = binaryImg.shape[0], binaryImg.shape[1]
    whitePixel = 0
    for i in range(height):
        for j in range(width):
            if binaryImg[i, j] == 255:
                whitePixel = whitePixel + 1
    if whitePixel / (height * width) > 0.1:
        return 1
    else:
        return -1


def getWindPower():
    rawImg = cv2.imread('test.jpg')
    y = rawImg.shape[0]
    x = rawImg.shape[1]
    ImgNumberPart = rawImg[7:25, 42:68]
    # ImgNumberPart = cv2.GaussianBlur(ImgNumberPart, (3, 3), 0)
    ImgNumberPart = imgResize(ImgNumberPart)
    grayImg = cv2.cvtColor(ImgNumberPart, cv2.COLOR_BGR2GRAY)
    ret, binaryImg = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((15, 15), np.uint8)
    erodeImg = ~cv2.erode(~binaryImg, kernel, 1000)
    # cv2.imshow('test', erodeImg)
    # cv2.waitKey(2000)
    config = r'--oem 3 --psm 6 outputbase digits'
    string = pytesseract.image_to_string(erodeImg, lang='eng', config=config)
    print(string)
    string = re.sub(r'\D', '', string)  # 滤除非数字字符
    if string == '':
        return 'NONE'
    print(int(string) * findArrow(rawImg))
    return int(string) * findArrow(rawImg)

# getWindPower()