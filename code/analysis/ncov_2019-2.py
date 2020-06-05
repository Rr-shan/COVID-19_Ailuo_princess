import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

filename='./ncov_100_modify.txt'
file = open (filename)
lines = file.readlines()
ls=[]
for line in lines:
    l=line.split(":")
    ls.append(float(l[1]))
print(ls)
date1=np.linspace(0,18,1000)
date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

valx=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
testx=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19',
       '20','21','22','23','24','25','26','27','28','29','30','31' ]
plt.xticks(valx,testx)

valy=[0,0.65,0.70,0.75,0.80]
testy=['0.60','0.65','0.70','0.75','0.80']
testy1=['A', 'negative', 'neutral', 'D', 'E']
plt.yticks(valy,testy1)

plt.plot(date,ls,linestyle='-',linewidth=3,color='orangered',label='sample points',zorder=6)
plt.show()
'''
labels='A','B','C'
#labels='A:controllable','B:serious','C:','D:uncontrollable'
fraces = [5,10,66]
plt.axes(aspect=1)
colors=['lightskyblue','deepskyblue','b']
plt.figure(figsize=(8, 6))
plt.pie(x=fraces,labels= labels,colors=colors)
plt.axis('equal')
plt.legend(loc='upper right')
plt.savefig('age.png', dpi=600)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
labels = np.array(['positive','neutral','negative'])

dataLenth = 3
data = np.array([10,6,33])
angles = np.linspace(0,2*np.pi,dataLenth,endpoint=False)
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[angles[0]]))

fig = plt.figure()
# 设置成极坐标格式
ax = fig.add_subplot(111,polar=True)
ax.plot(angles,data,'ro-',linewidth=3)
ax.set_thetagrids(angles*180/np.pi,labels,fontproperties="SimHei")
# 不显示标签
ax.tick_params('y', labelleft=False) 
# 添加网格线
ax.grid(True)
plt.show()

'''