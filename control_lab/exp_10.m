clc 
clear all 
close all 

A = input('Enter the matrix A: ')
B = input('Enter the matrix B: ')
C = input('Enter the matrix C: ')
D = input('Enter the matrix D: ')
[a,b] = ss2tf(A,B,C,D)
tf(a,b)