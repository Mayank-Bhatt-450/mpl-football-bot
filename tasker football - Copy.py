import pyautogui
import time
import PIL
import math,os,subprocess
from PIL import Image
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
#print(img.getpixel((211,196)))
#495,267=595
#595,298
def log(im,data):
    f=os.listdir('.\\data')
    k=0
    g=len(os.path.abspath(__file__).split('\\'))-1
    h=len(os.path.abspath(__file__).split('\\')[g])
    j=len(os.path.abspath(__file__))-h
    pth=os.path.abspath(__file__)[:j]

    while True:
        g=str(k)+'.png'
        if  g in f:
           k+=1
        else:
            im.save(pth+'\\data\\'+g,"PNG")
            break
    
    files=open(pth+'\\data\\fen.txt','a')
    files.write(g+'------'+data+'\n')
    files.close()


                        

def foot(img):
    side=''
    for i in range (308):
        if (tell_color_dis(img.getpixel((566+i,431)),( 136 , 21 , 30 ),37.881393849751625  )):#922,431
            if i<720:
                side='r'
            else:

                side='l'
            break
    if side!='':
        return side
    else:
        return False
#img = Image.open("Untitled6.jpg")
#log(img,'data')
#'''
def left(img,sender=''):
    global goal,fg
    for i in range(100):# find left side 
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
                    fg=(495+i,267+k)
                    print('find left',sender,fg)
                    break
            if find[0]==True:
                    #print((495+i,267+k))
                    break
def right(img,sender=''):
    global goal,fg
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
                    fg=(944-i,267+k)
                    print('find right',sender,fg)
                    break
            if find[0]==True:
                    #print((495+i,267+k))
                    break
for j in range(1):
#while True:
    img = Image.open("122.png")
    #img =pyautogui.screenshot()
    goal=[]
    if (tell_color_dis(img.getpixel((719,730)),( 238 , 241 , 237 ),105.36602868097478) and
        tell_color_dis(img.getpixel((740,742)),( 39 , 40 , 40 ),158.77972162716497)    and
        tell_color_dis(img.getpixel((701,746)),( 39 , 40 , 40 ),158.77972162716497)     ):
        side=foot(img)
        print(side)
        if side!=False:
            if side=='l':
                left(img)
            else:
                right(img)

        else:
            left(img,'foot not found')     
        
        
        print ('goal=',(round((fg[0]-495)*2.4053452115812917)),round(fg[1]*2.402669632925473))

        time.sleep(3)
#'''495,0 944,899
#00 499,899
#1080,2160
#2.164328657314629
#2.402669632925473
