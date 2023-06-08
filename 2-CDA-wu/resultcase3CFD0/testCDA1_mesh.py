CFViewBackward(1210,)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'

OpenCGNSAutogrid(mulu+'/testCDA1.cgns')
GmtToggleGrid()

mulu_fig_da = mulu+'/output/'+'mesh_all.tif'
mulu_fig_qian = mulu+'/output/'+'mesh_in.tif'
mulu_fig_hou = mulu+'/output/'+'mesh_out.tif'
SetNumecaLogo(0,0)

ViewPlaneY()
ViewPlaneY()
ViewPlaneZ()
ViewPlaneZ()

SetCamera(5.23497,5.01678,8.48518,5.23497,5.01678,0.5,0,1,0,3.19407,18.8673)
Print(6,0,1,1,100,1920,1080,0 ,mulu_fig_da ,'',1,1,1)
SetCamera(-0.5757,7.72231,0.904573,-0.5757,7.72231,0.5,0,1,0,0.020346,0.120183)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_qian ,'',1,1,1)
SetCamera(12.0712,3.38343,1.30284,12.0712,3.38343,0.64633,0.0728786,0.996825,0,0.0175118,0.103442)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_hou ,'',1,1,1)
SetCamera(5.23497,5.01678,8.48518,5.23497,5.01678,0.5,0,1,0,3.19407,18.8673)