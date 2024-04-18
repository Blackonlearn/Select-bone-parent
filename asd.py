import bpy


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
