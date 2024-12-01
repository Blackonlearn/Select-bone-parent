import bpy
#This simple code is mine, and it has already been pushed to github repo as my archive:https://github.com/Blackonlearn/Select-bone-parent

C = bpy.context
D = bpy.data
ArmatureName = "Data_RIG-CAGEDEFORM"
ArmatureData =  D.armatures[ArmatureName]


def NewBonelist():
    bonelist = []
    for i in C.selected_pose_bones:
        if not i.parent:
            bonelist.append(i)
    for i in C.selected_pose_bones:
        ArmatureData.bones[i.name].select = False
        print("asD")
    return bonelist

bonelist = NewBonelist()
    
def GetBoneParent(bonelist):
    for i in bonelist:
        ArmatureData.bones[i.name].select = True

GetBoneParent(bonelist)
