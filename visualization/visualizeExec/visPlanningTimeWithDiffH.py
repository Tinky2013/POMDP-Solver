import matplotlib.pyplot as plt

horizon = ['1','2','5','10','20','50','100']
planTime=[0.411,0.828,1.945,3.861,7.337,19.79,37.791]

#planning horizons: 100
#belief points: 2
p1= [0.015999999999999997, 0.019999999999999997, 0.019999999999999997, 0.019999999999999997, 0.020999999999999998, 0.030000000000000006, 0.05700000000000001]
#planning horizons: 100
#belief points: 5
p2= [0.019999999999999997, 0.019999999999999997, 0.019999999999999997, 0.019999999999999997, 0.030000000000000006, 0.06000000000000001, 0.10200000000000001]
#planning horizons: 100
#belief points: 10
p3= [0.019999999999999997, 0.019999999999999997, 0.020999999999999998, 0.031000000000000007, 0.05500000000000001, 0.11499999999999999, 0.213]
#planning horizons: 100
#belief points: 20
p4= [0.019999999999999997, 0.027000000000000003, 0.043, 0.06700000000000002, 0.1, 0.23000000000000004, 0.43899999999999995]
#planning horizons: 100
#belief points: 50
p5= [0.030000000000000006, 0.039999999999999994, 0.086, 0.15999999999999998, 0.30700000000000005, 0.746, 1.703]
#planning horizons: 100
#belief points: 100
p6= [0.041999999999999996, 0.096, 0.231, 0.461, 1.1250000000000002, 2.2920000000000007, 4.538000000000001]

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
ax.set_ylim([0, 4.7])
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.show()

