clc 
clear all 
close all 

num=input('enter the numerator of th transfer function: ')
den = input('Enter the denominator of the transfer function: ')
h=tf(num,den)
rlocus(h)