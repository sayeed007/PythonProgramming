from scipy import constants


print("Value of Constant Pi:", constants.pi)
#Value of pi

print("All Units under Constants\n", dir(constants))
#All Units under Constants  

#Metric (SI) Prefixes:
print("\n\nMetric (SI) Prefixes:")
print("1 Meter = ",constants.yotta,"yotta")
print("1 Meter = ",constants.zetta,"zetta")
print("1 Meter = ",constants.exa,"exa")
print("1 Meter = ",constants.peta,"peta")
print("1 Meter = ",constants.tera,"tera")
print("1 Meter = ",constants.giga,"giga")
print("1 Meter = ",constants.mega,"mega")
print("1 Meter = ",constants.kilo,"kilo")
print("1 Meter = ",constants.hecto,"hecto")
print("1 Meter = ",constants.deka,"deka")
print("1 Meter = ",constants.deci,"deci")
print("1 Meter = ",constants.centi,"centi")
print("1 Meter = ",constants.milli,"milli")
print("1 Meter = ",constants.micro,"micro")
print("1 Meter = ",constants.nano,"nano")
print("1 Meter = ",constants.pico,"pico")
print("1 Meter = ",constants.femto,"femto")
print("1 Meter = ",constants.atto,"atto")
print("1 Meter = ",constants.zepto,"zepto")

#Binary Prefixes:
print("\nBinary Prefixes:")
print("1 kibi = ",constants.kibi,"bytes") 
print("1 mebi = ",constants.mebi,"bytes") 
print("1 gibi = ",constants.gibi,"bytes") 
print("1 tebi = ",constants.tebi,"bytes") 
print("1 pebi = ",constants.pebi,"bytes") 
print("1 exbi = ",constants.exbi,"bytes") 
print("1 zebi = ",constants.zebi,"bytes") 
print("1 yobi = ",constants.yobi,"bytes")


#Mass
print("Mass Prefixes:")
print("1 gram =       ",constants.gram,"kg")       
print("1 metric ton = ",constants.metric_ton,"kg") 
print("1 grains =     ",constants.grain,"kg")      
print("1 lb =         ",constants.lb,"kg")         
print("1 pound =      ",constants.pound,"kg")      
print("1 oz =         ",constants.oz,"kg")         
print("1 ounce =      ",constants.ounce,"kg")      
print("1 stone =      ",constants.stone,"kg")      
print("1 long ton =   ",constants.long_ton,"kg")   
print("1 short ton =  ",constants.short_ton,"kg")  
print("1 troy ounce = ",constants.troy_ounce,"kg") 
print("1 troy pound = ",constants.troy_pound,"kg") 
print("1 carat =      ",constants.carat,"kg")      
print("1 atomicmass = ",constants.atomic_mass,"kg")
print("1 m u =        ",constants.m_u,"kg")        
print("1 u =          ",constants.u,"kg")          

#angles
print("\nAngles Return the specified unit in radians")
print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06

#Time
print("\nReturn the specified unit in seconds")
print(constants.minute)      #60.0
print(constants.hour)        #3600.0
print(constants.day)         #86400.0
print(constants.week)        #604800.0
print(constants.year)        #31536000.0
print(constants.Julian_year) #31557600.0

#Length:
print("\nReturn the specified unit in meters")
print(constants.inch)              #0.0254
print(constants.foot)              #0.30479999999999996
print(constants.yard)              #0.9143999999999999
print(constants.mile)              #1609.3439999999998
print(constants.mil)               #2.5399999999999997e-05
print(constants.pt)                #0.00035277777777777776
print(constants.point)             #0.00035277777777777776
print(constants.survey_foot)       #0.3048006096012192
print(constants.survey_mile)       #1609.3472186944373
print(constants.nautical_mile)     #1852.0
print(constants.fermi)             #1e-15
print(constants.angstrom)          #1e-10
print(constants.micron)            #1e-06
print(constants.au)                #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)        #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16

#Pressure:
print("\nReturn the specified unit in pascals")
print(constants.atm)         #101325.0
print(constants.atmosphere)  #101325.0
print(constants.bar)         #100000.0
print(constants.torr)        #133.32236842105263
print(constants.mmHg)        #133.32236842105263
print(constants.psi)         #6894.757293168361

#Area:
print("\nReturn the specified unit in square meters")
print(constants.hectare) #10000.0
print(constants.acre)    #4046.8564223999992

#Volume:
print("\nReturn the specified unit in cubic meters") 
print(constants.liter)            #0.001
print(constants.litre)            #0.001
print(constants.gallon)           #0.0037854117839999997
print(constants.gallon_US)        #0.0037854117839999997
print(constants.gallon_imp)       #0.00454609
print(constants.fluid_ounce)      #2.9573529562499998e-05
print(constants.fluid_ounce_US)   #2.9573529562499998e-05
print(constants.fluid_ounce_imp)  #2.84130625e-05
print(constants.barrel)           #0.15898729492799998

#Speed:
print("\nReturn the specified unit in meters per second")
print(constants.kmh)            #0.2777777777777778
print(constants.mph)            #0.44703999999999994
print(constants.mach)           #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot)           #0.5144444444444445


#Temperature:
print("\nReturn the specified unit in Kelvin")
print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556

#Energy:
print("\nReturn the specified unit in joules ")
print(constants.eV)            #1.6021766208e-19
print(constants.electron_volt) #1.6021766208e-19
print(constants.calorie)       #4.184
print(constants.calorie_th)    #4.184
print(constants.calorie_IT)    #4.1868
print(constants.erg)           #1e-07
print(constants.Btu)           #1055.05585262
print(constants.Btu_IT)        #1055.05585262
print(constants.Btu_th)        #1054.3502644888888
print(constants.ton_TNT)       #4184000000.0

#Power:
print("\nReturn the specified unit in watts")
print(constants.hp)         #745.6998715822701
print(constants.horsepower) #745.6998715822701

#Force:
print("\nReturn the specified unit in newton")
print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665









