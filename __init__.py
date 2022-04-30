# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from . operators import *


bl_info = {
    "name" : "project_media_library",
    "author" : "Mathieu Monfort",
    "description" : "A Première-like project window for preloading,collecting and reducing files",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "Video Sequencer",
    "warning" : "",
    "category" : "Video Editing"
}

classes = ( MediaLink,
            PML_LoadFromBrowser,
            PML_PrintAllMediaLinks
            )

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.media_library = bpy.props.CollectionProperty(type=MediaLink)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
