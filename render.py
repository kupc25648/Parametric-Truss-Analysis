import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Analysis import *
fig = plt.figure(figsize=plt.figaspect(0.3))
#========================
#  INITIAL
#========================
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.8, wspace=0, hspace=None)
ax1 = fig.add_subplot(1,3,1,projection='3d')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')

#Model Name
Analysis_type0 = 'Matrix Analysis'
Structure_type0 = 'Space Truss (Initial)'
Model_code0 = ModelCode
Node_and_Member = str(len(m1.nodes))+'nodes' + str(len(m1.elements))+'members'
Load = 'Point Load at upper nodes'



# NODES
Xcoord1 = []  #Horizontal
Ycoord1 = []  #Vertical
Zcoord1 = []  #Horizontal
for i in range(len(m1.nodes)):
    Xcoord1.append(m1.nodes[i].coord[0])
    Ycoord1.append(m1.nodes[i].coord[2]) #In Input and Analysis Z = Horizotal
    Zcoord1.append(m1.nodes[i].coord[1]) #In Input and Analysis Y = Vertical



Nodes1 = {'X':Xcoord1, 'Y':Ycoord1, 'Z':Zcoord1}
nodeplot1 = pd.DataFrame(Nodes1, columns = ['X','Y','Z'])
fignodeplot1 = ax1.scatter(xs=nodeplot1['X'],ys=nodeplot1['Y'],zs=nodeplot1['Z'],color ='black',s=1)

# ELEMENTS
for i in range(len(m1.elements)):
    xstart = m1.elements[i].nodes[0].coord[0]
    xend = m1.elements[i].nodes[1].coord[0]
    ystart = m1.elements[i].nodes[0].coord[2] #In Input and Analysis Z = Horizotal
    yend = m1.elements[i].nodes[1].coord[2] #In Input and Analysis Z = Horizotal
    zstart = m1.elements[i].nodes[0].coord[1] #In Input and Analysis Y = Vertical
    zend = m1.elements[i].nodes[1].coord[1] #In Input and Analysis Y = Vertical



    Xcoord = [xstart,xend]
    Zcoord = [zstart,zend]
    Ycoord = [ystart,yend]

    Elements = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
    elementplot = pd.DataFrame(Elements, columns = ['X','Y','Z'])
    figelementplot = ax1.plot(xs=elementplot['X'],ys=elementplot['Y'],zs=elementplot['Z'],color ='black')


# SUPPORT
#CASE 1 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_Zres1=[]
Ycoord_Zres1=[]
Zcoord_Zres1=[]

#CASE 2 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_ZresXres1=[]
Ycoord_ZresXres1=[]
Zcoord_ZresXres1=[]

#CASE 3 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresYres1=[]
Ycoord_ZresYres1=[]
Zcoord_ZresYres1=[]

#CASE 4 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresXresYres1=[]
Ycoord_ZresXresYres1=[]
Zcoord_ZresXresYres1=[]


for i in range(len(m1.nodes)):
    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_Zres1.append(m1.nodes[i].coord[0])
        Ycoord_Zres1.append(m1.nodes[i].coord[2])
        Zcoord_Zres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_ZresXres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresXres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresXres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresYres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresYres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresYres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresXresYres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresXresYres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresXresYres1.append(m1.nodes[i].coord[1])

    else:
        pass

if Xcoord_Zres1 != 0:
    Zres1 = {'X':Xcoord_Zres1, 'Y':Ycoord_Zres1, 'Z':Zcoord_Zres1}
    Zresplot1 = pd.DataFrame(Zres1, columns = ['X','Y','Z'])
    figZresplot1 = ax1.scatter(xs=Zresplot1['X'],ys=Zresplot1['Y'],zs=Zresplot1['Z'],color ='silver',marker="^",s=100)

if Xcoord_ZresXres1 != 0:
    ZresXres1 = {'X':Xcoord_ZresXres1, 'Y':Ycoord_ZresXres1, 'Z':Zcoord_ZresXres1}
    ZresXresplot1 = pd.DataFrame(ZresXres1, columns = ['X','Y','Z'])
    figZresXresplot1 = ax1.scatter(xs=ZresXresplot1['X'],ys=ZresXresplot1['Y'],zs=ZresXresplot1['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresYres1 != 0:
    ZresYres1 = {'X':Xcoord_ZresYres1, 'Y':Ycoord_ZresYres1, 'Z':Zcoord_ZresYres1}
    ZresYresplot1 = pd.DataFrame(ZresYres1, columns = ['X','Y','Z'])
    figZresYresplot1 = ax1.scatter(xs=ZresYresplot1['X'],ys=ZresYresplot1['Y'],zs=ZresYresplot1['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresXresYres1 != 0:
    ZresXresYres1 = {'X':Xcoord_ZresXresYres1, 'Y':Ycoord_ZresXresYres1, 'Z':Zcoord_ZresXresYres1}
    ZresXresYresplot1 = pd.DataFrame(ZresXresYres1, columns = ['X','Y','Z'])
    figZresXresYresplot1 = ax1.scatter(xs=ZresXresYresplot1['X'],ys=ZresXresYresplot1['Y'],zs=ZresXresYresplot1['Z'],color ='black',marker="^",s=100)
else:
    pass

# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([nodeplot1['X'].max()-nodeplot1['X'].min(), nodeplot1['Y'].max()-nodeplot1['Y'].min(), nodeplot1['Z'].max()-nodeplot1['Z'].min()]).max()
Xb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.01*(nodeplot1['X'].max()+nodeplot1['X'].min())
Yb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.01*(nodeplot1['Y'].max()+nodeplot1['Y'].min())
Zb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.01*(nodeplot1['Y'].max()+nodeplot1['Y'].min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax1.plot([xb], [yb], [zb], 'w')

plt.title('\n'+Analysis_type0+'\n'+Structure_type0+'\n'+Model_code0+'\n'+Node_and_Member+'\n'+Load,loc='left')


plt.grid()

plt.axis('equal')

#========================
#  INITIAL COMPRESSION & TENSION
#========================
ax1 = fig.add_subplot(1,3,2,projection='3d')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
ax1.view_init(azim=0, elev=90)

#Model Name
Analysis_type1 = 'Compression: Red'
Structure_type1 = 'Tension: Blue'
Model_code1 = 'Zero: White'


# NODES
Xcoord1 = []  #Horizontal
Ycoord1 = []  #Vertical
Zcoord1 = []  #Horizontal
for i in range(len(m1.nodes)):
    Xcoord1.append(m1.nodes[i].coord[0])
    Ycoord1.append(m1.nodes[i].coord[2]) #In Input and Analysis Z = Horizotal
    Zcoord1.append(m1.nodes[i].coord[1]) #In Input and Analysis Y = Vertical



Nodes1 = {'X':Xcoord1, 'Y':Ycoord1, 'Z':Zcoord1}
nodeplot1 = pd.DataFrame(Nodes1, columns = ['X','Y','Z'])
fignodeplot1 = ax1.scatter(xs=nodeplot1['X'],ys=nodeplot1['Y'],zs=nodeplot1['Z'],color ='black',s=1)

# ELEMENTS
for i in range(len(m1.elements)):
    # Tension member
    if m1.q[i][0][0] < 0:
        xstart = m1.elements[i].nodes[0].coord[0]
        xend = m1.elements[i].nodes[1].coord[0]
        ystart = m1.elements[i].nodes[0].coord[2] #In Input and Analysis Z = Horizotal
        yend = m1.elements[i].nodes[1].coord[2] #In Input and Analysis Z = Horizotal
        zstart = m1.elements[i].nodes[0].coord[1] #In Input and Analysis Y = Vertical
        zend = m1.elements[i].nodes[1].coord[1] #In Input and Analysis Y = Vertical

        Xcoord = [xstart,xend]
        Zcoord = [zstart,zend]
        Ycoord = [ystart,yend]

        Elements = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
        elementplot = pd.DataFrame(Elements, columns = ['X','Y','Z'])
        figelementplot = ax1.plot(xs=elementplot['X'],ys=elementplot['Y'],zs=elementplot['Z'],color ='blue')

    # Compression member
    elif m1.q[i][0][0] > 0:
        xstart = m1.elements[i].nodes[0].coord[0]
        xend = m1.elements[i].nodes[1].coord[0]
        ystart = m1.elements[i].nodes[0].coord[2] #In Input and Analysis Z = Horizotal
        yend = m1.elements[i].nodes[1].coord[2] #In Input and Analysis Z = Horizotal
        zstart = m1.elements[i].nodes[0].coord[1] #In Input and Analysis Y = Vertical
        zend = m1.elements[i].nodes[1].coord[1] #In Input and Analysis Y = Vertical

        Xcoord = [xstart,xend]
        Zcoord = [zstart,zend]
        Ycoord = [ystart,yend]

        Elements = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
        elementplot = pd.DataFrame(Elements, columns = ['X','Y','Z'])
        figelementplot = ax1.plot(xs=elementplot['X'],ys=elementplot['Y'],zs=elementplot['Z'],color ='red')

    # Zero force member
    else:
        xstart = m1.elements[i].nodes[0].coord[0]
        xend = m1.elements[i].nodes[1].coord[0]
        ystart = m1.elements[i].nodes[0].coord[2] #In Input and Analysis Z = Horizotal
        yend = m1.elements[i].nodes[1].coord[2] #In Input and Analysis Z = Horizotal
        zstart = m1.elements[i].nodes[0].coord[1] #In Input and Analysis Y = Vertical
        zend = m1.elements[i].nodes[1].coord[1] #In Input and Analysis Y = Vertical

        Xcoord = [xstart,xend]
        Zcoord = [zstart,zend]
        Ycoord = [ystart,yend]

        Elements = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
        elementplot = pd.DataFrame(Elements, columns = ['X','Y','Z'])
        figelementplot = ax1.plot(xs=elementplot['X'],ys=elementplot['Y'],zs=elementplot['Z'],color ='white')


# SUPPORT
#CASE 1 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_Zres1=[]
Ycoord_Zres1=[]
Zcoord_Zres1=[]

#CASE 2 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_ZresXres1=[]
Ycoord_ZresXres1=[]
Zcoord_ZresXres1=[]

#CASE 3 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresYres1=[]
Ycoord_ZresYres1=[]
Zcoord_ZresYres1=[]

#CASE 4 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresXresYres1=[]
Ycoord_ZresXresYres1=[]
Zcoord_ZresXresYres1=[]


for i in range(len(m1.nodes)):
    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_Zres1.append(m1.nodes[i].coord[0])
        Ycoord_Zres1.append(m1.nodes[i].coord[2])
        Zcoord_Zres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_ZresXres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresXres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresXres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresYres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresYres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresYres1.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresXresYres1.append(m1.nodes[i].coord[0])
        Ycoord_ZresXresYres1.append(m1.nodes[i].coord[2])
        Zcoord_ZresXresYres1.append(m1.nodes[i].coord[1])

    else:
        pass

if Xcoord_Zres1 != 0:
    Zres1 = {'X':Xcoord_Zres1, 'Y':Ycoord_Zres1, 'Z':Zcoord_Zres1}
    Zresplot1 = pd.DataFrame(Zres1, columns = ['X','Y','Z'])
    figZresplot1 = ax1.scatter(xs=Zresplot1['X'],ys=Zresplot1['Y'],zs=Zresplot1['Z'],color ='silver',marker="^",s=100)

if Xcoord_ZresXres1 != 0:
    ZresXres1 = {'X':Xcoord_ZresXres1, 'Y':Ycoord_ZresXres1, 'Z':Zcoord_ZresXres1}
    ZresXresplot1 = pd.DataFrame(ZresXres1, columns = ['X','Y','Z'])
    figZresXresplot1 = ax1.scatter(xs=ZresXresplot1['X'],ys=ZresXresplot1['Y'],zs=ZresXresplot1['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresYres1 != 0:
    ZresYres1 = {'X':Xcoord_ZresYres1, 'Y':Ycoord_ZresYres1, 'Z':Zcoord_ZresYres1}
    ZresYresplot1 = pd.DataFrame(ZresYres1, columns = ['X','Y','Z'])
    figZresYresplot1 = ax1.scatter(xs=ZresYresplot1['X'],ys=ZresYresplot1['Y'],zs=ZresYresplot1['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresXresYres1 != 0:
    ZresXresYres1 = {'X':Xcoord_ZresXresYres1, 'Y':Ycoord_ZresXresYres1, 'Z':Zcoord_ZresXresYres1}
    ZresXresYresplot1 = pd.DataFrame(ZresXresYres1, columns = ['X','Y','Z'])
    figZresXresYresplot1 = ax1.scatter(xs=ZresXresYresplot1['X'],ys=ZresXresYresplot1['Y'],zs=ZresXresYresplot1['Z'],color ='black',marker="^",s=100)
else:
    pass

# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([nodeplot1['X'].max()-nodeplot1['X'].min(), nodeplot1['Y'].max()-nodeplot1['Y'].min(), nodeplot1['Z'].max()-nodeplot1['Z'].min()]).max()
Xb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.01*(nodeplot1['X'].max()+nodeplot1['X'].min())
Yb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.01*(nodeplot1['Y'].max()+nodeplot1['Y'].min())
Zb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.01*(nodeplot1['Y'].max()+nodeplot1['Y'].min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax1.plot([xb], [yb], [zb], 'w')

plt.title(Analysis_type1+'\n'+Structure_type1+'\n'+Model_code1,loc='left')


plt.grid()

plt.axis('equal')

#========================
#  INITIAL + DEFORMATION
#========================
ax = fig.add_subplot(1,3,3,projection='3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

#Model Name
Analysis_type2 = 'Deformation'
Structure_type2 = 'Initial Form: Black '
Model_code2 = 'Nodal Deformation: Red'


# NODES
Xcoord = []  #Horizontal
Ycoord = []  #Vertical
Zcoord = []  #Horizontal
for i in range(len(m1.nodes)):
    Xcoord.append(m1.nodes[i].coord[0])
    Ycoord.append(m1.nodes[i].coord[2]) #In Input and Analysis Z = Horizotal
    Zcoord.append(m1.nodes[i].coord[1]) #In Input and Analysis Y = Vertical



Nodes = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
nodeplot = pd.DataFrame(Nodes, columns = ['X','Y','Z'])
fignodeplot = ax.scatter(xs=nodeplot['X'],ys=nodeplot['Y'],zs=nodeplot['Z'],color ='black',s=1)

# ELEMENTS
for i in range(len(m1.elements)):
    xstart = m1.elements[i].nodes[0].coord[0]
    xend = m1.elements[i].nodes[1].coord[0]
    ystart = m1.elements[i].nodes[0].coord[2] #In Input and Analysis Z = Horizotal
    yend = m1.elements[i].nodes[1].coord[2] #In Input and Analysis Z = Horizotal
    zstart = m1.elements[i].nodes[0].coord[1] #In Input and Analysis Y = Vertical
    zend = m1.elements[i].nodes[1].coord[1] #In Input and Analysis Y = Vertical



    Xcoord = [xstart,xend]
    Zcoord = [zstart,zend]
    Ycoord = [ystart,yend]

    Elements = {'X':Xcoord, 'Y':Ycoord, 'Z':Zcoord}
    elementplot = pd.DataFrame(Elements, columns = ['X','Y','Z'])
    figelementplot = ax.plot(xs=elementplot['X'],ys=elementplot['Y'],zs=elementplot['Z'],color ='black')


# SUPPORT
#CASE 1 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_Zres=[]
Ycoord_Zres=[]
Zcoord_Zres=[]

#CASE 2 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0)
Xcoord_ZresXres=[]
Ycoord_ZresXres=[]
Zcoord_ZresXres=[]

#CASE 3 (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresYres=[]
Ycoord_ZresYres=[]
Zcoord_ZresYres=[]

#CASE 4 (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1)
Xcoord_ZresXresYres=[]
Ycoord_ZresXresYres=[]
Zcoord_ZresXresYres=[]


for i in range(len(m1.nodes)):
    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_Zres.append(m1.nodes[i].coord[0])
        Ycoord_Zres.append(m1.nodes[i].coord[2])
        Zcoord_Zres.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 0):
        Xcoord_ZresXres.append(m1.nodes[i].coord[0])
        Ycoord_ZresXres.append(m1.nodes[i].coord[2])
        Zcoord_ZresXres.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 0) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresYres.append(m1.nodes[i].coord[0])
        Ycoord_ZresYres.append(m1.nodes[i].coord[2])
        Zcoord_ZresYres.append(m1.nodes[i].coord[1])


    if (m1.nodes[i].res[0] == 1) and (m1.nodes[i].res[1] == 1) and (m1.nodes[i].res[2] == 1):
        Xcoord_ZresXresYres.append(m1.nodes[i].coord[0])
        Ycoord_ZresXresYres.append(m1.nodes[i].coord[2])
        Zcoord_ZresXresYres.append(m1.nodes[i].coord[1])

    else:
        pass

if Xcoord_Zres != 0:
    Zres = {'X':Xcoord_Zres, 'Y':Ycoord_Zres, 'Z':Zcoord_Zres}
    Zresplot = pd.DataFrame(Zres, columns = ['X','Y','Z'])
    figZresplot = ax.scatter(xs=Zresplot['X'],ys=Zresplot['Y'],zs=Zresplot['Z'],color ='silver',marker="^",s=100)

if Xcoord_ZresXres != 0:
    ZresXres = {'X':Xcoord_ZresXres, 'Y':Ycoord_ZresXres, 'Z':Zcoord_ZresXres}
    ZresXresplot = pd.DataFrame(ZresXres, columns = ['X','Y','Z'])
    figZresXresplot = ax.scatter(xs=ZresXresplot['X'],ys=ZresXresplot['Y'],zs=ZresXresplot['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresYres != 0:
    ZresYres = {'X':Xcoord_ZresYres, 'Y':Ycoord_ZresYres, 'Z':Zcoord_ZresYres}
    ZresYresplot = pd.DataFrame(ZresYres, columns = ['X','Y','Z'])
    figZresYresplot = ax.scatter(xs=ZresYresplot['X'],ys=ZresYresplot['Y'],zs=ZresYresplot['Z'],color ='grey',marker="^",s=100)

if Xcoord_ZresXresYres != 0:
    ZresXresYres = {'X':Xcoord_ZresXresYres, 'Y':Ycoord_ZresXresYres, 'Z':Zcoord_ZresXresYres}
    ZresXresYresplot = pd.DataFrame(ZresXresYres, columns = ['X','Y','Z'])
    figZresXresYresplot = ax.scatter(xs=ZresXresYresplot['X'],ys=ZresXresYresplot['Y'],zs=ZresXresYresplot['Z'],color ='black',marker="^",s=100)
else:
    pass


# DEFROMATION

# NODES
NewXcoord = []
NewYcoord = []
NewZcoord = []
for i in range(len(m1.nodes)):
    NewXcoord.append(m1.nodes[i].coord[0])
    NewYcoord.append(m1.nodes[i].coord[2])
    NewZcoord.append(m1.nodes[i].coord[1])

for i in range(len(m1.d)):
    for j in range(len(m1.tnsc)):
        if m1.tnsc[j][0] == i + 1:
            NewXcoord[j] += m1.d[i][0]
        if m1.tnsc[j][2] == i + 1:
            NewYcoord[j] += m1.d[i][0]
        if m1.tnsc[j][1] == i + 1:
            NewZcoord[j] += m1.d[i][0]

NewNodes = {'X':NewXcoord, 'Y':NewYcoord, 'Z':NewZcoord}
Newnodeplot = pd.DataFrame(NewNodes, columns = ['X', 'Y', 'Z'])
figNewnodeplot = ax.scatter(xs=Newnodeplot['X'],ys=Newnodeplot['Y'],zs=Newnodeplot['Z'],color ='red',alpha=0.5,s=1)
# ELEMENTS
for i in range(len(m1.elements)):
    Newxstart = m1.elements[i].nodes[0].coord[0]
    Newxend = m1.elements[i].nodes[1].coord[0]
    Newystart = m1.elements[i].nodes[0].coord[2]
    Newyend = m1.elements[i].nodes[1].coord[2]
    Newzstart = m1.elements[i].nodes[0].coord[1]
    Newzend = m1.elements[i].nodes[1].coord[1]

    for k in range(len(m1.d)):
        if m1.tnsc[m1.elements[i].nodes[0].name-1][0] == k + 1:
            Newxstart += m1.d[k][0]
        if m1.tnsc[m1.elements[i].nodes[1].name-1][0] == k + 1:
            Newxend += m1.d[k][0]
        if m1.tnsc[m1.elements[i].nodes[0].name-1][2] == k + 1:
            Newystart += m1.d[k][0]
        if m1.tnsc[m1.elements[i].nodes[1].name-1][2] == k + 1:
            Newyend += m1.d[k][0]
        if m1.tnsc[m1.elements[i].nodes[0].name-1][1] == k + 1:
            Newzstart += m1.d[k][0]
        if m1.tnsc[m1.elements[i].nodes[1].name-1][1] == k + 1:
            Newzend += m1.d[k][0]
        else:
            pass

    NewXcoord = [Newxstart,Newxend]
    NewZcoord = [Newzstart,Newzend]
    NewYcoord = [Newystart,Newyend]

    NewElements = {'X':NewXcoord, 'Y':NewYcoord, 'Z':NewZcoord}
    Newelementplot = pd.DataFrame(NewElements, columns = ['X','Y','Z'])
    figNewelementplot = ax.plot(xs=Newelementplot['X'],ys=Newelementplot['Y'],zs=Newelementplot['Z'],color ='red',alpha=0.5)


# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([nodeplot['X'].max()-nodeplot['X'].min(), nodeplot['Y'].max()-nodeplot['Y'].min(), nodeplot['Z'].max()-nodeplot['Z'].min()]).max()
Xb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.01*(nodeplot['X'].max()+nodeplot['X'].min())
Yb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.01*(nodeplot['Y'].max()+nodeplot['Y'].min())
Zb = 0.01*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.01*(nodeplot['Y'].max()+nodeplot['Y'].min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax.plot([xb], [yb], [zb], 'w')

plt.title(Analysis_type2+'\n'+Structure_type2+'\n'+Model_code2,loc='left')

plt.grid()

plt.axis('equal')

plt.show()

