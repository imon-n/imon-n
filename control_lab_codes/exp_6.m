clc
clear all 
close all 
wn=input('Enter the valu of undamped natural frequency: ')
z= input('Enter the value of damping ratio: ')
n=[wn*wn]
p=sqrt(1-(z^2))
wd=wn*p
h=[p/z]
k=atan(h)
m=pi-k;
tr= [m/wd]
tp=[pi/wd]
q=z*wn
ts=[h/q]
r=z*pi
f=[r/p]
mp=exp(-f)
num=[0 0 n]
den=[1 2*z*wn n]
s=tf(num,den)
hold on
step(s)
impulse(s)
hold off