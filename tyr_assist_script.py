# purpose: assist in generating typical test cases
import random

'''
Keys and their range of values:
• sex with possible inputs F and M
• age with possible inputs positive integers between 20 and 79, inclusive
• cho (total cholesterol) with possible inputs any positive integers
• smo (smoking status) with possible inputs Y and N
• hdl with possible inputs any positive integers
• sbp (systolic BP) with possible inputs any positive integers
• med (medication status) with possible inputs Y and N
• out (output) as your expected 10-year risk % (use >30 for the last value in the table)
Example tyr_test_cases.py file (using inputs: female, age 39 years, 105 total cholesterol, non-smoker,
HDL 60 mg/dL, systolic BP 100 mmHg, not taking blood pressure medication; expected output: <1%):
sex:F age:39 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
'''

# create variables w/ default values
num_case = 10 # how test case(s) would you like to generate
case_patient = "" # a string representing one case

sex = ""
age = 0
cho = 0
smo = ""
hdl = 0
sbp = 0
med = ""

out = 0

# age point helper
def M_age_point(age):
    if 20 <= age <= 34:
        return -9
    elif 35 <= age <= 39:
        return -4
    elif 40 <= age <= 44:
        return 0
    elif 45 <= age <= 49:
        return 3
    elif 50 <= age <= 54:
        return 6
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 10
    elif 65 <= age <= 69:
        return 11
    elif 70 <= age <= 74:
        return 12
    elif 75 <= age <= 79:
        return 13
def F_age_point(age):
    if 20 <= age <= 34:
        return -7
    elif 35 <= age <= 39:
        return -3
    elif 40 <= age <= 44:
        return 0
    elif 45 <= age <= 49:
        return 3
    elif 50 <= age <= 54:
        return 6
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 10
    elif 65 <= age <= 69:
        return 12
    elif 70 <= age <= 74:
        return 14
    elif 75 <= age <= 79:
        return 16

# total cholesterol point helper
def M_cho_point(cho,age):
    #0 point
    if cho < 160:
        return 0
    # 1 point
    elif (60 <= age <= 69) and (160 <= cho <= 199):
        return 1
    elif (60 <= age <= 69) and (200 <= cho <= 239):
        return 1
    # 2 points
    
    return 0
def F_cho_point(cho):
    return 0

# non/smoker point helper
def M_smo_point(smo):
    return 0
def F_smo_point(smo):
    return 0

# HDL point helper
def M_hdl_point(hdl):
    return 0
def F_hdl_point(hdl):
    return 0

# Systolic BP and treatment
def M_sbp_med_point(sbp,med):
    return 0
def F_sbp_med_point(sbp,med):
    return 0

# point calculations
def point_calc(pc_sex, pc_age, pc_cho, pc_smo, pc_hdl, pc_sbp, pc_med):
    points = 0
    
    if pc_sex == "M":
        points += M_age_point(pc_age)
        points += M_cho_point(pc_cho,pc_age)
        points += M_smo_point(pc_smo)
        points += M_hdl_point(pc_hdl)
        points += M_sbp_med_point(pc_sbp,pc_med)
        
    elif pc_sex == "F":
        points += F_age_point(pc_age)
        points += F_cho_point(pc_cho,pc_age)
        points += F_smo_point(pc_smo)
        points += F_hdl_point(pc_hdl)
        points += F_sbp_med_point(pc_sbp,pc_med)

# output calculations
def out_calc (oc_point): # input point and return expected output (%)
    return 0

# loop generate random strings
for i in range (0,num_case):
    if random.random() < 0.5:
        sex = "M"
    elif random.random() >= 0.5:
        sex = "F"
    
    age = random.randrange(20, 79, 1)
    
    cho = random.randrange(0,480) # will tweak later once range is reasonable
    
    if random.random() < 0.5:
        smo = "N"
    elif random.random() >= 0.5:
        smo = "Y"
    
    hdl = random.randrange(0,120) # will tweak later once range is reasonable
    
    sbp = random.randrange(0,320) # will tweak later once range is reasonable
    
    if random.random() < 0.5:
        med = "N"
    elif random.random() >= 0.5:
        med = "Y"
        
    point_calc(sex,age,cho,smo,hdl,sbp,med)
        
    #case_patient = f"sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out}"
    #print(case_patient)
    
    
