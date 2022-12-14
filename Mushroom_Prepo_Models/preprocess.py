import pandas as pd 
import numpy as np 

from sklearn.preprocessing import OneHotEncoder



'''
    p = poisonous => 0
    e = edible => 1
'''
def class_encoding(c):
    if c == 'p':
        return 0
    elif c == 'e':
        return 1
    else:
        raise Exception("The class is not p or e")


'''
    bell = b 
    conical = c 
    convex = x 
    flat = f
    sunken = s
    spherical = p
    others = o
'''
def cap_shape_encoding(df):

    bell = []
    conical = []
    convex = []
    flat = []
    sunken = []
    spherical = []

    for index, row in df.iterrows():

        cap_shape = row['cap-shape']

        if cap_shape == 'b':

            bell.append(1)
            conical.append(0)
            convex.append(0)
            flat.append(0)
            sunken.append(0)
            spherical.append(0)

        elif cap_shape == 'c':

            bell.append(0)
            conical.append(1)
            convex.append(0)
            flat.append(0)
            sunken.append(0)
            spherical.append(0)

        elif cap_shape == 'x':

            bell.append(0)
            conical.append(0)
            convex.append(1)
            flat.append(0)
            sunken.append(0)
            spherical.append(0)

        elif cap_shape == 'f':

            bell.append(0)
            conical.append(0)
            convex.append(0)
            flat.append(1)
            sunken.append(0)
            spherical.append(0)

        elif cap_shape == 's':

            bell.append(0)
            conical.append(0)
            convex.append(0)
            flat.append(0)
            sunken.append(1)
            spherical.append(0)

        elif cap_shape == 'p':

            bell.append(0)
            conical.append(0)
            convex.append(0)
            flat.append(0)
            sunken.append(0)
            spherical.append(1)

        else:

            bell.append(0)
            conical.append(0)
            convex.append(0)
            flat.append(0)
            sunken.append(0)
            spherical.append(0)


    df['bell-shape'] = bell
    df['conical-shape'] = conical
    df['convex-shape'] = convex
    df['flat-shape'] = flat
    df['sunken-shape'] = sunken
    df['spherical-shape'] = spherical

    df.drop('cap-shape', axis = 1, inplace = True)

    return df

'''
    fibrous = i 
    grooves = g
    scaly = y
    smooth = s
    shiny = h 
    leathery = l
    silky = k
    sticky = t
    wrinkled = w
    fleshy = e
'''
def cap_surface_encoding(df):

    fibrous = []
    grooves = []
    scaly = []
    smooth = []
    shiny = []
    leathery = []
    silky = []
    sticky = []
    wrinkled = []

    for index, row in df.iterrows():

        cap_surface = row['cap-surface']

        if cap_surface == 'i':

            fibrous.append(1)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 'g':

            fibrous.append(0)
            grooves.append(1)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 'y':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(1)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 's':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(1)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 'h':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(1)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 'l':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(1)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 'k':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(1)
            sticky.append(0)
            wrinkled.append(0)

        elif cap_surface == 't':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(1)
            wrinkled.append(0)

        elif cap_surface == 'w':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(1)

        else:

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)


    df['fibrous-cap-surface'] = fibrous
    df['grooves-cap-surface'] = grooves
    df['scaly-cap-surface'] = scaly
    df['smooth-cap-surface'] = smooth
    df['shiny-cap-surface'] = shiny
    df['leathery-cap-surface'] = leathery
    df['silky-cap-surface'] = silky
    df['sticky-cap-surface'] = sticky
    df['wrinkled-cap-surface'] = wrinkled


    df.drop('cap-surface', axis = 1, inplace = True)

    return df

'''
    brown = n
    buff = b
    gray = g
    green = r
    pink = p
    purple = u
    red = e
    white = w
    yellow = y
    blue = l
    orange = o
    black = k
'''
def cap_color_encoding(df):

    brown = []
    buff = []
    gray = []
    green = []
    pink = []
    purple = []
    red = []
    white = []
    yellow = []
    blue = []
    orange = []

    for index, row in df.iterrows():

        cap_color = row['cap-color']

        if cap_color == 'n':

            brown.append(1)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'b':

            brown.append(0)
            buff.append(1)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'g':

            brown.append(0)
            buff.append(0)
            gray.append(1)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'r':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(1)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'p':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(1)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'u':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(1)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'e':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(1)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'w':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(1)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'y':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(1)
            blue.append(0)
            orange.append(0)

        elif cap_color == 'l':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(1)
            orange.append(0)

        elif cap_color == 'o':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(1)

        else:

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)


    df['brown-cap-color'] = brown
    df['buff-cap-color'] = buff
    df['gray-cap-color'] = gray
    df['green-cap-color'] = green
    df['pink-cap-color'] = pink
    df['purple-cap-color'] = purple
    df['red-cap-color'] = red
    df['white-cap-color'] = white
    df['yellow-cap-color'] = yellow
    df['blue-cap-color'] = blue
    df['orange-cap-color'] = orange


    df.drop('cap-color', axis = 1, inplace = True)

    return df


'''
    bruises-or-bleeding = t => 1
    no = f => 0
'''
def bruise_encoding(c):
    if c == 't':
        return 1
    elif c == 'f':
        return 0
    else:
        raise Exception("The does-bruise-bleed value is not t or f")

'''
    adnate = a 
    adnexed = x
    decurrent = d 
    free = e
    sinuate = s 
    pores = p 
    none = f 
    unknown = ?
'''
def gill_attachment_encoding(df):

    adnate = []
    adnexed = []
    decurrent = [] 
    free = []
    sinuate = [] 
    pores = [] 
    none = [] 

    for index, row in df.iterrows():

        gill_attachment = row['gill-attachment']

        if gill_attachment == 'a':

            adnate.append(1)
            adnexed.append(0)
            decurrent.append(0)
            free.append(0)
            sinuate.append(0)
            pores.append(0)
            none.append(0)

        elif gill_attachment == 'x':

            adnate.append(0)
            adnexed.append(1)
            decurrent.append(0)
            free.append(0)
            sinuate.append(0)
            pores.append(0)
            none.append(0)

        elif gill_attachment == 'd':

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(1)
            free.append(0)
            sinuate.append(0)
            pores.append(0)
            none.append(0)

        elif gill_attachment == 'e':

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(0)
            free.append(1)
            sinuate.append(0)
            pores.append(0)
            none.append(0)

        elif gill_attachment == 's':

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(0)
            free.append(0)
            sinuate.append(1)
            pores.append(0)
            none.append(0)

        elif gill_attachment == 'p':

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(0)
            free.append(0)
            sinuate.append(0)
            pores.append(1)
            none.append(0)

        elif gill_attachment == 'f':

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(0)
            free.append(0)
            sinuate.append(0)
            pores.append(0)
            none.append(1)

        else:

            adnate.append(0)
            adnexed.append(0)
            decurrent.append(0)
            free.append(0)
            sinuate.append(0)
            pores.append(0)
            none.append(0)



    df['adnate-gill-attachment'] = adnate
    df['adnexed-gill-attachment'] = adnexed
    df['decurrent-gill-attachment'] = decurrent
    df['free-gill-attachment'] = free
    df['sinuate-gill-attachment'] = sinuate
    df['pores-gill-attachment'] = pores
    df['none-gill-attachment'] = none

    df.drop('gill-attachment', axis = 1, inplace = True)

    return df


'''
    close = c 
    distant = d 
    none = f
'''

def gill_spacing_encoding(df):

    close = []
    distant = []

    for index, row in df.iterrows():

        gill_spacing = row['gill-spacing']

        if gill_spacing == 'c':

            close.append(1)
            distant.append(0)

        elif gill_spacing == 'd':

            close.append(0)
            distant.append(1)

        else:

            close.append(0)
            distant.append(0)


    df['close-gill-spacing'] = close
    df['distant-gill-spacing'] = distant

    df.drop('gill-spacing', axis = 1, inplace = True)

    return df


'''
    brown = n
    buff = b
    gray = g
    green = r
    pink = p
    purple = u
    red = e
    white = w
    yellow = y
    blue = l
    orange = o
    black = k
    none = f
'''
def gill_color_encoding(df):

    brown = []
    buff = []
    gray = []
    green = []
    pink = []
    purple = []
    red = []
    white = []
    yellow = []
    blue = []
    orange = []
    black = []

    for index, row in df.iterrows():

        gill_color = row['gill-color']

        if gill_color == 'n':

            brown.append(1)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'b':

            brown.append(0)
            buff.append(1)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'g':

            brown.append(0)
            buff.append(0)
            gray.append(1)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'r':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(1)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'p':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(1)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'u':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(1)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'e':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(1)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'w':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(1)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'y':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(1)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif gill_color == 'l':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(1)
            orange.append(0)
            black.append(0)

        elif gill_color == 'o':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(1)
            black.append(0)

        elif gill_color == 'k':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(1)

        else:
            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)


    df['brown-gill-color'] = brown
    df['buff-gill-color'] = buff
    df['gray-gill-color'] = gray
    df['green-gill-color'] = green
    df['pink-gill-color'] = pink
    df['purple-gill-color'] = purple
    df['red-gill-color'] = red
    df['white-gill-color'] = white
    df['yellow-gill-color'] = yellow
    df['blue-gill-color'] = blue
    df['orange-gill-color'] = orange
    df['black-gill-color'] = black


    df.drop('gill-color', axis = 1, inplace = True)

    return df


'''
    bulbous = b 
    swollen = s
    club = c 
    cup = u 
    equal = e
    rhizomorphs = z 
    rooted = r
'''
def stem_root_encoding(df):

    bulbous = []
    swollen = []
    club = []
    cup = []
    equal = []
    rhizomorphs = [] 
    rooted = []

    for index, row in df.iterrows():

        stem_root = row['stem-root']

        if stem_root == 'b':

            bulbous.append(1)
            swollen.append(0)
            club.append(0)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(0)

        elif stem_root == 's':

            bulbous.append(0)
            swollen.append(1)
            club.append(0)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(0)

        elif stem_root == 'c':

            bulbous.append(0)
            swollen.append(0)
            club.append(1)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(0)

        elif stem_root == 'u':

            bulbous.append(0)
            swollen.append(0)
            club.append(0)
            cup.append(1)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(0)

        elif stem_root == 'e':

            bulbous.append(0)
            swollen.append(0)
            club.append(0)
            cup.append(0)
            equal.append(1)
            rhizomorphs.append(0)
            rooted.append(0)

        elif stem_root == 'z':

            bulbous.append(0)
            swollen.append(0)
            club.append(0)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(1)
            rooted.append(0)

        elif stem_root == 'r':

            bulbous.append(0)
            swollen.append(0)
            club.append(0)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(1)

        else:

            bulbous.append(0)
            swollen.append(0)
            club.append(0)
            cup.append(0)
            equal.append(0)
            rhizomorphs.append(0)
            rooted.append(0)


    df['bulbous-stem-root'] = bulbous
    df['swollen-stem-root'] = swollen
    df['club-stem-root'] = club
    df['cup-stem-root'] = cup
    df['equal-stem-root'] = equal
    df['rhizomorphs-stem-root'] = rhizomorphs
    df['rooted-stem-root'] = rooted

    df.drop('stem-root', axis = 1, inplace = True)

    return df

'''
    fibrous = i 
    grooves = g
    scaly = y
    smooth = s
    shiny = h 
    leathery = l
    silky = k
    sticky = t
    wrinkled = w
    fleshy = e
    none = f
'''
def stem_surface_encoding(df):

    fibrous = []
    grooves = []
    scaly = []
    smooth = []
    shiny = []
    leathery = []
    silky = []
    sticky = []
    wrinkled = []
    fleshy = []

    for index, row in df.iterrows():

        stem_surface = row['stem-surface']

        if stem_surface == 'i':

            fibrous.append(1)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'g':

            fibrous.append(0)
            grooves.append(1)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'y':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(1)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 's':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(1)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'h':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(1)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'l':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(1)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'k':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(1)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 't':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(1)
            wrinkled.append(0)
            fleshy.append(0)

        elif stem_surface == 'w':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(1)
            fleshy.append(0)

        elif stem_surface == 'e':

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(1)

        else:

            fibrous.append(0)
            grooves.append(0)
            scaly.append(0)
            smooth.append(0)
            shiny.append(0)
            leathery.append(0)
            silky.append(0)
            sticky.append(0)
            wrinkled.append(0)
            fleshy.append(0)
 


    df['fibrous-stem-surface'] = fibrous
    df['grooves-stem-surface'] = grooves
    df['scaly-stem-surface'] = scaly
    df['smooth-stem-surface'] = smooth
    df['shiny-stem-surface'] = shiny
    df['leathery-stem-surface'] = leathery
    df['silky-stem-surface'] = silky
    df['sticky-stem-surface'] = sticky
    df['wrinkled-stem-surface'] = wrinkled
    df['fleshy-stem-surface'] = fleshy


    df.drop('stem-surface', axis = 1, inplace = True)

    return df

'''
    brown = n
    buff = b
    gray = g
    green = r
    pink = p
    purple = u
    red = e
    white = w
    yellow = y
    blue = l
    orange = o
    black = k
    none = f
'''
def stem_color_encoding(df):

    brown = []
    buff = []
    gray = []
    green = []
    pink = []
    purple = []
    red = []
    white = []
    yellow = []
    blue = []
    orange = []
    black = []

    for index, row in df.iterrows():

        stem_color = row['stem-color']

        if stem_color == 'n':

            brown.append(1)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'b':

            brown.append(0)
            buff.append(1)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'g':

            brown.append(0)
            buff.append(0)
            gray.append(1)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'r':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(1)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'p':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(1)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'u':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(1)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'e':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(1)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'w':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(1)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'y':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(1)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif stem_color == 'l':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(1)
            orange.append(0)
            black.append(0)

        elif stem_color == 'o':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(1)
            black.append(0)

        elif stem_color == 'k':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(1)

        else:
            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)


    df['brown-stem-color'] = brown
    df['buff-stem-color'] = buff
    df['gray-stem-color'] = gray
    df['green-stem-color'] = green
    df['pink-stem-color'] = pink
    df['purple-stem-color'] = purple
    df['red-stem-color'] = red
    df['white-stem-color'] = white
    df['yellow-stem-color'] = yellow
    df['blue-stem-color'] = blue
    df['orange-stem-color'] = orange
    df['black-stem-color'] = black


    df.drop('stem-color', axis = 1, inplace = True)

    return df

'''
    partial = p => 0
    universal = u => 1
'''
def veil_type_encoding(c):
    if c == 'p':
        return 0
    elif c == 'u':
        return 1
    else:
        raise Exception("The veil-type value is not p or u")

'''
    brown = n
    buff = b
    gray = g
    green = r
    pink = p
    purple = u
    red = e
    white = w
    yellow = y
    blue = l
    orange = o
    black = k
    none = f
'''
def veil_color_encoding(df):

    brown = []
    buff = []
    gray = []
    green = []
    pink = []
    purple = []
    red = []
    white = []
    yellow = []
    blue = []
    orange = []
    black = []

    for index, row in df.iterrows():

        veil_color = row['veil-color']

        if veil_color == 'n':

            brown.append(1)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'b':

            brown.append(0)
            buff.append(1)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'g':

            brown.append(0)
            buff.append(0)
            gray.append(1)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'r':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(1)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'p':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(1)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'u':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(1)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'e':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(1)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'w':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(1)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'y':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(1)
            blue.append(0)
            orange.append(0)
            black.append(0)

        elif veil_color == 'l':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(1)
            orange.append(0)
            black.append(0)

        elif veil_color == 'o':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(1)
            black.append(0)

        elif veil_color == 'k':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(1)

        else:
            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)
            black.append(0)


    df['brown-veil-color'] = brown
    df['buff-veil-color'] = buff
    df['gray-veil-color'] = gray
    df['green-veil-color'] = green
    df['pink-veil-color'] = pink
    df['purple-veil-color'] = purple
    df['red-veil-color'] = red
    df['white-veil-color'] = white
    df['yellow-veil-color'] = yellow
    df['blue-veil-color'] = blue
    df['orange-veil-color'] = orange
    df['black-veil-color'] = black


    df.drop('veil-color', axis = 1, inplace = True)

    return df

'''
    ring = t => 1
    none = f => 0
'''
def ring_encoding(c):
    if c == 't':
        return 1
    elif c == 'f':
        return 0
    else:
        raise Exception("The has-ring value is not t or f")


'''
    cobwebby = c
    evanescent = e
    flaring = r
    grooved = g
    large = l
    pendant = p
    sheathing = s
    zone = z
    scaly = y
    movable = m
    none = f
    unknown = ?
'''
def ring_type_encoding(df):

    cobwebby = []
    evanescent = []
    flaring = []
    grooved = []
    large = []
    pendant = []
    sheathing = []
    zone = []
    scaly = []
    movable = []
    none = []

    for index, row in df.iterrows():

        ring_type = row['ring-type']

        if ring_type == 'c':

            cobwebby.append(1)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'e':

            cobwebby.append(0)
            evanescent.append(1)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'r':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(1)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'g':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(1)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'l':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(1)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'p':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(1)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 's':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(1)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'z':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(1)
            scaly.append(0)
            movable.append(0)
            none.append(0)

        elif ring_type == 'y':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(1)
            movable.append(0)
            none.append(0)

        elif ring_type == 'm':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(1)
            none.append(0)

        elif ring_type == 'f':

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(1)

        else:

            cobwebby.append(0)
            evanescent.append(0)
            flaring.append(0)
            grooved.append(0)
            large.append(0)
            pendant.append(0)
            sheathing.append(0)
            zone.append(0)
            scaly.append(0)
            movable.append(0)
            none.append(0)


    df['cobwebby-ring'] = cobwebby
    df['evanescent-ring'] = evanescent
    df['flaring-ring'] = flaring
    df['grooved-ring'] = grooved
    df['large-ring'] = large
    df['pendant-ring'] = pendant
    df['sheathing-ring'] = sheathing
    df['zone-ring'] = zone
    df['scaly-ring'] = scaly
    df['movable-ring'] = movable
    df['none-ring'] = none


    df.drop('ring-type', axis = 1, inplace = True)

    return df

'''
    brown = n
    buff = b
    gray = g
    green = r
    pink = p
    purple = u
    red = e
    white = w
    yellow = y
    blue = l
    orange = o
    black = k
'''
def spore_print_color_encoding(df):

    brown = []
    buff = []
    gray = []
    green = []
    pink = []
    purple = []
    red = []
    white = []
    yellow = []
    blue = []
    orange = []

    for index, row in df.iterrows():

        spore_print_color = row['spore-print-color']

        if spore_print_color == 'n':

            brown.append(1)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'b':

            brown.append(0)
            buff.append(1)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'g':

            brown.append(0)
            buff.append(0)
            gray.append(1)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'r':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(1)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'p':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(1)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'u':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(1)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'e':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(1)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'w':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(1)
            yellow.append(0)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'y':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(1)
            blue.append(0)
            orange.append(0)

        elif spore_print_color == 'l':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(1)
            orange.append(0)

        elif spore_print_color == 'o':

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(1)

        else:

            brown.append(0)
            buff.append(0)
            gray.append(0)
            green.append(0)
            pink.append(0)
            purple.append(0)
            red.append(0)
            white.append(0)
            yellow.append(0)
            blue.append(0)
            orange.append(0)


    df['brown-spore-print-color'] = brown
    df['buff-spore-print-color'] = buff
    df['gray-spore-print-color'] = gray
    df['green-spore-print-color'] = green
    df['pink-spore-print-color'] = pink
    df['purple-spore-print-color'] = purple
    df['red-spore-print-color'] = red
    df['white-spore-print-color'] = white
    df['yellow-spore-print-color'] = yellow
    df['blue-spore-print-color'] = blue
    df['orange-spore-print-color'] = orange


    df.drop('spore-print-color', axis = 1, inplace = True)

    return df

'''
    grasses = g
    leaves = l
    meadows = m
    paths = p 
    heaths = h
    urban = u
    waste = w 
    woods = d
'''
def habitat_encoding(df):

    grasses = []
    leaves = []
    meadows = []
    paths = []
    heaths = []
    urban = []
    waste = [] 

    for index, row in df.iterrows():

        habitat = row['habitat']

        if habitat == 'g':

            grasses.append(1)
            leaves.append(0)
            meadows.append(0)
            paths.append(0)
            heaths.append(0)
            urban.append(0)
            waste.append(0)

        elif habitat == 'l':

            grasses.append(0)
            leaves.append(1)
            meadows.append(0)
            paths.append(0)
            heaths.append(0)
            urban.append(0)
            waste.append(0)

        elif habitat == 'm':

            grasses.append(0)
            leaves.append(0)
            meadows.append(1)
            paths.append(0)
            heaths.append(0)
            urban.append(0)
            waste.append(0)

        elif habitat == 'p':

            grasses.append(0)
            leaves.append(0)
            meadows.append(0)
            paths.append(1)
            heaths.append(0)
            urban.append(0)
            waste.append(0)

        elif habitat == 'h':

            grasses.append(0)
            leaves.append(0)
            meadows.append(0)
            paths.append(0)
            heaths.append(1)
            urban.append(0)
            waste.append(0)

        elif habitat == 'u':

            grasses.append(0)
            leaves.append(0)
            meadows.append(0)
            paths.append(0)
            heaths.append(0)
            urban.append(1)
            waste.append(0)

        elif habitat == 'w':

            grasses.append(0)
            leaves.append(0)
            meadows.append(0)
            paths.append(0)
            heaths.append(0)
            urban.append(0)
            waste.append(1)

        else:

            grasses.append(0)
            leaves.append(0)
            meadows.append(0)
            paths.append(0)
            heaths.append(0)
            urban.append(0)
            waste.append(0)
            

    df['grasses-habitat'] = grasses
    df['leaves-habitat'] = leaves
    df['meadows-habitat'] = meadows
    df['paths-habitat'] = paths
    df['heaths-habitat'] = heaths
    df['urban-habitat'] = urban
    df['waste-habitat'] = waste


    df.drop('habitat', axis = 1, inplace = True)

    return df

'''
    spring = s
    summer = u
    autumn = a
    winter = w
'''
def season_encoding(df):

    spring = []
    summer = []
    autumn = []

    for index, row in df.iterrows():

        season = row['season']

        if season == 's':

            spring.append(1)
            summer.append(0)
            autumn.append(0)

        elif season == 'u':

            spring.append(0)
            summer.append(1)
            autumn.append(0)

        elif season == 'a':

            spring.append(0)
            summer.append(0)
            autumn.append(1)

        else:

            spring.append(0)
            summer.append(0)
            autumn.append(0)

    df['summer-season'] = summer
    df['spring-season'] = spring
    df['autumn-season'] = autumn

    df.drop('season', axis = 1, inplace = True)

    return df



def main():


    df = pd.read_csv('complete_data.csv', sep=',')

    # Convert classes to 0 or 1
    df['class'] = df['class'].apply(class_encoding)

    # One Hot Encoding for Categorical Variables
    df = cap_shape_encoding(df)
    df = cap_surface_encoding(df)
    df = cap_color_encoding(df)
    df['does-bruise-or-bleed'] = df['does-bruise-or-bleed'].apply(bruise_encoding)
    df = gill_attachment_encoding(df)
    df = gill_spacing_encoding(df)
    df = gill_color_encoding(df)
    df = stem_root_encoding(df)
    df = stem_surface_encoding(df)
    df = stem_color_encoding(df)
    df['veil-type'] = df['veil-type'].apply(veil_type_encoding)
    df = veil_color_encoding(df)
    df['has-ring'] = df['has-ring'].apply(ring_encoding)
    df = ring_type_encoding(df)
    df = spore_print_color_encoding(df)
    df = habitat_encoding(df)
    df = season_encoding(df)

    df.drop('Unnamed: 0', axis = 1, inplace = True)

    df.to_csv('encoded_data.csv')

    # print(df.head())
    # print(df.columns)



if __name__ == '__main__':
    main()