import bpy
import rbt.rename


def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


class WM_OT_searchOp(bpy.types.Operator):
    """ Search and Replace Names in the Outliner """
    bl_label = "Search & Replace"
    bl_idname = "wm.searchop"
    
    look_for : bpy.props.StringProperty(name="Look For:", default= "")
    rep_with : bpy.props.StringProperty(name="Replace With:", default= "")
    
    def execute(self, context):
        look_for = self.look_for
        rep_with = self.rep_with
        try:
            test = rbt.rename.replace(look_for, rep_with)
            if test == None:
                ShowMessageBox("Name Not Found", "WARNING", "ERROR")
                return {'FINISHED'}
            ShowMessageBox("Search & Replace Success", "Valid", "CHECKMARK")
        except:
            ShowMessageBox("Unable to Search & Replace", "ERROR", "ERROR")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class WM_OT_addPrefix(bpy.types.Operator):
    """ Adds a given prefix to a selection of object(s) """
    bl_label = "Add Prefix"
    bl_idname = "wm.addprefix"
    
    prefix : bpy.props.StringProperty(name="Add Prefix:", default= "")
    
    def execute(self, context):
        prefix = self.prefix
        try:
            test = rbt.rename.add_prefix(prefix)
            if test == None:
                ShowMessageBox("At Least 1 Object Must Be Selected", "WARNING", "ERROR")
                return {'FINISHED'}
            ShowMessageBox("Prefix Added", "Valid", "CHECKMARK")
        except:
            ShowMessageBox("Unable to Add Prefix", "ERROR", "ERROR")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    

class WM_OT_addSuffix(bpy.types.Operator):
    """ Adds a given suffix to a selection of object(s) """
    bl_label = "Add Suffix"
    bl_idname = "wm.addsuffix"
    
    suffix : bpy.props.StringProperty(name="Add Suffix:", default= "")
    
    def execute(self, context):
        suffix = self.suffix
        try:
            test = rbt.rename.add_suffix(suffix)
            if test == None:
                ShowMessageBox("At Least 1 Object Must Be Selected", "WARNING", "ERROR")
                return {'FINISHED'}
            ShowMessageBox("Suffix Added", "Valid", "CHECKMARK")
        except:
            ShowMessageBox("Unable to Add Suffix", "ERROR", "ERROR")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    
class WM_OT_matchNames(bpy.types.Operator):
    """ Matches the names of all children of objects to the name of the object """
    bl_label = "Match to All Object Names"
    bl_idname = "wm.matchname"
    
    suffix : bpy.props.StringProperty(name="Add Suffix:", default= "")
    
    def execute(self, context):
        try:
            rbt.rename.match_all_names()
            ShowMessageBox("All Now Matched to Object Names", "Valid", "CHECKMARK")
        except:
            ShowMessageBox("Unable to Match to Object Names", "ERROR", "ERROR")
        return {'FINISHED'}

    
class WM_OT_renameNum(bpy.types.Operator):
    """ Renames a selection of object(s) from input & adds a number to the end """
    bl_label = "Rename & Number"
    bl_idname = "wm.renamenum"
    
    name : bpy.props.StringProperty(name="Name:", default= "")
    start_num : bpy.props.IntProperty(name= "Starting Number", default= 1)
    padding : bpy.props.IntProperty(name= "Padding", default= 1)
    
    def execute(self, context):
        name = self.name
        start_num = self.start_num
        padding = self.padding
        try:
            test = rbt.rename.add_number(name, start_num, padding)
            if test == None:
                ShowMessageBox("At Least 1 Object Must Be Selected", "WARNING", "ERROR")
                return {'FINISHED'}
            ShowMessageBox("Rename & Number Successful", "Valid", "CHECKMARK")
        except:
            ShowMessageBox("Rename & Number Failed", "ERROR", "ERROR")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)       
    
    
classes = (
    WM_OT_searchOp,
    WM_OT_addPrefix,
    WM_OT_addSuffix,
    WM_OT_matchNames,
    WM_OT_renameNum
)

def register():
    for c in classes:
      bpy.utils.register_class(c)


def unregister():
    for c in classes:
      bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
    
