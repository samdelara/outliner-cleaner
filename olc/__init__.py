bl_info = {
    "name": "Outliner Cleaner",
    "author": "Sam De Lara",
    "version": (1, 0),
    "blender": (2, 93, 1),
    "location": "Scene Properties Sidebar Menu",
    "description": "A small tool used to aid with outliner organization",
    "warning": "",
    "doc_url": "",
    "category": "User Interface",
}


import bpy
import traceback
import olc.operators
import olc.ui_panel


def register():
  try:
    olc.operators.register()
    olc.ui_panel.register()
  except:
    traceback.print_exc()
  print("Registered {}".format(bl_info["name"]))

def unregister():
  try:
    olc.operators.unregister()
    olc.ui_panel.unregister()
  except:
    traceback.print_exc()
  print("Unregistered {}".format(bl_info["name"]))