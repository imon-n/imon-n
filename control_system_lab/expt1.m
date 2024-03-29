clc
clear all 
close all 

z=input('Enter Zeros: ')
p = input('Enter Poles: ')
k = input('Enter gain: ')
[num,den] = zp2tf(z,p,k)
tf(num,den)