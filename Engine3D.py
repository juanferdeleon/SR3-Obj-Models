'''
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Engine 3D

'''

from gl import Bitmap

bmp = Bitmap(600, 800)

def glInit():
    return bmp


if __name__ == '__main__':
    '''Main Program'''

    #Initialize bmp Object
    bmp = glInit()

    #Set all pixels to same color
    bmp.glClear()

    #Set pixel Colors / Star
    bmp.glColor(1, 0.93, 0.2)
    #Polygon 1 / Star
    polygon_1 = ((165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383))
    bmp.glFillPolygon(polygon_1)

    #Set pixel Colors / Square
    bmp.glColor(0.2, 1, 0.87)
    #Polygon 2 / Square
    polygon_2 = ((321, 335), (288, 286), (339, 251), (374, 302))
    bmp.glFillPolygon(polygon_2)

    #Set pixel Colors / Triangle
    bmp.glColor(0.2, 1, 0.26)
    #Polygon 3 / Triangle
    polygon_3 = ((377, 249), (411, 197), (436, 249))
    bmp.glFillPolygon(polygon_3)

    #Set pixel Colors / Teapot
    bmp.glColor(0, 0, 1)
    #Polygon 4 / Teapot
    polygon_4 = ((413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180))
    bmp.glFillPolygon(polygon_4)

    #Set pixel Colors / Teapot hole
    bmp.glColor(1, 1, 1)
    #Polygon 5 / Teapot hole
    polygon_5 = ((682, 175), (708, 120), (735, 148), (739, 170))
    bmp.glFillPolygon(polygon_5)

    #Output BMP
    bmp.glWrite("test.bmp")
