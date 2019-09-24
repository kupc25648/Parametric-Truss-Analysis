'''
====================================================================
About
====================================================================
*   This program will generate a space truss

*   The upper surface value of x,y,z will be generated parametrically
    whereas:
    x = horizontal axis1
    z = horizontal axis2
    y = vertical axis

*   X,Y,Z will be generated from range of parametric value: p
    whereas:
    P_Val_Range_min = Lowest value of parametic range
    P_Val_Range_min = Highest value of parametic range


*   Every upper nodes will be equally subjected to a point load: l
    whereas:
    lx = load at x direction +:Right -:Left
    ly = load at y direction +:Up -:Down
    lz = load at z direction +:Right -:Left

*   Joint with bases will be automatically generated at every nodes with minimum y-value
    Every generated joints will fixed joint ( x,y,z and Mxy, Myz ,Mzx restrains)

*   Every member will have a same Young modulus: E and a same cross sectional area: Area
'''
'''
====================================================================
Import Part
====================================================================
'''
import math
import numpy as np
from Input import *
from render import *


'''
====================================================================
Input Part
====================================================================
==================================
Instruction
==================================
1   Please set the parametric range
2   Please set functions of x,y,z by parametric value
3   Please set the average length of member
4   Please set the distance between upper surface and lower surface
5   Please set member's Young's modulus
6   Please set member's cross sectional area
7   Please set point loads value at every upper nodes
8   Please set number of supports
9   Please set Model's code

==================================
1   Please define the parametric range below
==================================
'''

P_Val_Range_min = -3
P_Val_Range_max = 3

'''
==================================
2   Please define functions of x,y,z by parametric value below
==================================
'''

# Function of X
def X_Val_Range(p):
    #Change the function of x in () after "return"
    return (  p  )

# Function of Z
def Z_Val_Range(p):
    #Change the function of z in () after "return"
    return (  p  )

# Y as a function of X and Z
def Y_Val_Range(X_Val_Range,Z_Val_Range):
    # Change function of z in () after "return"
    return (-0.1*(X_Val_Range**2+Z_Val_Range**2))

'''
==================================
3   Please define the average length of member below
==================================
'''
Avg_length = 1

'''
==================================
4   Please define the distance between upper surface and lower surface below
==================================
'''
Diff_Space = 0.5
'''
==================================
5   Please define member's Young's modulus below
==================================
'''
E = 29000
'''
==================================
6   Please define member's cross sectional area below
==================================
'''
Area = 12
'''
==================================
7   Please define point loads value at every upper nodes below
==================================
'''
lx = 0
ly = -100
lz = 0
'''
==================================
8   Please set number of supprt
==================================
'''
num_support = 7
'''
==================================
8   Please set Model's code
==================================
'''
ModelCode = 'M15'
'''


==================================
Finish of Input
==================================
'''



'''
====================================================================
Generate code Part
====================================================================
'''
#Initial Nodes Values
n_u_x =[]
for i in range(P_Val_Range_min,P_Val_Range_max+1):
    n_u_x.append(X_Val_Range(i))
n_u_z =[]
for i in range(P_Val_Range_min,P_Val_Range_max+1):
    n_u_z.append(Z_Val_Range(i))
'''
==================================
Generate Load
==================================
'''
l1 = Load()
l1.set_name(1)
l1.set_type(1)
l1.set_size(lx,ly,lz,lx,ly,lz)
'''
==================================
Generate Node
==================================
'''
n = 'n'
#Generate Node lower cord
n_l_coord = []
for i in range(len(n_u_x)-1):
    for j in range(len(n_u_z)-1):
        n_l_coord.append([Avg_length*(n_u_x[i]+n_u_x[i+1])/2,(Avg_length*((Y_Val_Range(n_u_x[i],n_u_z[j])+Y_Val_Range(n_u_x[i+1],n_u_z[j+1]))/2))-Diff_Space,Avg_length*(n_u_z[j]+n_u_z[j+1])/2])

n_l_name=[]
counter = 1
for i in range(len(n_l_coord)):
    n_l_name.append(n+str(counter))
    counter+=1
counter = 1
for i in range(len(n_l_coord)):
    n_l_name[i] = Node()
    n_l_name[i].set_name(counter)
    n_l_name[i].set_coord(n_l_coord[i][0],n_l_coord[i][1],n_l_coord[i][2])
    n_l_name[i].set_res(0,0,0)
    counter+=1

#Generate Node upper cord
n_u_coord = []
for i in range(len(n_u_x)):
    for j in range(len(n_u_z)):
        n_u_coord.append([Avg_length*n_u_x[i],Avg_length*Y_Val_Range(n_u_x[i],n_u_z[j]),Avg_length*n_u_z[j]])

n_u_name=[]
counter = 1
for i in range(len(n_u_coord)):
    n_u_name.append(n+str(counter))
    counter+=1
counter = 1
for i in range(len(n_u_coord)):
    n_u_name[i] = Node()
    n_u_name[i].set_name(counter)
    n_u_name[i].set_coord(n_u_coord[i][0],n_u_coord[i][1],n_u_coord[i][2])
    n_u_name[i].set_res(0,0,0)
    counter+=1

#Set node name
node_pool =[]
for i in range(len(n_l_name)):
    node_pool.append(n_l_name[i])
for i in range(len(n_u_name)):
    node_pool.append(n_u_name[i])
counter = 1
for i in range(len(node_pool)):
    node_pool[i].set_name(counter)
    counter +=1

#Divide n_l_name and n_u_name into zrow
n_l_name_div =[]
for i in range(len(n_u_z)-1):
    n_l_name_div.append([])
for i in range(len(n_l_name)):
    for j in range(len(n_u_z)-1):
        if n_l_name[i].coord[2] == (n_u_z[j]+n_u_z[j+1])/2:
            n_l_name_div[j].append(n_l_name[i])

n_u_name_div =[]
for i in range(len(n_u_z)):
    n_u_name_div.append([])
for i in range(len(n_u_name)):
    for j in range(len(n_u_z)):
        if n_u_name[i].coord[2] == n_u_z[j]:
            n_u_name_div[j].append(n_u_name[i])

#Support


    n_l_name_y=[]
    n_l_name_y_index =[]
    for i in range(len(n_l_name)):
        n_l_name_y.append(n_l_name[i].coord[1])
        n_l_name_y_index.append(i)


    to_res =[]
    to_res_index =[]

    while len(to_res_index) <= num_support:
        for i in range(len(n_l_name_y)):
            if n_l_name_y[i] == min(n_l_name_y):
                to_res_index.append(i)
                n_l_name_y[i] = float('inf')

    while len(to_res_index) > num_support:
        to_res_index.pop()

    for i in range(len(to_res_index)):
        n_l_name[to_res_index[i]].set_res(1,1,1)





#Set load to upper nodes
for i in range(len(n_u_name_div)):
    for j in range(len(n_u_name_div)):
        n_u_name_div[i][j].set_load(l1)
'''
==================================
Generate Member
==================================
'''
e = 'e'
#E lower cord
E_type1_name =[]
counter = 1

for num in range(len(n_l_name_div)):
    for i in range(len(n_l_name_div[num])-1):
        if n_l_name_div[num][i].coord[1] <= n_l_name_div[num][i+1].coord[1]:
            E_type1_name.append(e+str(counter))
            E_type1_name[-1] = Element()
            E_type1_name[-1].set_name(str(counter))
            E_type1_name[-1].set_nodes(n_l_name_div[num][i],n_l_name_div[num][i+1])
            E_type1_name[-1].set_em(E)
            E_type1_name[-1].set_area(Area)
            counter+=1
        else:
            E_type1_name.append(e+str(counter))
            E_type1_name[-1] = Element()
            E_type1_name[-1].set_name(str(counter))
            E_type1_name[-1].set_nodes(n_l_name_div[num][i+1],n_l_name_div[num][i])
            E_type1_name[-1].set_em(E)
            E_type1_name[-1].set_area(Area)
            counter+=1

#E lower connect lower
E_type2_name =[]
counter = len(E_type1_name)+1

for num in range(len(n_l_name_div)-1):
    for i in range(len(n_l_name_div[num])):
        if n_l_name_div[num][i].coord[1] <= n_l_name_div[num+1][i].coord[1]:
            E_type2_name.append(e+str(counter))
            E_type2_name[-1] = Element()
            E_type2_name[-1].set_name(str(counter))
            E_type2_name[-1].set_nodes(n_l_name_div[num][i],n_l_name_div[num+1][i])
            E_type2_name[-1].set_em(E)
            E_type2_name[-1].set_area(Area)
            counter+=1
        else:
            E_type2_name.append(e+str(counter))
            E_type2_name[-1] = Element()
            E_type2_name[-1].set_name(str(counter))
            E_type2_name[-1].set_nodes(n_l_name_div[num+1][i],n_l_name_div[num][i])
            E_type2_name[-1].set_em(E)
            E_type2_name[-1].set_area(Area)
            counter+=1

#E lower connect upper 1-1
E_type3_name =[]
counter = len(E_type1_name)+len(E_type2_name)+1

for num in range(len(n_l_name_div)):
    for i in range(len(n_l_name_div[num])):
        if n_l_name_div[num][i].coord[1] <= n_u_name_div[num][i].coord[1]:
            E_type3_name.append(e+str(counter))
            E_type3_name[-1] = Element()
            E_type3_name[-1].set_name(str(counter))
            E_type3_name[-1].set_nodes(n_l_name_div[num][i],n_u_name_div[num][i])
            E_type3_name[-1].set_em(E)
            E_type3_name[-1].set_area(Area)
            counter+=1
        else:
            E_type3_name.append(e+str(counter))
            E_type3_name[-1] = Element()
            E_type3_name[-1].set_name(str(counter))
            E_type3_name[-1].set_nodes(n_u_name_div[num][i],n_l_name_div[num][i])
            E_type3_name[-1].set_em(E)
            E_type3_name[-1].set_area(Area)
            counter+=1

#E lower connect upper 1-2
E_type4_name =[]
counter = len(E_type1_name)+len(E_type2_name)+len(E_type3_name)+1

for num in range(len(n_l_name_div)):
    for i in range(len(n_l_name_div[num])):
        if n_l_name_div[num][i].coord[1] <= n_u_name_div[num][i+1].coord[1]:
            E_type4_name.append(e+str(counter))
            E_type4_name[-1] = Element()
            E_type4_name[-1].set_name(str(counter))
            E_type4_name[-1].set_nodes(n_l_name_div[num][i],n_u_name_div[num][i+1])
            E_type4_name[-1].set_em(E)
            E_type4_name[-1].set_area(Area)
            counter+=1
        else:
            E_type4_name.append(e+str(counter))
            E_type4_name[-1] = Element()
            E_type4_name[-1].set_name(str(counter))
            E_type4_name[-1].set_nodes(n_u_name_div[num][i+1],n_l_name_div[num][i])
            E_type4_name[-1].set_em(E)
            E_type4_name[-1].set_area(Area)
            counter+=1


#E lower connect upper 2-1
E_type5_name =[]
counter = len(E_type1_name)+len(E_type2_name)+len(E_type3_name)+len(E_type4_name)+1

for num in range(len(n_l_name_div)):
    for i in range(len(n_l_name_div[num])):
        if n_l_name_div[num][i].coord[1] <= n_u_name_div[num+1][i].coord[1]:
            E_type5_name.append(e+str(counter))
            E_type5_name[-1] = Element()
            E_type5_name[-1].set_name(str(counter))
            E_type5_name[-1].set_nodes(n_l_name_div[num][i],n_u_name_div[num+1][i])
            E_type5_name[-1].set_em(E)
            E_type5_name[-1].set_area(Area)
            counter+=1
        else:
            E_type5_name.append(e+str(counter))
            E_type5_name[-1] = Element()
            E_type5_name[-1].set_name(str(counter))
            E_type5_name[-1].set_nodes(n_u_name_div[num+1][i],n_l_name_div[num][i])
            E_type5_name[-1].set_em(E)
            E_type5_name[-1].set_area(Area)
            counter+=1

#E lower connect upper 2-1
E_type6_name =[]
counter = len(E_type1_name)+len(E_type2_name)+len(E_type3_name)+len(E_type4_name)+len(E_type5_name)+1

for num in range(len(n_l_name_div)):
    for i in range(len(n_l_name_div[num])):
        if n_l_name_div[num][i].coord[1] <= n_u_name_div[num+1][i+1].coord[1]:
            E_type6_name.append(e+str(counter))
            E_type6_name[-1] = Element()
            E_type6_name[-1].set_name(str(counter))
            E_type6_name[-1].set_nodes(n_l_name_div[num][i],n_u_name_div[num+1][i+1])
            E_type6_name[-1].set_em(E)
            E_type6_name[-1].set_area(Area)
            counter+=1
        else:
            E_type6_name.append(e+str(counter))
            E_type6_name[-1] = Element()
            E_type6_name[-1].set_name(str(counter))
            E_type6_name[-1].set_nodes(n_u_name_div[num+1][i+1],n_l_name_div[num][i])
            E_type6_name[-1].set_em(E)
            E_type6_name[-1].set_area(Area)
            counter+=1


#E upper cord
E_type7_name =[]
counter = len(E_type1_name)+len(E_type2_name)+len(E_type3_name)+len(E_type4_name)+len(E_type5_name)+len(E_type6_name)+1

for num in range(len(n_u_name_div)):
    for i in range(len(n_u_name_div[num])-1):
        if n_u_name_div[num][i].coord[1] <= n_u_name_div[num][i+1].coord[1]:
            E_type7_name.append(e+str(counter))
            E_type7_name[-1] = Element()
            E_type7_name[-1].set_name(str(counter))
            E_type7_name[-1].set_nodes(n_u_name_div[num][i],n_u_name_div[num][i+1])
            E_type7_name[-1].set_em(E)
            E_type7_name[-1].set_area(Area)
            counter+=1
        else:
            E_type7_name.append(e+str(counter))
            E_type7_name[-1] = Element()
            E_type7_name[-1].set_name(str(counter))
            E_type7_name[-1].set_nodes(n_u_name_div[num][i+1],n_u_name_div[num][i])
            E_type7_name[-1].set_em(E)
            E_type7_name[-1].set_area(Area)
            counter+=1

#E upper connect upper
E_type8_name =[]
counter = len(E_type1_name)+len(E_type2_name)+len(E_type3_name)+len(E_type4_name)+len(E_type5_name)+len(E_type6_name)+len(E_type7_name)+1

for num in range(len(n_u_name_div)-1):
    for i in range(len(n_u_name_div[num])):
        if n_u_name_div[num][i].coord[1] <= n_u_name_div[num+1][i].coord[1]:
            E_type8_name.append(e+str(counter))
            E_type8_name[-1] = Element()
            E_type8_name[-1].set_name(str(counter))
            E_type8_name[-1].set_nodes(n_u_name_div[num][i],n_u_name_div[num+1][i])
            E_type8_name[-1].set_em(E)
            E_type8_name[-1].set_area(Area)
            counter+=1
        else:
            E_type8_name.append(e+str(counter))
            E_type8_name[-1] = Element()
            E_type8_name[-1].set_name(str(counter))
            E_type8_name[-1].set_nodes(n_u_name_div[num+1][i],n_u_name_div[num][i])
            E_type8_name[-1].set_em(E)
            E_type8_name[-1].set_area(Area)
            counter+=1



'''
==================================
Generate Model
==================================
'''
m1 = Model()

#Add Load
m1.add_load(l1)

#Add Node
#Node lower
for i in range(len(n_l_name)):
    m1.add_node(n_l_name[i])
#Node upper
for i in range(len(n_u_name)):
    m1.add_node(n_u_name[i])

#Add Element
#E_type1
for i in range(len(E_type1_name)):
    m1.add_element(E_type1_name[i])
#E_type2
for i in range(len(E_type2_name)):
    m1.add_element(E_type2_name[i])
#E_type3
for i in range(len(E_type3_name)):
    m1.add_element(E_type3_name[i])
#E_type4
for i in range(len(E_type4_name)):
    m1.add_element(E_type4_name[i])
#E_type5
for i in range(len(E_type5_name)):
    m1.add_element(E_type5_name[i])
#E_type6
for i in range(len(E_type6_name)):
    m1.add_element(E_type6_name[i])
#E_type7
for i in range(len(E_type7_name)):
    m1.add_element(E_type7_name[i])
#E_type8
for i in range(len(E_type8_name)):
    m1.add_element(E_type8_name[i])

m1.gen_all()
'''
==================================
Print out the result
==================================
'''

'''
print('COORD {0}'.format(m1.coord))
print('________________')
print('MSUP {0}'.format(m1.msup))
print('________________')
print('EM {0}'.format(m1.em))
print('________________')
print('CP {0}'.format(m1.cp))
print('________________')
print('MPRP {0}'.format(m1.mprp))
print('________________')
print('JP {0}'.format(m1.jp))
print('________________')
print('PJ {0}'.format(m1.pj))
print('________________')
print('MP {0}'.format(m1.mp))
print('________________')
print('PM {0}'.format(m1.pm))
print('________________')
print('nDOF {0}'.format(m1.ndof))
print('________________')
print('Q_ALL {0}'.format(m1.Qall))
print('________________')
print('NSC {0}'.format(m1.nsc))
print('________________')
print('TNSC {0}'.format(m1.tnsc))
print('________________')
print('P_MATRIX {0}'.format(m1.p_matrix))
print('________________')
print('JLV {0}'.format(m1.jlv))
print('________________')
print('GLOBAL_K {0}'.format(m1.global_k))
print('________________')
print('SSM {0}'.format(m1.ssm))
print('________________')
print('________________')
'''
print('D {0}'.format(m1.d))
print('________________')
print('v {0}'.format(m1.v))
print('________________')
print('u {0}'.format(m1.u))
print('________________')
print('q {0}'.format(m1.q))
print('________________')
print('f {0}'.format(m1.f))
print('________________')


