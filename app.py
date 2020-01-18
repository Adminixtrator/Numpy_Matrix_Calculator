# Created by: ADMINIXTRATOR             Date: 28th August, 2019
# Twitter: Adminixtrator                Email: minixtrator@gmail.com

import numpy as admin


while True:
    print('''\n\t -------------------\n\t| MATRIX CALCULATOR |
\t -------------------\n''')

    print('''\n Created by: ADMINIXTRATOR             Date: 28th August, 2019
 Twitter: Adminixtrator                Email: minixtrator@gmail.com\n\n''')


    print('''[1.] Determinant\n[2.] Transpose\n[3.] Inverse
[4.] Addition\n[5.] Subtraction\n[6.] Multiplication\n[7.] Division\n[8.] Simultaneous Equation\n''')
    op = input("Please select an operation e.g 1\n")
        
#-------- CONDITIONS ----------
    #OP1--------
#----------------------------| OPERATION 01  - DETERMINANT|------------------------------------------------------------------
    if op == '1':
        asd = input("Please enter the dimension of the matrix e.g 4,4\n")
        #A1----------
        if asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.arange(1,10).reshape(3,3)
            matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))
            #Output----------
            print('MATRIX:\n',matA,'\nDeterminant: ',det,'\n\n')
        #A2----------
        elif asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(2,2)
            matA.flat[[0,1,2,3]] = a11,a12,a21,a22
            det = ((a11*a22) - (a12*a21))
            #Output----------
            print('MATRIX:\n',matA,'\nDeterminant: ',det,'\n\n')
        #A3-----------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.arange(1,17).reshape(4,4)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
            det = (a11*a22*a33*a44)-(a12*a23*a34*a41)+(a13*a24*a31*a42)-(a14*a21*a32*43)+(a14*a23*a32*a41)-(a11*a24*a33*42)+(a12*a21*a34*a43)-(a13*a22*a31*a44)
            #Output----------
            print('MATRIX:\n',matA,'\nDeterminant: ',det,'\n\n')
        #A4-----------
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#--------------------------------------------------------------------------------------------------------------------------------------------
    #OP2--------
#----------------------------| OPERATION 02 - TRANSPOSE |------------------------------------------------------------------

    elif op == '2':
        asd = input("Please enter the dimension of the matrix e.g 2,3\n")
        #B1--------
        if asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B2---------
        elif asd == '2,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a21,a22,a23]).reshape(2,3)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B3---------
        elif asd == '3,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            a31 = int(input())
            a32 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a21,a22,a31,a32]).reshape(3,2)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B4---------
        elif asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B5----------
        elif asd == '2,1':
            a11 = int(input('''Please enter a11 and a21 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a21]).reshape(2,1)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B6---------
        elif asd == '3,1':
            a11 = int(input('''Please enter a11 a21 and a31 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            a31 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a21,a31]).reshape(3,1)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B7---------
        elif asd == '1,2':
            a11 = int(input('''Please enter a11 and a12 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12]).reshape(1,2)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')

        #B8---------
        elif asd == '1,3':
            a11 = int(input('''Please enter a11 a12 and a13 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13]).reshape(1,3)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B9---------
        elif asd == '1,4':
            a11 = int(input('''Please enter a11 a12 a13 and a14 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14]).reshape(1,4)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B10---------
        elif asd == '4,1':
            a11 = int(input('''Please enter a11 a21 a31 and a41 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            a31 = int(input())
            a41 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a21,a31,a41]).reshape(4,1)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
         #B11---------
        elif asd == '4,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a43 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43]).reshape(4,3)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B12---------
        elif asd == '3,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(3,4)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B13---------
        elif asd == '4,2':
            a11 = int(input('''Please enter a11 a12 a21 to a42 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            a31 = int(input())
            a32 = int(input())
            a41 = int(input())
            a42 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a21,a22,a31,a32,a41,a42]).reshape(4,2)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B14---------
        elif asd == '2,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24]).reshape(2,4)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B15---------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA,'\nTranspose: \n',trans,'\n\n')
        #B16----------
        else:
            print('''\nInvalid matrix dimension--
 --Please check your input and try again!\n\n''')
#---------------------------------------------------------------------------------------------------------------------------------------
    #OP3--------
#----------------------------| OPERATION 03  - INVERSE|------------------------------------------------------------------

    elif op == '3':
        asd = input("Please enter the dimension of the matrix e.g 3,3\n")
        #C1----------
        if asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))           
            inv = admin.linalg.inv(matA)
            #Output----------
            print('\nINVERSE:\n',inv,'\n','\nDeterminant: ',det,'\n\n')
        #C2----------
        elif asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
            det = ((a11*a22) - (a12*a21))
            inv = admin.linalg.inv(matA)
            #Output----------
            print('\nINVERSE:\n',inv,'\n','\nDeterminant: ',det,'\n\n')
        #C3-----------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(4,4)
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))
            inv = admin.linalg.inv(matA)
            #Output----------
            print('\nINVERSE:\n',inv,'\n','\nDeterminant: ',det,'\n\n')
        #C4-----------
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#-----------------------------------------------------------------------------------------------------------------------------------------
    #OP4--------
#----------------------------| OPERATION 04 - ADDITION |------------------------------------------------------------------
    elif op == '4':
        asd = input("Please enter the dimension of the matA e.g 3,2\n")
        #------ CHECK --------
        if asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,1' or asd == '2,2' or asd == '2,3' or asd == '2,4' or asd == '3,1' or asd == '3,2' or asd == '3,3' or asd == '3,4' or asd == '4,1' or asd == '4,2' or asd == '4,3' or asd == '4,4' :
            asc = input("Please enter the dimension of the matB e.g 3,2\n")
            #D1--------
            if asc == '2,2' and asd == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
                matB = admin.matrix([b11,b12,b21,b22]).reshape(2,2)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D2---------
            elif asc == '2,3' and asd == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23]).reshape(2,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23]).reshape(2,3)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D3---------
            elif asc == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a32,a32]).resahpe(3,2)
                matB = admin.matrix([b11,b12,b21,b22,b32,b32]).reshape(3,2)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D4---------
            elif asc == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33]).reshape(3,3)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D5----------
            elif asc == '2,1':
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21]).reshape(2,1)
                matB = admin.matrix([b11,b21]).reshape(2,1)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D6---------
            elif asc == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31]).reshape(3,1)
                matB = admin.matrix([b11,b21,b31]).reshape(3,1)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D7---------
            elif asc == '1,2':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12]).reshape(1,2)
                matB = admin.matrix([b11,b12]).reshape(1,2)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D8---------
            elif asc == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13]).reshape(1,3)
                matB = admin.matrix([b11,b12,b13]).reshape(1,3)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D9---------
            elif asc == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14]).reshape(1,4)
                matB = admin.matrix([b11,b12,b13,b14]).reshape(1,4)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D10---------
            elif asc == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                b41 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31,a41]).reshape(4,1)
                matB = admin.matrix([b11,b21,b31,b41]).reshape(4,1)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D11---------
            elif asc == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                #HANDLER---------
                matA = admin.matrix([ a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43]).reshape(4,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43]).reshape(4,3)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D12---------
            elif asc == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(3,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34]).reshape(3,4)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D13---------
            elif asc == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                b41 = int(input())
                b42 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a31,a32,a41,a42]).reshape(4,2)
                matB = admin.matrix([b11,b12,b21,b22,b31,b32,b41,b42]).reshape(4,2)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D14---------
            elif asc == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24]).reshape(2,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24]).reshape(2,4)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D15---------
            elif asc == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                b44 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44]).reshape(4,4)
                matC = matA + matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nAddition: \n',matC,'\n\n')
            #D16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')     
#------------------------------------------------------------------------------------------------------------------------------------------------
    #OP5--------
#----------------------------| OPERATION 05 - SUBTRACTION |------------------------------------------------------------------

    elif op == '5':
        asd = input("Please enter the dimension of the matA e.g 3,2\n")
        #------ CHECK --------
        if asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,1' or asd == '2,2' or asd == '2,3' or asd == '2,4' or asd == '3,1' or asd == '3,2' or asd == '3,3' or asd == '3,4' or asd == '4,1' or asd == '4,2' or asd == '4,3' or asd == '4,4' :
            asc = input("Please enter the dimension of the matB e.g 3,2\n")
            #E1--------
            if asc == '2,2' and asd == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
                matB = admin.matrix([b11,b12,b21,b22]).reshape(2,2)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E2---------
            elif asc == '2,3' and asd == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23]).reshape(2,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23]).reshape(2,3)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E3---------
            elif asc == '3,2' and asd == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a32,a32]).resahpe(3,2)
                matB = admin.matrix([b11,b12,b21,b22,b32,b32]).reshape(3,2)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E4---------
            elif asc == '3,3' and asd == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33]).reshape(3,3)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E5----------
            elif asc == '2,1' and asd == '2,1':
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21]).reshape(2,1)
                matB = admin.matrix([b11,b21]).reshape(2,1)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E6---------
            elif asc == '3,1' and asd == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31]).reshape(3,1)
                matB = admin.matrix([b11,b21,b31]).reshape(3,1)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E7---------
            elif asc == '1,2' and asd == '1,2':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12]).reshape(1,2)
                matB = admin.matrix([b11,b12]).reshape(1,2)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E8---------
            elif asc == '1,3' and asd == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13]).reshape(1,3)
                matB = admin.matrix([b11,b12,b13]).reshape(1,3)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E9---------
            elif asc == '1,4' and asd == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14]).reshape(1,4)
                matB = admin.matrix([b11,b12,b13,b14]).reshape(1,4)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E10---------
            elif asc == '4,1' and asd == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                b41 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31,a41]).reshape(4,1)
                matB = admin.matrix([b11,b21,b31,b41]).reshape(4,1)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E11---------
            elif asc == '4,3' and asd == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                #HANDLER---------
                matA = admin.matrix([ a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43]).reshape(4,3)
                matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43]).reshape(4,3)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E12---------
            elif asc == '3,4' and asd == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(3,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34]).reshape(3,4)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E13---------
            elif asc == '4,2' and asd == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                b41 = int(input())
                b42 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a31,a32,a41,a42]).reshape(4,2)
                matB = admin.matrix([b11,b12,b21,b22,b31,b32,b41,b42]).reshape(4,2)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E14---------
            elif asc == '2,4' and asd == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24]).reshape(2,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24]).reshape(2,4)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E15---------
            elif asc == '4,4' and asd == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                b44 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
                matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44]).reshape(4,4)
                matC = matA - matB
                #Output----------
                print('matA:\n',matA,'\nmatB:\n',matB,'\nSubtraction: \n',matC,'\n\n')
            #E16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#----------------------------------------------------------------------------------------------------------------------------------------------------
 #OP6--------
#----------------------------| OPERATION 06 - MULTIPLICATION |------------------------------------------------------------------

    elif op == '6':
        opt = input('Please select option\n\t a. Matrix by Matrix\n\tb. Matrix by Integer\n')
        #Opt as A-----------------------------------------------------------------------------------------------------
        if opt == 'a' or opt == 'A':
            asd = input("Please enter the dimension of the matA e.g 3,2\n")
            #------ CHECK --------
            if asd == '2,2' or asd == '3,3' or asd == '4,4' or asd == '2,1' or asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,3' or asd == '2,4' or asd == '4,2' or asd == '3,2' or asd == '3,4' or asd == '3,1' or asd == '4,1' or asd == '4,2' or asd == '4,3' :
                asc = input("Please enter the dimension of the matB e.g 3,2\n")
                #E1--------
                if asc == '2,2' and asd == '2,2':
                    a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
                    matB = admin.matrix([b11,b12,b21,b22]).reshape(2,2)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E2---------
                elif asc == '2,3' and asd == '2,3':
                    a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a21,a22,a23]).reshape(2,3)
                    matB = admin.matrix([b11,b12,b13,b21,b22,b23]).reshape(2,3)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E3---------
                elif asc == '3,2' and asd == '3,2':
                    a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a21,a22,a32,a32]).resahpe(3,2)
                    matB = admin.matrix([b11,b12,b21,b22,b32,b32]).reshape(3,2)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E4---------
                elif asc == '3,3' and asd == '3,3':
                    a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    a33 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    b33 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
                    matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33]).reshape(3,3)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E5----------
                elif asc == '2,1' and asd == '2,1':
                    a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a21 = int(input())
                    b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b21 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a21]).reshape(2,1)
                    matB = admin.matrix([b11,b21]).reshape(2,1)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E6---------
                elif asc == '3,1' and asd == '3,1':
                    a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a21 = int(input())
                    a31 = int(input())
                    b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b21 = int(input())
                    b31 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a21,a31]).reshape(3,1)
                    matB = admin.matrix([b11,b21,b31]).reshape(3,1)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E7---------
                elif asc == '1,2' and asd == '1,2':
                    a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12]).reshape(1,2)
                    matB = admin.matrix([b11,b12]).reshape(1,2)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E8---------
                elif asc == '1,3' and asd == '1,3':
                    a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13]).reshape(1,3)
                    matB = admin.matrix([b11,b12,b13]).reshape(1,3)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E9---------
                elif asc == '1,4' and asd == '1,4':
                    a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a14 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b14 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a14]).reshape(1,4)
                    matB = admin.matrix([b11,b12,b13,b14]).reshape(1,4)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E10---------
                elif asc == '4,1' and asd == '4,1':
                    a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a21 = int(input())
                    a31 = int(input())
                    a41 = int(input())
                    b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b21 = int(input())
                    b31 = int(input())
                    b41 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a21,a31,a41]).reshape(4,1)
                    matB = admin.matrix([b11,b21,b31,b41]).reshape(4,1)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E11---------
                elif asc == '4,3' and asd == '4,3':
                    a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    a33 = int(input())
                    a41 = int(input())
                    a42 = int(input())
                    a43 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    b33 = int(input())
                    b41 = int(input())
                    b42 = int(input())
                    b43 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([ a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43]).reshape(4,3)
                    matB = admin.matrix([b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43]).reshape(4,3)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E12---------
                elif asc == '3,4' and asd == '3,4':
                    a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a14 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    a24 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    a33 = int(input())
                    a34 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b14 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    b24 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    b33 = int(input())
                    b34 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(3,4)
                    matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34]).reshape(3,4)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E13---------
                elif asc == '4,2' and asd == '4,2':
                    a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    a41 = int(input())
                    a42 = int(input())
                    b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    b41 = int(input())
                    b42 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a21,a22,a31,a32,a41,a42]).reshape(4,2)
                    matB = admin.matrix([b11,b12,b21,b22,b31,b32,b41,b42]).reshape(4,2)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E14---------
                elif asc == '2,4' and asd == '2,4':
                    a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a14 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    a24 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b14 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    b24 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24]).reshape(2,4)
                    matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24]).reshape(2,4)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                #E15---------
                elif asc == '4,4' and asd == '4,4':
                    a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                    a12 = int(input())
                    a13 = int(input())
                    a14 = int(input())
                    a21 = int(input())
                    a22 = int(input())
                    a23 = int(input())
                    a24 = int(input())
                    a31 = int(input())
                    a32 = int(input())
                    a33 = int(input())
                    a34 = int(input())
                    a41 = int(input())
                    a42 = int(input())
                    a43 = int(input())
                    a44 = int(input())
                    b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                    b12 = int(input())
                    b13 = int(input())
                    b14 = int(input())
                    b21 = int(input())
                    b22 = int(input())
                    b23 = int(input())
                    b24 = int(input())
                    b31 = int(input())
                    b32 = int(input())
                    b33 = int(input())
                    b34 = int(input())
                    b41 = int(input())
                    b42 = int(input())
                    b43 = int(input())
                    b44 = int(input())
                    #HANDLER---------
                    matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
                    matB = admin.matrix([b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44]).reshape(4,4)
                    matC = matA * matB
                    #Output----------
                    print('matA:\n',matA,'\nmatB:\n',matB,'\nMultiplication: \n',matC,'\n\n')
                
                else:
                    print('''Dimension error--
 --Multiplication can only be performed with matrix of the same row and column size.\n''')
            else:
                print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
        #Opt as B-----------------------------------------------------------------------------------
        elif opt == 'b' or 'B':
            asc = input("Please enter the dimension of the matA e.g 3,2\n")
            mul = int(input("Please enter the integer e.g 4\n"))
            if asc == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F2---------
            elif asc == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23]).reshape(2,3)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F3---------
            elif asc == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a32,a32]).resahpe(3,2)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F4---------
            elif asc == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F5----------
            elif asc == '2,1':
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21]).reshape(2,1)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F6---------
            elif asc == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31]).reshape(3,1)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F7---------
            elif asc == '1,2':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12]).reshape(1,2)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F8---------
            elif asc == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13]).reshape(1,3)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F9---------
            elif asc == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14]).reshape(1,4)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F10---------
            elif asc == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a21,a31,a41]).reshape(4,1)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F11---------
            elif asc == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                #HANDLER---------
                matA = admin.matrix([ a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43]).reshape(4,3)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F12---------
            elif asc == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34]).reshape(3,4)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F13---------
            elif asc == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a21,a22,a31,a32,a41,a42]).reshape(4,2)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F14---------
            elif asc == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24]).reshape(2,4)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F15---------
            elif asc == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                mul = int(input("Please enter the Integer e.g 4\n"))
                #HANDLER---------
                matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
                matC = matA * mul
                #Output----------
                print('matA:\n',matA,'\nMultiplication by ',mul,':\n',matC,'\n\n')
            #F16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Invalid operation--
 --Please enter either A or B.\n''')
#------------------------------------------------------------------------------------------------------------------------------------------------
 #OP7--------
#------------------------------------| OPERATION 07 - DIVISION |------------------------------------------------------------------

    elif op == '7':
        asd = input("Please enter the dimension of the matrix e.g 2,3\n")
        div = input("Please enter the divisor e.g 2\n")
        #G'--------
        if ask == 0:
            print('''Division error--
 --Divisor cannot be zero, please enter a valid divisor. \n''')
        else:
            #G1--------
            if asd == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
            #HANDLER---------
                matA = admin.arange(1,5).reshape(2,2)
                matA.flat[[0,1,2,3]] = a11,a12,a21,a22
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G2---------
            elif asd == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a13,a21,a22,a23
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G3---------
            elif asd == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(3,2)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a21,a22,a31,a32
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G4---------
            elif asd == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                #HANDLER---------
                matA = admin.arange(1,10).reshape(3,3)
                matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G5----------
            elif asd == '2,1':
                a11 = int(input('''Please enter a11 and a21 respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(2,1)
                matA.flat[[0,1]] = a11,a21
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G6---------
            elif asd == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(3,1)
                matA.flat[[0,1,2]] = a11,a21,a31
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G7---------
            elif asd == '1,2':
                a11 = int(input('''Please enter a11 and a12 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(1,2)
                matA.flat[[0,1]] = a11,a12
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G8---------
            elif asd == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(1,3)
                matA.flat[[0,1,2]] = a11,a12,a13
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G9---------
            elif asd == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = a11,a12,a13,a14
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G10---------
            elif asd == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(4,1)
                matA.flat[[0,1,2,3]] = a11,a21,a31,a41
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G11---------
            elif asd == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(4,3)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G12---------
            elif asd == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(3,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G13---------
            elif asd == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(4,2)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a21,a22,a31,a32,a41,a42
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G14---------
            elif asd == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(2,4)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a13,a14,a21,a22,a23,a24
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G15---------
            elif asd == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                #HANDLER---------
                matA = admin.arange(1,17).reshape(4,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44
                division = matA/div
                #Output----------
                print('MATRIX:\n',matA,'\nDivision by:',div,' \n',division,'\n\n')
            #G16----------
            else:
                print('''\nInvalid matrix dimension--
 --Please check your input and try again!\n\n''')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #OP8--------
#----------------------------| OPERATION 08 - SIMULTANEOUS EQUATION |------------------------------------------------------------------
    elif op == '8':
        asd = str(input('Enter the number of unknown variables\n')) 
        #H1----------
        if asd == '3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of the 3x3 matrix respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            b11 = int(input('''Please enter b11 b21 and b31 of the 3x1 matrix respectively--
 --Pressing enter after each input.\n'''))
            b21 = int(input())
            b31 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a21,a22,a23,a31,a32,a33]).reshape(3,3)
            matB = admin.matrix([b11,b21,b31]).reshape(3,1)
            matC = admin.linalg.inv(matA).dot(matB)
            #Output----------
            print('\nMatA:\n',matA,'\n\nMatB:\n',matB,'\n\nX, Y, Z:\n',matC,'\n\n')
        #H2----------
        elif asd == '2':
            a11 = int(input('''Please enter a11 a12 a21 a22 of the 2x2 matrix respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            b11 = int(input('''Please enter b11 and b21 of the 2x1 matrix respectively--
 --Pressing enter after each input.\n'''))
            b21 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a21,a22]).reshape(2,2)
            matB = admin.matrix([b11,b21]).reshape(2,1)
            matC = admin.linalg.inv(matA).dot(matB)
            #Output----------
            print('\nMatA:\n',matA,'\n\nMatB:\n',matB,'\n\nX, Y, Z:\n',matC,'\n\n')
        #Aa3-----------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 to a44 of the 4x4 matrix respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            b11 = int(input('''Please enter b11 b21 b31 b41 of the 4x1 matrix respectively--
 --Pressing enter after each input.\n'''))
            b21 = int(input())
            b31 = int(input())
            b41 = int(input())
            #HANDLER---------
            matA = admin.matrix([a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]).reshape(4,4)
            matB = admin.matrix([b11,b21,b31,b41]).reshape(4,1)
            matC = admin.linalg.inv(matA).dot(matB)
            #Output----------
            print('\nMatA:\n',matA,'\n\nMatB:\n',matB,'\n\nX, Y, Z:\n',matC,'\n\n')
        #Aa4-----------
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
        
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------| EXIT |---------------------------------------------------------------------
    elif op == 'exit':
        break
#--------------------------------------------------------------------------------------------------------------------------------------------
    #OP9----------
#--------------------------------------------------| EXCEPTION |---------------------------------------------------------------------
    else:
        print('''\nOperation not recognized--
 --please check your input and try again!\n\n''')
    
