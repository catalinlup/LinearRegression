#Recomended alfa 0.0001
#Recomended threshhold 1
import sys
try:
    import matplotlib.pyplot as plt
except:
    print("Error! Install matplotlib!")
    sys.exit()
try:
    import numpy as np
except:
    print("Error! Install numpy!")
    sys.exit()
try:
    import csv
except:
    print("Error! Install csv!")
    sys.exit()
try:
    from drawnow import*
except:
    print("Error! Install drawnow!")
    sys.exit()
import time
inputData=''
outputModel=''
alfa=0
threshhold=0
try:
    inputData=sys.argv[1]
    outputModel=sys.argv[2]
    alfa=float(sys.argv[3])
    threshhold=float(sys.argv[4])
except:
    print("Error! Invalid arguments!")
    sys.exit()
costPlot=plt.figure(1)
plt.ion()
x=[]
y=[]
dataset=[]
toDraw1=[]
toDraw2=[]

def h(x,t0,t1):
    return t0+t1*x
def costFunction(t0,t1):
    m=len(dataset)
    sum=0.0
    for data in dataset:
        sum=sum+(1/2*m)*((h(data[1],t0,t1)-data[2])**2)
    return sum
def costFunctionDeriv(i,t0,t1):
    m=len(dataset)
    sum=0.0
    for data in dataset:
        sum=sum+(1/m)*(h(data[1],t0,t1)-data[2])*data[i]
    return sum
def makeFig():
    plt.title('Cost Function Graph')
    plt.xlabel('iterations')
    plt.ylabel('Cost function value')
    plt.plot(toDraw2,toDraw1,label="Cost Function")
    plt.legend()
    costPlot.show()
def GradientDescent():
    oldCostFunctionVal=0.0
    thetha0=0.0
    thetha1=0.0
    iter=0
    startTime=time.time()
    while abs(oldCostFunctionVal-costFunction(thetha0,thetha1))>threshhold:
        oldCostFunctionVal=costFunction(thetha0,thetha1)
        temp0=thetha0-alfa*costFunctionDeriv(0,thetha0,thetha1)
        temp1=thetha1-alfa*costFunctionDeriv(1,thetha0,thetha1)
        thetha0=temp0
        thetha1=temp1
        toDraw1.append(oldCostFunctionVal)
        toDraw2.append(iter)
        drawnow(makeFig)
        iter+=1
    stopTime=time.time()
    dt=stopTime-startTime
    return thetha0,thetha1,iter,dt

with open(inputData,'r') as file:
    data=csv.reader(file,delimiter=',')
    num=0
    for row in data:
        num+=1
        x.append(float(row[0]))
        y.append(float(row[1]))
        dataset.append([1,float(row[0]),float(row[1])])
v1,v2,nrIt,tm=GradientDescent()
print('Estimated time: '+str(int(tm))+' seconds')
print('Number of iterations: '+str(nrIt))
fileToSave=open(outputModel,'w')
fileToSave.write(str(v1)+','+str(v2))
fileToSave.close()
plt.figure(2)
plt.title("Linear Regression")
plt.ylabel('Y')
plt.xlabel('X')
plt.scatter(x,y,label="Data")
yh=[]
for i in x:
    yh.append(h(i,v1,v2))
plt.plot(x,yh,"r-",label="Hypothesis")
plt.legend()
plt.show(block=True)
