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
    elif (70 <= age <= 79) and (240 <= cho):
        return 1
    # 2 points
    elif (50 <= age <= 59) and (160 <= cho <= 199):
        return 2
    elif (60 <= age <= 69) and (240 <= cho <= 279):
        return 2
    #3 Points
    elif (40 <= age <= 49) and (160 <= cho <= 199):
        return 3
    elif (50 <= age <= 59) and (200 <= cho <= 239):
        return 3
    elif (60 <= age <= 69) and (280 <= cho):
        return 3
    #4 Points
    elif (20 <= age <= 39) and (160 <= cho <= 199):
        return 4
    elif (50 <= age <= 59) and (240 <= cho <= 279):
        return 4
    #5 points
    elif (40 <= age <= 49) and (200 <= cho <= 239):
        return 5
    elif (50 <= age <= 59) and (280 <= cho):
        return 5
    #6 points
    elif (40 <= age <= 49) and (240 <= cho <= 279):
        return 6
    #7 points
    elif (20 <= age <= 39) and (160 <= cho <= 199):
        return 7
    #8 points
    elif (40 <= age <= 49) and (280 <= cho):
        return 8
    #9 points
    elif (20 <= age <= 39) and (240 <= cho <= 279):
        return 9
    #11 points
    elif (20 <= age <= 39) and (280 <= cho):
        return 11
    else:
        return 0

def F_cho_point(cho, age):
    #0 point
    if cho < 160:
        return 0
    # 1 point
    elif (60 <= age <= 69) and (160 <= cho <= 199):
        return 1
    elif (70 <= age <= 79) and (160 <= cho <= 199):
        return 1
    elif (70 <= age <= 79) and (200 <= cho <= 239):
        return 1
    # 2 points
    elif (50 <= age <= 59) and (160 <= cho <= 199):
        return 2
    elif (60 <= age <= 69) and (200 <= cho <= 239):
        return 2
    elif (70 <= age <= 79) and (240 <= cho):
        return 2
    #3 Points
    elif (60 <= age <= 69) and (240 <= cho <= 279):
        return 3
    elif (40 <= age <= 49) and (160 <= cho <= 199):
        return 3
    #4 Points
    elif (20 <= age <= 39) and (160 <= cho <= 199):
        return 4
    elif (50 <= age <= 59) and (200 <= cho <= 239):
        return 4
    elif (60 <= age <= 69) and (280 <= cho):
        return 4
    #6 points
    elif (40 <= age <= 49) and (200 <= cho <= 239):
        return 6
    #7 points
    elif (50 <= age <= 59) and (280 <= cho):
        return 7
    #8 points
    elif (20 <= age <= 39) and (200 <= cho <= 239):
        return 8
    elif (40 <= age <= 49) and (240 <= cho <= 279):
        return 8
    #10 points
    elif (40 <= age <= 49) and (280 <= cho):
        return 10
    #11 points
    elif (20 <= age <= 39) and (240 <= cho <= 279):
        return 11
    #13 points
    elif (20 <= age <= 39) and (280 <= cho):
        return 13
    else:
        return 0

# non/smoker point helper
def M_smo_point(smo, age):
    if smo == "N":
        return 0
    elif smo == "Y" and (20 <= age <= 39):
        return 8
    elif smo == "Y" and (40 <= age <= 49):
        return 5
    elif smo == "Y" and (50 <= age <= 59):
        return 3
    elif smo == "Y" and (60 <= age <= 69):
        return 1
    elif smo == "Y" and (70 <= age <= 79):
        return 1
    else:
        return 0

def F_smo_point(smo, age):
    if smo == "N":
        return 0
    elif smo == "Y" and (20 <= age <= 39):
        return 9
    elif smo == "Y" and (40 <= age <= 49):
        return 7
    elif smo == "Y" and (50 <= age <= 59):
        return 4
    elif smo == "Y" and (60 <= age <= 69):
        return 2
    elif smo == "Y" and (70 <= age <= 79):
        return 1
    else:
        return 0

# HDL point helper
def M_hdl_point(hdl):
    if (hdl >= 60):
        return -1
    elif (50 <= hdl <= 59):
        return 0
    elif (40 <= hdl <= 49):
        return 1
    elif (hdl < 40):
        return 2

def F_hdl_point(hdl):
    if (hdl >= 60):
        return -1
    elif (50 <= hdl <= 59):
        return 0
    elif (40 <= hdl <= 49):
        return 1
    elif (hdl < 40):
        return 2

# Systolic BP and treatment
def M_sbp_med_point(sbp,med):
    if med == "Y":
        if (sbp < 120):
            return 0
        elif (120 <= sbp <= 129):
            return 1
        elif (130 <= sbp <= 139):
            return 2
        elif (140 <= sbp <= 159):
            return 2
        elif (sbp >= 160):
            return 3
    elif med == "N":
        if (sbp < 120):
            return 0
        elif (120 <= sbp <= 129):
            return 0
        elif (130 <= sbp <= 139):
            return 1
        elif (140 <= sbp <= 159):
            return 1
        elif (sbp >= 160):
            return 2
    else:
        return 0

def F_sbp_med_point(sbp,med):
    if med == "Y":
        if (sbp < 120):
            return 0
        elif (120 <= sbp <= 129):
            return 3
        elif (130 <= sbp <= 139):
            return 4
        elif (140 <= sbp <= 159):
            return 5
        elif (sbp >= 160):
            return 6
    elif med == "N":
        if (sbp < 120):
            return 0
        elif (120 <= sbp <= 129):
            return 1
        elif (130 <= sbp <= 139):
            return 2
        elif (140 <= sbp <= 159):
            return 3
        elif (sbp >= 160):
            return 4
    else:
        return 0


# point calculations
def point_calc(pc_sex, pc_age, pc_cho, pc_smo, pc_hdl, pc_sbp, pc_med):
    points = 0
    
    if pc_sex == "M":
        points += M_age_point(pc_age)
        points += M_cho_point(pc_cho,pc_age)
        points += M_smo_point(pc_smo,pc_age)
        points += M_hdl_point(pc_hdl)
        points += M_sbp_med_point(pc_sbp,pc_med)
        return points
        
    elif pc_sex == "F":
        points += F_age_point(pc_age)
        points += F_cho_point(pc_cho,pc_age)
        points += F_smo_point(pc_smo,pc_age)
        points += F_hdl_point(pc_hdl)
        points += F_sbp_med_point(pc_sbp,pc_med)
        return(points)

# output calculations
def out_calc (oc_point, sex): # input point and return expected output (%)
    if sex == "M":
        if oc_point < 0:
            return "<1"
        elif oc_point == 0:
            return 1
        elif oc_point == 1:
            return 1
        elif oc_point == 2:
            return 1
        elif oc_point == 3:
            return 1
        elif oc_point == 4:
            return 1
        elif oc_point == 5:
            return 2
        elif oc_point == 6:
            return 2
        elif oc_point == 7:
            return 3
        elif oc_point == 8:
            return 4
        elif oc_point == 9:
            return 5
        elif oc_point == 10:
            return 6
        elif oc_point == 11:
            return 8
        elif oc_point == 12:
            return 10
        elif oc_point == 13:
            return 12
        elif oc_point == 14:
            return 16
        elif oc_point == 15:
            return 20
        elif oc_point == 16:
            return 25
        elif oc_point >= 17:
            return ">30"
    else:
        if oc_point < 9:
            return "<1"
        elif oc_point == 9:
            return 1
        elif oc_point == 10:
            return 1
        elif oc_point == 11:
            return 1
        elif oc_point == 12:
            return 1
        elif oc_point == 13:
            return 2
        elif oc_point == 14:
            return 2
        elif oc_point == 15:
            return 3
        elif oc_point == 16:
            return 4
        elif oc_point == 17:
            return 5
        elif oc_point == 18:
            return 6
        elif oc_point == 19:
            return 8
        elif oc_point == 20:
            return 11
        elif oc_point == 21:
            return 14
        elif oc_point == 22:
            return 17
        elif oc_point == 23:
            return 22
        elif oc_point == 24:
            return 27
        elif oc_point >= 25:
            return ">30"

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
    
    hdl = random.randrange(0,70) # will tweak later once range is reasonable
    
    sbp = random.randrange(0,170) # will tweak later once range is reasonable
    
    if random.random() < 0.5:
        med = "N"
    elif random.random() >= 0.5:
        med = "Y"
        
    point = point_calc(sex,age,cho,smo,hdl,sbp,med)
    out = out_calc(point, sex)
    
    case_patient = f"sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out}"
    print(case_patient)
