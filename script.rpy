init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]



image splash ="slash.jpg"
image mal ="mel.jpg"
image warn ="warn.jpg"
image sunflower ="sunflowers.ong"
image darkthought ="startup2.png"
image dt2 ="startup 1.png"
label splashscreen:
    scene black
    with Pause(1)

    play sound "ping.ogg"

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show mal with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(1)

    show warn with dissolve
    with Pause(6)

    scene black with dissolve
    with Pause(1)

    return

define k = Character("Kuno", what_prefix='"', what_suffix='"')
define ka = Character("Kazuo", what_prefix='"', what_suffix='"')
define t = Character("Teacher", what_prefix='"', what_suffix='"')
define s = Character("Stranger", what_prefix='"', what_suffix='"')
define I = Character("Tian Yi", what_prefix='"', what_suffix='"')
define f = Character("Fang Xin", what_prefix='"', what_suffix='"')
define a = Character("An", what_prefix='"', what_suffix='"')
# The game starts here.

label start:
    $ hatred = False
    $ change = 0
    $ goodyearfocus = False
    $ hundredfriend = False
    $ friendpoints = 0
    $ love = 0
    $ kunolove = 0
    $ izumilove = 0
    $ fanglove = 0
    $izumifriend = False
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    with Pause(2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show eileen random


# T#these display lines of dialogue.
#prolougue

#two months later

    "New school, new friends, new teachers."

    if hatred:
        "new enemies and victims"
    "I think to myself..."
    "How will this one go?"
    "I've never decided what I wanted... its a careless mistake on my part."
    "Yet, it seems as if everything flows perfectly."
    "Like a river, the water flows through my life and I don't have to lift a finger."
    "Taking so many things for granted puts me in a bind."
    "Tet, I don't care about those; I care about friends."
    "Friends..."
    "You can't take those for granted."
    "Moving all the time, changing, developing differently..."
    "It's all fate."
    "You could meet the perfect friend but never get to know them,"
    "I feel a sense of melancholia as I process that last thought..."
    "Anyway what should my goal be?"
    "Every school asks that in their opening speech."

    menu:
        "I want a hundred friends":
            $friendpoints +=1
            jump hundredfriend

        "hope to spend a good year with all of you":
            jump goodyearfocus

label hundredfriend:
    $ hundredfriend = True
    "this sounds like a good idea"
    "except I sound like a total loner."
    "but I've said other weird stuff..."
    "what's there to worry?"
    jump con


label goodyearfocus:
    $ goodyearfocus = True
    "hmmm..."
    "I don't sound like an idiot for once"
    "interesting"
    jump con

label con:
    "well then..."
    "this will be interesting,"
    "I enter the class now that the doors have opened up"

    t "everybody this is Kazuo"

    t "He is new this year and recently moved from down south"
    "The whole class seemed to have seen this coming..."
    "Nothing new to them"
    "They silently applaud me"

    t "This is Kuno, class representative."
    "A young girl whom I recognize gets up from her seat"
    "She is deeply embedded in my childhood..."
    "Yet I can't remember her strongly"

    k "You alright there?"

    "..."
    "I can't utter a word."
    with Pause(5)

    k "Looks like something happened"
    "She smiles and sits down"

    t "well, I spoke too much for Kazuo he doesn't have anything to say..."
    "The teacher blushes embarrassed"
    t "Then tell us what is your goal for this year at least?"
    "I breath deeply remembering my answer"


    if hundredfriend:
      "I want hundred friends"
    jump contwo

    if goodyearfocus:
      "I want a good year!"
    jump contwo

label contwo:
    "welp"
    "This definitely was not what I expected."
    "Their reaction is not a typical reaction."
    "Everyone is dead quiet."
    "Something which worries me."
    "I bow slightly in respect and sit down next to Kuno."
    "Which coincidently was the only seat available."
    "I adjust myself awkwardly and sit"
    "The teacher begins to speak..."

    #scene bgt
    #with xxxx

    "Recess begins.."
    "Something that relieves me from the traumatic intro I was given."
    "Many students begin to collect into clusters of groups..."
    "I remain on my desk, sloppily bringing out my lunch."
    "It's nothing magnificent"
    "After all I had to make it myself."
    "I look around the room in an attempt to observe my surroundings."
    "After staring at the desk beside me for a few seconds..."
    "I realized Kuno had disappeared."
    "It was a 25 minute break..."
    "I had no idea what to do..."
    "I was genuinely curious to her whereabouts..."

    menu:
        "See what Kuno is upto.":
            $friendpoints +=1
            jump kunosearch

        "Have a walk around the groups...":
            jump walk

        "Stay where I am":
            jump standstill

    label kunosearch:
    "I stand up"
    "She is a class representative..."
    "Where could she go?"
    "I peek out of the doorway where some students were ambling about."
    s "Are you looking for Kuno?"
    "I turn around to see a girl."
    "She is noticeably shorter than me."
    "In a way that she appears cute."
    s "Are you looking for Kuno?"
    ka "Yeah"
    s "Ohh"
    "She gives out a rather intimidating smile."
    s "I see what is happening..."
    "She giggles softly,"
    ka "No"
    ka "you ar-"
    s "I'm Tian Yi."
    "Before I could mutter anything else, she spoke again"
    s "Just call me Yi."
    "She gives out another small giggle."
    s "She went to the office to hand in some textbooks that this class had borrowed"
    ka "Oh, I see"
    s "Hey, You already sit next to her,"
    "She smiles"
    s "Don't ask for more than you have"
    "Of course."
    "Middle school taught me that with relationships..."
    "I grit my teeth as they resurface."
    s "Don't tell me; you were one of the boys she turned down!"
    "Her attention was concentrated and intimidating"
    "..."
    ka "No."
    I "Oh well; class time..."
    I "we'll talk later."

    jump conthree

    label walk:
    "I stand up."
    "The groups have big tables made from desks of their peers."
    s "Ah"
    "I turn around to see a girl."
    "She is noticeably shorter than me"
    s "Kazuo... right?"
    ka "I guess you weren't paying attention then,"
    "She puffs out her cheeks guiltily"
    s "I was eating breakfast."
    ka "What?"
    s "Yeah, I tend to miss out."
    s "I was eating a rice ball."
    ka "A rice ball?"
    s "Yeah, It is the only food I can cook for now."
    ka "For now?"
    s "I'm not some Gordon Ramsey, okay?"
    ka "I could tell..."
    s "Are you telling me I can't cook well!"
    ka "Up to your interpretation."
    s "Hmmp"
    s "I found out about you through the other people who were paying attention."
    ka "Like who?"
    s "Meet them yourself."
    ka "What?"
    "What a confusing girl."
    ka "Who are you then?"
    s "Tian Yi"
    "She smiles politely,"
    ka "Okay"
    I "Just call me Yi."
    I "Oh, It's time for class"
    I "Nice meeting you,"
    "She swiftly walks to her seat and sits down,"

    jump conthree

    label standstill:
    "Why should I?"
    "I shouldn't stand out too much,"
    "I don't know what they are like..."
    s "Hey; Why so lonely?"
    "I look up to see a girl"
    "I feel she is noticeably shorter than me."
    ka "I Don't know; Why do you ask?"
    s "I Don't know either..."
    ka "Ok..."
    s "Don't find me strange yet please!"
    "Yet. Interesting."
    ka "okay. Redeem yourself then?"
    s "I.."
    ka "Yeah?"
    s "I haven't redeemed anyone I've annoyed..."
    "How unfortunate."
    "I should say that out loud."
    ka "How unfortunate."
    "She grimaces with embarrassment."
    "Now I felt a psychological gut punch of guilt"
    "Surely I haven't done anything that bad yet?"
    ka "Fine, you are redeemed,"
    s "Ha! Got you!"
    "I fell right into it."
    s "Works every time!"
    s "You have to be my friend now!"
    ka "What?"
    s "If you don't hate me; you have to be something better than a stranger."
    "What a strange person."
    ka "I thought you have lots?"
    s "I do,"
    ka "What's so good to add me?"
    s "Everybody has potential."
    "So is everybody her friend?"
    ka "Have everyone you met become your friend then?"
    s "No"
    "I managed to suppress my laughter."
    ka "why?"
    s "Some don't feel the same way."
    "Which is understandable."
    s "Wanna be my friend?"
    "Strangely cute and polite"
    menu:
        "Yes":
            $izumifriend = True
            jump izumif

        "No":
            jump izumiu

    label izumif:
    s "Thank you!"
    s "I promise you a happy year!"
    s "You made a smart move, kiddo!"
    ka "kiddo..."
    ka "Thanks...?"
    s "I'm Tian Yi, but just address me by Yi.."
    I "and it's class time."
    "She quickly hops backs to her window seat."
    I "Nice meeting you!"


    jump conthree

    label izumiu:
    s "Ah, your loss"
    s "I'm Tian Yi by the way."
    I "But you can just call me Yi."
    I "It's class time now"
    ka "Ok"
    I "But I'm not done with you."
    ka "Acquaintances?"
    I "Yeah, that!"
    ka "ok"
    I "See you!"
    jump conthree

    label conthree:
    "The Teacher stands behind her pedestal,"
    "Kuno enters the doorway"
    k "Sorry for being late."
    "She bows in remorse,"
    t "You are excused,"
    t "Did we do attendance?"
    k "No"
    I "No, we didn't."
    t "Ok then,"
    "I turned around to scan the class."
    "There were two empty seats."
    "Yi had chosen a window seat,"
    "Dozing off as I had expected."
    t "Yi! Wake up!"
    I "I am!"
    "Despite the fact her eyes were still closed."
    "I noticed not many guys sat around her..."
    "That's a dangerous sign."
    t "Is Hiro away again? Fang also?"
    t "Geez..."
    "She clicks away on her laptop.."
    t "Free time for 20 minutes as I sort this out..."
    "Yi slides her desk up towards mine."
    I "So what are you going to do?"
    ka "Why do you bother with me?"
    k "Nearly all guys are scared of her."
    "Kuno has her desk faced towards us, joining in the conversation."
    ka "What?"
    I "Uh... Yeah."
    k "Any guy that knows her since middle school, is not willing to interact with her."
    ka "Ok"
    k "We're not supposed to bring it up..."
    I "Yeah."
    ka "I see."
    k "It's referred to as the great taming."
    "A few students laugh and giggle away as the phrase is mentioned."
    "Yi smiles patiently."
    ka "Taming... wow."
    "A brief moment of silence passes by..."
    "Before Yi initiates another conversation."
    I "Where are you going after school?"
    ka "I'll be going home straight away,"
    I "What?"
    ka "I might go buy some groceries..."
    I "Don't your parents buy them?"
    ka "I'm a transfer student.."
    "Kuno giggles away at Yi's blunder."
    "Another scarily awkward moment of silence passes between us."
    k "How much Chinese can you read in our class?"
    ka "eh?"
    ka "I can read it all; but I can't understand them all..."
    I "wow"
    ka "So..."
    I"Yeah?"
    ka "What is it about those students who are away?"
    I "Eh?"
    ka "Normally teachers don't have to 'sort out' an absence."
    I "True but ..."
    k "They have been away for 2 weeks now."
    k "They have no contact with anyone."
    "My spine shivers upon hearing this."
    I "I tried calling Fang, but she doesn't respond at all."
    k "yeah"
    ka "Is that worrying?"
    I "They aren't normally like this."
    k "They attended school everyday."
    k "Fang is a model student."
    I "Plus Hiro got a scholarship here."
    ka "So this isn't normal for them?"
    k "I guess so, but who are we to judge, no one truly knows each other..."
    k "Right?"
    "yeah."
    ka "Have you guys tried to go to their houses?"
    I "I knocked and was let inside but Fang was still shut in her room."
    I "She didn't respond or anything, she just knocked on the door..."
    ka "That is strange."
    k "Hiro is also a transfer student like you."
    k "He lives in an apartment."
    k "I knocked on his door, but I got no answer."
    k "Everyday I visited it the entrance looked more hostile."
    ka "What do you mean?"
    "Kuno's face went into deep thought."
    "It looked painful to remember..."
    k "You don't want to know."
    "I processed this surprisingly calmly."
    ka "Are you going to visit him today?"
    "Her face went down again."
    k "I don't know."
    I "I'm going to meet Fang. Her mum told me to come today."
    ka "why?"
    "I realized instead of thinking I just spoke aloud."
    I "She didn't say, but I am definitely coming."

    "Class seemed to skip quickly."
    "I was absorbed in my thoughts when Yi slammed a pile of books on my desks."

    menu:
        "Ask her what it is":

            jump izumiplain

        "Sigh":
            jump izumiannoying





    label confive:
    "You expect me to carry your books?"
    jump tempend

    label izumiplain:
    I "Don't you know?"
    jump tempend

    label izumiannoying:
    "Leave me alone"
    jump tempend

    label tempend:
    I "You have to carry my books!"
    ka "You're kidding me right?"
    I "Can't you take me seriously?"
    "She whines for a minute."
    "How does a cute girl like her become like this?"
    "Kuno seems tired of this already."
    k "Here... I can."
    "kuno steps in to grab the books..."
    I "ahhhhh Its fine!"
    "She smiles embarrassingly"
    k "Stop trying to annoy him then."
    I "I'm not"
    "Her face didn't match her phrase."
    "Yet I wasn't that cruel right?"
    "I felt inclined to help her."
    "Regardless of my reluctance with her."

    menu:
         "Help her out":

             jump helpTian
             $ izumilove +=1

         "Leave her be":
             jump leaveTian
             $ kunolove +=1
label leaveTian:
    "She whines and walks ahead"
    "Kuno stares off at her as she walks heaving the books."
    k "She can lift those books."
    k "Regardelss of how heavy they will be."
    k "I guess she wants Fang to meet someone new."
    ka "So where is your house?"
    "She was absorbed in thought when I said this."
    k "Oh!"
    k "I have to visit Hiro."
    "That boy she mentioned who was absent."
    k "As class leader it is my responsibility to check up on them."
    "Was that the onyl reason she wss going?"
    k "Wanna come?"
    "What is the worst that can happen?"
    ka "Sure"
    "Kuno begans to lead the way."
    k "My house is on the way to his house actually."
    ka "I see."
    "We walk side by side in silence for a few minutes."
    k "So do you remember me?"
    ka "I don't know."
    k "When you looked like you saw a ghost I knew you knew."
    ka "What?"
    k "Don't be stupid."
    ka "Fine."
    "No wonder she is class representive"
    k "Do you remember that school?"
    "I clench my fist in my pockets as I attempt to think."
    "Old windows, creepy teachers and lots of drama."
    "Something I genuinely want to forget."
    ka "Yeah."
    k "Do you remember the girl that left early?"
    "I have to force myself to think once again."
    "Long hair, depressed as hell, wearing a mask in the bathrooms apparently."
    ka "The mask one?"
    k "Wearing a scarf around her mouth... yeah."
    ka "I remember."
    k "She's ended up in this school."
    "I was slightly surprised by this."
    "How did so many childhood acquaintances end up here?"
    "Across the country?"
    ka "How come both you and her ended up here?"
    k "She's my sister now."
    "Wow, I always wondered of that girl, Kuno should know eerything about her at this point."
    ka "Your dad remarried?"
    k "He decided he moved on."
    "It must have been a few years since he lost her."
    ka "How did he meet 'her' mum?"
    k "'her' name is An"
    ka "I see, quite or peace."
    k "When did your chinese get really good?"
    "I myself have no idea."
    k "You went to Japan for like 8 years."
    k "The stayed across southern China for four years."
    ka "Mosty Guangzhou."
    k "Must be a good four years huh?"
    "She giggles gently."
    ka "I've bet you've had 10 boyfriends already right?"
    k "What a rookie. It's against school rules."
    "She smirked."
    "I seemed to forget that relatioships<education in these schools."
    "Down South it never happened; I guess it was a silent rule."
    ka "But guys break it stil right?"
    k "Yeah."
    "She giggled once again."
    k "5 confesisons!"
    ka "What!"
    "We both burst out laughing."
    k "They weren't that attractive actually."
    "She facepalms."
    k "One of them confessed twice in fact."
    k "But you know Fang got way more!"
    "That girl that is absent."
    ka "How many?"
    k "Like 10 guys more than once!"
    k "Even the hottest guys!"
    ka "Looks aren't everything idiot."
    k 'Of course.'
    "She looks at me with a smile I haven't seen in a long time."
    k "While you were in Japan didn't you get a girlfriend?"
    "How should I answer this..."
    menu:
         "Lie":

             jump girllie

         "Tell the truth":
             jump girltruth
             $ kunolove +=1
label girllie:
    ka "Yeah I had one."
    k "what?!"
    "She looks very surprised."
    "This seemed to hurt my ego."
    ka "The hottest girl there."
    k "You're kidding right?"
    ka "Nope."
    k "How?"
    ka "She confessed to me."
    k "What did it feel like?"
    ka "Amazing."
    "I won't be able to keep this up much longer."
    k "What kind fo things did you guys do?"
    ka "Shopping, eating together, karaoke."
    "Somehow the smart Kuno I know is beleiving all this quite easily."
    k "Did y-y guys... k-"
    ka "Kiss?"
    k "Yeah lots."
    "She turns aways clenching her fists angrily."
    k "Fuck, you're lucky as!"
    ka "We broke up when we had to move here."
    k "Was she the type your mum would like?"
    "I couldn't hold in my laughter."
    "It was still depressing this was all my imagination."
    ka "My mum was happy as her as my girlfriend."
    ka "She said a 'perfect wife'."
    k "Lie."
    ka "What?"
    k "Your mum would never allow you to have a girlfriend."
    "She turns and laughs into the shadows of the bush adjacent to us."
    k "Nice story."
    k "idiot."
    "I sigh."
    jump toldthetruth

label girltruth:
    ka "I didn't."
    "Kuno was trying to keep in a smirk."
    k "Not surprised."
    ka "Why?"
    "She places her hand on her chin and thinks."
    k "Your mum would kill you."
    "She giggles."
    "She warned me many times in fact."
    jump toldthetruth

label toldthetruth:
    k "So no girl confessed to you also?"
    ka "Well... one did."
    "She turns surprised."
    k "Tell me more!"
    ka "Just my best friend at the time."
    "She turns to face ahead of us again."
    k "Would you have said yes if you could?"
    ka "I don't know."
    "Long hair swinging in the wind."
    "chocolate brown eyes."
    "pink lips with a beautiful smile."
    "Warm hands and caressing touch."
    "A soft heart, pitiful."

    menu:
         "Yes":
            "Why not."
            "SHe was the only girl who ever cared for me."
            "Why did I have to hurt her that day..."
            jump hirohouse

         "No":
            "I said No for a reason."
            "What she chose to do was not my fault."
            "..."
            $ change +=1
            jump hirohouse


label hirohouse:
    k "Hey!"
    "I'm knocked out of my mind."
    ka "Are we here?"
    "I said that as I realised I was standing eight in front of a door to a houe."
    k "What do you think idiot?"
    ka "yep."
    "We wait for a minute patiently."
    "I notice the crickets don't chirp."
    ""
    ka "Why aren't they answering?"
    k "Did you knock?"
    ka "No I was busy thinking..."
    ka "Did you?"
    k "No?!?"
    "What the hell?...."
    k "I swear I heard you?"
    "She swiftly steps in front and knocks on the door."
    k "We're both so stupid."
    ka "Means you haven't changed."
    "I cracked up inside but I couldn't laught at all."
    "There was some shuffling towards the door."
    "After a few clicks and clacks the door opens."
    "A young attractive girl stands there."
    ka "Who is that?"
    k "Shut up."
    "She pokes my ribs."
    k "We are hear to see Hiro."
    "The women stood there confused."
    "It was cler she couldn't understand us."
    k "Idiot speak Japanese to her."
    ka "Fine."
    "I sigh to her and turn to the woman."
    "I explain we have to meet Hiro."
    "She nods her head."
    "She walks off into the house leaving us to explore."
    ka "It's a nice place."
    "It was spotlessly clean. A feat I couldn't achieve."
    "I look at Kuno who keeps walking into the house."
    "She stops at a door with posters taped on it."
    "She knocks lightly."
    k "Hiro! It's me Kuno!"
    "She said it softly yet urgently."
    "She waited for a minute."
    "No reply."
    "She turns to me."
    "Oh boy."
    k "Get over here!"
    "I amble over to his door."
    "I must speak Japanese to him."
    "I mutter some phrases."
    "I can hear a sob on the other side."
    "should I keep talking?"
    menu:
         "I keep talking to him.":
            "My words seem to reach him as more sounds begins to manifest through the door."
            "His sobs fade as jumbled detactched fragemtns of phrases are deciphered."

            jump hirosave

         "I ask him to open the door.":
            "The sounds stop and there is no more response."
            $ hirofirstfail = True
            jump hiroend
label hirosave:
    "The door clicks and turns."
    "It creaks open to show a boy with dark circles and baggy eyes."
    "They're red from crying."
    'Kuno looks at me surprisingly.'
    k "Keep going..."
    "He's silent with her arms folded."
    "It seems he won't budge anytime soon."
    k "I'll go gt something for him to eat."
    "Kuno quickly walks towards the kitchen, leaving me with Hiro."
    "He looks like a corpse."
    jump nexxday

label hiroend:
 k "Great, smartass"
 ka "What?"
 k "You've ruined it."
 ka "I didn't mean to."
 "Kuno facepalms and stands up."
 k "I'm not bringing you next time."
 "Come on."
 "The women from earlier keeps her eyes from us above a smile."
 "Almost like a mask."
 jump nexxday

label nexxday:

 "fin"
 "(we are not French)"
 "we aren't finished also"
    # This ends the game.

return

#car sound
#2 months later
