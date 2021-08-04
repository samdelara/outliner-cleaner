import bpy
import rbt.operators

class RigBuddyPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Outliner Cleaner"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        # Move Origin
        
        # Recalculate 
        
        # Mirroring
        
        # Add Control Shapes
        
        # Renamer
        col = layout.column()
        col.scale_y = 1.5
        col.label(text="Outliner Cleaner:")
        col.operator("wm.searchop", icon="ZOOM_PREVIOUS")
        
        row = layout.row()
        row.scale_y = 1.5
        row.operator("wm.addprefix", icon="LOOP_BACK")
        row.operator("wm.addsuffix", icon="LOOP_FORWARDS")
        
        col = layout.column()
        col.scale_y = 1.5
        col.operator("wm.renamenum", icon="SEQ_STRIP_DUPLICATE")
        
        col = layout.column()
        col.scale_y = 1.5
        col.operator("wm.matchname", icon="SELECT_EXTEND")


def register():
    bpy.utils.register_class(RigBuddyPanel)


def unregister():
    bpy.utils.unregister_class(RigBuddyPanel)


if __name__ == "__main__":
    register()
