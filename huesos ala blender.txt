#boton para hacer los huesos de un ala en blender
import bpy
#crear un boton
#class ToolsPanel.types.Panel):#plantilla del boton
    #bl_label = "Ala Rig" #Nombre de lo que vamos a crear
    #Bl_space_type = "PROPERTIES" #donde se va a crear
    #bl_region_type = "WINDOW"
    
    #def draw(self, context):#donde va a trabajar el codigo
        #self.layout.operator("crear.ala")
#class OBJECT_OTGEO(bpy.types.Operator):
    #bl_idname = "falta definirlo"
    #bl_label = "falta la etiqueta de lo escrito abajo"
    
    #def execute(self, context):
        #bpy.ops.lo que está escrito abajo y sus caracteristicas
        #return{'FINISHED'}
#bpy.utils.register_module(_name_)
        
#Crear los huesos
#(X,Y,Z)
bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(2, 0, 1))
bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(2, 0, -2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(2, 0, 2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(4, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
#cambiar el nombre del Armature
bpy.ops.object.editmode_toggle()
Ala_I = [bpy.data.objects['Armature']]
for i in Ala_I:
    i.name = "Ala_I"
    print(i.name)
#cambiar el nombre de los huesos
context = bpy.context
obj = context.object

namelist = [("Bone", "HAla"),("Bone.001", "HAla.1"), ("Bone.002", "HAla.2"), ("Bone.003", "HAla.3")]

for name, newname in namelist:
    pb = obj.pose.bones.get(name)
    if pb is None:
        Continue
    #renombrar
    pb.name = newname
#poner IK
bpy.ops.object.posemode_toggle()
#falta linea de "seleccionar objeto
#bpy.context.space_data.context = 'BONE_CONSTRAINT'
#bpy.ops.pose.constraint_add(type='IK')