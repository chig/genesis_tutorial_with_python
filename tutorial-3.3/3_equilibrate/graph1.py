import matplotlib.pyplot as plt
import sys
sys.path.append("../scripts/get_genesis_log")
import genesislog
(x,y)=genesislog.read_genesis("log1", "TEMPERATURE")
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.grid()
ax.plot(x,y)
ax.set_xlabel("Steps", size=14)
ax.set_ylabel("Temperature (K)",size=14)
plt.savefig("log1_temp.pdf")
plt.savefig("log1_temp.png")
quit()
