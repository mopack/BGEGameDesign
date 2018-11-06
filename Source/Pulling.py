import bge
cont = bge.logic.getCurrentController()
own = cont.owner

space = cont.sensors["space"]
pull = cont.actuators["pull"]
fire = cont.actuators["fire"]
launcher = bge.logic.getSceneList()[0].objects["arrow_launcher"]

if space.positive:
    pull.frameStart = 1
    pull.frameEnd = 40
    cont.activate(pull)

else:
    launcher.actuators["add_arrow"].linearVelocity = [-(pull.frame*15),0,0]
    pull.frameStart = 41
    pull.frameEnd = 46
    cont.activate(pull)
    cont.activate(fire)