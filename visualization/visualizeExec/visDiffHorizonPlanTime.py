import matplotlib.pyplot as plt

horizon = ['10','20','30','40','50','60','70','80','90','100']

#numBelief= 2
p1= [0.01, 0.01, 0.01, 0.02, 0.02, 0.03, 0.03, 0.04, 0.04, 0.05]
#numBelief= 5
p2= [0.01, 0.02, 0.03, 0.05, 0.06, 0.07, 0.08, 0.11, 0.12, 0.13]
#numBelief= 10
p3= [0.07, 0.07, 0.09, 0.11, 0.14, 0.17, 0.2, 0.22, 0.24, 0.26]
#numBelief= 20
p4= [0.06, 0.12, 0.18, 0.23, 0.29, 0.34, 0.39, 0.44, 0.51, 0.58]
#numBelief= 50
p5= [0.21, 0.44, 0.66, 0.81, 1.09, 1.29, 1.57, 1.75, 2.0, 2.25]
#numBelief= 100
p6= [0.59, 1.26, 1.89, 2.42, 3.07, 3.62, 4.34, 5.06, 5.61, 6.19]

fig, ax = plt.subplots(figsize=(13,9))
plt.xticks(fontproperties='Times New Roman', fontsize=14)
plt.yticks(fontproperties='Times New Roman', fontsize=14)

plt.plot(horizon, p1, 'deepskyblue', marker='+', markersize=14,label='2 Belief Points', linewidth='2')
plt.plot(horizon, p2, 'mediumblue', marker='+', markersize=14, label='5 Belief Points', linewidth='2')
plt.plot(horizon, p3, 'darkviolet', marker='+', markersize=14, label='10 Belief Points', linewidth='2')
plt.plot(horizon, p4, 'mediumvioletred', marker='+', markersize=14, label='20 Belief Points', linewidth='2')
plt.plot(horizon, p5, 'red', marker='+', markersize=14, label='50 Belief Points', linewidth='2')
plt.plot(horizon, p6, 'darkorange', marker='+', markersize=14, label='100 Belief Points', linewidth='2')

ax.set_xlabel('Planning Horizons', fontdict={'family': 'Times New Roman', 'size': 14})
ax.set_ylabel('Times (second)', fontdict={'family': 'Times New Roman', 'size': 14})
plt.title('PBVI Planning Times of Different Horizon & Belief Points',
          fontdict={'family': 'Times New Roman', 'size': 14})
ax.legend(loc='upper left', prop={'family': 'Times New Roman', 'size': 14})
ax.set_ylim([0, 6.5])
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.show()

