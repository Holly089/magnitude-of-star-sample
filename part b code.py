import random
import math
sun_Mv = 4.83 #absolute magnitude of the sun

#sample A
#generating rangdom numbers
ran_A = []
count = 0
while count< 7:
    ran_A.append(random.randint(1,6))
    count += 1
   
#calculating star magnitudes 
mag_A = []
for num in ran_A:
    M = sun_Mv + 0.3 *(num -3.5)
    mag_A.append(M)
    count += 1
    
print(mag_A)
ave_MA = sum(mag_A) / float(len(mag_A))

#stars that are observed calculations
obsereved_M_A = []
observed_m_A = []
m_A = []
DA = []
for star in mag_A:
    m = 5 *math.log10(90) -5 + star
    m_A.append(m)
    if m <= 9.8:
        obsereved_M_A.append(star)
        y= (m - star +5)/5
        d = math.pow (10, y)
        DA.append(d)
        observed_m_A.append(m)

avesee_A = sum(obsereved_M_A) / float(len(obsereved_M_A)) # observed absolute magnitude of stars in A
aveDA = sum(DA) / float(len(DA)) #caculated distcance A from obsereved stars 

# distance to A
ave_ob_m_A = sum(observed_m_A) / float(len(observed_m_A))
z= (ave_ob_m_A - avesee_A +5)/5
ave_d_A = math.pow (10, z)
print(ave_d_A)


#sample B
ran_B = []

count = 0
while count< 10:
    ran_B.append(random.randint(1,6))
    count += 1
    

star = 0
mag_B = []
for num in ran_B:
    M = sun_Mv + 0.3 *(num -3.5)
    mag_B.append(M)
    count += 1
    
print (mag_B)

ave_MB = sum(mag_B) / float(len(mag_B))
obsereved_m_B = []
m_B = []
DB = []
obsereved_M_B = []
for star in mag_B:
    m = 5 *math.log10(100) -5 + star
    m_B.append(m)
    if m <= 9.8:
        obsereved_M_B.append(star)
        y= (m - star +5)/5
        d = math.pow (10, y)
        DB.append(d)
        obsereved_m_B.append(m)
        
avesee_B = sum(obsereved_M_B) / float(len(obsereved_M_B)) #observed absolute magnitude of stars in B
aveDB = sum(DB) / float(len(DB)) #caculated distcance B from obsereved stars 

# distance to B
ave_ob_m_B = sum(obsereved_m_B) / float(len(obsereved_m_B))
z= (ave_ob_m_B - avesee_B +5)/5
ave_d_B = math.pow (10, z)
print(ave_d_B)



#sample C
ran_C = []

count = 0
while count< 13:
    ran_C.append(random.randint(1,6))
    count += 1
    

star = 0
mag_C = []
for num in ran_C:
    M = sun_Mv + 0.3 *(num -3.5)
    mag_C.append(M)
    count += 1
    
print(mag_C)

ave_MC = sum(mag_C) / float(len(mag_C))

obsereved_m_C = []
m_C = []
DC = []
obsereved_M_B = []
for star in mag_C:
    m = 5 *math.log10(110) -5 + star
    m_C.append(m)
    if m <= 9.8:
        obsereved_M_B.append(star)
        y= (m - star +5)/5
        d = math.pow (10, y)
        DC.append(d) 
        obsereved_m_C.append(m)
        

avesee_C = sum(obsereved_M_B) / float(len(obsereved_M_B)) #observed absolute magnitude of stars in C

aveDC = sum(DC) / float(len(DC)) #caculated distcance C from obsereved stars 

# distance to C
ave_ob_m_C = sum(obsereved_m_C) / float(len(obsereved_m_C))
z= (ave_ob_m_B - avesee_C +5)/5
ave_d_C = math.pow (10, z)
print(ave_d_C)
