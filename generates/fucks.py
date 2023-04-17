
import adsk.core, adsk.fusion, adsk.cam

# Define the function that will generate the rectangular plate
def run():
    # Get the Fusion 360 application object
    app = adsk.core.Application.get()
    # Get the root component of the active design
    rootComp = app.activeProduct.rootComponent
 
    # Create a new sketch on the XY plane
    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
 
    # Create a rectangle using the sketch
    lines = sketch.sketchCurves.sketchLines
    startPoint = adsk.core.Point3D.create(0, 0, 0)
    endPoint = adsk.core.Point3D.create(20, 0, 0)
    lines.addByTwoPoints(startPoint, endPoint)
    endPoint = adsk.core.Point3D.create(20, 5, 0)
    lines.addByTwoPoints(lines.item(0).endSketchPoint, endPoint)
    endPoint = adsk.core.Point3D.create(0, 5, 0)
    lines.addByTwoPoints(lines.item(1).endSketchPoint, endPoint)
    lines.addByTwoPoints(lines.item(2).endSketchPoint, startPoint)
 
    # Create an extrusion of the sketch to make a 3D solid
    extrudes = rootComp.features.extrudeFeatures
    profile = sketch.profiles.item(0)
    distance = adsk.core.ValueInput.createByReal(10)
    extrude = extrudes.addSimple(profile, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

# Run the function to generate the rectangular plate
run()
