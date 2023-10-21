import colorgram as color
colors=color.extract('image.jpeg',30)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.g
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
