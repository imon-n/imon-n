clc 
clear all 
close all

num = input('Enter the numerator of the transfer function: ')
den = input('Enter the denominator of the transfer function: ')
[z,p,k] = tf2zp(num,den)