import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#method= RA
#r1= [-100.0, -100.0, -100.0, -100.0, -100.0, 197.0, 219.0, 142.0, 153.0, 208.0, 175.0, 98.0, 109.0, 208.0, 43.0, 186.0, 54.0, 219.0, 164.0, 197.0, 98.0, -23.0, 10.0, 98.0, 76.0, 98.0, -12.0, 98.0, -12.0, -122.0, 219.0, 219.0, 219.0, 164.0, 230.0, -12.0, 98.0, -34.0, 153.0, 230.0, 175.0, 32.0, -122.0, 120.0, 87.0, 208.0, 219.0, 197.0, 197.0, 230.0, 186.0, 10.0, 208.0, 197.0, -1.0, 76.0, 208.0, -56.0, -166.0, 197.0, 21.0, 164.0, -56.0, 142.0, 208.0, 208.0, 186.0, -78.0, 98.0, 186.0, -1.0, -34.0, 230.0, -23.0, 186.0, 208.0, 120.0, 131.0, 186.0, 153.0, 76.0, 76.0, 87.0, 186.0, -23.0, -155.0, -45.0, 87.0, -23.0, -45.0, -133.0, 98.0, 208.0, -23.0, 109.0, 98.0, -12.0, -111.0, 219.0, 186.0]
#t1= [0.02, 0.04, 0.06, 0.09, 0.12, 0.16, 0.2, 0.24, 0.29, 0.36, 0.44, 0.52, 0.6, 0.68, 0.77, 0.87, 0.97, 1.08, 1.19, 1.31, 1.42, 1.54, 1.67, 1.8, 1.94, 2.08, 2.24, 2.39, 2.56, 2.72, 2.91, 3.09, 3.28, 3.47, 3.67, 3.87, 4.09, 4.31, 4.54, 4.78, 5.03, 5.28, 5.55, 5.81, 6.1, 6.42, 6.79, 7.16, 7.57, 7.97, 8.4, 8.77, 9.14, 9.51, 9.88, 10.27, 10.66, 11.07, 11.55, 12.11, 12.63, 13.1, 13.56, 14.02, 14.51, 15.0, 15.49, 15.99, 16.49, 17.01, 17.53, 18.06, 18.61, 19.16, 19.72, 20.28, 20.97, 21.75, 22.43, 23.16, 23.83, 24.48, 25.16, 25.84, 26.52, 27.22, 27.92, 28.63, 29.36, 30.31, 31.24, 32.07, 32.89, 33.77, 34.78, 35.72, 36.55, 37.48, 38.35, 39.25]
#------------------------------
#method= SSRA
#r2= [-100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, -100.0, 164.0, -34.0, 186.0, -12.0, 197.0, -23.0, 208.0, 65.0, 208.0, 65.0, -12.0, -1.0, 219.0, 197.0, 76.0, -144.0, -12.0, 98.0, 175.0, 109.0, 175.0, 186.0, 98.0, 186.0, 197.0, -45.0, 186.0, -56.0, -12.0, 76.0, 208.0, 98.0, 164.0, 230.0, -45.0, 76.0, 186.0, -232.0, 164.0, 87.0, 197.0, 76.0, 175.0, 208.0, 186.0, 76.0, 76.0, -12.0, 54.0, 120.0, -45.0, 76.0, 175.0, 76.0, 208.0, 120.0, 186.0, 230.0, 208.0, 175.0, 164.0, 98.0, 186.0, -12.0, 208.0, 153.0, 197.0, 208.0, 76.0, -12.0, 197.0, 197.0, 186.0, 230.0, 153.0, 87.0, 76.0, 197.0, -12.0, 87.0, 164.0, 197.0, 219.0, 76.0, 76.0, 98.0, 54.0, -12.0, 186.0]
#t2= [0.02, 0.04, 0.06, 0.09, 0.12, 0.16, 0.2, 0.24, 0.29, 0.35, 0.4, 0.47, 0.53, 0.61, 0.68, 0.76, 0.85, 0.94, 1.03, 1.13, 1.26, 1.4, 1.52, 1.65, 1.78, 1.92, 2.06, 2.22, 2.37, 2.53, 2.7, 2.87, 3.05, 3.24, 3.43, 3.64, 3.86, 4.08, 4.31, 4.54, 4.78, 5.02, 5.28, 5.55, 5.82, 6.11, 6.4, 6.69, 6.99, 7.3, 7.62, 7.96, 8.3, 8.64, 9.0, 9.37, 9.75, 10.14, 10.56, 10.99, 11.42, 11.84, 12.28, 12.75, 13.21, 13.72, 14.22, 14.72, 15.25, 15.79, 16.37, 16.92, 17.47, 18.1, 18.72, 19.32, 19.96, 20.57, 21.19, 21.8, 22.43, 23.09, 23.77, 24.43, 25.1, 25.83, 26.54, 27.25, 27.97, 28.69, 29.43, 30.2, 30.98, 31.79, 32.59, 33.39, 34.21, 35.03, 35.89, 36.78]
#------------------------------
#method= SSEA
#r3= [-100.0, -100.0, 164.0, 219.0, 153.0, 76.0, 65.0, 120.0, 164.0, 186.0, 76.0, 54.0, 186.0, 197.0, 120.0, 208.0, 164.0, 109.0, 120.0, -144.0, 76.0, 186.0, -122.0, 197.0, 98.0, 186.0, 186.0, 197.0, 164.0, 76.0, 197.0, -166.0, 186.0, 142.0, 164.0, 76.0, -12.0, 98.0, 164.0, 120.0, 164.0, 186.0, -12.0, 76.0, 186.0, 230.0, 76.0, 208.0, 32.0, 197.0, 208.0, 208.0, 230.0, 186.0, -56.0, 54.0, 175.0, 219.0, 186.0, 87.0, 186.0, 153.0, 230.0, 164.0, 98.0, 131.0, 197.0, 109.0, -144.0, -12.0, 76.0, 87.0, 76.0, -23.0, 208.0, 10.0, 76.0, -12.0, 175.0, 98.0, 153.0, 208.0, 186.0, 120.0, 175.0, 76.0, 197.0, 54.0, 175.0, 98.0, 186.0, 76.0, 87.0, 98.0, -12.0, 164.0, 208.0, 208.0, 76.0, 120.0]
#t3= [0.02, 0.04, 0.06, 0.09, 0.12, 0.16, 0.2, 0.24, 0.29, 0.34, 0.4, 0.46, 0.53, 0.6, 0.68, 0.76, 0.84, 0.93, 1.03, 1.13, 1.23, 1.34, 1.46, 1.58, 1.71, 1.84, 1.98, 2.13, 2.28, 2.44, 2.61, 2.79, 2.98, 3.17, 3.37, 3.57, 3.79, 4.02, 4.24, 4.47, 4.71, 4.95, 5.22, 5.48, 5.75, 6.02, 6.31, 6.61, 6.94, 7.28, 7.61, 7.94, 8.29, 8.68, 9.05, 9.41, 9.78, 10.2, 10.65, 11.06, 11.47, 11.89, 12.31, 12.75, 13.19, 13.66, 14.13, 14.62, 15.12, 15.63, 16.15, 16.68, 17.22, 17.76, 18.33, 19.18, 19.87, 20.48, 21.09, 21.77, 22.42, 23.07, 23.72, 24.39, 25.06, 25.76, 26.7, 27.51, 28.24, 28.97, 29.72, 30.48, 31.26, 32.05, 32.85, 33.71, 34.59, 35.46, 36.34, 37.28]
#------------------------------

#method= RA
r1= [-100.0, -45.0, -10.899999999999999, 3.4000000000000057, 81.50000000000001, 49.599999999999994, 109.0, 126.6, 100.19999999999999, 80.4, 143.1, 170.6, 128.79999999999998, 182.70000000000002, 168.4, 171.7, 139.8, 38.6, 100.2, 150.79999999999998, 80.4, 87.0, 113.39999999999999, 88.10000000000001, 135.4, 149.70000000000002, 125.50000000000001, 12.2, 75.99999999999999, 55.10000000000001, 106.8, 105.7, 199.20000000000002, 111.19999999999999, 66.1, 137.60000000000002, 94.7, 101.29999999999998, 77.10000000000001, 132.1, 133.20000000000002, 161.79999999999998, 121.1, 134.29999999999998, 79.3, 127.69999999999999, 104.60000000000002, 137.6, 132.1, 126.59999999999998, 106.80000000000003, 129.9, 170.6, 110.1, 132.1, 118.9, 100.19999999999997, 59.5, 127.69999999999999, 125.50000000000001, 113.39999999999999, 139.79999999999998, 65.0, 87.0, 158.5, 149.7, 77.10000000000001, 93.6, 110.10000000000001, 62.800000000000004, 102.4, 156.29999999999998, 81.5, 61.7, 62.800000000000004, 87.0, 113.39999999999999, 33.10000000000001, 120.0, 85.9, 86.99999999999999, 150.8, 79.30000000000001, 105.69999999999999, 146.4, 107.90000000000002, 121.1, 16.600000000000005, 127.69999999999999, 134.29999999999998, 90.3, 122.20000000000002, 117.79999999999998, 99.1, 44.1, 124.4, 111.19999999999999, 135.39999999999998, 102.4, 132.1]
t1= [0.0, 0.0, 0.09999999999999999, 0.09999999999999999, 0.09999999999999999, 0.16, 0.19999999999999998, 0.21, 0.30000000000000004, 0.31000000000000005, 0.39999999999999997, 0.44999999999999996, 0.51, 0.6100000000000001, 0.7000000000000002, 0.7300000000000002, 0.8199999999999998, 0.9299999999999998, 1.01, 1.12, 1.2200000000000002, 1.3399999999999999, 1.4400000000000004, 1.5899999999999999, 1.7199999999999998, 1.8599999999999997, 1.9999999999999998, 2.16, 2.3200000000000003, 2.4800000000000004, 2.66, 2.84, 3.0, 3.1900000000000004, 3.39, 3.6000000000000005, 3.8200000000000007, 4.05, 4.28, 4.51, 4.7700000000000005, 5.01, 5.2700000000000005, 5.540000000000001, 5.8100000000000005, 6.09, 6.370000000000001, 6.68, 6.979999999999999, 7.29, 7.610000000000001, 7.93, 8.27, 8.619999999999997, 8.969999999999999, 9.36, 9.72, 10.13, 10.54, 10.970000000000002, 11.39, 11.799999999999997, 12.260000000000002, 12.700000000000001, 13.18, 13.65, 14.149999999999999, 14.66, 15.139999999999999, 15.660000000000002, 16.209999999999997, 16.73, 17.3, 17.88, 18.450000000000003, 19.029999999999998, 19.619999999999997, 20.209999999999997, 20.83, 21.46, 22.130000000000003, 22.78, 23.439999999999998, 24.1, 24.81, 25.49, 26.200000000000003, 26.91, 27.650000000000002, 28.380000000000003, 29.13, 29.910000000000004, 30.709999999999997, 31.509999999999998, 32.32, 33.169999999999995, 34.0, 34.87, 35.71000000000001, 36.59]
#------------------------------
#method= SSRA
r2= [-100.0, -72.5, -73.6, -75.8, -70.3, -70.3, -40.599999999999994, -40.599999999999994, 13.3, 63.9, 74.9, 66.1, 58.39999999999999, 65.0, 60.6, 62.800000000000004, 76.0, 88.10000000000001, 88.1, 77.1, 60.6, 70.5, 90.3, 68.3, 84.8, 115.6, 166.2, 115.6, 167.29999999999998, 136.49999999999997, 146.4, 135.39999999999998, 172.8, 153.0, 149.7, 140.9, 91.4, 112.30000000000001, 150.79999999999998, 118.89999999999999, 147.50000000000003, 120.0, 145.3, 35.3, 159.6, 162.9, 154.10000000000002, 113.4, 101.30000000000001, 87.00000000000001, 140.9, 124.39999999999999, 136.5, 138.70000000000002, 133.20000000000002, 138.7, 109.0, 142.0, 154.1, 81.5, 120.00000000000001, 149.70000000000005, 83.7, 90.3, 154.1, 121.10000000000001, 114.5, 119.99999999999999, 175.0, 114.5, 164.0, 97.99999999999999, 50.699999999999996, 98.0, 69.4, 103.5, 143.1, 99.1, 87.0, 157.4, 147.50000000000003, 121.1, 51.800000000000004, 51.8, 77.10000000000002, 106.8, 86.99999999999999, 112.30000000000001, 70.5, 100.2, 92.5, 87.0, 103.5, 157.4, 102.4, 142.0, 96.9, 147.5, 111.20000000000002, 74.9]
t2= [0.0, 0.0, 0.09999999999999999, 0.09999999999999999, 0.09999999999999999, 0.15000000000000002, 0.19999999999999998, 0.19999999999999998, 0.30000000000000004, 0.30000000000000004, 0.39999999999999997, 0.41999999999999993, 0.49999999999999994, 0.6000000000000001, 0.7000000000000002, 0.7100000000000002, 0.7999999999999999, 0.9099999999999998, 0.9999999999999999, 1.1, 1.21, 1.3199999999999998, 1.4300000000000006, 1.5599999999999998, 1.7199999999999998, 1.8299999999999996, 2.01, 2.14, 2.3, 2.45, 2.6499999999999995, 2.79, 2.97, 3.1700000000000004, 3.3600000000000003, 3.5600000000000005, 3.7700000000000005, 4.0, 4.2, 4.41, 4.68, 4.91, 5.18, 5.420000000000001, 5.700000000000001, 5.96, 6.270000000000001, 6.589999999999999, 6.89, 7.200000000000001, 7.510000000000002, 7.859999999999999, 8.200000000000001, 8.52, 8.87, 9.28, 9.71, 10.1, 10.51, 10.91, 11.33, 11.729999999999997, 12.16, 12.600000000000001, 13.040000000000001, 13.490000000000002, 13.979999999999999, 14.47, 14.909999999999997, 15.39, 15.900000000000002, 16.45, 17.0, 17.53, 18.090000000000003, 18.65, 19.27, 19.85, 20.449999999999996, 21.060000000000002, 21.7, 22.380000000000003, 23.010000000000005, 23.699999999999996, 24.36, 25.070000000000004, 25.779999999999998, 26.48, 27.2, 27.900000000000002, 28.629999999999995, 29.41, 30.16, 30.949999999999996, 31.770000000000003, 32.599999999999994, 33.400000000000006, 34.23, 35.07, 35.92999999999999]
#------------------------------
#method= SSEA
r3= [-100.0, -71.4, -49.4, 13.3, 9.999999999999998, -12.0, -12.0, 6.700000000000003, 34.2, 24.299999999999997, 22.099999999999998, 62.8, 82.6, 26.499999999999993, 51.8, 10.0, 27.599999999999994, 94.69999999999999, 76.00000000000001, 143.09999999999997, 95.79999999999998, 173.9, 165.1, 172.79999999999998, 123.30000000000001, 93.6, 133.20000000000002, 132.1, 117.79999999999998, 137.60000000000002, 99.1, 69.39999999999998, 105.69999999999999, 159.60000000000002, 116.69999999999999, 110.1, 137.6, 60.60000000000001, 118.9, 146.4, 121.1, 127.69999999999999, 150.8, 176.10000000000002, 132.1, 166.2, 132.1, 172.79999999999998, 180.5, 145.3, 121.1, 121.10000000000002, 103.5, 84.8, 111.2, 92.49999999999999, 106.80000000000001, 88.10000000000001, 127.70000000000002, 139.8, 101.3, 116.69999999999997, 96.89999999999999, 99.10000000000001, 103.49999999999999, 110.1, 16.6, 118.90000000000002, 127.69999999999999, 142.0, 118.89999999999999, 112.3, 96.89999999999999, 148.6, 55.1, 83.70000000000002, 129.9, 71.60000000000001, 111.2, 135.39999999999998, 136.5, 52.90000000000001, 57.3, 145.29999999999998, 93.6, 127.70000000000002, 80.39999999999999, 101.30000000000001, 118.9, 116.7, 148.6, 146.4, 58.400000000000006, 94.7, 66.10000000000001, 153.0, 91.4, 74.9, 35.3, 149.7]
t3= [0.0, 0.0, 0.09999999999999999, 0.09999999999999999, 0.09999999999999999, 0.16999999999999998, 0.19999999999999998, 0.21999999999999997, 0.30000000000000004, 0.31000000000000005, 0.39999999999999997, 0.4599999999999999, 0.51, 0.6000000000000001, 0.7000000000000002, 0.7200000000000002, 0.8099999999999999, 0.9199999999999998, 1.02, 1.12, 1.23, 1.33, 1.4300000000000002, 1.6099999999999999, 1.7399999999999998, 1.8399999999999996, 2.03, 2.15, 2.3400000000000003, 2.45, 2.6499999999999995, 2.8500000000000005, 2.99, 3.18, 3.38, 3.59, 3.8200000000000003, 4.070000000000001, 4.300000000000001, 4.550000000000001, 4.77, 5.02, 5.32, 5.54, 5.84, 6.14, 6.420000000000001, 6.7, 7.02, 7.340000000000001, 7.680000000000001, 8.000000000000002, 8.33, 8.680000000000001, 9.040000000000001, 9.43, 9.78, 10.17, 10.6, 11.0, 11.419999999999998, 11.85, 12.28, 12.74, 13.23, 13.680000000000003, 14.169999999999998, 14.670000000000002, 15.16, 15.66, 16.19, 16.740000000000002, 17.3, 17.849999999999998, 18.45, 19.03, 19.619999999999997, 20.23, 20.79, 21.409999999999997, 22.050000000000004, 22.67, 23.290000000000003, 23.98, 24.62, 25.3, 26.019999999999996, 26.73, 27.459999999999997, 28.180000000000003, 28.959999999999997, 29.71, 30.509999999999998, 31.3, 32.12, 32.94, 33.78, 34.61, 35.49, 36.339999999999996]
#------------------------------

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
t1=countNAve(t1,N)
t2=countNAve(t2,N)
t3=countNAve(t3,N)

fig, ax = plt.subplots(figsize=(13,9))
plt.xticks(fontproperties='Times New Roman', fontsize=14)
plt.yticks(fontproperties='Times New Roman', fontsize=14)
plt.axis([0,10,-150,250])

plt.plot(t1, r1, 'deepskyblue', marker='.', markersize=9, label='RA', linewidth='1.3')
plt.plot(t2, r2, 'darkviolet', marker='.', markersize=9, label='SSRA', linewidth='1.3')
plt.plot(t3, r3, 'red', marker='.', markersize=9, label='SSEA', linewidth='1.3')

ax.legend(loc='lower right', prop={'family': 'Times New Roman', 'size': 14})
plt.title('Average 100-play total reward with different belief expend method (h=20)', fontdict={'family': 'Times New Roman', 'size': 14})

ax.set_xlabel('run time', fontdict={'family': 'Times New Roman', 'size': 14})
ax.set_ylabel('total reward', fontdict={'family': 'Times New Roman', 'size': 14})
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
plt.show()