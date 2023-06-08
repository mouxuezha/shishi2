mulu = 'C:/Users/y/Desktop/EnglishMulu/testCDA11'
beta=0.878 # 0.878 # beta = 0.872665 # 50(90-40) degree.
# mulu = '.'
#for calculate: testCDA1 in Fin Turbo 14.1
FT.create_project(mulu+"/testCDA1.iec")
FT.set_cyl_cart_configuration(0)
FT.select_output("_SD_YPLUS_")
FT.set_azimuthal_output_flag(0, 0)
FT.set_azimuthal_output_flag(3, 0)
FT.set_azimuthal_output_flag(46, 0)
FT.select_output("_ABSOLUTE_TOTAL_TEMPERATURE_")
FT.select_output("_ABSOLUTE_TOTAL_PRESSURE_")
FT.select_output("_TURB_WALL_DISTANCE_")
FT.set_azimuthal_output_flag(68, 0)
FT.set_space_configuration(1, 0, 0, 0, 1, 0)
FT.link_mesh_file(mulu+"/testCDA1.igg", 0)
FT.set_unit_ratio(0.01)

#start set the configuration.
# FT.select_fluid_from_database("AIR", "Real Gas")
FT.select_fluid_from_database("AIR(Perfect)", "Perfect Gas")
FT.set_mathematical_model(SPALART_ALLMARAS)
FT.set_tracer(0)
FT.set_harmonic_maximum_rank(1)
FT.set_preconditioning(1)
FT.set_reference_length(0.1)
FT.set_reference_velocity(100)

import math
import random
#set bounndary condition.
# beta = 0.6981 # 40degree
# beta = 0.872665 # 50(90-40) degree.
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([124,2])
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([124,4])
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vz/|V|", 0)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vr/|V|", math.cos(beta))
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vt/|V|", math.sin(beta))
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Absolute Total Pressure", 1.03*101325)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Absolute Total Temperature", 294)
FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_parameter_value("Static Pressure", 101325)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Turbulent Viscosity", 1e-7)
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Turbulent Viscosity", 0.005)

FT.set_user_solver_precision(1)
FT.select_output("_ABSOLUTE_TOTAL_TEMPERATURE_")
FT.select_output("_ABSOLUTE_TOTAL_PRESSURE_")

# bushu = random.randint(0,70)
FT.set_nb_iter_max(3000) # for postprocess
# for 3 in Hakimi
# FT.set_nb_iter_max(800+bushu) # for 4 in Hakimi

# # low Ma model. This one looks better.
# FT.set_preconditioning_model(0)
# FT.set_preconditioning_model_params(4, 0)

# initial
FT.get_initial_solution(0).set_velocity(Vector(85,0,0))



# # #calculate
FT.save_selected_computations()