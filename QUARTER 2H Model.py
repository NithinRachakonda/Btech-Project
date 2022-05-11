b=1.0
phi=0.8
rho=12.00
Lp=rho*b
lth = 12.0625
wth = 2.5
thih = 0.5 ## thickness matrix in 2nd hierarchy


ltp = 24.0625
wtp = 4.75
thth = 0.5*thih
di = 6
rad=di/2

u1 =[]
u2 = []
xx=[]
yy=[]
elst=[]
nel=[]
xcenp=[]
ycenp=[]
xcenpall=[]
ycenpall=[]
tot=[]
maxi_s11=[]
ns = []
scf = []
s11=[]
s22=[]
s33=[]
s44=[]
import random
import numpy
from itertools import repeat
import job
import os
from jobMessage import *



w=b/2.00
Lp=rho*b

Gm = 7
num = 0.49
Em = 2*Gm*(1+num)
Q11_1H=461.0268
Q12_1H=53.056
Q22_1H=1230.25
G12_1H=34.1
vg = b/phi - b
hg=0.25*vg
w=b/2.0
lb=hg/2

meshsize=vg/2##mesh size

Lrve=hg+Lp
Wrve=2*(vg+b)
Lrve=hg+Lp
Wrve=2*(vg+b)

os.chdir(r"E:\\9.5D")
flag=1
n= 1
tim=0
k=0     
while flag<=n:
    con=1
    ok=0
    u1 =[]
    u2 = []
    xx=[]
    yy=[]
    e11 =[]
    e12 = []
    e22 = []
    from abaqus import *
    from abaqusConstants import *
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=121.633964538574, 
        height=118.363288879395)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()
    from caeModules import *
    from driverUtils import executeOnCaeStartup
    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    Mdb()

    lbls=[]
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    import sketch
    import part
    ###Whatever print functions we are using we do it to be shown in message area.
    print('iteration number '+repr(flag))

    a11=random.randint(131,185)      #last value wont count
    a12=random.randint(55,75) 

    xcenpall.append(a11)
    ycenpall.append(a12)
    numpy.savetxt('a11.txt',xcenpall,fmt='%f')
    numpy.savetxt('a12.txt',ycenpall,fmt='%f')


    #mdb.models.changeKey(fromName='Model-1', toName='Model-10')

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=5000.0)

    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(lb, 0.0), point2=(lb+Lp, b/2))
    s.rectangle(point1=(Lrve - Lp/2,  vg + b*0.5), point2=(Lrve,  vg + b*1.5))
    s.rectangle(point1=(lb,  2*vg + b*1.5), point2=(Lrve-lb,  2*vg + b*2))
    s.rectangle(point1=(Lp/2, vg + b*1.5), point2=(0, vg + b*.5))
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-1'].Part(name='Platelet', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()



    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=5000.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(lb, 0.0))
    s1.Line(point1=(lb, 0.0), point2=(lb, b/2))
    s1.Line(point1=(lb, b/2), point2=(lb+Lp, b/2))
    s1.Line(point1=(lb+Lp, b/2), point2=(lb+Lp, 0.0))
    s1.Line(point1=(lb+Lp, 0.0), point2=(Lrve, 0.0))
    session.viewports['Viewport: 1'].view.fitView()
    s1.Line(point1=(Lrve, 0.0), point2=(Lrve, vg + b*0.5))
    s1.Line(point1=(Lrve, vg + b*0.5), point2=(Lrve- Lp/2,  vg + b*0.5))
    s1.Line(point1=(Lrve - Lp/2,  vg + b*0.5), point2=(Lrve - Lp/2,  vg + b*1.5))
    s1.Line(point1=(Lrve - Lp/2,  vg + b*1.5), point2=(Lrve,  vg + b*1.5))
    s1.Line(point1=(Lrve,  vg + b*1.5), point2=(Lrve,  2*vg + b*2))
    s1.Line(point1=(Lrve,  2*vg + b*2), point2=(Lrve-lb,  2*vg + b*2))
    s1.Line(point1=(Lrve-lb,  2*vg + b*2), point2=(Lrve-lb,  2*vg + b*1.5))
    s1.Line(point1=(Lrve-lb,  2*vg + b*1.5), point2=(lb,  2*vg + b*1.5))
    s1.Line(point1=(lb,  2*vg + b*1.5), point2=(lb,  2*vg + b*2))
    s1.Line(point1=(lb,  2*vg + b*2), point2=(0,  2*vg + b*2))
    s1.Line(point1=(0,  2*vg + b*2), point2=(0,  1*vg + b*1.5))
    s1.Line(point1=(0, vg + b*1.5), point2=(Lp/2,  1*vg + b*1.5))
    s1.Line(point1=(Lp/2, vg + b*1.5), point2=(Lp/2,  1*vg + b*.5))
    s1.Line(point1=(Lp/2, vg + b*.5), point2=(0,  1*vg + b*.5))
    s1.Line(point1=(0, vg + b*.5), point2=(0, 0))
    p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()


    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN) 
    p = mdb.models['Model-1'].parts['Platelet']
    a.Instance(name='Part-1-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Matrix']
    a.Instance(name='Part-2-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Compositee', instances=(a.instances['Part-1-1'], 
        a.instances['Part-2-1'], ), keepIntersections=ON, 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN) 
    p = mdb.models['Model-1'].parts['Platelet']
    a.Instance(name='Part-1-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Matrix']
    a.Instance(name='Part-2-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Compositee', instances=(a.instances['Part-1-1'], 
        a.instances['Part-2-1'], ), keepIntersections=ON, 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly

    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Compositee']
    a.Instance(name='Compositee-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=20.2979, 
        farPlane=28.9775, width=27.6671, height=12.5126, viewOffsetX=3.08641, 
        viewOffsetY=-1.90263)
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('Compositee-1', ), direction1=(1.0, 0.0, 
        0.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=3, 
        spacing1=lth, spacing2=wth)
    a = mdb.models['Model-1'].rootAssembly

    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='merge1', instances=(
        a.instances['Compositee-1'], a.instances['Compositee-1-lin-1-2'], ), 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='merge2', instances=(
        a.instances['Compositee-1-lin-1-3'], a.instances['merge1-1'], ), 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='merge3', instances=(
        a.instances['Compositee-1-lin-2-3'], 
        a.instances['Compositee-1-lin-2-2'], ), originalInstances=SUPPRESS, 
        domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='merge4', instances=(a.instances['merge3-1'], 
        a.instances['Compositee-1-lin-2-1'], ), originalInstances=SUPPRESS, 
        domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    del a.features['merge2-1']
    a1 = mdb.models['Model-1'].rootAssembly
    a1.LinearInstancePattern(instanceList=('merge4-1', ), direction1=(1.0, 0.0, 
        0.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=1, 
        spacing1=12.0625, spacing2=7.5)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.InstanceFromBooleanMerge(name='lower_PLATELET', instances=(
        a1.instances['merge4-1'], a1.instances['merge4-1-lin-2-1'], ), 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a1 = mdb.models['Model-1'].rootAssembly

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)

    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(6*lth, 3*lth))
    p = mdb.models['Model-1'].Part(name='CUT BOX1', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['CUT BOX1']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['CUT BOX1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)

    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=125.29, gridSpacing=3.13)

    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['CUT BOX1']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.rectangle(point1=((lth + (0.5)*hg), 0.3*wth), point2=((3*lth - (0.5)*hg) , 2.2*wth))
    p = mdb.models['Model-1'].parts['CUT BOX1']
    p.Cut(sketch=s1)
    s1.unsetPrimaryObject()

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['CUT BOX1']
    a.Instance(name='CUT BOX1-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['lower_PLATELET']
    a.Instance(name='lower_PLATELET-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='CUT lower_PLATELET', 
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['lower_PLATELET-1'], 
        cuttingInstances=(a.instances['CUT BOX1-1'], ), 
        originalInstances=SUPPRESS)
    a = mdb.models['Model-1'].rootAssembly
    a.features['lower_PLATELET-1'].suppress()

    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['CUT lower_PLATELET']
    a.Instance(name='CUT lower_PLATELET-2', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('CUT lower_PLATELET-2', ), direction1=(
        1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=1, number2=2, 
        spacing1=2*lth - hg, spacing2=1.9*wth+thih)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('CUT lower_PLATELET-2-lin-1-2', ), vector=(-(lth-(0.5*hg)+0.5*thih), 
        0.0, 0.0))
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('CUT lower_PLATELET-2-lin-1-2', ), 
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=2, 
        number2=1, spacing1= 2*lth - hg + thih, spacing2=1.9*wth+thih)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='middleplate', instances=(
        a.instances['CUT lower_PLATELET-2-lin-1-2'], 
        a.instances['CUT lower_PLATELET-2-lin-1-2-lin-2-1'], ), 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8051, 
        farPlane=85.4432, width=59.7347, height=29.9616, viewOffsetX=5.91214, 
        viewOffsetY=-3.50546)
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('CUT lower_PLATELET-2', ), direction1=(
        1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=1, number2=2, 
        spacing1=2*lth - hg, spacing2=4.2*wth)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='wholerve', instances=(
        a.instances['CUT lower_PLATELET-2-lin-1-2-1'], 
        a.instances['middleplate-1'], a.instances['CUT lower_PLATELET-2'], ), 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)

    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(-lth, 0.0), point2=(6*lth, 3*lth))
    p = mdb.models['Model-1'].Part(name='CUT BOX', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['CUT BOX']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['CUT BOX']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)

    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=125.29, gridSpacing=3.13)

    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['CUT BOX']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.rectangle(point1=((lth - (0.5)*thih + 0.5*hg), 1.25*wth), point2=((3*lth + (0.5)*thih - 0.5*hg) , 5.45*wth))
    p = mdb.models['Model-1'].parts['CUT BOX']
    p.Cut(sketch=s1)
    s1.unsetPrimaryObject()

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['CUT BOX']
    a.Instance(name='CUT BOX-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['wholerve']
    a.Instance(name='wholerve-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='CUT RVE new', 
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['wholerve-1'], 
        cuttingInstances=(a.instances['CUT BOX-1'], ), 
        originalInstances=SUPPRESS)
    a = mdb.models['Model-1'].rootAssembly
    a.features['wholerve-1'].suppress()
    a = mdb.models['Model-1'].rootAssembly
    a.features['CUT lower_PLATELET-1'].suppress()

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
            sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)

    ##point1
    s.Line(point1=(lth + 0.5*hg, 1.25*wth), point2=(lth - 0.5*thih + 0.5*hg, 1.25*wth))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)

    #point2

    s.Line(point1=(lth - 0.5*thih + 0.5*hg, 1.25*wth), point2=(lth - 0.5*thih + 0.5*hg, 2*wth + 2*thih))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)

    #point3
    s.Line(point1=(lth - 0.5*thih + 0.5*hg, 2*wth + 2*thih), point2=(2*lth + 3*hg - 0.875*thih, 2*wth + 2*thih))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)


    #point4
    s.Line(point1=(2*lth + 3*hg - 0.875*thih, 2*wth + 2*thih), point2=(2*lth + 3*hg - 0.875*thih, 3.9*wth + 2*thih)) 
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)

    #point5
    s.Line(point1=(2*lth + 3*hg - 0.875*thih, 3.9*wth + 2*thih), point2=(lth - 0.5*thih + 0.5*hg, 3.9*wth + 2*thih))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)


    #####################################

    #point6
    s.Line(point1=(lth - 0.5*thih + 0.5*hg, 3.9*wth + 2*thih), point2=(lth - 0.5*thih + 0.5*hg, 4.65*wth + 4*thih))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)

    #point7
    s.Line(point1=(lth - 0.5*thih + 0.5*hg,4.65*wth + 4*thih), point2=(lth + 0.5*hg, 4.65*wth + 4*thih))
    s.HorizontalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)

    #point8
    s.Line(point1=(lth + 0.5*hg, 4.65*wth + 4*thih), point2=(lth + 0.5*hg, 3.9*wth + 3*thih))
    s.VerticalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)

    #point9
    s.Line(point1=(lth + 0.5*hg, 3.9*wth + 3*thih), point2=(3*lth - 0.5*hg, 3.9*wth + 3*thih))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    #point10
    s.Line(point1=(3*lth - 0.5*hg, 3.9*wth + 3*thih), point2=(3*lth - 0.5*hg, 4.65*wth + 4*thih))
    s.VerticalConstraint(entity=g[11], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    #point11
    s.Line(point1=(3*lth - 0.5*hg, 4.65*wth + 4*thih), point2=(3*lth+ (0.5*thih)- 0.5*hg, 4.65*wth + 4*thih))
    s.HorizontalConstraint(entity=g[12], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
    #point12
    s.Line(point1=(3*lth+ (0.5*thih)- 0.5*hg, 4.65*wth + 4*thih), point2=(3*lth+ (0.5*thih) - 0.5*hg, 3.9*wth + 2*thih))
    s.VerticalConstraint(entity=g[13], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
    #point13
    s.Line(point1=(3*lth+ (0.5*thih)- 0.5*hg, 3.9*wth + 2*thih), point2=(2*lth+ 0.125*(thih)+ 3*hg, 3.9*wth + 2*thih))
    s.HorizontalConstraint(entity=g[14], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
    #point14
    s.Line(point1=(2*lth+ 0.125*(thih)+ 3*hg, 3.9*wth + 2*thih), point2=(2*lth+ 0.125*(thih)+ 3*hg, 2*wth + 2*thih))
    s.VerticalConstraint(entity=g[15], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
    #point15
    s.Line(point1=(2*lth+ 0.125*(thih)+ 3*hg, 2*wth + 2*thih), point2=(3*lth+ (0.5*thih)- 0.5*hg, 2*wth + 2*thih))
    s.HorizontalConstraint(entity=g[16], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
    #point16
    s.Line(point1=(3*lth+ (0.5*thih)- 0.5*hg, 2*wth + 2*thih), point2=(3*lth+ (0.5*thih)- 0.5*hg, 1.25*wth))
    s.VerticalConstraint(entity=g[17], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)
    #point17
    s.Line(point1=(3*lth+ (0.5*thih)- 0.5*hg, 1.25*wth), point2=(3*lth- 0.5*hg, 1.25*wth))
    s.HorizontalConstraint(entity=g[18], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[17], entity2=g[18], addUndoState=False)
    #point18
    s.Line(point1=(3*lth- 0.5*hg, 1.25*wth), point2=(3*lth-0.5*hg, 2*wth + thih))
    s.VerticalConstraint(entity=g[19], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[18], entity2=g[19], addUndoState=False)
    #point19
    s.Line(point1=(3*lth - 0.5*hg, 2*wth + thih), point2=(lth+0.5*hg, 2*wth + thih))
    s.HorizontalConstraint(entity=g[20], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[19], entity2=g[20], addUndoState=False)
    #point20
    s.Line(point1=(lth+0.5*hg,2*wth + thih), point2=(lth+ 0.5*hg, 1.25*wth))
    s.VerticalConstraint(entity=g[21], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[20], entity2=g[21], addUndoState=False)



    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.054, 
        farPlane=203.07, width=95.0541, height=42.9888, cameraPosition=(
        8.20676, 0.731673, 188.562), cameraTarget=(8.20676, 0.731673, 0))


    p = mdb.models['Model-1'].Part(name='MATRIX2H', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['MATRIX2H']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['MATRIX2H']






    mdb.models['Model-1'].Material(name='MATRIX MATERIAL 2H')
    mdb.models['Model-1'].materials['MATRIX MATERIAL 2H'].Elastic(table=((100.0, 
        0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='matrix2h', 
        material='MATRIX MATERIAL 2H', thickness=None)
    p = mdb.models['Model-1'].parts['MATRIX2H']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['MATRIX2H']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['MATRIX2H']
    p.SectionAssignment(region=region, sectionName='matrix2h', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

    mdb.models['Model-1'].Material(name='MATRIX MATERIAL 1H')
    mdb.models['Model-1'].materials['MATRIX MATERIAL 1H'].Elastic(table=((100.0, 
        0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='matrix1h', 
        material='MATRIX MATERIAL 1H', thickness=None)
    p = mdb.models['Model-1'].parts['CUT RVE new']
    f = p.faces
    matrix_face_point_1 = (2*lth, 1.75*wth,0.0)
    matrix_face_point_2 = (2*lth, 4.95*wth,0.0)
    matrix_face_point_3 = (2.5181*lth, 3.5*wth,0.0)
    matrix_face_point_4 = (1.4818*lth,3.5*wth,0.0)
    matrix_face_1 = p.faces.findAt((matrix_face_point_1,))
    matrix_face_2 = p.faces.findAt((matrix_face_point_2,))
    matrix_face_3 = p.faces.findAt((matrix_face_point_3,))
    matrix_face_4 = p.faces.findAt((matrix_face_point_4,))
    matrix_region=(matrix_face_1,matrix_face_2,matrix_face_3,matrix_face_4,)
    p = mdb.models['Model-1'].parts['CUT RVE new']
    p.SectionAssignment(region=matrix_region, sectionName='matrix1h', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].Material(name='Platelet material')
    mdb.models['Model-1'].materials['Platelet material'].Elastic(table=((1000.0, 
        0.2), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='platelet 1h', 
        material='Platelet material', thickness=None)

    p = mdb.models['Model-1'].parts['CUT RVE new']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    platelet_face_point_1 = (1.25*lth,1.5*wth,0.0)
    platelet_face_point_2 = ((2*lth),(1.5*wth),0.0)
    platelet_face_point_3 = ((2.75*lth),(1.5*wth),0.0)
    platelet_face_point_4 = (1.5*lth,2*wth,0.0)
    platelet_face_point_5 = (2.5*lth,2*wth,0.0)

    platelet_face_point_6 = ((1.23056*lth),(2.6*wth),0.0)
    platelet_face_point_7 = ((1.7318*lth),(2.6*wth),0.0)
    platelet_face_point_8 = (1.4818*lth,3.1*wth,0.0)
    platelet_face_point_9 = ((1.23056*lth),3.6*wth,0.0)
    platelet_face_point_10 = ((1.7318*lth),(3.6*wth),0.0)
    platelet_face_point_11 = (1.4818*lth,4.1*wth,0.0)

    platelet_face_point_12 = ((2.2681*lth),(2.6*wth),0.0)
    platelet_face_point_13 = ((2.7694*lth),(2.6*wth),0.0)
    platelet_face_point_14 = (2.5181*lth,3.1*wth,0.0)
    platelet_face_point_15 = ((2.2681*lth),3.6*wth,0.0)
    platelet_face_point_16 = ((2.7694*lth),(3.6*wth),0.0)
    platelet_face_point_17 = (2.5181*lth,4.1*wth,0.0)

    platelet_face_point_18 = ((1.25*lth),(4.7*wth),0.0)
    platelet_face_point_19 = ((2*lth),(4.7*wth),0.0)
    platelet_face_point_20 = (2.75*lth,4.7*wth,0.0)
    platelet_face_point_21 = ((1.5*lth),5.2*wth,0.0)
    platelet_face_point_22 = ((2.5*lth),(5.2*wth),0.0)


    platelet_face_1 = p.faces.findAt((platelet_face_point_1,))
    platelet_face_2 = p.faces.findAt((platelet_face_point_2,))
    platelet_face_3 = p.faces.findAt((platelet_face_point_3,))
    platelet_face_4 = p.faces.findAt((platelet_face_point_4,))

    platelet_face_5 = p.faces.findAt((platelet_face_point_5,))
    platelet_face_6 = p.faces.findAt((platelet_face_point_6,))
    platelet_face_7 = p.faces.findAt((platelet_face_point_7,))
    platelet_face_8 = p.faces.findAt((platelet_face_point_8,))

    platelet_face_9 = p.faces.findAt((platelet_face_point_9,))
    platelet_face_10 = p.faces.findAt((platelet_face_point_10,))
    platelet_face_11 = p.faces.findAt((platelet_face_point_11,))
    platelet_face_12 = p.faces.findAt((platelet_face_point_12,))

    platelet_face_13 = p.faces.findAt((platelet_face_point_13,))
    platelet_face_14 = p.faces.findAt((platelet_face_point_14,))
    platelet_face_15 = p.faces.findAt((platelet_face_point_15,))
    platelet_face_16 = p.faces.findAt((platelet_face_point_16,))

    platelet_face_17 = p.faces.findAt((platelet_face_point_17,))
    platelet_face_18 = p.faces.findAt((platelet_face_point_18,))
    platelet_face_19 = p.faces.findAt((platelet_face_point_19,))
    platelet_face_20 = p.faces.findAt((platelet_face_point_20,))
    platelet_face_21 = p.faces.findAt((platelet_face_point_21,))
    platelet_face_22 = p.faces.findAt((platelet_face_point_22,))


    platelet_region=(platelet_face_1, platelet_face_2, platelet_face_3, platelet_face_4,platelet_face_5, platelet_face_6, 
        platelet_face_7, platelet_face_8,platelet_face_9, platelet_face_10, platelet_face_11, platelet_face_12,
        platelet_face_13, platelet_face_14, platelet_face_15, platelet_face_16,platelet_face_17, platelet_face_18, platelet_face_19, platelet_face_20,
        platelet_face_21, platelet_face_22,)
    p = mdb.models['Model-1'].parts['CUT RVE new']
    p.SectionAssignment(region=platelet_region, sectionName='platelet 1h', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

    p1 = mdb.models['Model-1'].parts['CUT RVE new']


    session.viewports['Viewport: 1'].setValues(displayedObject=p)

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['CUT RVE new']
    a.Instance(name='CUT RVE new-2', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['MATRIX2H']
    a.Instance(name='MATRIX2H-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Part-4', instances=(
        a.instances['CUT RVE new-2'], a.instances['MATRIX2H-1'], ), 
        keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)
    a = mdb.models['Model-1'].rootAssembly
    a.features['wholerve-1'].suppress()
    a.features['CUT RVE new-1'].suppress()
    a.features['Compositee-2'].suppress()

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=2000.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s1=a11-65.5
    s2=a11+65.5
    s3=a12-27.5
    s4=a12+27.5
    s.rectangle(point1=(s1,s3), point2=(s2,s4))
    #s.rectangle(point1=(s1,s3), point2=(s2,s4))
    s.CircleByCenterPerimeter(center=(a11,a12), point1=(a11+rad,a12))
    p = mdb.models['Model-1'].Part(name='Part-3', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-3']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()

    for i in range(0,144):
        p1 = mdb.models['Model-1'].parts['Part-4']
        session.viewports['Viewport: 1'].setValues(displayedObject=p1)
        p = mdb.models['Model-1'].Part(name='rve'+repr(i), 
            objectToCopy=mdb.models['Model-1'].parts['Part-4'])
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        p = mdb.models['Model-1'].parts['rve'+repr(i)]
        a = mdb.models['Model-1'].rootAssembly
        a.Instance(name='rve'+repr(i)+'-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a.features['Part-4-1'].suppress()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    dis1=ltp+thth+thth
    dis2=0.0
    b1=0
    for j in range(1,13):
        for i in range(0,12):
            a1 = mdb.models['Model-1'].rootAssembly
            a1.translate(instanceList=('rve'+repr(b1)+'-1', ), vector=(i*dis1, dis2, 0.0))
            b1=b1+1
        dis2=j*(wtp+wtp+thih+thih)   
    session.viewports['Viewport: 1'].view.fitView()
    a = mdb.models['Model-1'].rootAssembly
    q=[0]*len(range(0,144))
    for i in range(0,144):
        q[i]=a.instances['rve'+repr(i)+'-1']
    a.InstanceFromBooleanMerge(name='Part-5', instances=q, 
        originalInstances=SUPPRESS, domain=GEOMETRY)
    a.makeIndependent(instances=(a.instances['Part-5-1'], ))
    p = mdb.models['Model-1'].parts['Part-5']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)

    p = mdb.models['Model-1'].parts['Part-3']
    a.Instance(name='Part-3-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Part-5']
    a.Instance(name='Part-5-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='Part-6',
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-5-1'],
        cuttingInstances=(a.instances['Part-3-1'], ), originalInstances=DELETE)
    p1 = mdb.models['Model-1'].parts['Part-6']
    a.makeIndependent(instances=(a.instances['Part-6-1'], ))
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-5']
    a1.Instance(name='Part-5-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Part-6']
    a1.Instance(name='Part-6-1', part=p, dependent=OFF)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.InstanceFromBooleanCut(name='Part-7', 
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-5-1'], 
        cuttingInstances=(a1.instances['Part-6-1'], ), originalInstances=DELETE)
    a.makeIndependent(instances=(a.instances['Part-7-1'], ))
    p1 = mdb.models['Model-1'].parts['Part-7']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    
   


    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=2000.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s8=a11
    s9=a12
    s6=a11+65.5
    s7=a12+27.5
    s.rectangle(point1=(s8,s9), point2=(s6,s7))
    #s.ArcByCenterEnds(center=(a11, a12), point1=(a11, a12 + rad), point2=(a11+rad, a12), direction=CLOCKWISE)
    p = mdb.models['Model-1'].Part(name='Part-9', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-9']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=2000.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ArcByCenterEnds(center=(a11, a12), point1=(a11, a12 + rad), point2=(a11+rad, a12), direction=CLOCKWISE)
    s.Line(point1=(a11, a12), point2=(a11, a12 + rad))
    s.Line(point1=(a11, a12), point2= (a11+rad, a12))
    p = mdb.models['Model-1'].Part(name='Part-8', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-8']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()

    p = mdb.models['Model-1'].parts['Part-8']
    a.Instance(name='Part-8-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Part-9']
    a.Instance(name='Part-9-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='Part-10',
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-9-1'],
    cuttingInstances=(a.instances['Part-8-1'], ), originalInstances=DELETE)
    p1 = mdb.models['Model-1'].parts['Part-10']
    a.makeIndependent(instances=(a.instances['Part-10-1'], ))
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)

    p = mdb.models['Model-1'].parts['Part-10']
    a.Instance(name='Part-10-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Part-7']
    a.Instance(name='Part-7-1', part=p, dependent=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='Part-11',
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-7-1'],
    cuttingInstances=(a.instances['Part-10-1'], ), originalInstances=DELETE)
    p1 = mdb.models['Model-1'].parts['Part-11']
    a.makeIndependent(instances=(a.instances['Part-11-1'], ))
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-7']
    a1.Instance(name='Part-7-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['Part-11']
    a1.Instance(name='Part-11-1', part=p, dependent=OFF)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.InstanceFromBooleanCut(name='Part-12', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-7-1'], 
    cuttingInstances=(a1.instances['Part-11-1'], ), originalInstances=DELETE)
    a.makeIndependent(instances=(a.instances['Part-12-1'], ))
    p1 = mdb.models['Model-1'].parts['Part-12']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)

    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    timePeriod=0.1, initialInc=0.1, minInc=1e-06, maxInc=0.1)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')

    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)

    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U','UT','UR', 'RF', 'CF', 'CSTRESS', 'CDISP', 
    'COORD'))


    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    f1 = a.instances['Part-12-1'].faces
    t = a.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    0, 0, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=2000.0, gridSpacing=5.00, transform=t)
    s.setPrimaryObject(option=SUPERIMPOSE)
    a = mdb.models['Model-1'].rootAssembly
    a.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.rectangle(point1=(a11-4*rad, a12-4*rad), point2=(a11+4*rad, a12+4*rad))
    s.rectangle(point1=(a11-8*rad, a12-8*rad), point2=(a11+8*rad, a12+8*rad))
    s.rectangle(point1=(s8+.5, s9+.5), point2=(s6-.5,s7-.5 ))
    #s.rectangle(point1=(a11-3*rad, a12-3*rad), point2=(a11+3*rad, a12+3*rad))
    s.rectangle(point1=(a11-2*rad, a12-2*rad), point2=(a11+2*rad, a12+2*rad))
    #s.Line(point1=(a11, a12-20), point2=(a11, a12 + 20))
    a.PartitionFaceBySketch(faces=f1, sketch=s)
    s.unsetPrimaryObject()



    #a = mdb.models['Model-1'].rootAssembly
    #e1 = a.instances['Part-12-1'].edges
    #bon = e1.getByBoundingBox(s8, s9, 0.0, s8, s7, 0.0)+e1.getByBoundingBox(s6, s9, 0.0, s6, s7, 0.0) \
    #+e1.getByBoundingBox(s8, s7, 0.0, s6, s7, 0.0)+e1.getByBoundingBox(s8, s9, 0.0, s6, s9, 0.0) \
    #+e1.getByBoundingBox(s8+.5, s9+.5, 0.0, s8+.5, s7-.5, 0.0)+e1.getByBoundingBox(s6-.5, s9+.5, 0.0, s6-.5, s7-.5, 0.0)\
    #+e1.getByBoundingBox(s8+.5, s7-.5, 0.0, s6-.5, s7-.5, 0.0)+e1.getByBoundingBox(s8+.5, s9+.5, 0.0, s6-.5, s9+.5, 0.0)

    #a.Set(edges=bon, name='boundaries')


    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-12-1'].faces
    e1 = a.instances['Part-12-1'].edges
    Face=f1.getByBoundingBox(s8, s9, 0.0, s6, s7, 0.0)
    a.Set(faces=Face, name='cut6')
    region=a.sets['cut6']
    a = mdb.models['Model-1'].rootAssembly.sets['cut6'].faces  
    mg = mdb.models['Model-1'].rootAssembly.sets['cut6']
    elemType1 = mesh.ElemType(elemCode=CPE4,elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    a.setElementType(regions=mg, elemTypes=(elemType1,))

    #face1 = f1.getByBoundingBox(a11-4*rad, a12-4*rad, 0.0, a11+4*rad, a12+4*rad, 0.0)
    #a.Set(faces=face1, name='reqreg')
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-12-1'].faces
    e1 = a.instances['Part-12-1'].edges
    Face=f1.getByBoundingBox(a11-4*rad, a12-4*rad, 0.0, a11+4*rad, a12+4*rad, 0.0)
    a.Set(faces=Face, name='cut66')
    region=a.sets['cut66']
    a = mdb.models['Model-1'].rootAssembly.sets['cut66'].faces  
    mg = mdb.models['Model-1'].rootAssembly.sets['cut66']
    elemType1 = mesh.ElemType(elemCode=CPE4,elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    a.setElementType(regions=mg, elemTypes=(elemType1,))

    remesh3 = e1.getByBoundingSphere((a11, a12, 0.0) , 1.01*rad)
    a.Set(edges=remesh3, name='circle')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-12-1'].edges

    remesh2 = e1.getByBoundingBox(a11-2*rad, a12-2*rad, 0.0, a11+2*rad, a12+2*rad, 0.0)
    a.Set(edges=remesh2, name='smallbox')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-12-1'].edges

    remesh1 = e1.getByBoundingBox(a11-4*rad, a12-4*rad, 0.0, a11+4*rad, a12+4*rad, 0.0)
    a.Set(edges=remesh1, name='bigbox')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-12-1'].edges

    remesh4 = e1.getByBoundingBox(a11-8*rad, a12-8*rad, 0.0, a11+8*rad, a12 + 8*rad, 0.0)
    a.Set(edges=remesh4, name='largebox')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-12-1'].edges

    #a.seedEdgeBySize(edges=bon, size=0.05, deviationFactor=0.1, 
    #constraint=FINER)
    a.seedEdgeBySize(edges=remesh1, size=0.15, deviationFactor=0.1, 
    constraint=FINER)
    a.seedEdgeBySize(edges=remesh2, size= 0.035, deviationFactor=0.1, 
    constraint=FINER)
    a.seedEdgeBySize(edges=remesh3, size= 0.035, deviationFactor=0.1, 
    constraint=FINER)
    a.seedEdgeBySize(edges=remesh4, size= 0.25, deviationFactor=0.1, 
    constraint=FINER)



    a = mdb.models['Model-1'].rootAssembly  
    partInstances =(a.instances['Part-12-1'], ) 
    a.seedPartInstance(regions=partInstances, size=0.3, deviationFactor=0.1, 
    minSizeFactor=0.1)



    a.generateMesh(regions=partInstances)

    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-12-1'].edges



    be = e1.getByBoundingBox(s8, s9, 0.0, s6, s9, 0.0)
    te = e1.getByBoundingBox(s8, s7, 0.0, s6, s7, 0.0)
    le = e1.getByBoundingBox(s8, s9, 0.0, s8, s7, 0.0)
    re = e1.getByBoundingBox(s6, s9, 0.0, s6, s7, 0.0)
    a.Set(edges=be, name='be')
    a.Set(edges=te, name='te')
    a.Set(edges=le, name='le')
    a.Set(edges=re, name='re')
    a2 = mdb.models['Model-1'].rootAssembly

    # region = a2.sets['te']
    # mdb.models['Model-1'].DisplacementBC(name='TE', createStepName='Step-1', 
    # region=region, u1=-0.1*50*flag, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    # distributionType=UNIFORM, fieldName='', localCsys=None)
    # region = a2.sets['le']
    # mdb.models['Model-1'].DisplacementBC(name='LE', createStepName='Step-1', 
    # region=region, u1=-0.015, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    # distributionType=UNIFORM, fieldName='', localCsys=None)
    region = a2.sets['re']
    mdb.models['Model-1'].DisplacementBC(name='RE', createStepName='Step-1', 
    region=region, u1=0.015, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)

    region = a2.sets['be'] 
    mdb.models['Model-1'].YsymmBC(name='BC-1', createStepName='Initial', region=region, localCsys=None)
    # a = mdb.models['Model-1'].rootAssembly
    # e1 = a.instances['Part-1-1'].edges

    region = a2.sets['le']
    mdb.models['Model-1'].XsymmBC(name='BC-2', createStepName='Initial', region=region, localCsys=None)


    # region = a.sets['re']
    # mdb.models['Model-1'].XsymmBC(name='RE', createStepName='Step-1', 
    # region=region, localCsys=None)


    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)

    #   # mdb.Job(name='Jobinput', model='Model-10', description='', type=ANALYSIS, 
    #   #     atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    #   #     memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    #   #     explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    #   #     modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    #   #     scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
    #   # mdb.jobs['Jobinput'].writeInput(consistencyChecking=OFF)



    mdb.Job(name='tD', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=4,numDomains=4 , numGPUs=0)
    mdb.jobs['tD'].submit(consistencyChecking=OFF)

    mdb.jobs['tD'].waitForCompletion()


    job_name='tD'


    sta=mdb.jobs[job_name].status
    st=str(sta)



    odbPath='E:\\9.5D\\'+job_name+'.odb'                   ##Path
    odb=session.openOdb(odbPath)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=0)
    lastFrame=odb.steps['Step-1'].frames[-1]
    disp=lastFrame.fieldOutputs['U']                      ##S-stress ##U-displacement
    reg=odb.rootAssembly.nodeSets['CUT66']                 ##Set name in capital ##only working for element sets  
    asd=disp.getSubset(region=reg,position=NODAL)
    locxo=s1
    locyo=s3
    for do in asd.values:   
        ff=do.nodeLabel
        u1r = do.data[0]
        u2r = do.data[1] 
        u1.append(u1r)
        u2.append(u2r)  



    pos=lastFrame.fieldOutputs['COORD']                      ##S-stress ##U-displacement
    reg=odb.rootAssembly.nodeSets['CUT66']                 ##Set name in capital ##only working for element and node sets  
    asp=pos.getSubset(region=reg,position=NODAL)
    for do in asp.values:   
        ff=do.nodeLabel
        xxr = do.data[0] 
        yyr = do.data[1] 
        locxo=s1
        locyo=s3
        xr=xxr-locxo
        yr=yyr-locyo 
        xx.append(xr)
        yy.append(yr)





    numpy.savetxt('rbtx'+repr(flag)+'.txt',xx,fmt='%f')
    numpy.savetxt('rbty'+repr(flag)+'.txt',yy,fmt='%f')
    numpy.savetxt('rbtu1'+repr(flag)+'.txt',u1,fmt='%f')
    numpy.savetxt('rbtu2'+repr(flag)+'.txt',u2,fmt='%f')
    print(st)



    # #     # if st =='COMPLETED':
    # #     #   tim=0
    # #     #   ok=1
    # #     #   os.remove('Job.inp')

    # #     # else:
    # #     #   sys.exc_clear()
    # #     #   tim=1
    # #     #   os.remove(job_name+'.lck')
    # #     # #     k=k+1
    # #     #   os.remove('Job.inp')

    # #     # if ok==1:

    #odb = session.odbs['E:\10D\\Ar20\\'+job_name+'.odb']


    # #                   ####To store number of elements
    # #     ##To get fieldoutputs(stress,diplacement etc..) without writing xydata


    # # session.Path(name='Path-2', type=POINT_LIST, expression=((a11 , a12-4*rad, 0.0), (
    # #     a11 , a12-rad, 0.0)))
    # # session.Path(name='Path-1', type=POINT_LIST, expression=((a11, a12+rad, 0.0), (
    # #     a11 , a12+4*rad, 0.0)))
    # # # session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    # # #   variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    # # #   'E22'))
    # # # pth = session.paths['Path-1']



    # # # session.XYDataFromPath(name='XYData-1', path=pth, includeIntersections=True, 
    # # #    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, labelType=TRUE_DISTANCE)
    # # # #     x0 = session.xyDataObjects['XYData-1']


    # # #   total=0
    # # #   for i in range(0,(len(x0)-1)):
    # # #       a1=list(x0[i])
    # # #       a2=list(x0[i+1])
    # # #       c=.5*(a2[0]-a1[0])*(a1[1]+a2[1])
    # # #       total=c+total
    # # #   nom_stress = total/(a2[0]-di)

    # # #   ns.append(nom_stress)
    # # #   scf.append(maxi_s11/nom_stress)

    # # #   save('AR20')
    flag+=1