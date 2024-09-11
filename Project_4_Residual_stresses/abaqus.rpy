# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-23.19.31 163176
# Run by Mohd Babar Malik on Wed Sep 11 11:07:30 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=107.20442199707, 
    height=107.326393127441)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Residual_Stresses.cae')
#: The model database "C:\Abaqus Projects\Project_4_Residual_stresses\Residual_Stresses.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=806.333, 
    farPlane=1505.53, width=538.949, height=242.591, cameraPosition=(97.9294, 
    397.736, 1331.18), cameraUpVector=(-0.550561, 0.628198, -0.549772), 
    cameraTarget=(-6.78639, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=805.83, 
    farPlane=1509.05, width=538.613, height=242.439, cameraPosition=(84.3939, 
    327.852, 1357.06), cameraUpVector=(-0.59498, 0.629487, -0.499745), 
    cameraTarget=(-6.7864, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=753.899, 
    farPlane=1324.56, width=222.829, height=100.299, cameraPosition=(-29.7497, 
    437.251, 1192.3), cameraUpVector=(0.0771278, 0.905324, -0.417659))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=807.968, 
    farPlane=1511.48, width=540.043, height=243.083, cameraPosition=(40.0544, 
    220.91, 1387.98), cameraUpVector=(-0.155671, 0.844115, -0.513065), 
    cameraTarget=(-6.78638, -15.2111, 271.998))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=(
    '[#0:7 #fc000000 #ffffffff:15 #3fff ]', ), )
a.Set(elements=elements1, name='Set-Centre')
#: The set 'Set-Centre' has been edited (500 elements).
session.viewports['Viewport: 1'].view.setValues(nearPlane=818.07, 
    farPlane=1497.06, width=546.795, height=246.122, cameraPosition=(11.3407, 
    356.378, 1351.48), cameraUpVector=(-0.121845, 0.777961, -0.616385), 
    cameraTarget=(-7.234, -13.0993, 271.429))
session.viewports['Viewport: 1'].view.setValues(nearPlane=815.758, 
    farPlane=1503.22, width=545.249, height=245.426, cameraPosition=(71.1252, 
    221.866, 1386.03), cameraUpVector=(-0.114122, 0.849985, -0.514297), 
    cameraTarget=(-6.41201, -14.9487, 271.904))
session.viewports['Viewport: 1'].view.setValues(nearPlane=815.4, 
    farPlane=1503.56, width=545.01, height=245.318, cameraPosition=(-179.958, 
    316.843, 1350.93), cameraUpVector=(0.0784113, 0.805938, -0.586784), 
    cameraTarget=(-10.2751, -13.4874, 271.364))
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=745.37, 
    farPlane=1333.09, width=220.308, height=99.1648, cameraPosition=(-113.361, 
    300.281, 1238.42), cameraUpVector=(0.469476, 0.858356, -0.206923))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=808.567, 
    farPlane=1509.93, width=540.443, height=243.263, cameraPosition=(-35.5415, 
    273.342, 1376.2), cameraUpVector=(-0.0499529, 0.825806, -0.561738), 
    cameraTarget=(-6.78638, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=807.91, 
    farPlane=1512.86, width=540.004, height=243.065, cameraPosition=(-75.7846, 
    221.358, 1386.73), cameraUpVector=(-0.604798, 0.612629, -0.508828), 
    cameraTarget=(-6.78637, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=809.096, 
    farPlane=1507.46, width=540.797, height=243.422, cameraPosition=(-19.5028, 
    320.177, 1363.2), cameraUpVector=(0.0222428, 0.803163, -0.595344), 
    cameraTarget=(-6.78636, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=891.761, 
    farPlane=1448.5, width=596.05, height=268.293, cameraPosition=(-935.018, 
    -194.418, 926.381), cameraUpVector=(0.33755, 0.931744, 0.133843), 
    cameraTarget=(-19.9331, -22.6007, 265.725))
session.viewports['Viewport: 1'].view.setValues(nearPlane=824.311, 
    farPlane=1517.22, width=550.967, height=248, cameraPosition=(-91.0105, 
    -25.7335, -917.087), cameraUpVector=(-0.419808, 0.831892, 0.362929), 
    cameraTarget=(0.608337, -18.4953, 220.859))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=808.833, 
    farPlane=1507.52, width=540.62, height=243.343, cameraPosition=(-28.2547, 
    328.109, 1360.59), cameraUpVector=(0.114273, 0.7936, -0.597612), 
    cameraTarget=(-6.78636, -15.2111, 271.998))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=(
    '[#0:23 #ffffc000 #ffffffff:2 #efffffff #ffffffff:4 #ff ]', ), )
a.Set(elements=elements1, name='Set-Left')
#: The set 'Set-Left' has been edited (249 elements).
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=936.24, 
    farPlane=1360.18, width=625.779, height=281.674, cameraPosition=(414.829, 
    -1047.86, 28.6281), cameraUpVector=(-0.819048, -0.0990691, 0.565107), 
    cameraTarget=(-6.78646, -15.2109, 271.998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=789.714, 
    farPlane=1474.31, width=527.842, height=237.591, cameraPosition=(80.5897, 
    -586.834, -714.906), cameraUpVector=(-0.565116, -0.5205, 0.640097), 
    cameraTarget=(-8.69696, -12.5757, 267.748))
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=809.945, 
    farPlane=1503.43, width=541.364, height=243.678, cameraPosition=(-24.178, 
    400.871, 1334.98), cameraUpVector=(0.459572, 0.650212, -0.604994), 
    cameraTarget=(-6.78636, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=812.477, 
    farPlane=1493.45, width=543.056, height=244.439, cameraPosition=(70.0586, 
    539.684, 1266.76), cameraUpVector=(-0.0981108, 0.661174, -0.74379), 
    cameraTarget=(-6.78639, -15.2112, 271.998))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#ffffffff:7 #3ffffff ]', ), )
a.Set(elements=elements1, name='Set-Right')
#: The set 'Set-Right' has been edited (250 elements).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Left']
mdb.models['Model-1'].Stress(name='PS_Left', region=region, 
    distributionType=UNIFORM, sigma11=0.0, sigma22=0.0, sigma33=100.0, 
    sigma12=0.0, sigma13=0.0, sigma23=0.0)
mdb.models['Model-1'].PredefinedField(name='PS_Right', 
    objectToCopy=mdb.models['Model-1'].predefinedFields['PS_Left'], 
    toStepName='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Right']
mdb.models['Model-1'].predefinedFields['PS_Right'].setValues(region=region, 
    sigma11=0.0, sigma22=0.0, sigma33=100.0, sigma12=0.0, sigma13=0.0, 
    sigma23=0.0)
mdb.models['Model-1'].PredefinedField(name='PS_Center', 
    objectToCopy=mdb.models['Model-1'].predefinedFields['PS_Right'], 
    toStepName='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Centre']
mdb.models['Model-1'].predefinedFields['PS_Center'].setValues(region=region, 
    sigma11=0.0, sigma22=0.0, sigma33=-100.0, sigma12=0.0, sigma13=0.0, 
    sigma23=0.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
import os
os.chdir(r"C:\temp\Project_4_Residual_Stresses")
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=817.37, 
    farPlane=1495.84, width=546.326, height=245.911, cameraPosition=(-103.012, 
    430.787, 1318.72), cameraUpVector=(0.0257616, 0.736376, -0.676082), 
    cameraTarget=(-8.48525, -16.2801, 272.508))
session.viewports['Viewport: 1'].view.setValues(nearPlane=818.334, 
    farPlane=1498.48, width=546.97, height=246.201, cameraPosition=(4.23581, 
    319.405, 1363.77), cameraUpVector=(-0.0501817, 0.801352, -0.596085), 
    cameraTarget=(-7.09864, -17.7202, 273.09))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
del mdb.models['Model-1'].rootAssembly.sets['Set-Centre']
del mdb.models['Model-1'].rootAssembly.sets['Set-Left']
del mdb.models['Model-1'].rootAssembly.sets['Set-Right']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#0:23 #7c000 #0:3 #f800 ]', ), )
a.Set(elements=elements1, name='Set-Left')
#: The set 'Set-Left' has been created (10 elements).
a=mdb.models['Model-1'].rootAssembly
a.Set(name='Set-Right', objectToCopy=a.sets['Set-Left'])
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#1f #0:2 #e0000000 #3 ]', ), )
a.Set(elements=elements1, name='Set-Right')
#: The set 'Set-Right' has been edited (10 elements).
mdb.models['Model-1'].rootAssembly.deleteSets(setNames=('Set-Left', 
    'Set-Right', ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=933.709, 
    farPlane=1327.79, width=624.087, height=280.913, cameraPosition=(942.285, 
    600.572, 425.077), cameraUpVector=(-0.765018, 0.611391, -0.202358), 
    cameraTarget=(-6.78654, -15.2112, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=806.57, 
    farPlane=1510.1, width=539.108, height=242.662, cameraPosition=(-122.339, 
    342.784, 1349.89), cameraUpVector=(-0.0906524, 0.778333, -0.621273), 
    cameraTarget=(-6.78636, -15.2111, 271.998))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#0:23 #ffffc000 #ffffffff:7 #ff ]', 
    ), )
a.Set(elements=elements1, name='Set-Left')
#: The set 'Set-Left' has been created (250 elements).
a=mdb.models['Model-1'].rootAssembly
a.Set(name='Set-Right', objectToCopy=a.sets['Set-Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=832.517, 
    farPlane=1502.21, width=556.451, height=250.468, cameraPosition=(132.188, 
    -645.91, 1213.41), cameraUpVector=(-0.451673, 0.859736, 0.238424), 
    cameraTarget=(-6.7864, -15.2109, 271.998))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#ffffffff:7 #3ffffff ]', ), )
a.Set(elements=elements1, name='Set-Right')
#: The set 'Set-Right' has been edited (250 elements).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=806.652, 
    farPlane=1509.7, width=539.162, height=242.687, cameraPosition=(58.676, 
    299.471, 1367.47), cameraUpVector=(0.410071, 0.707796, -0.575211), 
    cameraTarget=(-6.78639, -15.2111, 271.998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=822.181, 
    farPlane=1487.51, width=549.543, height=247.359, cameraPosition=(-56.9317, 
    513.728, 1282.95), cameraUpVector=(0.366258, 0.629336, -0.685413), 
    cameraTarget=(-8.43602, -12.1538, 270.792))
a=mdb.models['Model-1'].rootAssembly
a.Set(name='Set-Center', objectToCopy=a.sets['Set-Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=812.865, 
    farPlane=1494.22, width=543.316, height=244.556, cameraPosition=(39.0093, 
    524.828, 1276.8), cameraUpVector=(-0.310875, 0.635939, -0.706356), 
    cameraTarget=(-6.78638, -15.2112, 271.998))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=(
    '[#0:7 #fc000000 #ffffffff:15 #3fff ]', ), )
a.Set(elements=elements1, name='Set-Center')
#: The set 'Set-Center' has been edited (500 elements).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
del mdb.models['Model-1'].predefinedFields['PS_Center']
del mdb.models['Model-1'].predefinedFields['PS_Left']
del mdb.models['Model-1'].predefinedFields['PS_Right']
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Left']
mdb.models['Model-1'].Stress(name='RS_Left', region=region, 
    distributionType=UNIFORM, sigma11=0.0, sigma22=0.0, sigma33=100.0, 
    sigma12=0.0, sigma13=0.0, sigma23=0.0)
mdb.models['Model-1'].PredefinedField(name='RS_Right', 
    objectToCopy=mdb.models['Model-1'].predefinedFields['RS_Left'], 
    toStepName='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Right']
mdb.models['Model-1'].predefinedFields['RS_Right'].setValues(region=region, 
    sigma11=0.0, sigma22=0.0, sigma33=100.0, sigma12=0.0, sigma13=0.0, 
    sigma23=0.0)
mdb.models['Model-1'].PredefinedField(name='RS_Center', 
    objectToCopy=mdb.models['Model-1'].predefinedFields['RS_Right'], 
    toStepName='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['Set-Center']
mdb.models['Model-1'].predefinedFields['RS_Center'].setValues(region=region, 
    sigma11=0.0, sigma22=0.0, sigma33=-100.0, sigma12=0.0, sigma13=0.0, 
    sigma23=0.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
del mdb.jobs['Job-1']
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4, 
    numDomains=4, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET5 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Error in job Job-1: NODE SET ASSEMBLY__PICKEDSET5 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Model-1'].boundaryConditions['BC-Fixed']
a = mdb.models['Model-1'].rootAssembly
del a.features['Fixed']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=764.208, 
    farPlane=1465.88, width=512.402, height=229.917, cameraPosition=(341.1, 
    340.019, -755.692), cameraUpVector=(-0.928102, 0.33098, 0.170527))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
region = a.Set(faces=faces1, name='Set-4')
mdb.models['Model-1'].EncastreBC(name='BC-Fixed', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(name='C:/temp/Project_4_Residual_Stresses/Job-1.odb')
#: Model: C:/temp/Project_4_Residual_Stresses/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=838.889, 
    farPlane=1444.27, width=677.206, height=303.865, viewOffsetX=-24.1346, 
    viewOffsetY=0.220125)
mdb.save()
#: The model database has been saved to "C:\Abaqus Projects\Project_4_Residual_stresses\Residual_Stresses.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=832.999, 
    farPlane=1450.16, width=715.373, height=320.991, viewOffsetX=-17.4965, 
    viewOffsetY=-0.0343914)
session.viewports['Viewport: 1'].view.setValues(nearPlane=810.94, 
    farPlane=1488.23, width=696.428, height=312.491, cameraPosition=(593.45, 
    524.685, 1083.64), cameraUpVector=(-0.513789, 0.670428, -0.535301), 
    cameraTarget=(-5.22869, -13.0719, 273.852), viewOffsetX=-17.0331, 
    viewOffsetY=-0.0334807)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=844.963, 
    farPlane=1439.59, width=566.719, height=254.289, viewOffsetX=57.8284, 
    viewOffsetY=-26.2751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=835.646, 
    farPlane=1448.91, width=671.819, height=301.448, viewOffsetX=60.1352, 
    viewOffsetY=-34.6309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=834.827, 
    farPlane=1449.73, width=671.161, height=301.153, viewOffsetX=85.8902, 
    viewOffsetY=-20.3568)
session.viewports['Viewport: 1'].view.setValues(nearPlane=830.856, 
    farPlane=1453.7, width=702.609, height=315.264, viewOffsetX=86.9499, 
    viewOffsetY=-23.0502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=830.011, 
    farPlane=1454.55, width=701.894, height=314.943, viewOffsetX=96.7783, 
    viewOffsetY=-33.5064)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(85, 95))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(65, 95))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(50, 95))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(60, 95))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(60, 90))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports[session.currentViewportName].animationController.stop()
session.viewports[session.currentViewportName].animationController.showFrame(
    frame=10)
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.decrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.incrementFrame()
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=100)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=10)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
mdb.save()
#: The model database has been saved to "C:\Abaqus Projects\Project_4_Residual_stresses\Residual_Stresses.cae".
