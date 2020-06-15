
import matplotlib.pyplot as plt


x = range(10,30,1)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,3,3,3,2,1,2,1,1,1,1,1,1,1,1,1]


plt.figure(figsize=(20,8),dpi=80)

plt.xlabel('Ages',fontsize=16)
plt.ylabel('# of girlfriend',fontsize=16)
plt.title('Attraction over Ages',fontsize=18)

plt.plot(x,y1,label='me', color='r',linestyle='--',linewidth=5,alpha=0.7)
plt.plot(x,y2,label='deskmate')

plt.xticks(range(10,30,1))
plt.yticks(range(min(y1),max(y1)+2,1))

plt.grid(alpha=0.5)

plt.legend(labels=['me','deskmate'],fontsize=18,loc='upper left')

plt.show()

##plt.xlim((-1,2))
##plt.ylim((-1,3))

##plt.plot(x,y1,label='me', color='r',linestyle='--', linewidth=5,alpha=0.7)

##plt.xlabel('I am x', fontsize=16)
##plt.ylabel('I am y',fontsize=16)
##plt.title('Temperature change during the daytime',fontsize=18)

## 调整图大小
##plt.figure(figsize=(20,8),dpi=80)


##轴刻度
##plt.xticks(range((2,25,5))
##plt.yticks(range(min(y),max(y)+2,2))

##new_ticks = np.linspace(-1,2,5)
##print(new_ticks)
##plt.xticks(new_ticks)
##plt.yticks([-2,-1.8,-1,1.22,3],
            ##['really bad','bad',r'$noraml\ \delta$','good','excellent'])

##网格
##plt.grid(alpha=0.4)

##图例
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')

##gca"get current axis'
##ax = plt.gca()
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.spines['bottom'].set_position(('data',0)) #outward, axes
##ax.spines['left'].set_position(('data',0))





