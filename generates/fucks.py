
import adsk.core, adsk.fusion, adsk.cam

app = adsk.core.Application.get()
ui = app.userInterface
design = app.activeProduct

# Create a new sketch.
sketches = design.rootComponent.sketches
xyPlane = design.rootComponent.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Create a rectangle using the dimensions provided.
length = 20
width = 5
height = 10

# Create 4 lines to form a rectangle.
line1 = sketch.sketchCurves.sketchLines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(length, 0, 0))
line2 = sketch.sketchCurves.sketchLines.addByTwoPoints(line1.endSketchPoint, adsk.core.Point3D.create(length, width, 0))
line3 = sketch.sketchCurves.sketchLines.addByTwoPoints(line2.endSketchPoint, adsk.core.Point3D.create(0, width, 0))
line4 = sketch.sketchCurves.sketchLines.addByTwoPoints(line3.endSketchPoint, adsk.core.Point3D.create(0, 0, 0))

# Extrude the rectangle to create a 3D model.
extrudes = design.rootComponent.features.extrudeFeatures
distance = adsk.core.ValueInput.createByReal(height)
extrudeInput = extrudes.createInput(sketch.profiles.item(0), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
extrudeInput.setDistanceExtent(False, distance)
ext = extrudes.add(extrudeInput)
