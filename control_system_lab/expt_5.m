clc 
clear all 
close all 
t=0:0.01:10;
u=t;
num=input('Enter the Numerator of the transfer function: ')
den=input('Enter the Denominator of the transfer function: ')
tf(num,den)
lsim(num,den,u,t)