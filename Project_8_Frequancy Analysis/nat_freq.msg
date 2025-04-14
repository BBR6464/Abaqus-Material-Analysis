1

   Abaqus 2020                                  Date 14-Apr-2025   Time 12:13:19
   For use by Supplied by Team-SolidSQUAD under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     C A L C U L A T I O N   O F   E I G E N V A L U E S

                                            F O R   N A T U R A L   F R E Q U E N C I E S



                                                                                          

     THE LANCZOS EIGENSOLVER IS USED FOR THIS ANALYSIS
     SYSTEM DATA WILL BE WRITTEN TO THE .SIM FILE

     Abaqus WILL COMPUTE UNCOUPLED
      STRUCTURAL AND ACOUSTIC MODES
     NUMBER OF EIGENVALUES                     10
     HIGHEST FREQUENCY OF INTEREST                  1.00000E+18
     MAXIMUM NUMBER OF STEPS WITHIN RUN               35
     BLOCK SIZE FOR LANCZOS PROCEDURE                  7
     THE EIGENVECTORS ARE SCALED SO THAT 
      THE GENERALIZED MASS IN EACH VECTOR IS UNITY

     THIS IS A LINEAR PERTURBATION STEP.
     ALL LOADS ARE DEFINED AS CHANGE IN LOAD TO THE REFERENCE STATE

     EXTRAPOLATION WILL NOT BE USED

     CHARACTERISTIC ELEMENT LENGTH     0.500    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     ELEMENT OPERATIONS WILL BE CARRIED OUT IN PARALLEL USING   5 PROCESSORS

     PARALLEL CONTACT TRACKING ENABLED


     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS
 
     INITIAL ELEMENT LOAD BALANCE
            PROCESS    1   THREAD     NUMBER OF ELEMENTS
                              1            20
                              2            20
                              3            20
                              4            20
                              5            20

     CHECK POINT   START OF SOLVER    
  
 COMPUTER PRECISION USED BY ABAQUS       2.22045e-16
 CONVERGENCE CRITERION FOR LANCZOS RUN   1.81899e-12
  
 NUMBER OF EQUATIONS                                                         303
 NUMBER OF UNRESTRAINED DEGREES OF FREEDOM                                   300
 HEURISTIC SCALE FOR THE FIRST NONZERO EIGENVALUES (PROBLEM SCALE)   3.12742e+06
 INITIAL SHIFT VALUE                                                 0.00000e+00
  
 NUMBER OF CPUS USED BY DIRECT SOLVER     5
  
 NUMBER OF NEGATIVE EIGENVALUES     0
 NUMBER OF POSITIVE EIGENVALUES   303
 NUMBER OF NEGATIVE EIGENVALUES NOT ASSOCIATED WITH LAGRANGE MULTIPLIERS     0
 NUMBER OF LAGRANGE MULTIPLIERS     0
  
 COMPUTATIONAL INTERVAL FOR THE INITIAL LANCZOS RUN
 
 EIGENVALUES NEEDED TO THE RIGHT OF SHIFT VALUE   10
 EIGENVALUES NEEDED TO THE LEFT OF SHIFT VALUE     0
 RIGHT BOUNDARY OF THE COMPUTATIONAL INTERVAL   3.95574e+37
 LEFT BOUNDARY OF THE COMPUTATIONAL INTERVAL   -3.95574e+37
  
 LANCZOS RUN TERMINATED. NUMBER OF STEPS:    6
 ALL THE EIGENVALUES REQUESTED ON THIS LANCZOS RUN ARE FOUND
  
 NUMBER OF ACCEPTED EIGENVALUES   10
  
 ACCEPTED EIGENVALUES
   7.20751e+03  2.82253e+05  2.20303e+06  8.40566e+06  2.27822e+07  5.03364e+07
   5.75715e+07  9.70603e+07  1.69782e+08  2.76005e+08
  
 FACTORIZATION WITH NEW SHIFT VALUE IS REQUIRED
  
 TRUST INTERVALS AFTER LANCZOS RUN AND COMPRESSION
  
 NUMBER OF TRUST INTERVALS    1
  
 -------------------------------------------------------------------------------------
 | KEY | INSIDE |      INERTIAS     |  SENTINELS  |   OUTSIDE   |  NEED TO FIND      |
 |      ENDS OF INTERVAL     |     ENDS OF SENTINEL      |   COMPUTATIONAL INTERVAL  |
 -------------------------------------------------------------------------------------
 |  +  |      0 |        0        0 |     0     0 |     0     0 |      0    10       |
 | -3.95574e+37  0.00000e+00 | -3.95574e+37  0.00000e+00 | -3.95574e+37  3.95574e+37 |
 -------------------------------------------------------------------------------------
  
 DATA FOR CHOOSING SHIFT
  
 NUMBER OF EIGENVALUES NEEDED IN THE PRIMARY TRUST INTERVAL   10
  
 NUMBER OF MODES FORMING SENTINEL TO THE RIGHT   10
 SHIFT RIGHT         3.49873e+08
  
 NUMBER OF MODES FORMING SENTINEL TO THE LEFT     0
 SHIFT LEFT          0.00000e+00
  
 SHIFTING TO THE RIGHT DIRECTION
 NEW SHIFT           3.49873e+08
  
 NUMBER OF NEGATIVE EIGENVALUES    10
 NUMBER OF POSITIVE EIGENVALUES   293
 NUMBER OF NEGATIVE EIGENVALUES NOT ASSOCIATED WITH LAGRANGE MULTIPLIERS    10
 NUMBER OF LAGRANGE MULTIPLIERS     0
  
 THE REQUIRED NUMBER OF EIGENVALUES IS FOUND
  
 FINAL TRUST INTERVAL
  
 -------------------------------------------------------------------------------------
 | KEY | INSIDE |      INERTIAS     |  SENTINELS  |   OUTSIDE   |  NEED TO FIND      |
 |      ENDS OF INTERVAL     |     ENDS OF SENTINEL      |   COMPUTATIONAL INTERVAL  |
 -------------------------------------------------------------------------------------
 |  +  |     10 |        0       10 |     0     0 |     0     0 |      0     0       |
 | -3.95574e+37  3.49873e+08 | -3.95574e+37  3.49873e+08 | -3.95574e+37  3.49873e+08 |
 -------------------------------------------------------------------------------------
  
 FIRST EIGENVALUE REQUESTED BY THE USER     1
  
 EIGENVALUES REQUESTED BY THE USER
   7.20751e+03  2.82253e+05  2.20303e+06  8.40566e+06  2.27822e+07  5.03364e+07
   5.75715e+07  9.70603e+07  1.69782e+08  2.76005e+08
  
 EIGENVALUE EXTRACTION USING THE LANCZOS EIGENSOLVER IS COMPLETE
 NUMBER OF LANCZOS RUNS       :   1
 NUMBER OF LANCZOS STEPS      :   6
 NUMBER OF FACTORIZATIONS     :   2
 NUMBER OF BACK SUBSTITUTIONS :   7

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.60000    
       ELAPSED SYSTEM TIME (SEC)    =  0.30000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.90000    
       ELAPSED WALLCLOCK TIME (SEC) =          1
 
     INITIAL ELEMENT LOAD BALANCE
            PROCESS    1   THREAD     NUMBER OF ELEMENTS
                              1            20
                              2            20
                              3            20
                              4            20
                              5            20
 
     INITIAL ELEMENT LOAD BALANCE
            PROCESS    1   THREAD     NUMBER OF ELEMENTS
                              1            20
                              2            20
                              3            20
                              4            20
                              5            20


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          1  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                       0  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                       9  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                       2  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       0  WARNING MESSAGES DURING USER INPUT PROCESSING
                       0  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   1.5000    
       SYSTEM TIME (SEC)    =  0.40000    
       TOTAL CPU TIME (SEC) =   1.9000    
       WALLCLOCK TIME (SEC) =          2
