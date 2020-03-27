from numpy import *
import pandas as pd
import numpy as np
from numpy import loadtxt
from io import StringIO, BytesIO
import csv
import urllib
import matplotlib.pyplot as plt
from scipy import optimize

yes=0
no=0
n=0
while n<10000:
    p_b=random.uniform(0,1)
    p1=random.uniform(0,10)
    p2=random.uniform(0,10)
    a2=random.uniform(0,1)

    def f_1(p1,p2,a2,p_b):
        return 1/p1*(1-p1*np.exp(p2*a2)*(2*p_b-np.exp(-p2*a2)))

    if 0<=f_1(p1,p2,a2,p_b)<=1:
        a1=f_1(p1,p2,a2,p_b)
    elif f_1(p1,p2,a2,p_b)>1:
        a1=1
    else:
        a1=0

    print(a1)
    # a1=0.1
    def p_2(p2,a2,a1):
        return (1-a1)*np.exp(-p2*a2)

    def p_1(p1,a2,a1):
        return (1-a2)*np.exp(-p1*a1)

    # print((1-p_1(p1,a2,a1)*p_2(p2,a2,a1))/(1-p_1(p1,a2,a1))>2*p_b)
    #1 batte
    win_2=0
    win_1=0


    # p_1=0.4
    # p_2=0.8
    if 0<a1<1:
        n+=1
        for i in range(0,10000):
            x=random.uniform(0, 1)
            check=0


            if x<p_b:
                while check==0:

                    x=random.uniform(0, 1)
                    if x<p_1(p1,a2,a1): #1 risponde 
                        check=0
                    else: #1 non risponde
                        check=1
                        win_2+=1
                    if check==0:
                        x=random.uniform(0, 1)
                        if x<p_2(p2,a2,a1): #2 risponde 
                            check=0
                        else: #2 non risponde
                            check=1
                            win_1+=1
            else:
                win_1+=1

        if float(win_2)==0 and (1-p_1(p1,a2,a1)*p_2(p2,a2,a1))/(1-p_1(p1,a2,a1))>2*p_b:
            yes+=1
        elif float(win_2)!=0 and float(win_1)/float(win_2)>1 and (1-p_1(p1,a2,a1)*p_2(p2,a2,a1))/(1-p_1(p1,a2,a1))>2*p_b:
            yes+=1
        else:
            no+=1

print(yes,no)





