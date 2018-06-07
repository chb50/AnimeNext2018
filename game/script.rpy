label start:

#FLAGS
    $ chihiro = 0
    $ kiyoko = 0

    ### SCENE: INTRO ###

    python:
        userName = "protag"
    
    scene black with dissolve
    play music vn fadein 1.0
    "School began as any other school day did. It also ended in more or less the same manner."
    "It's what happened {i}after{/i} school that things started to get a little hectic."


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hallway with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    voice "voice/pro intro 1.ogg"
    pro "Chihiro, you gotta slow down! Running in the halls is dangerous, y'know!"

    voice "voice/pro intro 2.ogg"
    pro "And you don't have to hold my hand all the way! People are watching!"

    show chi default with dissolve
    voice "voice/chi intro 1.ogg"
    chi "You get to work on your cardio! And Anime Club's about to start, so we can't be late!"

    voice "voice/pro intro 3.ogg"
    pro "When you coerced me into this club thing, I didn't want it to cause, like, a big stir or something."

    voice "voice/pro intro 4.ogg"
    pro "You're not gonna make a huge deal out of this or anything, right?"

    show chi pity
    voice "voice/chi intro 2.ogg"
    chi "Ah, I'll try not to. I know you've wanted to lay low since what happened at archery club..."

    voice "voice/pro intro 5.ogg"
    pro "{i}Nothing{/i} happened at the archery club."

    show chi pityc
    voice "voice/chi intro 3.ogg"
    chi "Ooookayyy. I'm sure it was an accident anyway!"

    show chi default
    "This is Chihiro. She's been my best friend for as long as I can remember. We grew up as next-door neighbors."
    "My parents thought that frequently sticking me as close to her as possible would cause her positive, go-getter attitude to rub off onto me. It's a conniving plan, but I'm onto their game."

    voice "voice/chi intro 4.ogg"
    chi "We're gonna close that sordid chapter of your past and open a new one with the Anime Club, so big smiles, okay??"

    voice "voice/pro intro 6.ogg"
    pro "No one wants to see me smile."

    show chi defaultc
    voice "voice/chi intro 5.ogg"
    chi "That's the spirit! Don't sweat the details, I'm the Vice-Prez, so I already put in a good word for you."

    show chi default
    voice "voice/chi intro 6.ogg"
    chi "Ah, here we are!"

    scene classroom with dissolve

    show chi defaultc zorder 2 with easeinright:
        align (0.65, 1.0)
    voice "voice/chi intro 7.ogg"
    chi "Here we are! The abandoned classroom on the second floor."

    voice "voice/pro intro 7.ogg"
    pro "You sure this is allowed by the school?"

    show chi pityc
    voice "voice/chi intro 8.ogg"
    chi "It's probably not {i}against{/i} the rules..."

    voice "voice/pro intro 8.ogg"
    pro "...Well that's {i}very{/I} convincing."

    show tsu neutral zorder 2 with dissolve:
        align (0.35, 1.0)
    "Looking back into the room, I spot a red-headed girl in our uniform. I've seen her around the school; she had something of a reputation."

    show tsu glare
    show chi default
    "Not that we ever interacted much. Still, she was giving me... quite the dirty look."
    "Somehow, I felt like I was intruding on her den. Was she trying to memorize my scent?"

    show chi defaultc
    voice "voice/chi intro 9.ogg"
    chi "Oh, it's Kiyoko. She's the president of Anime Club! Hi Kiyoko!~"

    show tsu neutral
    voice "voice/Kiyoko_Line_1.ogg"
    tsu "Ah. Is this a new member you brought?"

    show chi default
    voice "voice/chi intro 10.ogg"
    chi "Yup! She'll be joining our nakama starting today!"

    show tsu smirk
    voice "voice/Kiyoko_Line_2.ogg"
    tsu "...Oh. I recognize {i}you{/i}."

    show chi neutral
    voice "voice/pro intro 9.ogg"
    pro "What? Did I do something wrong??"

    show tsu angryc
    voice "voice/Kiyoko_Line_3.ogg"
    tsu "You already forgot? Chihiro, isn't she from the school paper? Front page?"

    show chi sad
    voice "voice/chi intro 11.ogg"
    chi "She was, but..."

    show tsu neutral
    voice "voice/Kiyoko_Line_4.ogg"
    tsu "Something about the catastrophe that befell the archery club?"

    voice "voice/pro intro 10.ogg"
    pro "Uhhhh... dunno what you're talking about!"

    show tsu happy
    voice "voice/Kiyoko_Line_5.ogg"
    tsu "Hmph. Are they still fumigating the inside of the walls??"

    show chi sadc
    voice "voice/chi intro 12.ogg"
    chi "I imagine. The flood damage was real bad..."

    show tsu neutral
    voice "voice/Kiyoko_Line_6.ogg"
    tsu "Hmph. Not that there's anything dangerous she could use in here."

    show chi neutral
    voice "voice/pro intro 11.ogg"
    pro "Hey guys, change of topic... did anyone else bother showing up today?"

    show chi sad
    show tsu sad
    voice "voice/chi intro 13.ogg"
    chi "Aaaah..."

    show chi sadc
    voice "voice/chi intro 14.ogg"
    extend "weeeell..."

    show tsu angryc
    voice "voice/kiyoko plebs.ogg"
    tsu "They're cramming for finals instead of honoring their commitments to Anime Club. Like {i}plebeians{/i}."

    show tsu sadc
    voice "voice/Kiyoko_Line_8.ogg"
    tsu "Disappointing, really. I expected better, but they clearly fabricated their power level readings."

    show chi pity
    voice "voice/chi intro 15.ogg"
    chi "W-well, people have to mind their studies too..."

    show tsu glare
    show chi neutral
    voice "voice/Kiyoko_Line_9.ogg"
    tsu "A proper student minds their studies and practices their craft throughout the year! An unbalanced schedule is an unbalanced life!"

    "This Kiyoko person had a fiery passion lingering underneath her icy-cold stare. And her words cut like a katana."

    show chi default
    show tsu neutral
    voice "voice/Kiyoko_Line_10.ogg"
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

        show tsu neutralc
        voice "voice/Kiyoko_Line_11.ogg"
        tsu "Hm. Disappointing, but I suppose it fits for a dull person."
        jump endm1

    label m1c2:
        python:
            userName = "Susan Whitehorse"

        show tsu glare
        voice "voice/Kiyoko_Line_12.ogg"
        tsu "A transfer student? I bet you think that makes you {i}quirky{/i} and {i}interesting{/I} too."
        jump endm1

    label m1c3:
        python:
            userName = "Necromista the Edgewalker"

        voice "voice/Kiyoko_Line_13.ogg"
        show tsu sad
        tsu "Uhh... we don't use fake names here. Please leave your freeform jazz at home as well."
        jump endm1

    label m1c4:
        python:
            userName = "RED"

        show tsu smirkc
        voice "voice/Kiyoko_Line_14.ogg"
        tsu "So you're about to start your journey to become a-"

        show tsu glare
        show chi defaultc
        voice "voice/Kiyoko_Line_15.ogg"
        tsu "H-hey, wait, don't throw me off like that! Jerk!"
        jump endm1

    label endm1:
        #game continues

    "Kiyoko is... kind of abrasive too. Maybe everyone else at this club is just scared of her."

    show chi sad
    voice "voice/chi intro 16.ogg"
    chi "...Well! It looks like it's just the three of us in Anime Club today!"

    show tsu neutral
    voice "voice/pro intro 12.ogg"
    pro "Is there any paperwork I need to sign? To make it official or anything?"

    show chi neutral
    show tsu smirkc
    voice "voice/Kiyoko_Line_16.ogg"
    tsu "{i}Usually{/i}, we subject our new applicants to a test of strength."

    show tsu default
    voice "voice/pro intro 13.ogg"
    pro "...What?"

    show chi pity
    voice "voice/chi intro 17.ogg"
    chi "She usually just makes someone dance at the front of the classroom."

    show tsu glare
    voice "voice/pro intro 14.ogg"
    pro "...I didn't think there'd be hazing in Anime Club of all things."

    voice "voice/Kiyoko_Line_17.ogg"
    tsu "If you can't follow the choreography of your own favorite anime, then you can't call yourself a true otaku!"

    show chi neutral
    voice "voice/pro intro 15.ogg"
    pro "...what is she going on about??"

    show chi neutral
    voice "voice/chi intro 18.ogg"
    chi "Kiyoko used to be a pretty competitive dancer when she was a kid."

    voice "voice/pro intro 16.ogg"
    pro "That explains her figure."

    show tsu sad
    voice "voice/Kiyoko_Line_18.ogg"
    tsu "Pah. It's no fun where there isn't a packed room to watch."

    voice "voice/pro intro 17.ogg"
    pro "Aren't hazing rituals against school regulations??"

    show tsu sadc
    voice "voice/Kiyoko_Line_19.ogg"
    tsu "And we can't conclude the club's discussion of {i}Rama-sama's Ramen Saga{/i} with so few people. I marathoned the last hundred pages for nothing..."

    show chi sad
    voice "voice/pro intro 18.ogg"
    pro "...Is that a new release?"

    show chi default
    voice "voice/chi intro 19.ogg"
    chi "It's about a starving university student who attracts the attention of a prestigious cooking school for his reinventions of cheap ramen dishes."

    show tsu glare
    voice "voice/Kiyoko_Line_20.ogg"
    tsu "It's a modern masterpiece! It has drama, comedy, romance! It transcends the trivialities and trappings of traditional genres!"

    show chi neutral
    voice "voice/chi intro 20.ogg"
    chi "Y-your alliteration is on point today, Kiyoko!"

    show tsu neutral
    voice "voice/pro intro 19.ogg"
    pro "...So you're saying it's a manga about ramen."

    show tsu glare
    voice "voice/Kiyoko_Line_21.ogg"
    tsu "O-of course! It's in the title!"

    show chi pity
    voice "voice/chi intro 21.ogg"
    chi "I'm getting a little hungry thinking about it..."

    show tsu angryc
    voice "voice/Kiyoko_Line_22.ogg"
    tsu "It's deep and lovingly crafted, but of course, I wouldn't expect a {i}normie{/i} to grasp the nuances..."

    show tsu smirkc
    voice "voice/Kiyoko_Line_23.ogg"
    tsu "Chihiro's the only one who could ever be a worthy match for my esteemed intellect..."

    show chi defaultc
    voice "voice/chi intro 22.ogg"
    chi "Omigosh, that's so sweet of you to say!"

    show chi default
    voice "voice/chi intro 23.ogg"
    chi "I really treasure our friendship too!"

    show tsu happy
    voice "voice/Kiyoko_Line_24.ogg"
    tsu "...N-no problem. Don't mention it!"

    "Did those two just have a moment??"

    show tsu neutral
    show chi neutral
    voice "voice/pro intro 20.ogg"
    pro "So it's just us, then? What are we supposed to do?"

    voice "voice/pro intro 21.ogg"
    pro "Do we just, like, turn something on? There's a TV near the front."

    show chi default
    voice "voice/chi intro 24.ogg"
    chi "We could do the book club meeting as normal. Everyone else is pretty quiet, so this isn't too different..."

    show tsu glare
    voice "voice/Kiyoko_Line_25.ogg"
    tsu "They could speak up if they had something to say!"

    voice "voice/pro intro 22.ogg"
    pro "I didn't read the manga though? How am I supposed to keep up?"

    show chi pity
    voice "voice/chi intro 25.ogg"
    chi "Oh you don't have to! It's your first time, so it's okay to sit in and drink in the atmosphere a bit!"

    show tsu glare
    voice "voice/Kiyoko_Line_26.ogg"
    tsu "Sitting back and contributing nothing. Like a {i}leech.{/i}"

    show chi sad
    voice "voice/chi intro 26.ogg"
    chi "Did you have a better idea, Kiyoko??"

    show tsu thinking
    voice "voice/Kiyoko_Line_27.ogg"
    tsu "...Hmmmmmm..."

    show tsu smirk
    voice "voice/Kiyoko_Line_28.ogg"
    tsu "...We could make a {i}game{/i} out of it!~"

    show chi neutral
    voice "voice/pro intro 23.ogg"
    pro "I-I don't like that smile she's making..."

    show chi pityc
    voice "voice/chi intro 27.ogg"
    chi "I-it can be a little spooky. Stand your ground."

    show tsu smirkc
    voice "voice/Kiyoko_Line_29.ogg"
    tsu "We don't know anything about the newcomer's tastes or preferences. So how about we coax that out of her??"

    voice "voice/pro intro 24.ogg"
    pro "Y-you don't have to coax anything, you could just-"

    show tsu smirk
    voice "voice/Kiyoko_Line_30.ogg"
    tsu "We'll hold a debate! And our newcomer will decide who's in the right!"

    show chi default
    voice "voice/pro intro 25.ogg"
    pro "...What?"

    show chi pity
    voice "voice/chi intro 28.ogg"
    chi "It seems you lit something up inside of her after all..."

    show tsu happy
    voice "voice/Kiyoko_Line_31.ogg"
    tsu "Chihiro always brings out the best in the both of us. We've always stood as diametrically opposed to each other!~"

    show chi defaultc
    voice "voice/chi intro 29.ogg"
    chi "I-I mean, it's okay to respect differences in taste. All waifus are precious."

    voice "voice/pro intro 26.ogg"
    pro "Wait, are we actually talking about-"

    show tsu glare
    voice "voice/Kiyoko_Line_32.ogg"
    tsu "The characterization of waifu! ...And husbando too. Husbando are just as important."

    show chi default
    voice "voice/chi intro 30.ogg"
    chi "Mmhm! Would you humor us for a bit?"

    "I was stunned. Is this how Anime Clubs really behaved??"

    voice "voice/pro intro 27.ogg"
    pro "...I mean, it sounds fun? Don't let me stop you guys from going at it, or whatever."

    ### SCENE: Round 1 ###

    #could make this a round 3 subject instead

    stop music fadeout 1.0
    play music debate fadein 1.0

    show chi feisty
    show tsu smirk
    voice "voice/chi r1 1.ogg"
    chi "Okay! Round 1, fight!~"

    show chi default
    voice "voice/chi r1 2.ogg"
    chi "I got one! In {i}Rama-sama Ramen Saga{/i}, there's these two girls who are twins! But they're also super opposite in personalities??"

    show tsu smirkc
    voice "voice/Kiyoko_Line_33.ogg"
    tsu "Ah, Netsu and Hiyasu! Good thinking!"

    voice "voice/pro r1 1.ogg"
    pro "Who and who??"

    show tsu happy
    voice "voice/Kiyoko_Line_34.ogg"
    tsu "Two prodigal chefs specializing in complementing and contrasting symbols of yin and yang, carefully balancing opposing flavours to elevate the senses!"

    voice "voice/chi r1 3.ogg"
    chi "It was mostly a hot versus cold dynamic. One of them, Hiyasu, specialized in ramen with chilled noodles."

    voice "voice/pro r1 2.ogg"
    pro "...why would you have ramen with cold noodles? That sounds kinda gross."

    show chi pity
    voice "voice/chi r1 4.ogg"
    chi "It kinda does, but... it's delicious! That was the surprising thing!"

    show chi defaultc
    voice "voice/chi r1 5.ogg"
    chi "And she was a total sweetheart! She was shy, and soft-spoken, and you really wanted to encourage her to do her best!"

    show tsu sadc
    voice "voice/Kiyoko_Line_35.ogg"
    tsu "Chihiro also goes for the generically saccharine types. So predictable..."

    show chi sad
    voice "voice/chi r1 6.ogg"
    chi "I-I like a lot of cute girls! Danderes are up there for some of my favs..."

    voice "voice/pro r1 3.ogg"
    pro "What's a... {i}dare-dare??{/i}"

    show chi pity
    show tsu neutral
    "Did I get that right? Was I close?"

    "They're looking at me funny. I don't think I was close."

    "At least Chihiro is patient. Bless her soul."

    show chi pity
    voice "voice/Kiyoko_Line_36.ogg"
    tsu "Well, there's a lot of {i}dere{/i} archetypes. It comes from 'deredere'. Or lovey-dovey."

    show tsu neutralc
    voice "voice/kiyoko dan.ogg"
    tsu "The {i}dan{/i} comes from 'danmari'. Which means to shut up or stay calm."

    show chi default
    voice "voice/chi r1 8.ogg"
    chi "They're basically abbreviations! So you can think of them like that!"

    voice "voice/pro r1 4.ogg"
    pro "...Huh. That's neat."

    show tsu glare
    voice "voice/Kiyoko_Line_37.ogg"
    tsu "...You seriously didn't know this? We're at a Japanese school..."

    show chi pity
    voice "voice/pro r1 5.ogg"
    pro "I-I'll take any chance to brush up on my Japanese..."

    show chi default
    voice "voice/chi r1 9.ogg"
    chi "Well, anyway! I liked Hiyasu a lot. You really wanted to root for her and have her come out of her shell!"

    show chi defaultc
    show tsu neutral
    voice "voice/chi r1 10.ogg"
    chi "Those kind of characters are my super favourites!~"

    "So Chihiro liked soft-spoken and shy girls? Somehow that reminds me of her."
    "I guess she was always the motherly type. Still, it got me thinking. It sounds like a lot of investment..."

    stop music fadeout 1.0
    play music present fadein 1.0
    #PRESENTATION CUT
    #cg: placeholder
    "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
    stop music fadeout 1.0
    play music debate fadein 1.0

    show tsu smirkc
    voice "voice/Kiyoko_Line_38.ogg"
    tsu "Pfft. Netsu is way better. She doesn't beat around the bush and waste time."

    show chi sad
    voice "voice/chi r1 11.ogg"
    chi "I-it's not a waste of time! It's rewarding emotional investment..."

    show tsu smirk
    voice "voice/Kiyoko_Line_39.ogg"
    tsu "They're always the same pandering otaku fantasies! I like a more exciting flavour!"

    show chi pity
    voice "voice/chi r1 12.ogg"
    chi "Hum. I suppose you'd be the type to mirror Netsu's hot intensity."

    show tsu angryc
    voice "voice/Kiyoko_Line_40.ogg"
    tsu "Hmph! Intense is right! I don't half-ass anything, and neither does Netsu!"

    show tsu glare
    voice "voice/Kiyoko_Line_41.ogg"
    tsu "Netsu had her head on straight! Any time the idiot lead got up in his headspace, it was Netsu who smacked him straight!"

    show chi default
    voice "voice/chi r1 13.ogg"
    chi "Mmhm. She could be a sweetheart when she wanted to be, between all of the disciplining..."

    show tsu smirk
    voice "voice/Kiyoko_Line_42.ogg"
    tsu "She gets things done!"

    show chi defaultc
    voice "voice/chi r1 14.ogg"
    chi "...she's a total tsundere."

    show tsu sad
    voice "voice/Kiyoko_Line_43.ogg"
    tsu "W-well, I... I {i}guess{/i}, in the technical sense, she is..."

    show tsu sadc
    #muttering
    voice "voice/Kiyoko_Line_44.ogg"
    tsu "...kind of a basic taste to have though..."

    voice "voice/pro r1 6.ogg"
    pro "Oh, that one I heard before. When you're mean on the outside but sweet on the inside?"

    show chi defaultc
    voice "voice/chi r1 15.ogg"
    chi "Mmhm! Exactly!~"

    show tsu neutral
    voice "voice/kiyoko tsun.ogg"
    tsu "It's in the name. {i}Tsun{/i} comes from 'tsuntsun', meaning 'irritable or aloof'..."

    show tsu glare
    voice "voice/Kiyoko_Line_46.ogg"
    tsu "...and you already know what the 'dere' comes from. Don't tell me you forgot already..."

    show chi pity
    voice "voice/pro r1 7.ogg"
    pro "I wouldn't forget that quickly!"

    voice "voice/pro r1 8.ogg"
    pro "I didn't think I'd end up learning stuff here. Thanks Kiyoko!"

    show tsu sadc
    voice "voice/Kiyoko_Line_47.ogg"
    tsu "W-well, if... if you're at Anime Club, you might as well get a lesson in actual Japanese."

    show chi pityc
    voice "voice/chi r1 16.ogg"
    chi "It's not like you like him or anything, riiiight?~"

    show tsu glare
    voice "voice/Kiyoko_Line_48.ogg"
    tsu "I-it's not like I... {i}q, quiet, you! Stupid!{/i}"

    "So Kiyoko's into tsunderes? Maybe she likes self-inserts..."

    stop music fadeout 1.0
    play music present fadein 1.0
    #PRESENTATION CUT
    #cg: placeholder
    "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
    stop music fadeout 1.0
    play music debate fadein 1.0

    show tsu happy
    voice "voice/Kiyoko_Line_49.ogg"
    tsu "Well? What do you think?"

    voice "voice/pro r1 9.ogg"
    pro "...Eh? What do I think of what??"

    show chi default
    voice "voice/chi r1 17.ogg"
    chi "Who's the winner of the round?"

    show tsu neutral
    voice "voice/pro r1 10.ogg"
    pro "I didn't realize I was actually supposed to vote, uh..."

    show tsu angryc
    show chi sad
    voice "voice/Kiyoko_Line_50.ogg"
    tsu "It's the point of this entire debate, stupid!"

    voice "voice/pro r1 11.ogg"
    pro "I'm just not sure what to vote for! Like..."

    voice "voice/pro r1 12.ogg"
    pro "Do I vote for the character type I like more? Which argument was better?"

    voice "voice/pro r1 13.ogg"
    pro "Whatever point those guys up front made the most sense?"

    show chi pity
    show tsu neutral
    voice "voice/chi r1 18.ogg"
    chi "What guys?"

    voice "voice/pro r1 14.ogg"
    pro "N-nothing..."

    show chi neutralc
    voice "voice/chi r1 19.ogg"
    chi "Well... I guess any reason to vote is fine. Voting for your beliefs serves as the foundation of a free democracy after all!"

    show tsu glare
    voice "voice/Kiyoko_Line_51.ogg"
    tsu "And you {i}better{/i} not vote for the option that you think one of us will like more! This isn't some trashy VN!"

    voice "voice/pro r1 15.ogg"
    pro "Well of course, this is real life. Nothing's more real than arguing over anime."

    menu:
        "Chihiro and Danderes":
            $ chihiro += 1
            jump poll1Chi
        "Kiyoko and Tsunderes":
            $ kiyoko += 1
            jump poll1Tsu

    #TODO: Twilio poll here

    label poll1Chi:
        show chi defaultc
        voice "voice/chi r1end 1.ogg"
        chi "Woo! I argued the thingie better!"

        show tsu sadc
        voice "voice/Kiyoko_Line_52.ogg"
        tsu "Tch. This isn't even my final form."

        #poll: might be redundant
        #python:
        #    pollScore["chi"] = pollScore["chi"] + 1


        jump endpoll1
    label poll1Tsu:
        show tsu smirk
        voice "voice/Kiyoko_Line_53.ogg"
        tsu "Alright! President Kiyoko draws first blood!"
        voice "voice/chi r1end 2.ogg"

        show chi sad
        chi "Th-this isn't {i}that{/i} kind of contest...!"

        #poll: might be redundant
        #python:
        #    pollScore["tsu"] = pollScore["tsu"] + 1
        #jump endpoll1

    label endpoll1:
        #game continues

    ### SCENE: Round 2 ###

    stop music fadeout 1.0
    play music vn fadein 1.0
    show chi feisty
    show tsu default
    voice "voice/chi r2 1.ogg"
    chi "Okay, okay, we're gonna change gears!"

    show tsu sad
    voice "voice/Kiyoko_Line_54.ogg"
    tsu "Eh? But this is my game, you can't just-"

    show chi defaultc
    voice "voice/chi r2 a.ogg"
    chi "We should talk about husbandos! Can we?"

    show tsu smirkc
    voice "voice/Kiyoko_Line_55.ogg"
    tsu "...Huh. Not a bad idea, surprisingly."

    voice "voice/pro r2 1.ogg"
    pro "Eh? I thought this was just gonna be about waifus."

    show chi pity
    voice "voice/chi r2 2.ogg"
    chi "We talk about whoever we like! They don't have to be cute girls!"

    show tsu angryc
    voice "voice/Kiyoko_Line_56.ogg"
    tsu "Yeah, it's 2018. Get with the times."

    voice "voice/pro r2 2.ogg"
    pro "I-I'm not against it, I was just... okay, cool."

    show chi default
    show tsu neutral
    voice "voice/pro r2 3.ogg"
    pro "So {i}Ramen Saga{/i} has husbandos too?"

    show chi defaultc
    voice "voice/Kiyoko_Line_57.ogg"
    tsu "It was originally released as a best-selling visual novel. They went overboard with the routes they tacked on..."

    show chi feisty
    voice "voice/chi r2 3.ogg"
    chi "They advertise it as a harem-style adventure!"

    show tsu glare
    voice "voice/pro r2 4.ogg"
    pro "Of course. Harem endings."

    show tsu angryc
    voice "voice/kiyoko adaptation.ogg"
    tsu "As I recall, the adaptation took, ah, creative liberties... but Kazama and Hiro made the jump to the small screen remarkably well."

    show chi default
    voice "voice/chi r2 4.ogg"
    chi "Hiro's adorable! He has the best comedy scenes."

    show tsu sad
    voice "voice/Kiyoko_Line_59.ogg"
    tsu "Urgh, really? He looks more like the parody version of a bishonen lead..."

    show chi pity
    voice "voice/chi r2 5.ogg"
    chi "Well, yeah, he's obsessed with his appearance, but he's secretly a huge dork! He got the best comedy scenes!~"

    show chi defaultc
    voice "voice/chi r2 6.ogg"
    chi "And he has the best design too!"

    show tsu smirkc
    voice "voice/Kiyoko_Line_60.ogg"
    tsu "Heh. I figured someone like you would have such juvenile tastes."

    show chi sad
    voice "voice/chi r2 7.ogg"
    chi "I-it's not wrong to like pretty boys... pretty boys deserve love too!"

    "Chihiro seemed to be into bishonen characters. The prototypical pretty boy with effeminate features."
    "Wonder what the appeal is. It's probably in their design..."

    stop music fadeout 1.0
    play music present fadein 1.0
    #PRESENTATION CUT
    #cg: placeholder
    "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
    stop music fadeout 1.0
    play music vn fadein 1.0

    show tsu happy
    voice "voice/Kiyoko_Line_61.ogg"
    tsu "Well, thank you for sharing that. It's pedestrian, but we're entitled to our opinions."

    show tsu smirk
    voice "voice/Kiyoko_Line_62.ogg"
    tsu "I should remind you however, {i}my{/i} tastes are a lot more cultured and refined."

    show chi angryc
    voice "voice/chi r2 8.ogg"
    chi "Oh don't tell me you like Kazama..."

    show tsu glare
    voice "voice/Kiyoko_Line_63.ogg"
    tsu "He's good for drama! Without him, there wouldn't be anything to talk about!"

    show chi neutral
    show tsu smirk
    voice "voice/Kiyoko_Line_64.ogg"
    tsu "He's cold, calculating, willing to do whatever it takes to succeed..."

    show tsu happyc
    voice "voice/Kiyoko_Line_65.ogg"
    tsu "And that intimidating look he gives Rama-sama when they first met... oooh, it gives me the tingles!~"

    show chi sad
    "Calm down, Kiyoko, this is a classroom setting..."

    voice "voice/chi r2 9.ogg"
    chi "But he's a jerk! He's condescending, conceited"

    show chi annoyed
    voice "voice/chi r2 10.ogg"
    chi "...and he put too much salt in Rama-sama's broth!"

    show tsu glare
    voice "voice/kiyoko pp.ogg"
    tsu "It was a power play!"

    show chi angryc
    voice "voice/chi r2 11.ogg"
    chi "It was {i}cheating!{/i}"

    show tsu neutral
    voice "voice/pro r2 5.ogg"
    pro "Did you guys consult the official {i}Rama-sama Ramen Saga{/i} Rulebook?"

    show chi sad
    voice "voice/chi r2 12.ogg"
    chi "I-I doubt there is such a thing... either or, Kazama's a jerk!"

    show tsu smirk
    voice "voice/Kiyoko_Line_67.ogg"
    tsu "But he does it all in such a cool, dashing way!~"

    show chi defaultc
    voice "voice/chi r2 13.ogg"
    chi "B-but wouldn't you rather have a charming, friendly guy who cares for your wellbeing?"

    show tsu angryc
    voice "voice/Kiyoko_Line_68.ogg"
    tsu "And I suppose you'd want to hold hands and blush too? {i}Please.{/i}"

    show tsu neutral
    voice "voice/Kiyoko_Line_69.ogg"
    tsu "I'm a third-year, I'm getting too old to indulge in fluffy nonsense like that!"

    "Kiyoko was utterly smitten by bad boys, it seemed. Not exactly an uncommon opinion."
    "It's a cute enough fantasy, but it's a weirdly specific one? I don't think I get it..."

    menu:
        "Chihiro and Bishonen":
            $ chihiro += 1
            jump poll2Chi
        "Kiyoko and Bad Boys":
            $ kiyoko += 1
            jump poll2Tsu
    #TODO: Twilio poll here

    label poll2Chi:
        voice "voice/chi r2end 1.ogg"
        show chi default
        chi "Score one for the cute guys!"

        voice "voice/Kiyoko_Line_70.ogg"
        show tsu glare
        tsu "What's that supposed to mean? They're {i}both cute{/i}, stupid."

        #poll: might be redundant
        #python:
        #    pollScore["chi"] = pollScore["chi"] + 1

        jump endpoll2
    label poll2Tsu:
        voice "voice/Kiyoko_Line_71.ogg"
        show tsu smirkc
        tsu "Heheh! I didn't expect anything less!"

        voice "voice/chi r2end 2.ogg"
        show chi annoyed
        chi "I-I want a recount, that can't be right... something's fishy!"

        #poll: might be redundant
        #python:
        #    pollScore["tsu"] = pollScore["tsu"] + 1

        jump endpoll2

    label endpoll2:
        #game continues

    ### SCENE: Round 3 ###

    label round3:
        #game continues

    voice "voice/pro r3 1.ogg"
    pro "That's two rounds down. Jeez, you guys really get into this, don't you..."

    #poll: might be redundant
    #python:
    #    charTied = 1
    #    for char in pollScore:
    #        for compChar in pollScore:
    #            if char != compChar and pollScore[char] != pollScore[compChar]:
    #                charTied = 0
    #                break

    if kiyoko == chihiro:
        jump charTied
    else:
        jump charLead

    label charTied:
         #if it's tied up
        voice "voice/chi r3 1.ogg"
        show chi feisty
        chi "Okay! It's time for the third and final round!"

        voice "voice/Kiyoko_Line_72.ogg"
        show tsu sadc
        tsu "Mrgrgr... can't believe it's still tied up. I should've closed this off by now."

        voice "voice/Kiyoko_Line_73.ogg"
        show tsu glare
        tsu "Nuts to that! I got the final round!"

        voice "voice/pro r3 2.ogg"
        pro "Getting surprisingly competitive over here. I didn't think you two would be getting so into it."

        voice "voice/chi r3 2.ogg"
        show chi annoyed
        chi "Anime Club is serious business!"

        voice "voice/Kiyoko_Line_74.ogg"
        show tsu smirk
        tsu "Yeah, super serious! Try and keep up!"

        voice "voice/pro r3 3.ogg"
        pro "I'm getting a pretty clear picture of why no one else bothered to show up..."

    label charLead:
        #if one of the girls is leading by 2 already
        voice "voice/chi r3 3.ogg"
        show chi feisty
        show tsu smirk
        chi "Okay! It's time for the third and final round!"

        voice "voice/pro r3 4.ogg"
        pro "Wait, do we have to? Someone's already leading two nothing"

        voice "voice/chi r3 4.ogg"
        show chi feisty
        chi "We're having fun, right? We don't have to stop cuz of what's on the scoreboard..."

        voice "voice/pro r3 a.ogg"
        pro "Well, yeah, we are, but-"

        voice "voice/Kiyoko_Line_75.ogg"
        show tsu neutral
        tsu "The people running this prepared three rounds of this stuff, so we gotta go through with all of them. Them's the rules."

        voice "voice/pro r3 5.ogg"
        pro "Who?? You're the president. That means you're making up the rules, right??"

        show tsu sad
        show chi pity
        "...A hushed silence fell upon the classroom."

        voice "voice/pro r3 6.ogg"
        pro "I-I'm not sure I get it, but okay, let's go..."

        voice "voice/chi r3 5.ogg"
        show chi default
        chi "Yaaay!~"

    voice "voice/pro r3 7.ogg"
    pro "So what else's left on the menu?"

    show chi defaultc
    show tsu neutral
    voice "voice/chi r3 6.ogg"
    chi "Hmmmm... we could talk about {i}Rama-sama's Ramen Saga{/i} some more! There were a few other waifus..."

    voice "voice/pro r3 8.ogg"
    pro "This isn't a harem anime, right?"

    show tsu glare
    voice "voice/Kiyoko_Line_76.ogg"
    tsu "It's a very personal story about finding strength through the support of others!"

    show chi neutral
    voice "voice/pro r3 9.ogg"
    pro "Harem anime, got it."

    show chi default
    voice "voice/chi r3 7.ogg"
    chi "Oh, we could talk about the two most important girls, Rena and Kotone!"

    show chi defaultc
    show tsu neutral
    voice "voice/chi r3 8.ogg"
    chi "Rena's the cute, exuberant, and familiar next-door neighbor of Rama-sama, and Kotone is a mysterious visitor who whisks him away from his usual life!"

    "I nodded my head, trying to follow along. I should've studied up on this show before coming here..."

    voice "voice/pro r3 10.ogg"
    pro "So which one do you like?"

    show chi default
    voice "voice/chi r3 9.ogg"
    chi "Oh, I dug Kotone! She's so cool, super, mysterious, and distant... She barely says a word, but she has so much presence!"

    show chi feisty
    show tsu glare
    voice "voice/chi r3 10.ogg"
    chi "And you never really get a good read on her until the big reveal when you find out she's an-"

    show tsu angry
    show chi sad
    voice "voice/Kiyoko_Line_77.ogg"
    tsu "Chihiro! Spoilers!"

    show tsu glare
    show chi sadc
    voice "voice/chi r3 11.ogg"
    chi "A-ack! S-sorry, I... that was close..."

    voice "voice/pro r3 11.ogg"
    pro "...Guess I dodged a bullet there?"

    show chi annoyed
    voice "voice/chi r3 12.ogg"
    chi "She's central to the whole story! You gotta finish the rest of it!"

    show chi feistyc
    voice "voice/chi r3 13.ogg"
    chi "You just kind of see her and you {i}know{/i} she's gonna be super important and knowledgeable!"

    show tsu neutral
    voice "voice/pro r3 12.ogg"
    pro "...So she's a mysterious waifu? How do you know you like her if you don't know anything about her?"

    show chi pity
    voice "voice/chi r3 14.ogg"
    chi "W-well, it's not like you know {i}nothing{/i} about her, you just... get invested in her!"

    show chi defaultc
    voice "voice/chi r3 15.ogg"
    chi "And she delivers! Ohhh boy does she deliver!~"

    "Well Chihiro seems particularly interested in the silent and mysterious type. Still, there has to be something more to it..."

    stop music fadeout 1.0
    play music present fadein 1.0
    #PRESENTATION CUT
    #cg: placeholder
    "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
    stop music fadeout 1.0
    play music debate fadein 1.0

    show tsu neutralc
    voice "voice/Kiyoko_Line_78.ogg"
    tsu "Of course, Chihiro has always gravitated to those with otherworldly knowledge and insight!"

    show tsu happy
    voice "voice/Kiyoko_Line_79.ogg"
    tsu "That's why she sought me out after all! Hohoho!~"

    show chi pityc
    voice "voice/chi r3 16.ogg"
    chi "...Mm... I don't get that vibe from you though."

    show tsu sad
    voice "voice/Kiyoko_Line_80.ogg"
    tsu "Eh!? Are you calling me stupid!?"

    show tsu glare
    show chi sad
    voice "voice/chi r3 17.ogg"
    chi "No! I would never-"

    voice "voice/pro stupid.ogg"
    pro "I dunno, I think she was calling you stupid."

    show chi sadc
    voice "voice/chi r3 18.ogg"
    chi "Don't incense her, that's not what I meant!"

    show tsu angryc
    show chi neutral
    voice "voice/Kiyoko_Line_81.ogg"
    tsu "Anyway, Kotone's not much more than a token plot-thread. Rena's way better."

    show tsu neutral
    voice "voice/pro r3 14.ogg"
    pro "Huh. She didn’t strike me as your preference."

    show tsu sadc
    voice "voice/Kiyoko_Line_82.ogg"
    tsu "....I can like gentle characters too..."

    voice "voice/pro r3 15.ogg"
    pro "Huh?"

    show tsu happy
    voice "voice/Kiyoko_Line_83.ogg"
    tsu "I mean, she's reliable, and kind, and always supports Rama-sama! Because they're best friends."

    show tsu happyc
    show chi default
    voice "voice/Kiyoko_Line_84.ogg"
    tsu "It's a familiar relationship. Cozy, nice. I like it!"

    show tsu smirkc
    voice "voice/Kiyoko_Line_85.ogg"
    tsu "The pacing doesn't always have to be operating at a hundred percent, y'know."

    show chi pityc
    voice "voice/chi r3 19.ogg"
    chi "She says as she shames the club for minding their studies..."

    show tsu glare
    voice "voice/Kiyoko_Line_86.ogg"
    tsu "This isn't an anime, Chihiro!"

    "So Kiyoko liked the childhood, best friend character? That's still a pretty unexpected choice, coming from her, but I can kind of see it."
    "Still, I have to wonder what that's about..."

    stop music fadeout 1.0
    play music present fadein 1.0
    #PRESENTATION CUT
    #cg: placeholder
    "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
    stop music fadeout 1.0
    play music debate fadein 1.0

    #TODO: Twilio poll here
    menu:
        "Chihiro and Mysterious Waifus":
            $ chihiro += 1
            jump poll3Chi
        "Kiyoko and Childhood Best Friends":
            $ kiyoko += 1
            jump poll3Tsu

    label poll3Chi:
        voice "voice/chi r3end 1.ogg"
        show chi default
        chi "Yay! Mystery solved!~"

        voice "voice/Kiyoko_Line_87.ogg"
        show tsu angryc
        tsu "Hmph. Call it a curious case of crummy taste..."

        #poll: might be redundant
        #python:
        #    pollScore["chi"] = pollScore["chi"] + 1

        jump endpoll3

    label poll3Tsu:
        voice "voice/Kiyoko_Line_88.ogg"
        show tsu happyc
        tsu "Well, it was obvious that the power of love would win out in the end!~"

        voice "voice/chi r3end 2.ogg"
        show chi pity
        chi "But they aren't even dating in the anime..."

        #poll: might be redundant
        #python:
        #    pollScore["tsu"] = pollScore["tsu"] + 1

        jump endpoll3

    label endpoll3:
        stop music fadeout 1.0
        voice "voice/pro r3win.ogg"
        pro "So, uh, that's it? Then I guess the winner is..."
        if chihiro < kiyoko:
            jump routeTsu
        else:
            jump routeChi


    ##################################### SPLIT CODE IF NEEDED HERE ####################################################

    ### ROUTE SELECT: TSUNDERE ROUTE ###
    label routeTsu:
        play music tsutheme fadein 1.0
        show tsu smirkc zorder 2:
            align (0.35, 1.0)
        show chi neutral zorder 2:
            align (0.65, 1.0)
        show classroomevening zorder 1 with dissolve

        voice "voice/Kiyoko_Line_89.ogg"
        tsu "Ohoho!~ Like there was ever any doubt!"

        voice "voice/chi tsun 1.ogg"
        chi "Ah, she's been practicing her ojou-sama laugh for just such an occasion..."

        voice "voice/pro tsun 1.ogg"
        pro "It sounded like she had something caught in her windpipe."

        voice "voice/kiyoko gracious.ogg"
        show tsu neutral
        tsu "Ah, those glowering expressions are {i}such{/i} a killjoy. I'm a gracious winner!"

        voice "voice/chi tsun 2.ogg"
        show chi defaultc
        chi "Yeah, it was fun! And we all got to learn more about each other and what we like!~"

        voice "voice/pro tsun 2.ogg"
        pro "Who knew arguing about your favourite characters could be such an {i}intimate{/i} bonding experience..."

        voice "voice/Kiyoko_Line_91.ogg"
        show tsu sadc
        tsu "Y-you don't have to be so sarcastic about it!"

        voice "voice/pro tsun 3.ogg"
        show chi default
        pro "So, uh, what do we do now? Anime Club's almost over by now, right?"

        voice "voice/Kiyoko_Line_92.ogg"
        show tsu happyc
        tsu "Mm, true. I could spare some time to sort out your paperwork... what will you do, Chihiro?"

        show chi pity
        voice "voice/chi tsun 3.ogg"
        chi "Aaaah... well, we usually walk home, but that sounds like a good idea too!"

        show chi defaultc
        voice "voice/chi tsun 4.ogg"
        chi "Truthfully, I gotta get going anyway, I have a big test to study for!"

        show tsu neutral
        voice "voice/pro tsun 4.ogg"
        pro "Oh right, for calculus right? Better hit the books hard!"

        show chi pityc
        voice "voice/chi tsun 5.ogg"
        chi "Hehehe! I remember when math used to be fun..."

        show chi default
        voice "voice/chi tsun 6.ogg"
        chi "Anyway, I gotta go! Byeee!~"

        hide chi with dissolve
        show tsu neutralc with easeinleft:
            align (0.5, 1.0)
        "Scampering out the door, Chihiro soon left me alone with Kiyoko."
        "Silence hung between us. Kiyoko was pretty fun, but it still felt like being introduced to a friend of a friend."

        voice "voice/pro tsun 5.ogg"
        pro "...Well, uh... was I supposed to bring anything?"

        show tsu neutral
        voice "voice/Kiyoko_Line_93.ogg"
        tsu "N-no, no, not really. I just need you to go over our constitution real quick."

        show tsu sadc
        voice "voice/Kiyoko_Line_94.ogg"
        tsu "...Nnngh. Chihiro writes too small, I can barely make this out."

        show tsu neutral
        show glasses zorder 3 with dissolve
        "Reaching into her knapsack, Kiyoko pulled out a small pair of reading glasses, going over the letter-print."

        show tsucgsmile with dissolve
        voice "voice/Kiyoko_Line_95.ogg"
        tsu "You must attend at least one meeting a month. You must engage with tasteful, school-appropriate material. You are eligible to one viewing party recommendation..."

        voice "voice/pro tsun 6.ogg"
        pro "...Huh."

        show tsucgfrown
        hide tsucgsmile
        show tsu glare
        voice "voice/Kiyoko_Line_96.ogg"
        tsu "What? This stuff is simple. Don't tell me I’ve lost you already."

        voice "voice/pro tsun 7.ogg"
        pro "No, I just... didn't expect you to have a pair of reading glasses on hand."

        show tsu sad
        voice "voice/Kiyoko_Line_97.ogg"
        tsu "...I-it's not a big deal. I have troubles with fine print. I'm a little short-sighted."

        show tsu angryc
        voice "voice/Kiyoko_Line_98.ogg"
        tsu "B-but there's nothing wrong with that! I'm flawless otherwise!"

        voice "voice/pro tsun 8.ogg"
        pro "They're kinda cute, though..."

        show glare
        voice "voice/Kiyoko_Line_99.ogg"
        tsu "'Cute'?? They're for vision-correction! I've no used for a, a cloying fashion accessory!"

        voice "voice/pro tsun 9.ogg"
        pro "It's not an insult or anything! Chihiro wears glasses too, and everyone thinks she's cute!"

        show tsu sadc
        voice "voice/Kiyoko_Line_100.ogg"
        tsu "...Nnnn..."

        voice "voice/Kiyoko_Line_101.ogg"
        tsu "She's just cute in the pedestrian way though. The normies go for it..."

        "She groaned aloud, putting down the pamphlet."
        "There's probably something more to the whole glasses thing though..."

        stop music fadeout 1.0
        play music present fadein 1.0
        #PRESENTATION CUT
        #cg: placeholder
        "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
        stop music fadeout 1.0
        play music tsutheme fadein 1.0

        hide tsucgfrown with dissolve
        show tsu neutral
        voice "voice/Kiyoko_Line_102.ogg"
        tsu "I don't wanna wear my glasses too much around school. I get by fine as it is."

        show tsu glare
        voice "voice/Kiyoko_Line_103.ogg"
        tsu "Besides, everyone looks at me different when they do. I can't command respect like that!"

        voice "voice/pro tsun 10.ogg"
        pro "Are you sure you want to command respect?"

        show tsu angryc
        voice "voice/Kiyoko_Line_104.ogg"
        tsu "Wh, what else would I want??"

        voice "voice/pro tsun 11.ogg"
        pro "Based on the way you were blushing, I'd think you'd be happy if someone called you a cutie like Chihiro."

        show tsu glare
        voice "voice/Kiyoko_Line_105.ogg"
        tsu "Th-that's baseless conjecture!!"

        show tsu sad
        voice "voice/Kiyoko_Line_106.ogg"
        tsu "I, eh, ahem... c-can we just get through your paperwork?"

        voice "voice/pro tsun 12.ogg"
        pro "I didn't bring a pen though-"

        show tsu glare
        voice "voice/Kiyoko_Line_107.ogg"
        tsu "USE MINE!"

        voice "voice/pro tsun 13.ogg"
        pro "Okay, okay! ...Ouch, don't spear me with it!"

        scene black with dissolve
        "The new few minutes were spent marking my name on an assortment of forms."
        "That day, I confirmed my extracurricular membership into the Anime Club."
        "It beats going straight home every single day of school. Kiyoko can get to be a handful though."
        "She's eccentric, but she attracts her own little cult of personality. I imagine she wouldn't have it any other way."

        jump credits

    label routeChi:
        show tsu neutral zorder 2:
            align (0.35, 1.0)
        show chi defaultc zorder 2:
            align (0.65, 1.0)
        show classroomevening zorder 1 with dissolve
        play music chitheme fadein 1.0
        voice "voice/chi bf 1.ogg"
        chi "Me! Oh, I don't win very often! How exciting!"

        voice "voice/chi bf 2.ogg"
        show chi default
        chi "Okay, okay, I'd like to thank my mom and dad, and my coach for believing in me..."

        voice "voice/chi bf 3.ogg"
        show chi defaultc
        chi "...OH! And all my friends at the academy!~"

        show tsu glare
        voice "voice/Kiyoko_Line_108.ogg"
        tsu "Well. She seems pleased with herself."

        voice "voice/pro bf 1.ogg"
        pro "You don't have to get pouty about it. It was a fun way to talk about stuff you like."

        show chi feisty
        voice "voice/chi bf 4.ogg"
        chi "Yeah! And when it's a game, you gotta take it super seriously too!"

        show chi defaultc
        voice "voice/chi bf 5.ogg"
        chi "I had fun! This was a great idea, Kiyoko!~"

        show tsu happy
        voice "voice/Kiyoko_Line_109.ogg"
        tsu "...Eh? Eheh, you, uh... you don't have to flatter me..."

        show chi default
        voice "voice/chi bf 6.ogg"
        chi "How about it? You wanna do it again sometime??"

        voice "voice/pro bf 2.ogg"
        pro "Might be fun, but... Anime Club's over by now, right?"

        show tsu neutral
        voice "voice/Kiyoko_Line_110.ogg"
        tsu "Ah, technically? We reconvene every Tuesday and Thursday."

        voice "voice/pro bf 3.ogg"
        pro "Alright, I'll try to make the next one. ...So long as exams don't get in the way."

        show chi default
        voice "voice/chi bf 7.ogg"
        chi "You wanna walk home?"

        voice "voice/pro bf 4.ogg"
        pro "It's tradition at this point. What are you gonna do, Kiyoko?"

        show tsu sadc
        voice "voice/Kiyoko_Line_111.ogg"
        tsu "Well, our secretary didn't make it so... I'll have to jot the meeting notes myself."

        show chi feistyc
        voice "voice/chi bf 8.ogg"
        chi "Be sure to note who {i}actually{/i} won our little contest, okayyy?~"

        show tsu glare
        voice "voice/Kiyoko_Line_112.ogg"
        tsu "I-I-I wouldn't dream of sullying our club's name with lies and slander! How dare you??"

        show chi neutral
        voice "voice/pro bf 5.ogg"
        pro "Oh no, you're setting her off again. We should get going."

        voice "voice/chi bf 9.ogg"
        chi "Okay! I need to hit my locker first!~"

        scene hallwayevening with dissolve

        "Heading over to Chihiro's locker, she gathers her things in short order, readying for our regular commute home."

        show chi default with dissolve
        voice "voice/chi bf 10.ogg"
        chi "Hey, I was thinking about something random!"

        voice "voice/pro bf 6.ogg"
        pro "Hm? What?"

        show chi defaultc
        voice "voice/chi bf 11.ogg"
        chi "Do you like having a cute girl by your side to walk home with at the end of each day, every day?"

        voice "voice/pro bf 7.ogg"
        pro "Well, I mean, sure. We're friends. What, did you wanna shake up the routine a bit?"

        show chi pity
        voice "voice/chi bf 12.ogg"
        chi "N-no, that's not what I meant, I just... thought it was a cute thought, being together everyday..."

        show chi sad
        voice "voice/chi bf 13.ogg"
        chi "...B-but not in a creepy, yandere way!"

        voice "voice/pro bf 8.ogg"
        pro "...Huh?"

        show chi pity
        voice "voice/chi bf 14.ogg"
        chi "I-I mean, unless you liked it that way-"

        voice "voice/pro bf 9.ogg"
        pro "N-no, no, I... I like where we're at right now. With the walking to and from school thing. Very casual."

        show chi default
        voice "voice/chi bf 15.ogg"
        chi "It's kind of a weird thing to think about though, right? Yandere girlfriends?"

        voice "voice/pro bf 10.ogg"
        pro "Isn't that just a flirty way of calling someone a 'stalker'?"

        show chi defaultc
        voice "voice/chi bf 16.ogg"
        chi "Hehehe~! I guess? But they're pretty popular too!"

        show chi pity
        voice "voice/Chi-retake2.ogg"
        chi "Something about another person uncompromisingly in love with you is... kinda romantic, in a weird way!"

        voice "voice/pro bf 11.ogg"
        pro "...I could do without the stabbings, though. And how do you introduce someone like that to your family?"

        show chi neutral
        voice "voice/chi bf 18.ogg"
        chi "You don't."

        show chi neutralc
        voice "voice/chi bf 19.ogg"
        extend "Generally speaking."

        voice "voice/pro bf 12.ogg"
        pro "You sound like you thought about this stuff a lot..."

        show chi pity
        voice "voice/chi bf 20.ogg"
        chi "I-it's fun to fantasize about!"

        "Chihiro was pretty gentle and peaceful, but sometimes you gotta wonder if one of your best friends is about to just fling themselves off the deep end."
        "And now she's planted that little germ of a thought in my head..."

        stop music fadeout 1.0
        play music present fadein 1.0
        #PRESENTATION CUT
        #cg: placeholder
        "THIS IS A CG SEQUENCE. WE WILL PUT IT IN LATER."
        stop music fadeout 1.0
        play music chitheme fadein 1.0

        voice "voice/pro bf 13.ogg"
        pro "Well, Chihiro, you've given me a lot to think about."

        show chi defaultc
        voice "voice/chi animeclub.ogg"
        voice "voice/chi bf 21.ogg"
        chi "Mmhm! I knew you'd have a lot of fun at Anime Club!~"

        voice "voice/pro bf 14.ogg"
        pro "I had my doubts. I figured you were just fishing to assimilate me into the hivemind."

        show chi pity
        voice "voice/chi bf 22.ogg"
        chi "Ahhh, it's not really a hivemind! Kiyoko wishes she could be a queen bee though..."

        voice "voice/pro bf 15.ogg"
        pro "Of course, I might have to refer you to a psychiatrist to poke at your head a bit..."

        show chi sad
        voice "voice/chi bf 23.ogg"
        chi "J-just because I like reading about psychopaths doesn't make me one! It's relaxing!"

        show chi neutral
        voice "voice/pro bf 16.ogg"
        pro "I-I'm not here to judge. We should get going though, it's getting late."

        scene chicg with dissolve
        voice "voice/chi bf 24.ogg"
        chi "Oh! Right, and I have to study! See you another time?"

        voice "voice/pro bf 17.ogg"
        pro "Definitely."


        "That marked my first day at Anime Club. It was a little off-the-wall, but..."
        "With Chihiro, it felt familiar. Maybe this would work out after all."
        "...I hope they don't {i}actually haze me{/i} when more people show up to Anime Club, though. Jeez."
        jump credits

label credits:
    #make a credits image to put in here later
    return
