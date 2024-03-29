clc 
clear all 
close all 

J = 0.01;
b = 0.1;
K = 0.01;
R = 1;
L = 0.5;
s =  tf('s');
P_motor = K/((J*s+b)*(L*s+R)+K^2)
zpk(P_motor)
linearSystemAnalyzer('step',P_motor, 0:0.1:5);