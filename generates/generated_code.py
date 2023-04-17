
# Import necessary modules
import adsk.core, adsk.fusion, adsk.cam

# Get the application and root component
app = adsk.core.Application.get()
rootComp = adsk.fusion.Design.cast(app.activeProduct).rootComponent

# Create a new sketch
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Create a rectangle
points = adsk.core.ObjectCollection.create()
points.add(adsk.core.Point3D.create(0, 0, 0))
points.add(adsk.core.Point3D.create(20, 0, 0))
points.add(adsk.core.Point3D.create(20, 5, 0))
points.add(adsk.core.Point3D.create(0, 5, 0))
sketch.sketchCurves.sketchLines.addAdjacent(points)

# Create an extrusion
extrudes = rootComp.features.extrudeFeatures
profile = sketch.profiles.item(0)
distance = adsk.core.ValueInput.createByReal(10)
extrudeInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
extrudeInput.setDistanceExtent(True, distance)
extrude = extrudes.add(extrudeInput)
