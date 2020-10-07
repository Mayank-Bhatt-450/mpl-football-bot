import pyautogui
import time
import PIL
import math,os,subprocess
from PIL import Image
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
img = Image.open("lol2.jpg")
#print(img.getpixel((211,196)))
#495,267=595
#595,298
def left(s=(585,344)):
    for i in range(200):
        if (tell_color_dis(img.getpixel((s[0]+i,s[1])),( 178 , 173 , 173 ),90 )):
            find=True
            #pyautogui.moveTo((s[0]+i,s[1]))
            for k in range(20):
                if ( (tell_color_dis(img.getpixel(((s[0]+i,s[1]+k))),( 178 , 173 , 173 ),90 ))and
                (tell_color_dis(img.getpixel((s[0]+i+1,s[1]+k)),( 178 , 173 , 173 ),90 )) ):
                    pass
                else:
                    find=False
            if find==True:
                print((s[0]+i,s[1]))
                return('left')

                        
def right(s=(666,326)):
    
    for i in range(200):
        #print('in',(s[0]-i,s[1]))
        if (tell_color_dis(img.getpixel((s[0]-i,s[1])),( 178 , 173 , 173 ),90 )):
            

            find=True
            #pyautogui.moveTo((s[0]-i,s[1]))
            for k in range(20):
                if ( (tell_color_dis(img.getpixel(((s[0]-i,s[1]+k))),( 178 , 173 , 173 ),90 ))and
                (tell_color_dis(img.getpixel((s[0]-i-1,s[1]+k)),( 178 , 173 , 173 ),90 )) ):
                    pass
                else:
                    find=False
                    #print('f')
            if find==True:
                #print('r')
                return('right')

for i in range(100):
    for k in range(31):
        find=[True,False]
        for g in range(10):
            if (tell_color_dis(img.getpixel((495+i+g,267+k)),( 255 ,255 ,255 ),34.539832078341085 ) and
            tell_color_dis(img.getpixel((495+i,267+k+g)),( 255 ,255 ,255 ),20 )):
                find[0]=True
            else:
               find[0]=False
        if find[0]==True:
            print((495+i,267+k))
            print(left((495+i+20,267+k+62)))
            break
    if find[0]==True:
            #print((495+i,267+k))
            break


#944,267        
for i in range(100):
    i=i
    for k in range(31):
        find=[True,False]
        for g in range(10):
            if (tell_color_dis(img.getpixel((944-i-g,267+k)),( 255 ,255 ,255 ),34.539832078341085 ) and
            tell_color_dis(img.getpixel((944-i,267+k+g)),( 255 ,255 ,255 ),20)):    
                find[0]=True
            else:
               find[0]=False
        if find[0]==True:   
            print((944-i,267+k))
            print(right((944-i-20,267+k+62)))
            break
    if find[0]==True:
        break

#print(right((888,340)))
