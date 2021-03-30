import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")

selections = oEditor.GetSelections()

objectListStr = ''
for s in selections:
      objectListStr += s + ','
objectListStr = objectListStr[:-1] # whack-off trailing ','
   
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, objectListStr,
		"NewPartsModelFlag:="	, "Model"
	])
