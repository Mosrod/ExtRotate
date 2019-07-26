import bpy

bl_info = {
    "name" : "ExtRotate",
    "author" : "Mosrod",
    "description" : "Lets you extrude and rotate a face",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 2),
    "location" : "View3D",
    "warning" : "",
    "category" : "Mesh"
}
class ExtrudeRotate(bpy.types.Operator):
    """Extrude and Rotate Face"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "mesh.extrude_rotate"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Extrude and Rotate Face"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    
    extrudevalue: bpy.props.FloatProperty(name="Extrude Amount", default=-0.1, min=-100, max=100)
    rotatevalue: bpy.props.IntProperty(name="Rotate Amount", default=10, min=-100, max=100)
    scalevalue: bpy.props.FloatProperty(name="Scale Amount", default=1, min=-100, max=100)
    
    def execute(self, context):        # execute() is called when running the operator.
        
        # The original script
        
        # Extrudes and rotates a face
        extrude_value = self.extrudevalue
        rotate_value_raw = self.rotatevalue
        scale_value = self.scalevalue

        # Convert the degress to radians
        import math
        rotate_value = math.radians(rotate_value_raw)

        # Action!
        bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_shrink_fatten={"value":extrude_value, "use_even_offset":False, "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})
        bpy.ops.transform.rotate(value=rotate_value, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.resize(value=(scale_value, scale_value, scale_value), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(ExtrudeRotate.bl_idname)

def register():
    bpy.utils.register_class(ExtrudeRotate)
    bpy.types.VIEW3D_MT_edit_mesh_faces.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ExtrudeRotate)
    
    bpy.utils.unregister_class(ExtrudeRotate)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
