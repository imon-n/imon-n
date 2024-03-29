clc 
clear all 
close all 

num =input('Enter the numerator of the transfer function: ')
den = input('Enter the denominator of the transfer function: ')
h=tf(num,den)
[gm pm wcp wcg] = margin(h)
bode(h)