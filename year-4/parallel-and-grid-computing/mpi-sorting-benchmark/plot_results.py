import matplotlib.pyplot as plt
import numpy as np

# init cores list
num_cores = [1, 2, 4, 6, 8]

# direct=blue, bucket=green, odd-even=red, shell=yellow


# init Direct Sort times
# averages
direct_avg_exe = [2.223066, 1.27529, 0.825518, 0.686575, 0.633353625]
direct_avg_comm = [0.053354, 0.1028425, 0.137891, 0.1578485, 0.183987125]
direct_avg_proc = [2.169625, 1.125403, 0.641179, 0.486350333333333, 0.410510875]

# speedup
direct_speedup = [1.0, 1.74318468740443, 2.69293461802165, 3.23790700214835, 3.50999175223794]



# init Bucket Sort times
# averages
bucket_avg_exe = [2.228536, 1.34599, 0.967298, 0.907048166666667, 0.8495615]
bucket_avg_comm = [0.013006, 0.1029765, 0.223343, 0.304301166666667, 0.318767375]
bucket_avg_proc = [2.167307, 1.1379695, 0.635151, 0.487329833333333, 0.407412375]

# speedup
bucket_speedup = [1.0, 1.65568540628088, 2.30387739869203, 2.45691031843403, 2.62316030093172]



# init Odd-Even Sort times
# averages
odd_even_avg_exe = [2.211916, 1.3487715, 0.9982195, 0.936106666666667, 0.96097725]
odd_even_avg_comm = [0.053486, 0.232127, 0.33483275, 0.397432333333333, 0.49564175]
odd_even_avg_proc = [2.158344, 1.1160855, 0.63766875, 0.485995333333333, 0.412843375]

# speedup
odd_even_speedup = [1.0, 1.6399486495674, 2.21586134111786, 2.36288884457612, 2.30173607127536]



# init Shell Sort times
# averages
shell_avg_exe = [2.250178, 1.47445, 1.076674, np.nan, 0.893109625]
shell_avg_comm = [0.053249, 0.3239945, 0.3974835, np.nan, 0.459281375]
shell_avg_proc = [2.196844, 1.1490765, 0.64613625, np.nan, 0.417230125
]

# speedup
shell_speedup = [1.0, 1.52611346603818, 2.08993437196403, np.nan, 2.51948689949456]



'''
'''
# Handle NaN values (e.g., using linear interpolation)
shell_avg_exe = np.interp(range(len(shell_avg_exe)), 
                           [i for i, val in enumerate(shell_avg_exe) if not np.isnan(val)], 
                           [val for val in shell_avg_exe if not np.isnan(val)])

shell_avg_comm = np.interp(range(len(shell_avg_comm)), 
                           [i for i, val in enumerate(shell_avg_comm) if not np.isnan(val)], 
                           [val for val in shell_avg_comm if not np.isnan(val)])

shell_avg_proc = np.interp(range(len(shell_avg_proc)), 
                           [i for i, val in enumerate(shell_avg_proc) if not np.isnan(val)], 
                           [val for val in shell_avg_proc if not np.isnan(val)])

shell_speedup = np.interp(range(len(shell_speedup)), 
                          [i for i, val in enumerate(shell_speedup) if not np.isnan(val)], 
                          [val for val in shell_speedup if not np.isnan(val)])


# Plot 1: Execution Time Comparison
plt.figure(figsize=(10,6))
plt.plot(num_cores, direct_avg_exe, color='blue', marker='o', label='Direct Sort Execution')
plt.plot(num_cores, bucket_avg_exe, color='green', marker='o', label='Bucket Sort Execution')
plt.plot(num_cores, odd_even_avg_exe, color='red', marker='o', label='Odd-Even Sort Execution')
plt.plot(num_cores, shell_avg_exe, color='yellow', marker='o', label='Shell Sort Execution')
plt.title('Execution Time Comparison vs. Number of Cores')
plt.xlabel('Number of Cores')
plt.ylabel('Execution Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Communication Time Comparison
plt.figure(figsize=(10,6))
plt.plot(num_cores, direct_avg_comm, color='blue', marker='x', label='Direct Sort Communication')
plt.plot(num_cores, bucket_avg_comm, color='green', marker='x', label='Bucket Sort Communication')
plt.plot(num_cores, odd_even_avg_comm, color='red', marker='x', label='Odd-Even Sort Communication')
plt.plot(num_cores, shell_avg_comm, color='yellow', marker='x', label='Shell Sort Communication')
plt.title('Communication Time Comparison vs. Number of Cores')
plt.xlabel('Number of Cores')
plt.ylabel('Communication Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot 3: Processing Time Comparison
plt.figure(figsize=(10,6))
plt.plot(num_cores, direct_avg_proc, color='blue', marker='s', label='Direct Sort Processing')
plt.plot(num_cores, bucket_avg_proc, color='green', marker='s', label='Bucket Sort Processing')
plt.plot(num_cores, odd_even_avg_proc, color='red', marker='s', label='Odd-Even Sort Processing')
plt.plot(num_cores, shell_avg_proc, color='yellow', marker='s', label='Shell Sort Processing')
plt.title('Processing Time Comparison vs. Number of Cores')
plt.xlabel('Number of Cores')
plt.ylabel('Processing Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot 4: Speedup Comparison
plt.figure(figsize=(10,6))
plt.plot(num_cores, direct_speedup, color='blue', marker='^', label='Direct Sort Speedup')
plt.plot(num_cores, bucket_speedup, color='green', marker='^', label='Bucket Sort Speedup')
plt.plot(num_cores, odd_even_speedup, color='red', marker='^', label='Odd-Even Sort Speedup')
plt.plot(num_cores, shell_speedup, color='yellow', marker='^', label='Shell Sort Speedup')
plt.title('Speedup Comparison vs. Number of Cores')
plt.xlabel('Number of Cores')
plt.ylabel('Speedup')
plt.legend()
plt.grid(True)
plt.show()