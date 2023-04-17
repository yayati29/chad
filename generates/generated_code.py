
import adsk.core, adsk.fusion, adsk.cam

# Get the active design and root component.
app = adsk.core.Application.get()
design = adsk.fusion.Design.cast(app.activeProduct)
rootComp = design.rootComponent

# Create a new sketch on the XY plane.
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Draw a rectangle with the given dimensions.
point1 = adsk.core.Point3D.create(0, 0, 0)
point2 = adsk.core.Point3D.create(20, 0, 0)
point3 = adsk.core.Point3D.create(20, 5, 0)
point4 = adsk.core.Point3D.create(0, 5, 0)

sketch.sketchCurves.sketchLines.addByTwoPoints(point1, point2)
sketch.sketchCurves.sketchLines.addByTwoPoints(point2, point3)
sketch.sketchCurves.sketchLines.addByTwoPoints(point3, point4)
sketch.sketchCurves.sketchLines.addByTwoPoints(point4, point1)

# Extrude the sketch to create a solid block.
extrudes = rootComp.features.extrudeFeatures
profiles = adsk.core.ObjectCollection.create()
profiles.add(sketch.profiles.item(0))
extrudeInput = extrudes.createInput(profiles, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
extrudeDistance = adsk.core.ValueInput.createByReal(10)
extrudeInput.setDistanceExtent(False, extrudeDistance)
extrudes.add(extrudeInput)
