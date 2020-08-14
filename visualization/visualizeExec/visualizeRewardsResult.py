import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

horizon = ['1', '2','5','10','20','50','100']
finalR=[84.8,95.8,138.7,170.6,55.1,56.2,104.6]


figure(num=None, figsize=(2.8, 1.7), dpi=300)
plt.xticks(fontproperties='Times New Roman', fontsize=4)
plt.yticks(fontproperties='Times New Roman', fontsize=4)
plt.plot(horizon, finalR, 'blue', marker='+', label='average reward', linewidth='.8')

plt.ylim([0, 200])
plt.legend(loc='lower right', prop={'family': 'Times New Roman', 'size': 4})
plt.title('Average 100-play Rewards of 10 trials',
          fontdict={'family': 'Times New Roman', 'size': 4})

plt.xlabel('Planning Horizons', fontdict={'family': 'Times New Roman', 'size': 4})
plt.ylabel('Average 100-play Rewards', fontdict={'family': 'Times New Roman', 'size': 4})
plt.show()