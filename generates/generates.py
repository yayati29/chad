
import adsk.core, adsk.fusion, traceback

# Get the application and root component objects
app = adsk.core.Application.get()
des = adsk.fusion.Design.cast(app.activeProduct)
rootComp = des.rootComponent

# Create a new sketch on the xy plane
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
plateSketch = sketches.add(xyPlane)

# Draw a rectangle on the sketch
p0 = adsk.core.Point3D.create(0, 0, 0)
p1 = adsk.core.Point3D.create(20, 0, 0)
p2 = adsk.core.Point3D.create(20, 5, 0)
p3 = adsk.core.Point3D.create(0, 5, 0)

lines = plateSketch.sketchCurves.sketchLines
lines.addByTwoPoints(p0, p1)
lines.addByTwoPoints(p1, p2)
lines.addByTwoPoints(p2, p3)
lines.addByTwoPoints(p3, p0)

# Create an extrusion feature based on the sketch
extFeats = rootComp.features.extrudeFeatures
bottomFace = plateSketch.profiles.item(0)
extrudeDistance = adsk.core.ValueInput.createByReal(10)
extFeature = extFeats.addSimple(bottomFace, extrudeDistance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

# Redraw the viewport
app.activeViewport.refresh()
