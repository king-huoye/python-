math_grade=[65,92,65,38,56,85,45,63,54,77,76,75]
phy_grade=[58,66,68,78,52,66,30,88,91,60,56,88]
chem_grade=[75,85,52,98,66,74,58,99,32,85,83,82]
pro_grade=[80,85,65,36,98,56,47,78,85,56,25,98]
cet6_grade=[80,87,85,58,65,85,96,56,85,25,35,69]
#平方
t1,t2,t3,t4,t5=0,0,0,0,0
for Math in range(len(math_grade)):
    t1+=(66-math_grade[Math])**2
t1=t1/11
s1=t1**0.5

for py in range(len(phy_grade)):
    t2+=(67-phy_grade[py])**2
t2=t2/11
s2=t2**0.5

for ch in range(len(chem_grade)):
    t3+=(74-chem_grade[ch])**2
t3=t3/11
s3=t3**0.5

for plus in range(len(pro_grade)):
    t4+=(67-pro_grade[plus])**2
t4=t4/11
s4=t4**0.5

for six in range(len(cet6_grade)):
    t5+=(69-cet6_grade[six])**2
t5=t5/11
s5=t5**0.5
print(f'高等数学的标准差{s1},方差{t1}')
print(f'高等物理的标准差{s2}，方差{t2}')
print(f'高等化学的标准差{s3}，方差{t3}')
print(f'程序语言的标准差{s4}，方差{t4}')
print(f'英文六级的标准差{s5},方差{t5}')

