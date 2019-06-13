import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

# print("loading google traceroute... ")

# wifi_traceroute_google = np.loadtxt('tcptraceroute_google.txt',delimiter=' ',dtype=float)
# lte_traceroute_google = np.loadtxt('tcptraceroute_google_lte.txt',delimiter=' ',dtype=float)

# hop_w_google = wifi_traceroute_google[:,0]
# time_w_google = wifi_traceroute_google[:,1:4]
# avg_w_google = np.average(time_w_google,axis=1)

# hop_l_google = lte_traceroute_google[:,0]
# time_l_google = lte_traceroute_google[:,1:4]
# avg_l_google = np.average(time_l_google,axis=1)

# plt.plot(hop_w_google,avg_w_google,'r-', label='WiFi')
# plt.plot(hop_l_google,avg_l_google,'c--', label='LTE')

print("loading g5 traceroute... ")

wifi_traceroute_g5 = np.loadtxt('tcptraceroute_g5.txt',delimiter=' ',dtype=float)
lte_traceroute_g5 = np.loadtxt('tcptraceroute_g5_lte.txt',delimiter=' ',dtype=float)

hop_w_g5 = wifi_traceroute_g5[:,0]
time_w_g5 = wifi_traceroute_g5[:,1:]
avg_w_g5 = np.average(time_w_g5,axis=1)

hop_l_g5 = lte_traceroute_g5[:,0]
time_l_g5 = lte_traceroute_g5[:,1:4]
avg_l_g5 = np.average(time_l_g5,axis=1)

plt.plot(hop_w_g5,avg_w_g5,'r-', label='WiFi')
plt.plot(hop_l_g5,avg_l_g5,'c--', label='LTE')

plt.grid(True)
plt.legend()
plt.xlabel('hop')
plt.ylabel('rtt (ms)')

# plt.xlim(1,11)
# plt.ylim(0,60)
# plt.xticks(np.arange(1,12,step=1))
# plt.title('WiFi vs LTE tcpraceroute (www.google.com)')

plt.xlim(1,18)
plt.ylim(0,500)
plt.xticks(np.arange(1,19,step=1))
plt.title('WiFi vs LTE tcpraceroute (www.g5web.com)')
plt.show()
