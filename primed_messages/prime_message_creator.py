import json

messages=[
    ["open app","app = adsk.core.Application.get()"],
    ["open ui","ui = app.userInterface"],
    ["open design","design = adsk.fusion.Design.cast(app.activeProduct)"],
    ["Get the root component of the active design","root = design.rootComponent"],
    ["Create a new sketch on the xy plane.","sketches = rootComp.sketches \n xyPlane = rootComp.xYConstructionPlane \n sketch = sketches.add(xyPlane)"],
    ["Draw a circles","circles = sketch.sketchCurves.sketchCircles \n circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 1)"],
    ["Draw line","lines = sketch.sketchCurves.sketchLines; \n line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(3, 1, 0))"],
    ["A simple way of creating typical extrusions (extrusion that goes from the profile plane the specified distance).Define a distance extent of 5 cm","distance = adsk.core.ValueInput.createByReal(5) \n extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)"],
    ["Draw a line to use as the axis of revolution","lines = sketch.sketchCurves.sketchLines \n axisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, -5, 0), adsk.core.Point3D.create(1, -5, 0))"],
    ["Creates a new revolve feature, resulting in a new component","# Get the profile defined by the circle \n prof = sketch.profiles.item(0) \n "],
    ["Get the profile defined by the circle","prof = sketch.profiles.item(0)"],["Create an revolution input to be able to define the input needed for a revolution while specifying the profile and that a new component is to be created","revolves = rootComp.features.revolveFeatures \n revInput = revolves.createInput(prof, axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)"],
]

# # create a list of dictionaries
# l=[]
# for i in range(len(messages)):
#     l.append({"role": "system", "name":"example_user", "content": messages[i][0]})
#     l.append({"role": "system", "name":"example_assistant", "content": messages[i][1]})

# # write list to file
# with open("./primed_message.json", "w") as outfile:
#     json.dump(l, outfile)

# # read file
with open("./primed_message.json", "r") as read_file:
    data = json.load(read_file)
print(data)