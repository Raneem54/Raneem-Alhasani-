def squarePyramidVolume(Hight,baseArea):
    if Hight>=0 and baseArea>=0:
        return 0.33*Hight*baseArea
    else:
        return 0
print(squarePyramidVolume(7,4))
