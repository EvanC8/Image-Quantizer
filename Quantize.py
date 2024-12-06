from KMeans import KMeans

alg = KMeans(image="starrynight.jpg", k=24)

dom_colors = alg.dominate_colors()
print("Number of colors: " + str(len(dom_colors)))
for color in dom_colors:
    print(f"{color[0]}, {color[1]}, {color[2]}")

alg.quantize()