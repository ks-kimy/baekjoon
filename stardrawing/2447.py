import sys

def stars(N):
    if N == 1:
        return ['*']
    
    draw = stars(N//3)
    drawing = []
    for i in draw:
        drawing.append(i*3)
    for j in draw:
        drawing.append(j+ ' '*(N//3) + j)
    for i in draw:
        drawing.append(i*3)
    return drawing
N = int(sys.stdin.readline())
print('\n'.join(stars(N)))
