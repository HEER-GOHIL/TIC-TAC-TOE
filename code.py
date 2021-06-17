# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:21:12 2020

@author: HEER
@MAIL:heergohil1509@gmail.com
"""
#MY TIC TAC TOE GAME 
#DEFINING THE BOARD USING THE DICTIONARY

TTT = {'1':' ','2':' ','3':' ',
       '4':' ','5':' ','6':' ',
       '7':' ','8':' ','9':' '}

# value = []

# for i in TTT:
#     value.append(i)
    
#PRINT FUNCTION
def printTTT(tttvalue):
    print("------------")
    print(tttvalue['1'] + ' || ' + tttvalue['2'] + ' || ' + tttvalue['3'])
    print("------------")
    print(tttvalue['4'] + ' || ' + tttvalue['5'] + ' || ' + tttvalue['6'])
    print("------------")
    print(tttvalue['7'] + ' || ' + tttvalue['8'] + ' || ' + tttvalue['9'])
    print("------------")

#FUNCTION TO PLAY GAME
def playgame():
    print("THIS THE FORMAT FOR INPUT")
    print("1" + ' || ' + "2" + ' || ' + "3")
    print("------------")
    print("4" + ' || ' + "5" + ' || ' + "6")
    print("------------")
    print("7" + ' || ' + "8" + ' || ' + "9")
    p1 = input("ENTER NAME OF PLAYER ONE: ")
    p2 = input("ENTER NAME OF PLAYER TWO: ")
    p = p1
    c= 0
    s = 'X'
    for i in range(0,10):
        printTTT(TTT)
        
        print("TURN OF PLAYER "+ p + " : ")
        pos = input()
                
        
        
        if TTT[pos] == ' ':
            TTT[pos] = s   
            c = c + 1
        else:
            print("PLACE ALREADY OCCUPIED")
            continue
            
        if c>4:
            if TTT['1'] == TTT['2'] == TTT['3'] and TTT['1']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['4'] == TTT['5'] == TTT['6'] and TTT['4']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['7'] == TTT['8'] == TTT['9'] and TTT['7']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['1'] == TTT['4'] == TTT['7'] and TTT['1']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['2'] == TTT['5'] == TTT['8'] and TTT['2']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['3'] == TTT['6'] == TTT['9'] and TTT['3']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY  !!" + p + " WON ")                
                break
            elif TTT['1'] == TTT['5'] == TTT['9'] and TTT['1']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
            elif TTT['3'] == TTT['5'] == TTT['7'] and TTT['3']!=' ': 
                printTTT(TTT)
                print("GAME OVER")                
                print("HURRAYY!!  " + p + " WON ")                
                break
        if c==9:
            print("ITS A TIE!!!!!")
        if s == 'X':
            s = 'O'
        else:
            s = 'X'
        if p == p1:
            p = p2
        else:
            p = p1
    print("GAME BY : HHG")            
                 
#main code              
playgame()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
  
