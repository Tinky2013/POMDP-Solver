import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#horizon= 1
r1= [-100.0, -21.900000000000002, 38.599999999999994, 51.800000000000004, 93.6, 87.0, 139.8, 139.79999999999998, 148.6, 139.8, 138.70000000000002, 122.20000000000002, 143.1, 109.0, 106.80000000000001, 153.0, 169.5, 103.49999999999999, 155.2, 161.8, 127.69999999999999, 74.89999999999999, 113.4, 71.6, 47.4, 133.20000000000002, 72.7, 87.0, 77.1, 144.2, 131.0, 102.4, 84.79999999999998, 103.49999999999999, 91.4, 161.8, 116.69999999999999, 133.2, 158.49999999999997, 77.1, 109.0, 88.1, 144.20000000000002, 81.50000000000001, 132.1, 145.3, 104.60000000000002, 21.0, 134.29999999999998, 133.2]
t1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 2
r2= [-100.0, -68.1, -79.1, -70.3, -71.4, -82.4, -48.3, -21.9, 16.599999999999994, 7.800000000000001, 48.5, 21.0, 61.7, 61.70000000000002, 83.7, 65.00000000000001, 60.599999999999994, 48.5, 105.7, 94.7, 125.5, 102.4, 96.9, 134.3, 90.30000000000001, 78.2, 132.1, 138.70000000000002, 114.5, 137.6, 128.8, 138.70000000000002, 140.89999999999998, 122.2, 165.1, 120.0, 172.8, 114.5, 133.20000000000002, 161.79999999999998, 128.79999999999998, 109.0, 120.0, 72.7, 146.39999999999998, 107.89999999999999, 123.3, 129.9, 140.9, 98.0]
t2= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 5
r3= [-100.0, -100.0, -73.6, -68.1, -72.5, 16.599999999999998, 51.8, 21.0, 63.89999999999999, 54.0, 56.2, 50.699999999999996, 30.900000000000006, 63.900000000000006, 41.900000000000006, 107.9, 55.10000000000001, 33.1, 67.2, 115.6, 27.599999999999998, 109.0, 66.1, 55.1, 109.0, 69.4, 50.7, 56.2, 106.8, 83.7, 116.7, 88.1, 106.80000000000001, 148.60000000000002, 75.99999999999999, 112.29999999999998, 111.2, 121.1, 84.8, 128.79999999999998, 154.1, 125.5, 134.3, 111.20000000000002, 71.60000000000001, 85.9, 111.2, 76.0, 119.99999999999999, 93.6]
t3= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 10
r4= [-100.0, -35.1, -20.8, 19.9, 3.3999999999999986, 12.200000000000003, 40.8, 29.8, 88.1, 71.6, 39.699999999999996, 88.1, 63.89999999999999, 35.3, 92.5, 77.1, 82.6, 71.6, 26.499999999999996, 129.9, 103.5, 63.9, 111.19999999999999, 105.7, 22.1, 122.19999999999999, 59.49999999999999, 122.2, 68.3, 81.49999999999997, 59.50000000000001, 79.3, 145.3, 78.19999999999999, 102.4, 84.80000000000001, 135.4, 111.2, 66.10000000000001, 111.19999999999999, 83.70000000000002, 131.0, 114.5, 126.6, 94.7, 85.89999999999999, 74.89999999999999, 124.4, 155.2, 150.8]
t4= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 20
r5= [-100.0, -71.4, -39.5, -45.0, 13.299999999999997, 62.8, 45.2, 57.30000000000001, 43.000000000000014, 81.5, 55.099999999999994, 38.60000000000001, 39.699999999999996, 70.49999999999999, 140.9, 105.7, 105.7, 119.99999999999999, 102.39999999999998, 84.8, 76.0, 135.4, 159.6, 158.50000000000003, 123.3, 78.2, 76.0, 87.0, 154.1, 127.7, 126.6, 82.60000000000001, 55.099999999999994, 115.60000000000001, 142.0, 102.4, 114.5, 106.80000000000003, 136.5, 127.70000000000002, 156.29999999999998, 82.6, 95.8, 96.9, 103.50000000000001, 125.5, 70.5, 90.30000000000001, 148.60000000000002, 104.60000000000001]
t5= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 50
r6= [-100.0, -74.7, -16.4, 15.500000000000007, -32.900000000000006, 12.2, -18.6, 49.6, 61.7, 69.40000000000002, 102.40000000000002, 106.80000000000001, 91.4, 89.19999999999999, 150.8, 106.79999999999998, 170.6, 168.4, 152.99999999999997, 124.40000000000002, 134.29999999999998, 142.0, 106.80000000000001, 109.0, 157.4, 153.0, 124.4, 177.20000000000002, 116.69999999999999, 153.0, 118.90000000000002, 83.69999999999999, 111.19999999999999, 145.29999999999998, 74.9, 80.39999999999999, 94.69999999999999, 140.9, 125.5, 60.6, 105.7, 125.5, 96.89999999999998, 147.49999999999997, 106.80000000000001, 81.49999999999999, 138.70000000000002, 74.9, 124.4, 63.900000000000006]
t6= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#horizon= 100
r7= [-100.0, -71.4, 12.200000000000003, 7.800000000000001, 116.69999999999999, 159.6, 102.4, 88.1, 113.39999999999998, 96.89999999999999, 131.00000000000003, 151.9, 110.10000000000001, 124.4, 122.19999999999999, 142.0, 103.5, 122.20000000000003, 137.60000000000002, 91.4, 172.79999999999998, 91.39999999999999, 115.60000000000001, 164.0, 120.00000000000001, 145.3, 101.30000000000001, 134.29999999999998, 128.79999999999998, 84.80000000000001, 92.50000000000001, 83.69999999999999, 84.8, 113.4, 118.89999999999999, 150.79999999999998, 135.4, 100.2, 106.8, 134.3, 121.1, 132.10000000000002, 144.2, 133.20000000000002, 63.900000000000006, 118.89999999999999, 93.6, 91.4, 125.5, 129.9]
t7= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

N=2
def countNAve(List,N):
    AveN = []
    for i in range(len(List)//N):
        summation = 0
        for j in range(N):
            summation+=List[i*N+j]
        AveN.append(summation/N)
    return AveN
r1=countNAve(r1,N)
r2=countNAve(r2,N)
r3=countNAve(r3,N)
r4=countNAve(r4,N)
r5=countNAve(r5,N)
r6=countNAve(r6,N)
r7=countNAve(r7,N)
t1=countNAve(t1,N)
fig, ax = plt.subplots(figsize=(13,9))
plt.xticks(fontproperties='Times New Roman', fontsize=14)
plt.yticks(fontproperties='Times New Roman', fontsize=14)

plt.axis([0,50,-150,250])

plt.plot(t1, r1, 'deepskyblue', marker='.', markersize=9, label='horizon=1', linewidth='1.3')
plt.plot(t1, r2, 'royalblue', marker='.', markersize=9, label='horizon=2', linewidth='1.3')
plt.plot(t1, r3, 'mediumblue', marker='.', markersize=9, label='horizon=5', linewidth='1.3')
plt.plot(t1, r4, 'darkviolet', marker='.', markersize=9, label='horizon=10', linewidth='1.3')
plt.plot(t1, r5, 'mediumvioletred', marker='.', markersize=9, label='horizon=20', linewidth='1.3')
plt.plot(t1, r6, 'red', marker='.', markersize=9, label='horizon=50', linewidth='1.3')
plt.plot(t1, r7, 'darkorange', marker='.', markersize=9, label='horizon=100', linewidth='1.3')

ax.legend(loc='lower right', prop={'family': 'Times New Roman', 'size': 14})
plt.title('Average 100-play total reward', fontdict={'family': 'Times New Roman', 'size': 14})

ax.set_xlabel('num belief points', fontdict={'family': 'Times New Roman', 'size': 14})
ax.set_ylabel('total reward', fontdict={'family': 'Times New Roman', 'size': 14})

ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.show()
