grade_a = 70
grade_b = 60
grade_c = 50
grade_d = 40
grade_e = 30
grade_f = 10


phy_exam = int(input('what is your physics grade? '))
chem_exam = int(input('what is your chemistry grade? '))
bio_exam = int(input('what is your biology grade? '))


if phy_exam >= 70:
    print('your grade is A')
elif phy_exam >= 60:
    print('your grade is B')
elif phy_exam >= 50:
    print('your grade is C')
elif phy_exam >= 40:
    print('your grade is D')
elif phy_exam >= 30:
    print('your grade is E')    
else:
    print('your grade is F')

if chem_exam >= 70:
    print('your grade is A')
elif chem_exam >= 60:
    print('your grade is B')
elif chem_exam >= 50:
    print('your grade is C')
elif chem_exam >= 40:
    print('your grade is D')
elif chem_exam >= 30:
    print('your grade is E')
else:
    print('your grade is F')

if bio_exam >=  70:
    print('your grade is A')
elif bio_exam >= 60:
    print('your grade is B')
elif bio_exam >= 50:
    print('your grade is C')
elif bio_exam >= 40:
    print('your grade is D')
elif bio_exam >= 30:
    print('your grade is E')
else:
    print('your grade is F')