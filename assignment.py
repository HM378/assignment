#assignment
#1
'''production=[1050,980,1025,1100,975,990,1005,350]
sum=0
avg=0
for i in production:
    sum=sum+i
    if(i>500):
        print(i)
avg=sum/len(production)
print("the average production per day is ",avg)'''
#3
'''well_info={
    "well name": "b-25",
    "status": "active",
    "depth": 3200,
    "reservoir" : "sandstone"
}
if(well_info["status"]=="active"):
    print("the well status is active")
else:
    print("the well status is not active")
print(f"{well_info["well name"]} is currently {well_info["status"]} in {well_info["reservoir"]} formation")'''
#4
'''def ooip(a,h,phi,sw,bo):
    original_oil_place=(7758*a*h*phi*(1-sw))/bo
    return original_oil_place
a=ooip(500,30,0.2,0.25,1.2)
print(a)'''
#5
'''sum=0
i=0
day=int(input("enter the number of days production you want to mention :"))
for i in range(0,day):
    a=float(input("the oil production rate for the  is : "))
    sum=sum+a
print(f"the cumulative oil production is {sum}")
avg=sum/day
print("the average production is :",avg)'''

#6
'''import numpy as np
pressure=np.array([3500,3450,3400,3350,3300])
print("the average of pressures is :",pressure.mean())
pressure_drop=np.diff(pressure)
print("the pressure drop per interval is :",pressure_drop)'''
#7
'''import numpy  as np
import pandas as pd
data={
    "depth" : [1000,1010,1020,1030,1040],
    "gr_api" : [80,75,78,82,77],
    "rt_ohm_m" : [20,25,22,19,23]
}
df=pd.DataFrame(data)
gr_mean=df["gr_api"].mean()
rt_ohm_m_mean=df["rt_ohm_m"].mean()
data["lithology"]=np.where(df["gr_api"]<80,"sandstone","shale")
print(data)
print(gr_mean)
print(rt_ohm_m_mean)'''
#8
'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
production=[1050,980,1025,1100,975,990,1005]
plt.plot(days,production)
plt.scatter(1,1050,label="highest production",c="green")
plt.grid(True)
plt.xlabel("days")
plt.ylabel("oil production (bbl/day)")
plt.title("oil production vs days")
plt.legend()
plt.show()'''
