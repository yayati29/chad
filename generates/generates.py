
import adsk.core, adsk.fusion, adsk.cam

# Get the application and root component
app = adsk.core.Application.get()
rootComp = adsk.fusion.Design.cast(app.activeProduct).rootComponent

# Create a new sketch on the xy-plane
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Draw a rectangle with the given dimensions
length = 20
width = 5
height = 10
corner1 = adsk.core.Point3D.create(0, 0, 0)
corner2 = adsk.core.Point3D.create(length, 0, 0)
corner3 = adsk.core.Point3D.create(length, width, 0)
corner4 = adsk.core.Point3D.create(0, width, 0)
line1 = sketch.sketchCurves.sketchLines.addByTwoPoints(corner1, corner2)
line2 = sketch.sketchCurves.sketchLines.addByTwoPoints(corner2, corner3)
line3 = sketch.sketchCurves.sketchLines.addByTwoPoints(corner3, corner4)
line4 = sketch.sketchCurves.sketchLines.addByTwoPoints(corner4, corner1)

# Extrude the rectangle to the given height
extrudes = rootComp.features.extrudeFeatures
profile = sketch.profiles.item(0)
extrudeInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
extrudeInput.setDistanceExtent(True, adsk.core.ValueInput.createByReal(height))
extrudes.add(extrudeInput)
