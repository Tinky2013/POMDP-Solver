import matplotlib.pyplot as plt

horizon = ['10','20','30','40','50','60','70','80','90','100']
planTime=[0.411,0.828,1.945,3.861,7.337,19.79,37.791]

#belief points: 2
p1= [0.024, 0.028000000000000004, 0.03400000000000001, 0.034, 0.041999999999999996, 0.054000000000000006, 0.06600000000000002, 0.07000000000000002, 0.08299999999999999, 0.099]
#belief points: 5
p2= [0.044, 0.043000000000000003, 0.03200000000000001, 0.031000000000000007, 0.03200000000000001, 0.039999999999999994, 0.039999999999999994, 0.040999999999999995, 0.05, 0.05]
#belief points: 10
p3= [0.019999999999999997, 0.019999999999999997, 0.029000000000000005, 0.030000000000000006, 0.030000000000000006, 0.039999999999999994, 0.039999999999999994, 0.040999999999999995, 0.05, 0.05]
#belief points: 20
p4= [0.019999999999999997, 0.019999999999999997, 0.023, 0.030000000000000006, 0.03200000000000001, 0.039999999999999994, 0.039999999999999994, 0.048, 0.066, 0.06000000000000001]
#belief points: 50
p5= [0.019999999999999997, 0.019999999999999997, 0.029000000000000005, 0.030000000000000006, 0.030000000000000006, 0.039999999999999994, 0.039999999999999994, 0.040999999999999995, 0.05, 0.05]
#belief points: 100
p6= [0.019999999999999997, 0.019999999999999997, 0.026000000000000002, 0.030000000000000006, 0.030000000000000006, 0.040999999999999995, 0.040999999999999995, 0.043, 0.05, 0.052000000000000005]


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

