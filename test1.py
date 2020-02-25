import matplotlib.pyplot as plt

"""
#折线图
square = [1,4,9, 16,25,36]
value = [1,2,3,4,5,6]
plt.plot(value,square,linewidth = 5)
plt.title("squared",fontsize = 24)
plt.xlabel("Value",fontsize = 15)
plt.ylabel("Square",fontsize = 18)

plt.tick_params(axis= 'both',labelsize = 14)

#plt.show()
"""

"""
#散点图
x_value = list(range(101))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,s = 5,edgecolors='none',c= y_value,cmap= plt.cm.jet)
plt.title("Scatter",fontsize = 30)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Scatter Value",fontsize = 14)
plt.tick_params(axis= "both",labelsize = 10)
plt.axis([0,110,0,11000])

plt.show()
"""

"""练习

x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value,y_value,s= 5,c=y_value,cmap='jet',edgecolors=None)
plt.title('lifang')
plt.tick_params(axis='both',labelsize = 24)
plt.xlabel('value',fontsize= 30)
plt.ylabel('y',fontsize= 30)

plt.show()
"""
from random_walk import RandomWalk

#while True:

    #a = input('try again,type(y/n')
    #if a == 'n':
       # break

rw = RandomWalk(num_points=5000)
rw.fill_walk()

plt.figure(dpi=166,figsize=(10,6))
plt.plot(rw.x_value,rw.y_value)
plt.scatter(0,0,s= 10,c = 'blue')
plt.scatter(rw.x_value[-1],rw.y_value[-1],s= 10,c = 'green')
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

