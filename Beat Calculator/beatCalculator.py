# program to calculate which frames beats land on
fps = 24
bpm = 124
frameCount = 800
offset = 4

# calculate internal variables
fpm = fps * 60

# loop
beat = 0
frame = 0
while frame < frameCount:
    frame = round((fpm * beat) / bpm) + offset
    print(frame)
    beat += 1
