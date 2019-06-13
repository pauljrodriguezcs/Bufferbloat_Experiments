import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

print("loading WiFi series... ")

# wifi_bloated = np.loadtxt('wifi_bloated_g5.txt',delimiter=' ',dtype=float)
# wifi_clean = np.loadtxt('wifi_clean_g5.txt',delimiter=' ',dtype=float)
lte_bloated = np.loadtxt('lte_bloated_g5.txt',delimiter=' ',dtype=float)
lte_clean = np.loadtxt('lte_clean_g5.txt',delimiter=' ',dtype=float)

# time_w_b = wifi_bloated[:,0]
# ping_w_b = wifi_bloated[:,1]

# time_w_c = wifi_clean[:,0]
# ping_w_c = wifi_clean[:,1]

time_l_b = lte_bloated[:,0]
ping_l_b = lte_bloated[:,1]

time_l_c = lte_clean[:,0]
ping_l_c = lte_clean[:,1]

# plt.plot(time_w_c,ping_w_c,'r-', label='WiFi clean')
# plt.plot(time_w_b,ping_w_b,'m-', label='WiFi with bloat')
plt.plot(time_l_c,ping_l_c,'b--', label='LTE clean')
plt.plot(time_l_b,ping_l_b,'c--', label='LTE with bloat')

plt.xticks(np.arange(0,49,step=2))
plt.grid(True)
plt.legend()
plt.xlim(0,49)
plt.ylim(0,600)
plt.xlabel('time (s)')
plt.ylabel('ping time (ms)')
# plt.title('WiFi Results (www.g5web.com)')
plt.title('LTE Results (www.g5web.com)')
# plt.title('WiFi vs LTE Results (www.g5web.com)')
plt.show()
