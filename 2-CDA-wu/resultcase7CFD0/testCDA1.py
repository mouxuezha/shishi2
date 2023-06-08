mulu = 'C:/Users/y/Desktop/EnglishMulu/testCDA11'

# mulu = '.'
close_project()
set_project_configuration("2D", 2)
set_project_header("I G G", "Interactive Geometry Modeling and", "Grid Generation System")
import_data_file(mulu + "/pressure.dat")
import_data_file(mulu + "/suction.dat")
import_data_file(mulu + "/suction2.dat")
import_data_file(mulu + "/pressure2.dat")
import_data_file(mulu + "/suction3.dat")
import_data_file(mulu + "/pressure3.dat")

import math

L =10 
jiaodu_qian = 0.2513 
bili_qian = 0.0

endPoint_qianzhong = CurvePointNorm(Curve("pressure"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
print(CurvePointNorm(Curve("pressure"), bili_qian))
print('MXairfoil: trying to get the start point. ')
print(endPoint_qianzhong)
polyline_qianzhong = new_polyline("polyline_qianzhong")
polyline_qianzhong.insert_point(1, CurvePointNorm(Curve("pressure"), bili_qian))
polyline_qianzhong.insert_point(2, endPoint_qianzhong)

endPoint_qianshang = CurvePointNorm(Curve("pressure2"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianshang = new_polyline("polyline_qianshang")
polyline_qianshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_qian))
polyline_qianshang.insert_point(2, endPoint_qianshang)

endPoint_qianxia = CurvePointNorm(Curve("pressure3"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianxia = new_polyline("polyline_qianxia")
polyline_qianxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_qian))
polyline_qianxia.insert_point(2, endPoint_qianxia)

bili_hou = 1 
jiaodu_hou = 0 
endPoint_houshang = CurvePointNorm(Curve("pressure2"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houshang = new_polyline("polyline_houshang")
polyline_houshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_hou))
polyline_houshang.insert_point(2, endPoint_houshang)

endPoint_houzhong = CurvePointNorm(Curve("pressure"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houzhong = new_polyline("polyline_houzhong")
polyline_houzhong.insert_point(1, CurvePointNorm(Curve("pressure"), 1))
polyline_houzhong.move_point(1, CurvePointNorm(Curve("pressure"), 1))
polyline_houzhong.insert_point(2, endPoint_houzhong)

endPoint_houxia = CurvePointNorm(Curve("pressure3"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houxia = new_polyline("polyline_houxia")
polyline_houxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_hou))
polyline_houxia.insert_point(2, endPoint_houxia)

new_block_face(Point(-8.63135528564453, 4.5818395614624, 0), Point(-8.63135528564453, 1.16852641105652, 0), Point(-1.08887243270874, 1.16852641105652, 0), Point(-1.08887243270874, 4.5818395614624, 0))
# total_chang = 161
# cut = 65 # for 161
# cut2 = 95
total_y = 81
cut = 33 
cut2 = 45


total_x = 261
d1 = 41 
d2 = total_x-68 # 173 for total_x = 241
block("Block_1").set_size(total_y, total_x, 2, 1)


# d1 = 40  #what a stupid software. If I use 40 rather than 4n+1, numeca would say:  !createBcBranch : THIS BC COULD NOT BE COARSENED IN BLOCK 1  ! 1 1 1 40 1 2 
# d2 = 170


segment("Block_1", 1, 3, 1).cluster_end(0.05)
move_vertex(vertex("Block_1", 1, 1, 1), CurvePointNorm(polyline_qianshang, 1))
move_vertex(vertex("Block_1", 1, 1, 2), CurvePointNorm(polyline_qianzhong, 1))
move_vertex(vertex("Block_1", 1, 2, 1), CurvePointNorm(polyline_houshang, 1))
move_vertex(vertex("Block_1", 1, 2, 2), CurvePointNorm(polyline_houzhong, 1))

edge("Block_1", 1, 3).insert_vertex(0.3)
move_vertex(vertex("Block_1", 1, 3, 2), CurvePointNorm(polyline_qianshang, 0))
edge("Block_1", 1, 3).insert_vertex(0.7)
move_vertex(vertex("Block_1", 1, 3, 3), CurvePointNorm(polyline_houshang, 0))
edge("Block_1", 1, 3).insert_vertex(0.5)
move_vertex(vertex("Block_1", 1, 3, 3), CurvePointNorm(Curve("pressure2"), 0.5))
vertex("Block_1", 1, 3, 2).attach_fix_point()
vertex("Block_1", 1, 3, 4).attach_fix_point()
fixed_point("Block_1", 1, 3, 1).change_index(d1, edge("Block_1", 1, 3))
fixed_point("Block_1", 1, 3, 2).change_index(d2, edge("Block_1", 1, 3))

edge("Block_1", 1, 4).insert_vertex(0.3)
move_vertex(vertex("Block_1", 1, 4, 2), CurvePointNorm(polyline_qianzhong, 0))
edge("Block_1", 1, 4).insert_vertex(0.7)
move_vertex(vertex("Block_1", 1, 4, 3), CurvePointNorm(polyline_houzhong, 0))
edge("Block_1", 1, 4).insert_vertex(0.5)
move_vertex(vertex("Block_1", 1, 4, 3), CurvePointNorm(Curve("suction"), 0.5))
vertex("Block_1", 1, 4, 2).attach_fix_point()
vertex("Block_1", 1, 4, 4).attach_fix_point()
fixed_point("Block_1", 1, 4, 1).change_index(d1, edge("Block_1", 1, 4))
fixed_point("Block_1", 1, 4, 2).change_index(d2, edge("Block_1", 1, 4))

# block_by_face_extrusion_comb(face("Block_1", 1), vector(0, 0, 1), 0, point(0, 0, 0), 0, 0, 0, 0)

#distribution of mesh.
create_clustering_group("qian")
clustering_group("qian").add_segment(segment("Block_1", 1, 3, 1), 0)
clustering_group("qian").add_segment(segment("Block_1", 1, 4, 1), 0)
clustering_group("qian").cluster_end(0.01)
create_clustering_group("hou")
clustering_group("hou").add_segment(segment("Block_1", 1, 3, 3), 0)
clustering_group("hou").add_segment(segment("Block_1", 1, 4, 3), 0)
clustering_group("hou").cluster_start(0.01)
create_clustering_group("wall")
clustering_group("wall").add_segment(segment("Block_1", 1, 3, 2), 0)
clustering_group("wall").add_segment(segment("Block_1", 1, 4, 2), 0)
clustering_group("wall").cluster_both_ends2(0.01, 0.01, 0)
create_clustering_group("zhong")
clustering_group("zhong").add_segment(segment("Block_1", 1, 1, 1), 0)
clustering_group("zhong").add_segment(segment("Block_1", 1, 2, 1), 0)
# clustering_group("zhong").cluster_both_ends2(0.006, 0.006, 0) # 0.0004 this is for y+ =1
clustering_group("zhong").cluster_both_ends2(0.0004, 0.0004, 0) # # for postprocess



# for i in range(4):
	# face("Block_1", 1).smooth(1)
	
#add a piont to ajust the mesh

face("Block_1", 1).create_grid_point(cut, d2)
edge("Block_1", 1, 5).create_curve("Block_1_1_5")
edge("Block_1", 1, 6).create_curve("Block_1_1_6")
# move_vertex(vertex("Block_1", 1, 6, 2), CurvePointNorm(Curve("Block_1_1_5"), 0.73))
face("Block_1", 1).create_grid_point(cut, d1)
edge("Block_1", 1, 5).create_curve("Block_1_1_5_")
edge("Block_1", 1, 7).create_curve("Block_1_1_7")
# move_vertex(vertex("Block_1", 1, 7, 2), CurvePointNorm(Curve("Block_1_1_5_"), 0.27))


face("Block_1", 1).create_grid_point(cut2, d1)
edge("Block_1", 1, 8).create_curve("Block_1_1_8")
edge("Block_1", 1, 7).create_curve("Block_1_1_7_")

move_vertex(vertex("Block_1", 1, 7, 2), CurvePointNorm(Curve("Block_1_1_5"), 0.29))
move_vertex(vertex("Block_1", 1, 6, 2), CurvePointNorm(Curve("Block_1_1_5"), 0.71))
move_vertex(vertex("Block_1", 1, 8, 2), CurvePointNorm(Curve("Block_1_1_8"), 0.27))
move_vertex(vertex("Block_1", 1, 8, 3), CurvePointNorm(Curve("Block_1_1_8"), 0.73))

# distribute again, zhongjian lines.
create_clustering_group("heng")
clustering_group("heng").add_segment(segment("Block_1", 1, 5, 2), 0)
clustering_group("heng").add_segment(segment("Block_1", 1, 8, 2), 0)
clustering_group("heng").cluster_both_ends2(0.02, 0.02, 0)
segment("Block_1", 1, 5, 1).cluster_end(0.03)
segment("Block_1", 1, 5, 3).cluster_start(0.03)
segment("Block_1", 1, 8, 1).cluster_end(0.03)
segment("Block_1", 1, 8, 3).cluster_start(0.03)

for i in range(2):
	face("Block_1", 1).smooth(1)
	
#then boundary condition.
block_by_face_extrusion_comb(face("Block_1", 1), Vector(0, 0, 3.54680514335632), 0, Point(0, 0, 0), 0, 0, 0, 0)
patch("Block_1", 5, 1).divide_by_range(Range(1, d1, 1, 2))
patch("Block_1", 5, 2).divide_by_range(Range(d1, d2, 1, 2))
patch("Block_1", 6, 1).divide_by_range(Range(1, d1, 1, 2))
patch("Block_1", 6, 2).divide_by_range(Range(d1, d2, 1, 2))
set_repetition_all_blocks("TRANSLATION", 2, Vector(0, 7.62, 0))
block_by_face_extrusion_comb(face("Block_1", 1), Vector(0, 0, 3.54680514335632), 0, Point(0, 0, 0), 0, 0, 0, 0)
connect_patches(patch("Block_1", 5, 1), patch("Block_1", 6, 1), "IHIGH", "JHIGH", "PER", 1E-005)
connect_patches(patch("Block_1", 5, 3), patch("Block_1", 6, 3), "IHIGH", "JHIGH", "PER", 1E-005)
search_connections(1E-005)
patch("Block_1", 3, 1).set_type("INL")
patch("Block_1", 4, 1).set_type("OUT")
patch("Block_1", 5, 2).set_type("SOL")
patch("Block_1", 6, 2).set_type("SOL")

save_project("./testCDA1.igg")
