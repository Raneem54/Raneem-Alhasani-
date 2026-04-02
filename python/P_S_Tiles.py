totalWidth=100
tileWidth=5
maximumTiles=totalWidth/tileWidth
if maximumTiles%2 ==0:
    maximumTiles-=1
else:
    maximumTiles=maximumTiles
gap= (totalWidth-(maximumTiles*tileWidth))/2
print("Number of tiles is",maximumTiles)
print("The size on each side is",gap)