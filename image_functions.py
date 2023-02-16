import cv2
from scipy import ndimage

MIN_ALPHA_TO_APPEAR = 70

def inkLogo(file, rgb):
    logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    h, w = logo.shape[:2]
    for row in range(h):
        for col in range(w):
            if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                logo[row, col] = [*rgb, logo[row, col][3]]


def cropLogo(file):
    logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    h, w = logo.shape[:2]
    upRowChecker = 0
    bottomRowChecker = h
    leftColChecker = 0
    rightColChecker = w

    for row in range(h):
        for col in range(w):
            if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                upRowChecker = row
                break
        if (upRowChecker != 0):
            break

    for row in range(h-1, 0, -1):
        for col in range(w):
            if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                bottomRowChecker = row
                break
        if (bottomRowChecker != h):
            break

    for col in range(w):
        for row in range(h):
            if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                leftColChecker = col
                break
        if (leftColChecker != 0):
            break

    for col in range(w-1, 0, -1):
        for row in range(h):
            if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                rightColChecker = col
                break
        if (rightColChecker != w):
            break

    #return logo[upRowChecker:bottomRowChecker, leftColChecker:rightColChecker]


def largeCapLogoResize(file):
    logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    h, w = logo.shape[:2]
    ratio = h / w
    defaultDimensions = (230, int(ratio*230))
    logo = cv2.resize(logo, defaultDimensions, interpolation=cv2.INTER_AREA)
    cv2.imwrite(file, logo)
    return file

    
def smallCapLogoResize(file):
    logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    h, w = logo.shape[:2]
    ratio = h / w
    defaultDimensions = (55, int(ratio*55))
    logo = cv2.resize(logo, defaultDimensions, interpolation=cv2.INTER_AREA)
    cv2.imwrite('small'+file, logo)
    return 'small'+file


def getPerspectiveLogo(file):
    logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    h, w = logo.shape[:2]
    leftViewPerspective = logo[0:h, 0:int(w/2)]
    rightViewPerspective = logo[0:h, int(w/2):w]
    leftViewPerspective = ndimage.rotate(leftViewPerspective, 25)
    rightViewPerspective = ndimage.rotate(rightViewPerspective, -25)
    cv2.imwrite('leftViewPerspective'+file, leftViewPerspective)
    cv2.imwrite('rightViewPerspective'+file, rightViewPerspective)
    return ['leftViewPerspective'+file, 'rightViewPerspective'+file]
