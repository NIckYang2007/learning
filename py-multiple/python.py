import matplotlib.pyplot as plt
x_range=range(1,6)
y_range=[x**3 for x in x_range]

#plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
#fig (figure)：代表整个图形窗口，可以包含多个坐标轴
#ax (axes)：代表具体的坐标轴，用于绘制数据
ax.scatter(x_range,y_range,c=y_range, cmap=plt.cm.Reds,s=10)
#plot方法用于绘制线段
 # 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
 # 设置刻度标记的样式
ax.tick_params(labelsize=14)
ax.axis([0, 5, 0, 250])
plt.show()