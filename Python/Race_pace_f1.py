import matplotlib.pyplot as plt
import numpy as np
import fastf1 as F1
from fastf1 import plotting
import seaborn as sns


F1.Cache.enable_cache(r"F:\! Fast F1 Cache")
F1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')


from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FuncFormatter
Race = F1.get_session(2026,"Bahrain","R")
Race.load()

Laps = Race.laps

Drivers = ["ANT","LEC"]
for i in Drivers:
    drv = Laps.pick_drivers(i).pick_quicklaps()
    color = F1.plotting.get_driver_color(i,session=Race)
    if i == "RUS":
        plt.plot(drv["LapNumber"],drv["LapTime"],color=color,label=i,linestyle=':')
    
    else:
        plt.plot(drv["LapNumber"],drv["LapTime"],color=color,label=i)

ax = plt.gca()

ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))



#print()
plt.legend(
    loc = "center right"
)
plt.grid()
plt.show()