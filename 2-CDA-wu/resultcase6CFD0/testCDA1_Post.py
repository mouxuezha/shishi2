CFViewBackward(1210,) 
mulu = 'C:/Users/y/Desktop/EnglishMulu/testCDA11'
#post process in CFviewer

FileOpenProject(mulu+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run',)
MacroModuleLoad('TW',)
CutPlaneSaveFrom3Points(0, 0, 0, 0, 0.00773624, 0, 0.12, 0.12, 0)
# DeleteAll()
# DeletePlot()
QntFieldScalar('Static Pressure',)
SclContourSmooth()
ViewScroll(0, 0, 0)

QntFieldDerived(0, 'Cpt', '(Total Pressure-101325)/101325', '', '0')
QntFieldDerived(0, 'Cpt2', '(Total Pressure-101325)/101325/0.1273', '', '0')
QntFieldDerived(0 ,'jiaodu' ,'atan(Vxyz_Y/Vxyz_X)/pi*180' ,'' ,'0')
# QntFieldScalar('Cpt',)
# SclContourSmooth()
# SclPlotBoundarySolid(0)

SelectedSurfacesRemove('Block_1.Imin Solid')
SelectedSurfacesRemove('Block_1.Imax Solid')
SelectedSurfacesRemove('CUT1')
SelectedSurfacesAdd('Block_1.Jmin Inlet')
QntFieldScalar('Total Pressure')
Ptinlet=SclAverage()
# print('============================================')
# print('MXairfoil: Ptinlet =')
# print(Ptinlet)
# print('============================================')
wenjianming = mulu+'/testCDA1/jieguo/'
Ptinlet_file = open(wenjianming+'Ptinlet.dat','w')
Ptinlet_file.write(str(Ptinlet)) 
Ptinlet_file.close()


# moew post process
QntFieldDerived(0 ,'V' ,'sqrt(Vxyz_X*Vxyz_X + Vxyz_Y*Vxyz_Y  + Vxyz_Z*Vxyz_Z)' ,'' ,'0')
# SelectedSurfacesAdd('Block_1.Jmax Outlet')
# QntFieldScalar('Density')
# rhom = SclAverage()
# QntFieldScalar('V')
# Vm = SclAverage()
QntFieldScalar('Total Pressure')
# Ptin = SclAverage()
Ptin = WeightedIntegral()
Ptin_file = open(wenjianming+'Ptin.dat','w')
Ptin_file.write(str(Ptin)) 
Ptin_file.close()

QntFieldScalar('Static Pressure')
#Psin = SclAverage()
Psin = WeightedIntegral()
Psin_file = open(wenjianming+'Psin.dat','w')
Psin_file.write(str(Psin)) 
Psin_file.close()

SelectedSurfacesRemove('Block_1.Jmin Inlet')
SelectedSurfacesAdd('Block_1.Jmax Outlet')
QntFieldScalar('Total Pressure')
# Ptout = SclAverage()
Ptout = WeightedIntegral()
Ptout_file = open(wenjianming+'Ptout.dat','w')
Ptout_file.write(str(Ptout)) 
Ptout_file.close()

QntFieldScalar('Static Pressure')
# Psout = SclAverage()
Psout = WeightedIntegral()
Psout_file = open(wenjianming+'Psout.dat','w')
Psout_file.write(str(Psout)) 
Psout_file.close()

omega = (Ptin - Ptout)/(Ptin - Psin)
omega_file = open(wenjianming+'omega.dat','w')
omega_file.write(str(omega)) 
omega_file.close()

sigma = Ptout / Ptin 
sigma_file = open(wenjianming+'sigma.dat','w')
sigma_file.write(str(sigma)) 
sigma_file.close()

rise = Ptin/Psin
rise_file = open(wenjianming+'rise.dat','w')
rise_file.write(str(rise)) 
rise_file.close()

QntFieldDerived(0, 'Cps', '(Static Pressure-'+str(Psin)+')/('+str(Ptin)+'-'+str(Psin)+')', '', '0')
# QntFieldDerived(0, 'Cps2', '(Static Pressure-99318.5)/(104650-99318.5)', '', '0')
SelectedSurfacesRemove('Block_1.Jmin Inlet')
SelectedSurfacesRemove('Block_1.Jmax Outlet')
SelectedSurfacesAdd('Block_1.Imin Solid')
SelectedSurfacesAdd('Block_1.Imax Solid')
QntFieldScalar('Cps',)
SclContourSmooth()
SclPlotBoundarySolid(0)
PlotCurveOutput(wenjianming+'Cps.dat')

# get the qiliu zhuanzhejiao, turning angle
CutPlaneSave(-0.02,0.0779226,0.00445256,1,0,0,0,0) # this is jinkou inlet, CUT2
CutPlaneSave(0.13,0.0998964,-0.001547,1,0,0,0,0) # this is chukou outlet, CUT3

SelectedSurfacesRemove('Block_1.Imin Solid')
SelectedSurfacesRemove('Block_1.Imax Solid')
SelectedSurfacesRemove('CUT3') # it was auto selected after cut.
SelectedSurfacesAdd('CUT2')
QntFieldScalar('jiaodu')
angle_in = SclAverage()

SelectedSurfacesRemove('CUT2')
SelectedSurfacesAdd('CUT3')
angle_out = SclAverage()

turning = angle_in-angle_out
turning_file = open(wenjianming+'turning.dat','w')
turning_file.write(str(turning)) 
turning_file.close()

'''
angle_in_file = open(wenjianming+'angle_in.dat','w')
angle_in_file.write(str(angle_in)) 
angle_in_file.close()

angle_out_file = open(wenjianming+'angle_out.dat','w')
angle_out_file.write(str(angle_out)) 
angle_out_file.close()
'''

# Quit()