clc 
clear all 
close all 


num=input('Enter the Numerator of the transfer function: ')
den=input('Enter the Denominator of the transfer function: ')
tf(num,den)
impulse(num,den)