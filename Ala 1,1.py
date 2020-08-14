bl_info = {
    "name": "Armature wing",
    "author": "Roberto Contreras Ramírez",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy
#crear un boton

#Crear los huesos. El orden es X,Y,Z
bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(2, 0, 1)) 
bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(2, 0, -2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.object.posemode_toggle()
bpy.ops.pose.constraint_add(type='IK')
bpy.context.object.pose.bones["Bone.001"].constraints["IK"].chain_count = 2
bpy.ops.object.editmode_toggle()
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(2, 0, 2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.object.posemode_toggle()
bpy.ops.pose.constraint_add(type='IK')
bpy.context.object.pose.bones["Bone.002"].constraints["IK"].chain_count = 2
bpy.ops.object.editmode_toggle()
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(4, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.object.posemode_toggle()
bpy.ops.pose.constraint_add(type='IK')
bpy.context.object.pose.bones["Bone.003"].constraints["IK"].chain_count = 2

#cambiar el nombre del Armature, 
bpy.ops.object.editmode_toggle()#primero cambia de vista a edicion de objeto
Ala_I = [bpy.data.objects['Armature']]#La I es por izquierda. Ala_I es el nuevo nombre que se le pondrá. bpy.data.objjects ['Armature'] es lo que se está creando, un esqueleto
for i in Ala_I:#este loop busca i que es el nombre del armature
    i.name = "Ala_I"#i.name es la funcion? que cambia de nombre al objeto creado, después del = se pone entre comillas el nuevo nombre

obj = bpy.context.object#selecciona al objeto  para cambiar el nombre de los huesos

namelist = [("Bone", "HAla"),("Bone.001", "HAla.1"), ("Bone.002", "HAla.2"), ("Bone.003", "HAla.3")]

for name, newname in namelist:
    pb = obj.pose.bones.get(name)
    if pb is None:
        Continue
    #renombrar
    pb.name = newname

bpy.ops.object.posemode_toggle()#pasa a pantalla de pose


#poner IK
#bpy.ops.pose.constraint_add(type='IK')
#bpy.context.object.pose.bones["HAla"].constraints["IK"].chain_count = 2

#falta linea de "seleccionar objeto
#bpy.context.space_data.context = 'BONE_CONSTRAINT'
#bpy.ops.pose.constraint_add(type='IK')
