# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-23.19.31 163176
# Run by Mohd Babar Malik on Wed Sep 11 09:51:29 2024
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
openMdb('GI.cae')
#: The model database "C:\Abaqus Projects\Project_3_Geometric_Imperfection\GI.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-Main'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
import os
os.chdir(r"C:\temp\Geometric Imperfection")
mdb.Model(name='Model-Bukling', objectToCopy=mdb.models['Model-Main'])
#: The model "Model-Bukling" has been created.
p = mdb.models['Model-Bukling'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-Bukling'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-Bukling', model='Model-Bukling', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-Bukling'].submit(consistencyChecking=OFF)
#: The job input file "Job-Bukling.inp" has been submitted for analysis.
#: Job Job-Bukling: Analysis Input File Processor completed successfully.
#: Job Job-Bukling: Abaqus/Standard completed successfully.
#: Job Job-Bukling completed successfully. 
del mdb.jobs['Job-Bulkig']
o3 = session.openOdb(name='C:/temp/Geometric Imperfection/Job-Bukling.odb')
#: Model: C:/temp/Geometric Imperfection/Job-Bukling.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          9
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3177.52, 
    farPlane=5666.75, width=2761.75, height=1178.44, viewOffsetX=92.1346, 
    viewOffsetY=62.2029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3176.47, 
    farPlane=5667.79, width=2760.84, height=1178.05, viewOffsetX=228.629, 
    viewOffsetY=-193.822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3176.45, 
    farPlane=5667.81, width=2760.83, height=1178.05, viewOffsetX=319.644, 
    viewOffsetY=-133.074)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=50)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
p = mdb.models['Model-Bukling'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-Main'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-Main'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
del mdb.models['Model-Main'].steps['Step-Buklig']
mdb.models['Model-Main'].StaticStep(name='Loading-Step', previous='Initial', 
    maxNumInc=100000, initialInc=0.1, minInc=1e-15, maxInc=0.1, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading-Step')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-Main'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region = a.Set(referencePoints=refPoints1, name='Set-7')
mdb.models['Model-Main'].DisplacementBC(name='BC-Beam-Displ', 
    createStepName='Loading-Step', region=region, u1=0.0, u2=-100.0, u3=UNSET, 
    ur1=0.0, ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-Main'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-Bukling'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-Main'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-Bukling'].parts['Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-Bukling'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buklig')
import job
mdb.models['Model-Bukling'].keywordBlock.synchVersions(
    storeNodesAndElements=False)
mdb.models['Model-Bukling'].keywordBlock.replace(49, """
*Output, field, variable=PRESELECT
*NODE FILE, GLOBAL=NO,
MODE=1, LAST MODE=2,
U""")
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.models['Model-Bukling'].keywordBlock.synchVersions(
    storeNodesAndElements=False)
mdb.models['Model-Bukling'].keywordBlock.replace(50, """
*NODE FILE, GLOBAL=NO,
MODE=1, LAST MODE=2
U""")
mdb.jobs['Job-Bukling'].submit(consistencyChecking=OFF)
#: The job input file "Job-Bukling.inp" has been submitted for analysis.
#: Job Job-Bukling: Analysis Input File Processor completed successfully.
#: Job Job-Bukling: Abaqus/Standard completed successfully.
#: Job Job-Bukling completed successfully. 
a = mdb.models['Model-Main'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-Main'].keywordBlock.synchVersions(
    storeNodesAndElements=False)
mdb.models['Model-Main'].keywordBlock.replace(38, """
** ----------------------------------------------------------------
*Imperfection,
file=Job-Bukling, step=1
1, 10
2, -10
**
** STEP: Loading-Step
**""")
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.Job(name='Job-loading', model='Model-Main', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-loading'].submit(consistencyChecking=OFF)
#: The job input file "Job-loading.inp" has been submitted for analysis.
#: Job Job-loading: Analysis Input File Processor completed successfully.
#: Error in job Job-loading: Too many attempts made for this increment
#: Error in job Job-loading: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. OUTPUT FOR THE LAST CONVERGED INCREMENT HAS NOT BEEN WRITTEN DUE TO CONVERGENCE ISSUES.
#: Job Job-loading: Abaqus/Standard aborted due to errors.
#: Error in job Job-loading: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-loading aborted due to errors.
o3 = session.openOdb(name='C:/temp/Geometric Imperfection/Job-loading.odb')
#: Model: C:/temp/Geometric Imperfection/Job-loading.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          10
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.fitView()
mdb.save()
#: The model database has been saved to "C:\Abaqus Projects\Project_3_Geometric_Imperfection\GI.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
