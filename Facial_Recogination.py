from skimage import data, io, filters

# image = data.coins()
image = r"G:\DOWNLOADS\38672464-bioshock-wallpapers.png"
# ... or any other NumPy array!

edges = filters.sobel(image)

io.imshow(edges)
io.show()