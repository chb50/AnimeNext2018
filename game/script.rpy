# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#TODO: Add backgrounds and sprites where appropriate
#TODO: add audio where appropriate

#TODO: if your are adding more characters, dont forget to update them in pollScore variable as well
define pro = Character("Protagonist")
define chi = Character("Chihiro")
define tsu = Character("Kiyoko")

define user = Character(_("[userName]"), color = "#ff9900")
            
init python:
    pollScore = {"chi": 0, "tsu": 0} #TODO: add more characters here as needed


# The game starts here.

label start:
    ### TEST LABELS ###
    jump round3
        
    ### SCENE: INTRO ###
    
    "School began as any other school day did. It also ended in more or less the same manner."
    "It's what happened {i}after{/i} school that things started to get a little hectic."


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    pro "Chihiro, you gotta slow down! Running in the halls is dangerous, y'know!"
    pro "And you don't have to hold my hand all the way! People are watching!"

    chi "You get to work on your cardio! And Anime Club's about to start, so we can't be late!"
    
    pro "When you coerced me into this club thing, I didn't want it to cause, like, a big stir or something."
    pro "You're not gonna make a huge deal out of this or anything, right?"
    
    chi "Ah, I'll try not to. I know you've wanted to lay low since what happened at archery club..."

    pro "{i}Nothing{/i} happened at archery club."
    
    chi "Ooookayyy. I'm sure it was an accident anyway!"

    "This is Chihiro. She's been my best friend for as long as I can remember. We grew up as next-door neighbors."
    "My parents thought that frequently sticking me as close to her as possible would cause her positive, go-getter attitude to rub off onto me. It's a conniving plan, but I'm onto their game."
    
    chi "We're gonna close that sordid chapter of your past and open a new one with the Anime Club, so big smiles, okay??"
    
    pro "No one wants to see me smile."
    
    chi "That's the spirit! Don't sweat the details, I'm the Vice-Prez, so I already put in a good word for you."
    chi "Ah, here we are!"
    
    scene bg classroom
    
    chi "Here we are! The abandoned classroom on the second floor."

    pro "You sure this is allowed by the school?"

    chi "It's probably not {i}against{/i} the rules..."

    pro "...Well that's {i}very{/I} convincing."
    
    chi "Oh, it's Kiyoko. She's the president of Anime Club! Hi Kiyoko!~"

    tsu "Ah. Is this a new member you brought?"

    chi "Yup! She'll be joining our nakama starting today!"

    tsu "...Oh. I recognize {i}you{/i}."

    pro "What? Did I do something wrong??"

    tsu "You forgot already? Chihiro, isn't she from the school paper? Front page?"

    chi "She was, but..."

    tsu "Something about the catastrophe that befell the archery club?"

    pro "Uhhhh... dunno what you're talking about!"
                                                   
    tsu "Hmph. Are they still fumigating the inside of the walls??"
                                                                   
    chi "I imagine. The flood damage was real bad..."
                                                 
    tsu "Hmph. Not that there's anything dangerous she could use in here."
                          
    pro "Hey guys, change of topic... did anyone else bother showing up today?"
                          
    chi "Aaaah..."
    
    extend "weeeell..."
                          
    tsu "They're cramming for finals instead of honoring their commitments to Anime Club. Like {i}plebians{/i}."
    
    tsu "Disappointing, really. I expected better, but they clearly fabricated their power level readings."

    chi "W-well, people have to mind their studies too..."

    tsu "A proper student minds their studies and practices their craft throughout the year! An unbalanced schedule is an unbalanced life!"
    
    "This Kiyoko person had a fiery passion lingering underneath her icy-cold stare. And her words cut like a katana."
    
    tsu "Alright, you. You have a name?"

    "My name? What was my name...?"
    
    menu:
        "Makoto Shirogane":
            jump m1c1
        "Susan Whitehorse":
            jump m1c2
        "Necromista the Edgewalker":
            jump m1c3
        "RED":
            jump m1c4
    
    label m1c1:
        python:
            userName = "Makoto Shirogane"
            
        tsu "Hm. Disappointing, but I suppose it fits for a dull person."
        jump endm1
        
    label m1c2:
        python:
            userName = "Susan Whitehorse"
            
        tsu "A transfer student? I bet you think that makes you {i}quirky{/i} and {i}interesting{/I} too."
        jump endm1
        
    label m1c3:
        python:
            userName = "Necromista the Edgewalker"
        
        tsu "Uhh... we don't use fake names here. Please leave your freeform jazz at home as well."
        jump endm1
        
    label m1c4:
        python:
            userName = "RED"
        
        tsu "So you're about to start your journey to become a-"
        tsu "H-hey, wait, don't throw me off like that! Jerk!"
        jump endm1
    
    label endm1:
        #game continues
        
    "Kiyoko is... kind of abrasive too. Maybe everyone else at this club is just scared of her." 
    
    chi "...Well! It looks like it's just the three of us in Anime Club today!" 
    
    pro "Is there any paperwork I need to sign? To make it official or anything?"

    tsu "{i}Usually{/i}, we subject our new applicants to a test of strength."

    pro "...What?"

    chi "She usually just makes someone dance at the front of the classroom."

    pro "...I didn't think there'd be hazing in Anime Club of all things."

    tsu "If you can't follow the choreography of your own favorite anime, then you can't call yourself a true otaku!"

    pro "...what is she going on about??"

    chi "Kiyoko used to be a pretty competitive dancer when she was a kid."

    pro "That explains her figure."

    tsu "Pah. It's no fun where there isn't a packed room to watch."

    pro "Aren't hazing rituals against school regulations??"

    tsu "And we can't conclude the club's discussion of {i}Rama-sama's Ramen Saga{/i} with so few people. I marathoned the last hundred pages for nothing..."

    pro "...Is that a new release?"

    chi "It's about a starving university student who attracts the attention of a prestigious cooking school for his reinventions of cheap ramen dishes."

    tsu "It's a modern masterpiece! It has drama, comedy, romance! It transcends the trivialities and trappings of traditional genres!"

    chi "Y-your alliteration is on point today, Kiyoko!"

    pro "...So you're saying it's a manga about ramen."

    tsu "O-of course! It's in the title!"

    chi "I'm getting a little hungry thinking about it..." 

    tsu "It's deep and lovingly crafted, but of course, I wouldn't expect a {i}normie{/i} to grasp the nuances..."
    tsu "Chihiro's the only one who could ever be a worthy match for my esteemed intellect..."

    chi "Omigosh, that's so sweet of you to say!"
    chi "I really treasure our friendship too!"

    tsu "...N-no problem. Don't mention it!"

    "Did those two just have a moment??"

    pro "So it's just us, then? What are we supposed to do?" 
    pro "Do we just, like, turn something on? There's a TV near the front."

    chi "We could do the book club meeting as normal. Everyone else is pretty quiet, so this isn't too different..."

    tsu "They could speak up if they had something to say!"

    pro "I didn't read the manga though? How am I supposed to keep up?"

    chi "Oh you don't have to! It's your first time, so it's okay to sit in and drink in the atmosphere a bit!"

    tsu "Sitting back and contributing nothing. Like a {i}leech.{/i}"

    chi "Did you have a better idea, Kiyoko??"

    tsu "...Hmmmmmm..."
    tsu "...We could make a {i}game{/i} out of it!~"

    pro "I-I don't like that smile she's making..."

    chi "I-it can be a little spooky. Stand your ground."

    tsu "We don't know anything about the newcomer's tastes or preferences. So how about we coax that out of her??"

    pro "Y-you don't have to coax anything, you could just-"

    tsu "We'll hold a debate! And our newcomer will decide who's in the right!"

    pro "...What?"

    chi "It seems you lit something up inside of her after all..."

    tsu "Chihiro always brings out the best in the both of us. We've always stood as diametrically opposed to each other!~"

    chi "I-I mean, it's okay to respect differences in taste. All waifus are precious."

    pro "Wait, are we actually talking about-"

    tsu "The characterization of waifu! ...And husbando too. Husbando are just as important."

    chi "Mmhm! Would you humor us for a bit?"

    "I was stunned. Is this how Anime Clubs really behaved??"

    pro "...I mean, it sounds fun? Don't let me stop you guys from going at it, or whatever."

    ### SCENE: Round 1 ###
    
    #could make this a round 3 subject instead

    chi "Okay! Round 1, fight!~"
    chi "I got one! In {i}Rama-sama Ramen Saga{/i}, there's these two girls who are twins! But they're also super opposite in personalities??"

    tsu "Ah, Netsu and Hiyasu! Good thinking!"

    pro "Who and who??"

    tsu "Two prodigal chefs specializing in complementing and contrasting symbols of yin and yang, carefully balancing opposing flavours to elevate the senses!"

    chi "It was mostly a hot versus cold dynamic. One of them, Hiyasu, specialized in ramen with chilled noodles."

    pro "...why would you have ramen with cold noodles? That sounds kinda gross."

    chi "It kinda does, but... it's delicious! That was the surprising thing!"
    chi "And she was a total sweetheart! She was shy, and soft-spoken, and you really wanted to encourage her to do her best!"

    tsu "Chihiro also goes for the generically saccharine types. So predictable..."

    chi "I-I like a lot of cute girls! Danderes are up there for some of my favs..."

    pro "What's a dandere?"

    tsu "Well, there's a lot of {i}dere{/i} archetypes. It comes from 'deredere'. Or lovey-dovey."
    tsu "The {i}dan{/i} comes from 'danmari'. Which means to shut up or stay calm."

    chi "They're basically abbreviations! So you can think of them like that!"

    pro "...Huh. That's neat."

    tsu "...You seriously didn't know this? We're at a Japanese school..."

    pro "I-I'll take any chance to brush up on my Japanese..."

    chi "Well, anyway! I liked Hiyasu a lot. You really wanted to root for her and have her come out of her shell!"
    chi "Those kind of characters are my super favourites!~"

    "So Chihiro liked soft-spoken and shy girls? Somehow that reminds me of her."
    "I guess she was always the motherly type. Still, it got me thinking. It sounds like a lot of investment..."

    #PRESENTATION CUT

    tsu "Pfft. Netsu's way better. She doesn't beat around the bush and waste time."

    chi "I-it's not a waste of time! It's rewarding emotional investment..."

    tsu "They're always the same pandering otaku fantasies! I like a more exciting flavour!"

    chi "Hum. I suppose you'd be the type to mirror Netsu's hot intensity."

    tsu "Hmph! Intense is right! I don't half-ass anything, and neither does Netsu!"
    tsu "Netsu had her head on straight! Any time the idiot lead got up in his headspace, it was Netsu who smacked him straight!"

    chi "Mmhm. She could be a sweetheart when she wanted to be, between all of the disciplining..."

    tsu "She gets things done!"

    chi "...she's a total tsundere."

    tsu "W-well, I... I {i}guess{/i}, in the technical sense, she is..."

    #muttering
    tsu "...kind of a basic taste to have though..."

    pro "Oh, that one I heard before. When you're mean on the outside but sweet on the inside?"

    chi "Mmhm! Exactly!~"

    tsu "It's in the name. {i}Tsun{/i} comes from 'tsuntsun', meaning 'irritable or aloof'..."
    tsu "...and you already know what the 'dere' comes from. Don't tell me you forgot already..."

    pro "I wouldn't forget that quickly!" 
    pro "I didn't think I'd end up learning stuff here. Thanks Kiyoko!"

    tsu "W-well, if... if you're at Anime Club, you might as well get a lesson in actual Japanese."

    chi "It's not like you like him or anything, riiiight?~"

    tsu "I-it's not like I... {i}q, quiet, you! Stupid!{/i}"

    "So Kiyoko's into tsunderes? Maybe she likes self-inserts..."

    #PRESENTATION CUT

    tsu "Well? What do you think?"

    pro "...Eh? What do I think of what??"

    chi "Who's the winner of this round?"

    pro "I didn't realize I was actually supposed to vote, uh..."

    tsu "It's the point of this entire debate, stupid!"

    pro "I'm just not sure what to vote for! Like..."
    pro "Do I vote for the character type I like more? Which argument was better?"
    pro "Whatever point those guys up front made the most sense?"

    chi "What guys?"

    pro "N-nothing..."

    chi "Well... I guess any reason to vote is fine. Voting for your beliefs serves as the foundation of a free democracy after all!"

    tsu "And you {i}better{/i} not vote for the option that you think one of us will like more! This isn't some trashy VN!"

    pro "Well of course, this is real life. Nothing's more real than arguing over anime."

    #TODO: Twilio poll here
    
    label poll1Chi:
        chi "Woo! I argued the thingie better!"
        tsu "Tch. This isn't even my final form."
        python:
            pollScore["chi"] = pollScore["chi"] + 1
        jump endpoll1
    label poll1Tsu:
        tsu "Alright! President Kiyoko draws first blood!"
        chi "Th-this isn't {i}that{/i} kind of contest...!"
        python:
            pollScore["tsu"] = pollScore["tsu"] + 1
        jump endpoll1
    
    label endpoll1:
        #game continues
    
    ### SCENE: Round 2 ###
    
    chi "Okay, okay, we're gonna change gears!"
    
    tsu "Eh? But this is my game, you can't just-"
    
    chi "We should talk about husbandos! Can we?"
    
    tsu "...Huh. Not a bad idea, surprisingly."
    
    pro "Eh? I thought this was just gonna be about waifus."
    
    chi "We talk about whoever we really like! They don't have to be cute girls!"
    
    tsu "Yeah, it's 2018. Get with the times."
    
    pro "I-I'm not against it, I was just... okay, cool."
    pro "So {i}Ramen Saga{/i} has husbandos too?"
    
    tsu "It was originally released as a best-selling visual novel. They went overboard with the routes they tacked on..."
    
    chi "They advertised it as a harem-style adventure!"
    
    pro "Of course. Harem endings."
    
    tsu "As I recall, the adaptation took, ah, creative liberties... but Kazama and Hiro made the jump to the small screen remarkably well."
    
    chi "Hiro's adorable! He has the best comedy scenes."
    
    tsu "Urgh, really? He looks more like the parody version of a bishonen lead..."
    
    chi "Well, yeah, he's obsessed with his appearance, but he's secretly a huge dork! He got the best comedy scenes!~"
    chi "And he has the best design too!"
    
    tsu "Heh. I figured someone like you would have such juvenile tastes."
    
    chi "I-it's not wrong to like pretty boys... pretty boys deserve love too!"
    
    "Chihiro seemed to be into bishonen characters. The prototypical pretty boy with effeminate features."
    "Wonder what the appeal is. It's probably in their design..."

    #PRESENTATION CUT

    tsu "Well, thank you for sharing that. It's pedestrian, but we're entitled to our opinions."
    tsu "I should remind you however, {i}my{/i} tastes are a lot more cultured and refined."
    
    chi "Oh don't tell me you like Kazama..."
    
    tsu "He's good for drama! Without him, there wouldn't be anything to talk about!"
    tsu "He's cold, calculating, willing to do whatever it takes to succeed..."
    tsu "And that intimidating look he gives Rama-sama when they first met... oooh, it gives me the tingles!~"
    
    "Calm down, Kiyoko, this is a classroom setting..."
    
    chi "But he's a jerk! He's condescending, conceited"
    chi "...and he put too much salt in Rama-sama's broth!"
    
    tsu "It was a power play!"
    
    chi "It was {i}cheating!{/i}"
    
    pro "Did you guys consult the official {i}Rama-sama Ramen Saga{/i} Rulebook?"
    
    chi "I-I doubt there is such a thing... either or, Kazama's a jerk!"
    
    tsu "But he does it all in such a cool, dashing way!~"
    
    chi "B-but wouldn't you rather have a charming, friendly guy who cares for your wellbeing?"
    
    tsu "And I suppose you'd want to hold hands and blush too? {i}Please.{/i}"
    
    tsu "I'm a third-year, I'm getting too old to indulge in fluffy nonsense like that!"
    
    "Kiyoko was utterly smitten by bad boys, it seemed. Not exactly an uncommon opinion."
    "It's a cute enough fantasy, but it's a weirdly specific one? I don't think I get it..."

    #TODO: Twilio poll here
    
    label poll2Chi:
        chi "Score one for the cute guys!"
        tsu "What's that supposed to mean? They're {i}both cute{/i}, stupid."
        python:
            pollScore["chi"] = pollScore["chi"] + 1
        jump endpoll2
    label poll2Tsu:
        tsu "Heheh! I didn't expect anything less!"
        chi "I-I want a recount, that can't be right... something's fishy!"
        python:
            pollScore["tsu"] = pollScore["tsu"] + 1
        jump endpoll2
    
    label endpoll2:
        #game continues
    
    ### SCENE: Round 3 ###
    
    label round3:
        #game continues
    
    pro "That's two rounds down. Jeez, you guys really get into this, don't you..."
    
    python:
        charTied = 1
        for char in pollScore:
            for compChar in pollScore:
                if char != compChar and pollScore[char] != pollScore[compChar]:
                    charTied = 0
                    break
        
    if charTied:
         #if it's tied up
        chi "Okay! It's time for the third and final round!"
        
        tsu "Mrgrgr... can't believe it's still tied up. I should've closed this off by now."
        tsu "Nuts to that! I got the final round!"
        
        pro "Getting surprisingly competitive over here. I didn't think you two would be getting so into it."
        
        chi "Anime Club is serious business!"
        
        tsu "Yeah, super serious! Try and keep up!"
        
        pro "I'm getting a pretty clear picture of why no one else bothered to show up..."
        
    else:
        #if one of the girls is leading by 2 already
        chi "Okay! It's time for the third and final round!"
        
        pro "Wait, do we have to? Someone's already leading two nothing"
        
        chi "We're having fun, right? We don't have to stop cuz of what's on the scoreboard..."
        
        pro "Well, yeah, we are, but-"
        
        tsu "The people running this prepared three rounds of this stuff, so we gotta go through with all of them. Them's the rules."
        
        pro "Who?? You're the president. That means you're making up the rules, right??"
        
        "...A hushed silence fell upon the classroom."
        
        pro "I-I'm not sure I get it, but okay, let's go..."
        
        chi "Yaaay!~"

    pro "So what else's left on the menu?"
    
    chi "Hmmmm... we could talk about {i}Rama-sama's Ramen Saga{/i} some more! There were a few other waifus..."
    
    pro "This isn't a harem anime, right?"
    
    tsu "It's a very personal story about finding strength through the support of others!"
    
    pro "Harem anime, got it."
    
    chi "Oh, we could talk about the two most important girls, Rena and Kotone!"
    chi "Rena's the cute, exuberant, and familiar next-door neighbor of Rama-sama, and Kotone is a mysterious visitor who whisks him away from his usual life!"
    
    "I nodded my head, trying to follow along. I should've studied up on this show before coming here..."
    
    pro "So which one do you like?"
    
    chi "Oh, I dug Kotone! She's so cool, super mysterious, and distant... She barely says a word, but she has so much presence!"
    chi "And you never really get a good read on her until the big reveal when you find out she's an-"
    
    tsu "Chihiro! Spoilers!"
    
    chi "A-ack! S-sorry, I... that was close..."
    
    pro "...Guess I dodged a bullet there?"
    
    chi "She's central to the whole story! You gotta finish the rest of it!"
    chi "You just kind of see her and you {i}know{/i} she's gonna be super important and knowledgeable!"
    
    pro "...So she's a mysterious waifu? How do you know you like her if you don't know anything about her?"
    
    chi "W-well, it's not like you know {i}nothing{/i} about her, you just... get invested in her!"
    chi "And she delivers! Ohhh boy does she deliver!~"
    
    "Well Chihiro seems particularly interested in the silent and mysterious type. Still, there has to be something more to it..."

    #PRESENTATION CUT 

    tsu "Of course, Chihiro has always gravitated to those with otherworldly knowledge and insight!"
    tsu "That's why she sought me out after all! Hohoho!~"
    
    chi "...Mm... I don't get that vibe from you though."
    
    tsu "Eh!? Are you calling me stupid!?"
    
    chi "No! I would never-"
    
    pro "I dunno, I think she was calling you stupid."
    
    chi "Don't incense her, that's not what I meant!"
    
    tsu "Anyway, Kotone is not much more than a token plot-thread. Rena's way better."
    
    pro "Huh. She didn’t strike me as your preference."
    
    tsu "....I can like gentle characters too..."
    
    pro "Huh?"
    
    tsu "I mean, she's reliable, and kind, and always supports Rama-sama! Because they're best friends."
    tsu "It's a familiar relationship. Cozy, nice. I like it!"
    tsu "The pacing doesn't always have to be operating at 100% y'know."
    
    chi "She says as she shames the club for minding their studies..."
    
    tsu "This isn't an anime, Chihiro!"
    
    "So Kiyoko liked the childhood, best friend character? That's still a pretty unexpected choice, coming from her, but I can kind of see it."
    "Still, I have to wonder what that's about..." 

#PRESENTATION CUT

    #TODO: Twilio poll here
    
    label poll3Chi:
        chi "Yay! Mystery solved!~"
        tsu "Hmph. Call it a curious case of crummy taste..."
        python:
            pollScore["chi"] = pollScore["chi"] + 1
        jump endpoll3
    label poll3Tsu:
        tsu "Well, it was obvious that the power of love would win out in the end!~"
        chi "But they aren't even dating in the anime..."
        python:
            pollScore["tsu"] = pollScore["tsu"] + 1
        jump endpoll3
    
    label endpoll3:
        
    
    
    ##################################### SPLIT CODE IF NEEDED HERE ####################################################
    
    ### ROUTE SELECT: TSUNDERE ROUTE ###
    label routeTsu:
    
        tsu "Ohoho!~ Like there was ever any doubt!"

        chi "Ah, she's been practicing her ojou-sama laugh for just such an occasion..."

        pro "It sounded like she had something caught in her windpipe."

        tsu "Ah, those glowering expressions are {i}such{/i} a killjoy. I'm a gracious winner!"

        chi "Yeah, it was fun! And we all got to learn more about each other and what we like!~"

        pro "Who knew arguing about your favourite characters could be such an {i}intimate{/i} bonding experience..."

        tsu "Y-you don't have to be so sarcastic about it!"

        pro "So, uh, what do we do now? Anime Club's almost over by now, right?"

        tsu "Mm, true. I could spare some time to sort out your paperwork... what will you do, Chihiro?"

        chi "Aaaah... well, we usually walk home, but that sounds like a good idea too!"
        chi "Truthfully, I gotta get going anyway, I have a big test to study for!"

        pro "Oh right, for calculus right? Better hit the books hard!"

        chi "Hehehe! I remember when math used to be fun..."
        chi "Anyway, I gotta go! Byeee!~"

        "Scampering out the door, Chihiro soon left me alone with Kiyoko."
        "Silence hung between us. Kiyoko was pretty fun, but it still felt like being introduced to a friend of a friend."

        pro "...Well, uh... was I supposed to bring anything?"

        tsu "N-no, no, not really. I just need you to go over our constitution real quick."
        tsu "...Nnngh. Chihiro writes too small, I can barely make this out."

        "Reaching into her knapsack, Kiyoko pulled out a small pair of reading glasses, going over the letter-print."
        tsu "You must attend at least one meeting a month. You must engage with tasteful, school-appropriate material. You are eligible to one viewing party recommendation..."

        pro "...Huh."

        tsu "What? This is simple stuff. Don't tell me I’ve lost you already."

        pro "No, I just... didn't expect you to have a pair of reading glasses on hand."

        tsu "...I-it's not a big deal. I have troubles with fine print. I'm a little short-sighted."
        tsu "B-but there's nothing wrong with that! I'm flawless otherwise!"

        pro "They're kinda cute, though..."

        tsu "'Cute'?? They're for vision-correction! I've no used for a, a cloying fashion accessory!"

        pro "It's not an insult or anything! Chihiro wears glasses too, and everyone thinks she's cute!"

        tsu "...Nnnn..."
        tsu "She's just cute in the pedestrian way though. The normies go for it..."

        "She groaned aloud, putting down the pamphlet."
        "There's probably something more to the whole glasses thing though..."

        #PRESENTATION CUT

        tsu "I don't wanna wear my glasses too much around school. I get by fine as it is."
        tsu "Besides, everyone looks at me different when they do. I can't command respect like that!"

        pro "Are you sure you want to command respect?"

        tsu "Wh, what else would I want??"

        pro "Based on the way you were blushing, I'd think you'd be happy if someone called you a cutie like Chihiro."

        tsu "Th-that's baseless conjecture!!"
        tsu "I, eh, ahem... c-can we just get through your paperwork?"

        pro "I didn't bring a pen though-"

        tsu "USE MINE!"

        pro "Okay, okay! ...Ouch, don't spear me with it!"

        "The new few minutes were spent marking my name on an assortment of forms."
        "That day, I confirmed my extracurricular membership into the Anime Club."
        "It beats going straight home every single day of school. Kiyoko can get to be a handful though."
        "She's eccentric, but she attracts her own little cult of personality. I imagine she wouldn't have it any other way."

        jump gameEnd
    
    label routeChi:
        chi "Me! Oh, I don't win very often! How exciting!"
        chi "Okay, okay, I'd like to thank my mom and dad, and my coach for believing in me..."
        chi "...OH! And all my friends at the academy!~"
        
        tsu "Well. She seems pleased with herself."
        
        pro "You don't have to get pouty about it. It was a fun way to talk about stuff you like."
        
        chi "Yeah! And when it's a game, you gotta take it super seriously too!"
        chi "I had fun! This was a great idea, Kiyoko!~"
        
        tsu "...Eh, eheh, you, uh... you don't have to flatter me..."
        
        chi "How about it? You wanna do it again sometime??"
        
        pro "Might be fun, but... Anime Club's over by now, right?"
        
        tsu "Ah, technically? We reconvene every Tuesday and Thursday."
        
        pro "Alright, I'll try to make the next one. ...So long as exams don't get in the way."
        
        chi "You wanna walk home?"
        
        pro "It's tradition at this point. What are you gonna do, Kiyoko?"
        
        tsu "Well, our secretary didn't make it out so... I'll have to jot the meeting notes myself."
        
        chi "Be sure to note who {i}actually{/i} won our little contest, okayyy?~"
        
        tsu "I-I-I wouldn't dream of sullying our club's name with lies and slander! How dare you??"
        
        pro "Oh no, you're setting her off again. We should get going."
        
        chi "Okay! I need to hit my locker first!~"

        scene hallway

        "Heading over to Chihiro's locker, she gathers her things in short order, readying for our regular commute home."
        
        chi "Hey, I was thinking about something random!"
        
        pro "Hm? What?"
        
        chi "Do you like having a cute girl by your side to walk home with at the end of each day, every day?"
        
        pro "Well, I mean, sure. We're friends. What, did you wanna shake up the routine a bit?"
        
        chi "N-no, that's not what I meant, I just... thought it was a cute thought, being together everyday..."
        chi "...B-but not in a creepy, yandere way!"
        
        pro "...Huh?"
        
        chi "I-I mean, unless you liked it that way-"
        
        pro "N-no, no, I... I like where we're at right now. With the walking to and from school thing. Very casual."
        
        chi "It's kind of a weird thing to think about though, right? Yandere girlfriends?"
        
        pro "Isn't that just a flighty way of calling someone a 'stalker'?"
        
        chi "Hehehe~! I guess? But they're pretty popular too!"
        chi "Something about another person uncompromisingly in love with you is... kinda romantic, in a weird way!"
        
        pro "...I could do without the stabbings, though. And how do you introduce someone like that to your family?"
        
        chi "You don't."
        extend "Generally speaking."
        
        pro "You sound like you thought about this stuff a lot..."
        
        chi "I-it's fun to fantasize about!"
        
        "Chihiro was pretty gentle and peaceful, but sometimes you gotta wonder if one of your best friends is about to just fling themselves off the deep end."
        "And now she's planted that little germ of a thought in my head..."

        #PRESENTATION CUT

        pro "Well, Chihiro, you've given me a lot to think about."
        
        chi "Mmhm! I knew you'd have a lot of fun at Anime Club!~"
        
        pro "I had my doubts. I figured you were just fishing to assimilate me into the hivemind."
        
        chi "Ahhh, it's not really a hivemind! Kiyoko wishes she could be a queen bee though..."
        
        pro "Of course, I might have to refer you to a psychiatrist to poke at your head a bit..."
        
        chi "J-just because I like reading about psychopaths doesn't make me one! It's relaxing!"
        
        pro "I-I'm not here to judge. We should get going though, it's getting late."
        
        chi "Oh! Right, and I have to study! See you another time?"
        
        pro "Definitely."
        
        jump gameEnd



    # This ends the game.

    return
