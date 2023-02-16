from rmbgapi import removeBG
from image_functions import *
from combiner import Combiner
from PIL import ImageColor


class Manager:
    def __init__(self):
        self._layoutUrl = ''
        self._logoUrl = ''
        self._logoUrl2 = ''
        self._smallLeftLogoUrl = ''
        self._smallLeftLogoUrl2 = ''
        self._smallRightLogoUrl = ''
        self._smallRightLogoUrl2 = ''
        self._color1 = ''
        self._color2 = ''
        self._processImgUrl = ''

    def validate(self):
        if (self._layoutUrl != ''
           and self._logoUrl != ''
           and self._logoUrl2 != ''
           and self._smallLeftLogoUrl != ''
           and self._smallLeftLogoUrl2 != ''
           and self._smallRightLogoUrl != ''
           and self._smallRightLogoUrl2 != ''):
            return True
        else:
            return False

    def getLayoutUrl(self):
        return self._layoutUrl

    def setLayoutUrl(self, value):
        self._layoutUrl = value
        self._processImgUrl = value

    def getLogoUrl(self):
        return self._logoUrl

    def setLogoUrl(self, value):
        self._logoUrl = value

    def getColor1(self):
        return self._color1

    def setColor1(self, value):
        self._color1 = value
        if(self.validate()):
            self.inkLogo(1, value)

    def getColor2(self):
        return self._color2

    def setColor2(self, value):
        self._color2 = value
        if(self.validate()):
            self.inkLogo(2, value)

    def getProcessImgUrl(self):
        return self._processImgUrl

    def setProcessImgUrl(self, value):
        self._processImgUrl = value

    def inkLogo(self, index, color):
        if index == 1:
            print(ImageColor.getrgb(color))
            self._logoUrl = Combiner.inkLogo(
                self._logoUrl, ImageColor.getrgb(color))
            self._smallLeftLogoUrl = Combiner.inkLogo(self._smallLeftLogoUrl,
                                                      ImageColor.getrgb(color))
            self._smallRightLogoUrl = Combiner.inkLogo(self._smallRightLogoUrl,
                                                       ImageColor.getrgb(color))
        else:
            self._logoUrl2 = Combiner.inkLogo(self._logoUrl2,
                                              ImageColor.getrgb(color))
            self._smallLeftLogoUrl2 = Combiner.inkLogo(self._smallLeftLogoUrl2,
                                                       ImageColor.getrgb(color))
            self._smallRightLogoUrl2 = Combiner.inkLogo(self._smallRightLogoUrl2,
                                                        ImageColor.getrgb(color))

    def cleanLogo(self):
        self._logoUrl, self._logoUrl2 = removeBG(self._logoUrl)
        self._logoUrl = largeCapLogoResize(self._logoUrl)
        self._logoUrl2 = largeCapLogoResize(self._logoUrl2)
        self._smallLeftLogoUrl, self._smallRightLogoUrl = getPerspectiveLogo(
            smallCapLogoResize(self._logoUrl))
        self._smallLeftLogoUrl2, self._smallRightLogoUrl2 = getPerspectiveLogo(
            smallCapLogoResize(self._logoUrl2))

    def update(self):
        self._processImgUrl = Combiner.combine(self._layoutUrl, [
                                               self._logoUrl, self._smallLeftLogoUrl, self._smallRightLogoUrl, self._logoUrl2, self._smallLeftLogoUrl2, self._smallRightLogoUrl2])
        return self._processImgUrl
