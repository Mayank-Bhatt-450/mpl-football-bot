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
def left(img,s=(585,344)):
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

                        
def right(img,s=(666,326)):

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
def foots(img):
    flg=0
    for i in range (200):
        if (tell_color_dis(img.getpixel((922-i,431)),( 136 , 21 , 30 ),37.881393849751625  )):#922,431
            flg+=1
            break
    if flg==0:
        return False
    else:
        return True
            
for j in range(1):
#while True:
    img = Image.open("Untitled6.jpg")
    #img =pyautogui.screenshot()
    goal=[]
    if (tell_color_dis(img.getpixel((719,730)),( 238 , 241 , 237 ),105.36602868097478) and
        tell_color_dis(img.getpixel((740,742)),( 39 , 40 , 40 ),158.77972162716497)    and
        tell_color_dis(img.getpixel((701,746)),( 39 , 40 , 40 ),158.77972162716497)     ):
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
                    fg=left(img,(495+i+10,267+k+62))
                    print(fg)
                    if fg!=None:
                        goal.append((495+i,267+k))
                        goal.append(fg)
                    else:
                        if foots(img):
                            goal.append((495+i,267+k))
                            goal.append('left')
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
                    fg=right(img,(944-i-10,267+k+62))
                    print(fg)
                    if fg!=None and goal==[]:
                        goal.append((944-i,267+k))
                        goal.append(fg)
                    else:
                        if goal==[]:
                            goal.append((944-i,267+k))
                            goal.append('right') 
                    break
            if find[0]==True:
                break
        print ('goal=',goal)
        pyautogui.moveTo(720,731)

        if goal[1]=='left':
            pyautogui.dragTo(goal[0][0]+30,goal[0][1]+70,duration=0.2)
        if goal[1]=='right':
            pyautogui.dragTo(goal[0][0]-30,goal[0][1]+70,duration=0.2)
        pyautogui.moveTo(600,600)
        time.sleep(2)
