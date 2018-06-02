# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#TODO: Add backgrounds and sprites where appropriate
### BACKGROUNDS ###

image classroom = im.Scale("bgs/classroom.png", 1920, 1080)
image classroomevening = im.Scale("bgs/classroom evening.png", 1920, 1080)
image hallway = im.Scale("bgs/hallway school.png", 1920, 1080)
image hallwayevening = im.Scale("bgs/hallway school evening.png", 1920, 1080)


#TODO: add audio where appropriate

#TODO: if your are adding more characters, dont forget to update them in pollScore variable as well
define pro = Character("Protagonist", callback=speaker("pro"))
define user = Character(_("[userName]"), color = "#ff9900")

##DYNAMIC CHARACTER LABBING SECTION##

define chi = Character("Chihiro", callback=speaker("chi"))
define tsu = Character("Kiyoko", callback=speaker("tsu"))

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages("sprites")
    layerorder = ['base','blush','mouth','eyes','brow','optional']
    DefineImages("sprites", overrideLayerOrder=layerorder)

    #use map emotes to compile complex emotions with layers
    MapEmote('chi pity', 'chi base ed sad md default')
    MapEmote('chi pityc', 'chi base ec sad md default')
    MapEmote('chi defaultc', 'chi base ec default md default')
    MapEmote('chi neutral', 'chi base ed default md sad')
    MapEmote('chi neutralc', 'chi base ec default md sad')
    MapEmote('chi feisty', 'chi base ed angry md default')
    MapEmote('chi feistyc', 'chi base ed angry md default')
    MapEmote('chi feistyc', 'chi base ec angry md angry')
    MapEmote('chi angryc', 'chi base ec angry md sad')
    MapEmote('chi annoyed', 'chi base ed angry md sad')
    MapEmote('chi sadc', 'chi base ec sad md sad')

    MapEmote('tsu neutral', 'tsu base ed default md sad')
    MapEmote('tsu neutralc', 'tsu base ec default md sad')
    MapEmote('tsu glare', 'tsu base ed angry md sad')
    MapEmote('tsu smirk', 'tsu base ed angry md happy')
    MapEmote('tsu smirkc', 'tsu base ec angry md happy')
    MapEmote('tsu angryc', 'tsu base ec angry md sad')
    MapEmote('tsu sadc', 'tsu base ec sad md sad')
    MapEmote('tsu happyc', 'tsu base ec happy md happy')

    MapEmote('tsu neutralg', 'tsu base ed default md sad glasses')
    MapEmote('tsu neutralcg', 'tsu base ec default md sad glasses')
    MapEmote('tsu glareg', 'tsu base ed angry md sad glasses')
    MapEmote('tsu smirkg', 'tsu base ed angry md happy glasses')
    MapEmote('tsu smirkcg', 'tsu base ec angry md happy glasses')
    MapEmote('tsu angrycg', 'tsu base ec angry md sad glasses')
    MapEmote('tsu sadcg', 'tsu base ec sad md sad glasses')
    MapEmote('tsu happycg', 'tsu base ec happy md happy glasses')



init python:
    pollScore = {"chi": 0, "tsu": 0} #TODO: add more characters here as needed

## SPRITES ##

# The game starts here.