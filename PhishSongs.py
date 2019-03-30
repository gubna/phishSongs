# The jamband Phish has been playing together for over 30 years and have a library of 290 songs.
# This program randomly generates one of their songs. For all the wooks out there.

import random
from tkinter import *
from PIL import ImageTk, Image
import os


root = Tk()
canvas = Canvas(root, width = 800, height = 525)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Beth\Documents\python\Phish\phFB.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)

phishsongs = ["46 Days", "A Song I Heard the Ocean Sing","AC/DC Bag","Access Me","Acoustic Army","Aftermath", "Alaska",
              "Albert","All of These Dreams","All Things Reconsidered","Alumni Blues","Anarchy","And So To Bed",
              "Anything But Me","Architect","Army of One","At the Barbecue","Avenu Malkenu","Axilla","Axilla Part II",
              "Babylon Baby","Back on the Train","Backwards Down the Number Line","Backwards Food for Backwards Folks",
              "Bathtub Gin","Beauty of a Broken Heart","Big Ball Jam","Big Black Furry Creature from Mars",
              "Billy Breathes", "Birds of a Feather","Birdwatcher, The","Bittersweet Motel","Bliss","Blue Over Yellow",
              "Bouncing Around the Room","Brian and Robert","Brother","Bubble Wrap","Buffalo Bill","Bug","Buried Alive",
              "Burn That Bridge", "Bye Bye Foot","Camel Walk","Can't Come Back","Carini","Cars Trucks Buses","Catapult",
              "Cataract Song","Cavern", "Chalkdust Torture","Character Zero","Clone","Colonel Forbin's Ascent",
              "Connection, The","Contact","Crowd Control","Curtain, The","Curtain With, The","Dave's Energy Guide",
              "David Bowie","Dear Mrs. Reagan","Demand", "Den of Iniquity","Destiny Unbound","Dinner and a Movie",
              "Dirt","Discern","Divided Sky, The","Dog Faced Boy", "Dog Log","Dogs Stole Things","Don't Get Me Wrong",
              "Down With Disease","Dr. Gabel","Drifting","Driver","Eliza", "End of Session","Esther","Faht","Farmhouse",
              "Fast Enough for You","Fee","Fikus","Final Flight","First Tube", "Fish Bass","Flat Fee","Fluff's Travels",
              "Fluffhead","Fly Famous Mockingbird","Foam","Frankie Says","Free", "Friday","Fuck Your Face","Gatekeeper",
              "Ghost","Glide","Glide II","Golgi Apparatus","Gone","Gotta Jibboo","Grind","Guantanamo Strut",
              "Guelah Papyrus","Gumbo","Guy Forget","Guyute","Ha Ha Ha","Halfway to the Moon", "Halley's Comet",
              "Happy Whip and Dung Song, The","Harpua","Harry Hood","He Ent to the Bog","Heartache","Heavy Things",
              "Horn","Horse, The","I Am Hydrogen","I Been Around","I Didn't Know","Icculus","Idea","If I Could",
              "If I Told You","In a Hole","In a Misty Glade","Ingest","Inlaw Josie Wales, The","Insects","Invisible",
              "It's Ice","Jaegermeister Song","Jennifer Dances","Joy","Julius","Keyboard Army","Kill Devil Falls",
              "Kung", "Landlady, The","Last Victor Jam","Lawn Boy","Lazy and Red","Lengthwise","Leprechaun",
              "Let Me Lie","Letter to Jimmy Page","Lifeboy","Light","Limb By Limb","Liquid Time","Lizards, The",
              "Llama","Lushington","Maggie's Revenge","Magilla","Makisupa Policeman",
              "Man Who Stepped Into Yesterday, The","Mango Song, The","Maze", "McGrupp and the Watchful Hosemasters",
              "Meat","Meatstick, The","Mexican Cousin","Mike's Song","Minkin","Mock Song","Moma Dance, The","Montana",
              "Mound","Mountains in the Mist","Mozambique","Mr. Completely","My Friend, My Friend","My Left Toe",
              "My Problem Right There","My Sweet One","N02","Name Is Slick, The","Never","NICU","No Dogs Allowed",
              "Nothing","Ocelot","Oh Kee Pa Ceremony, The","Only a Dream","Party Time","Pebbles And Marbles","Pigtail",
              "Piper","Poor Heart","Possum","Practical Song, The","Prep School Hippie","Prince Caspian",
              "Punch Me in the Eye","Punch You in the Eye","Quadrophonic Toppling","Reba","Revolution",
              "Rift","Riker's Mailbox","Rocka William","Roggae","Round Room","Run Like An Antelope","Runaway Jim",
              "Running Scared","Sample in a Jar","Sand","Sanity","Saw it Again","Scent of a Mule",
              "Scents and Subtle Sounds","Secret Smile","Setting Sail","Seven Below","Shafty","Show of Life","Shrine",
              "Silent in the Morning","Simple","Skippy the Wondermouse","Sky Train Wand","Slave to the Traffic Light",
              "Sleep","Sleep Again","Sleeping Monkey","Sloth, The","Somantin","Sparkle","Spices","Splinters of Hail",
              "Split Open and Melt","Spock's Brain","Spread it Round","Squirming Coil, The","Stash",
              "Stealing Time From The Faulty Plan","Steam","Steep","Strange Design","Sugar Shack","Summer of '89",
              "Susskind Hotel","Suzy Greenberg","Swept Away","Talk","Taste","Tela","Theme From the Bottom",
              "Thunderhead","Time Turns Elastic","Tiny","Title Track","Tomorrow's Song","Train Song","Tube","Tweezer",
              "Tweezer Reprise","Twenty Years Later","Twist","Two Versions of Me","Undermind","Union Federal",
              "Victor Jam Session","Vultures","Wading in the Velvet Sea","Waking Up","Walfredo","Walls Of The Cave",
              "Waste","Water in the Sky","Waves","Wedge The","Weekapaug Groove","Weekly Time","Weigh",
              "What Things Seem","What's the Use?","Wilson","Windora Bug","Windy City","Wolfman's Brother","Wombat",
              "You Enjoy Myself"]

print(random.choice(phishsongs))
print('\nBy The Phish From Vermont\n')

root.mainloop()