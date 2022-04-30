import bpy
from bpy_extras.io_utils import ImportHelper


class PML_LoadFromBrowser(bpy.types.Operator, ImportHelper):
    bl_idname = "object.pml_load_from_browser"
    bl_label = "Load footage from blender's file browser"

    def execute(self, context):
        link = context.scene.media_library.add() 
        link.path = self.filepath


        return {'FINISHED'}

class PML_PrintAllMediaLinks(bpy.types.Operator):
    bl_idname = "object.pml_debug_print_medialinks"
    bl_label = "Print all MediaLinks in blender's Info Console"

    def execute(self, context):

        for ml in context.scene.media_library:
           self.report({'INFO'}, ml.path)
        
        return {'FINISHED'}


class MediaLink(bpy.types.PropertyGroup): 
    path : bpy.props.StringProperty(
        default = ""
    )

    name : bpy.props.StringProperty(

    )

    mod_framerate : bpy.props.FloatProperty(
        default = 24,
        description = "Determines the framerate at wich the footage should be interpreted as"
    )

    
