from image_functions import *
import cv2

BG_CAP_CENTER_POINTS = {
    'front_cap_1': [290, 270],
    'left_cap_1': [310, 590],
    'right_cap_1': [435, 680],
    'front_cap_2': [850, 270],
    'left_cap_2': [870, 590],
    'right_cap_2': [1000, 682],
}

MIN_ALPHA_TO_APPEAR = 70


class Combiner:

    def inkLogo(file, rgb):
        logo = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        h, w = logo.shape[:2]
        for row in range(h):
            for col in range(w):
                if (logo[row, col][3] > MIN_ALPHA_TO_APPEAR):
                    logo[row, col] = [rgb[2],rgb[1],rgb[0], logo[row, col][3]]
        cv2.imwrite(file, logo)
        return file

    def combine(layoutUrl, logoUrls):
        largeLogoUrl, smallLeftLogoUrl, smallRightLogoUrl, largeLogoUrl2, smallLeftLogoUrl2, smallRightLogoUrl2 = logoUrls
        background = cv2.imread(layoutUrl)
        largeSizeLogo = cv2.imread(largeLogoUrl, cv2.IMREAD_UNCHANGED)
        leftSizeLogo = cv2.imread(
            smallLeftLogoUrl, cv2.IMREAD_UNCHANGED)
        rightSizeLogo = cv2.imread(
            smallRightLogoUrl, cv2.IMREAD_UNCHANGED)
        largeSizeLogo2 = cv2.imread(largeLogoUrl2, cv2.IMREAD_UNCHANGED)
        leftSizeLogo2 = cv2.imread(
            smallLeftLogoUrl2, cv2.IMREAD_UNCHANGED)
        rightSizeLogo2 = cv2.imread(
            smallRightLogoUrl2, cv2.IMREAD_UNCHANGED)

        bgHeight, bgWidth = background.shape[:2]

        for cap in BG_CAP_CENTER_POINTS:
            logoIteratorX = 0
            logoIteratorY = 0
            logoHeight, logoWidth = largeSizeLogo.shape[:2] if cap.startswith(
                'front') else leftSizeLogo.shape[:2] if cap.startswith('right') else rightSizeLogo.shape[:2]

            for row in range(BG_CAP_CENTER_POINTS[cap][0] - int(logoHeight/2), BG_CAP_CENTER_POINTS[cap][0] + int(logoHeight/2)):
                for col in range(BG_CAP_CENTER_POINTS[cap][1] - int(logoWidth/2), BG_CAP_CENTER_POINTS[cap][1] + int(logoWidth/2)):

                    if not cap.endswith('2'):
                        logo_channels = largeSizeLogo[logoIteratorX, logoIteratorY] if cap.startswith(
                            'front') else leftSizeLogo[logoIteratorX, logoIteratorY] if cap.startswith('right') else rightSizeLogo[logoIteratorX, logoIteratorY]
                    else:
                        logo_channels = largeSizeLogo2[logoIteratorX, logoIteratorY] if cap.startswith(
                            'front') else leftSizeLogo2[logoIteratorX, logoIteratorY] if cap.startswith('right') else rightSizeLogo2[logoIteratorX, logoIteratorY]

                    logoIteratorY += 1
                    if (row > bgHeight or col > bgWidth):
                        break
                    background_channels = background[row, col]
                    composite_channels = logo_channels[:
                                                       3] if logo_channels[3] > MIN_ALPHA_TO_APPEAR else background_channels

                    background[row, col] = composite_channels
                logoIteratorX += 1
                logoIteratorY = 0

        cv2.imwrite('combined.png', background)
        return 'combined.png'
