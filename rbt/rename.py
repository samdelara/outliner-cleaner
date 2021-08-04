import bpy


def find_obj(string):
  """ Returns a list of objects that use a given string in Blender objects """
  same_objects = []
  for obj in bpy.data.objects:
    if obj.name.find(string) != -1:
      same_objects.append(obj)
  return same_objects

def find_obj_data(string):
  """ Returns a list of objects that use a given string in Blender objects """
  same_objects = []
  for obj in bpy.data.objects:
    if obj.data.name.find(string) != -1:
      same_objects.append(obj.data)
  return same_objects 

def find_mat(string):
  """ Returns a list of materials that use a given string in Blender objects """
  same_materials = []
  for mat in bpy.data.materials:
    if mat.name.find(string) != -1:
      same_materials.append(mat)
  return same_materials
      
def count_obj(string):
  """ Counts the number of instances a string is used in Blender objects """
  num = (len(find_obj(string)))
  return num

def count_obj_data(string):
  """ Counts the number of instances a string is used in Blender objects """
  num = (len(find_obj_data(string)))
  return num

def count_mat_data(string):
  """ Counts the number of instances a string is used in Blender objects """
  num = (len(find_mat(string)))
  return num

def replace(old_str, new_str):
  """ Replaces the name of objects in Blender with an inputed string """
  # If the object level matches the string
  if (count_obj(old_str)) > 0:
    for obj in bpy.data.objects:
      if obj in find_obj(old_str):
        name = obj.name.replace(old_str, new_str)
        obj.name = name
        obj.data.name = name
  # If the object data level matches the string
  if (count_obj_data(old_str)) > 0:
    for obj in bpy.data.objects:
      data = obj.data
      if data in find_obj_data(old_str):
        name = data.name.replace(old_str, new_str)
        data.name = name 
  # If the material name matches the string 
  if (count_mat_data(old_str)) > 0:
    for mat in bpy.data.materials:
      if mat in find_mat(old_str):
        name = mat.name.replace(old_str, new_str)
        mat.name = name 
    return 1
  # Else return none if no string found
  else:
    return None
   
def match_all_names():
  """ Match all the object data names to the respective objects """
  for obj in bpy.data.objects:
    if obj.data.name != obj.name:
      name = obj.name
      obj.data.name = name
  
def add_prefix(prefix):
  """ Adds a given prefix to a group of selected objects """
  if bpy.context.selected_objects == []:
    return None
  else:
    for obj in bpy.context.selected_objects:
      name = obj.name
      obj.name = prefix + name
    return 1
  
def add_suffix(suffix):
  """ Adds a given suffix to a group of selected objects """
  if bpy.context.selected_objects == []:
    return None
  else:
    for obj in bpy.context.selected_objects:
      name = obj.name
      obj.name = name + suffix
    return 1
      
def add_number(string, number, padding=0):
  """ Adds a given number at the end of group of selected objects, can be padded with "0"s """
  if bpy.context.selected_objects == []:
    return None
  else:
    for obj in bpy.context.selected_objects:
      zeros = ""
      name = string
      word_num = str(number)
      obj.name = name + "." + str(zeros.zfill(padding)) + word_num
      number += 1
    return 1