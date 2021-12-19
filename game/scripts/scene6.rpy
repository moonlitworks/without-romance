label scene6:
  # SCENE 6: Decision
  risa dress_worried "Ren..."

  "I watch him leave, my back turned on the girl who'd just spilled her heart out."

  risa "..."

  "Words abandon me. As Ren vanishes beyond the doorway, her whisper fills the room."

  rose neutral "That must have given you quite the show."
  risa dress_neutral "I didn't want to interrupt the two of you."
  rose "How thoughtful."

  "Her eyes are distant, looking somewhere far away; to something beyond her reach."
  "A long, tired sigh escapes her lips - gazing at them only reminds me of their embrace..."

  rose "To be honest with you Risa..."
  risa "Yes?"
  rose smile_open "This is my first time meeting a voyeur."
  rose "My heart really started racing when I saw you!"
  rose "I can't help but worry you might have awakened something..."
  risa "Can we hurry up and put it behind us? I'm not particularly proud of it, you know."

  "My brows knit together but Rose only chuckles at my frustration."
  "When her eyes had first met mine through the doorway, I could have sworn a fire burned inside, but the way she spoke..."

  risa "...You aren't angry at me for spying on you?"
  rose neutral "Angry? Hmm..."

  "The churning of my stomach makes the wait for her words stretch on and on."
  "Is she doing it to me on purpose?"

  rose smile_open "I say forgive and forget."
  rose "There are worse things to worry about in life, and I'm sure I'd have done the same."

  "I breathe a sigh of relief, only to hear that trademark giggle."

  rose "I don't think we've ever had much of a chat before have we?"
  rose "For all the time we spend around one another, it amazes me."

  "I think back on the days we spent skittering around the Yamato estate."
  "Despite me being Ren's fiancée, Rose had dominated his time."
  "I'd rarely had a chance to even offer her my greetings, let alone have a leisurely talk."

  risa dress_smile "I think you're right. How odd."
  rose "Isn't it?"

  "I couldn't help but smile at the idle chatter, warmth slowly returning to the room."

  rose "What do you do for fun, Risa?"
  rose "I've been trying gardening lately myself, but..."
  rose "I'm loath to admit it, but I think my name is the closest I'll get to that talent..."

  "I choke back a laugh but not well enough for Rose's keen eyes, a grin breaching her face."

  risa "That's a surprise. I'd have thought you'd be a natural!"
  rose "If only! I'm sure you're a magnificent gardener, Risa."
  risa "Gardening, huh?"

  "My eyes turn to Ren's garden."
  "With not so much as a single leaf out of place, I can't even begin to imagine the work that goes into maintaining it."
  "Rose tilts her head softly to one side, regarding me curiously."

  rose "You've never tried?"
  risa "I've never had the chance."
  risa "Our home doesn't have a garden, after all."
  rose "O-oh, I see. That's quite a shame."
  rose "Although before long I'm sure you could have an entire field to yourself if you wished."
  rose "Lucky."

  "Rose's lips twist into a wry smirk."

  risa dress_neutral "There's a lot of luck in this world, and if it finds me - or my family - I'd be a fool to refuse it."
  rose smile_closed "Well it certainly seems you'll all be living a good life. How nice it will be!"

  "My body stiffens. The fire is back, burning inside her eyes as fiercely as before."
  "I clench my fist until my knuckles turn white, fighting to hold what courage I can muster."

  risa "I could want nothing more than warmth for the parents who gave me everything."
  rose smile_open "My, how touching. It really brings a tear to the eye..."

  "Rose dabs at the corner of her eye, dry as bone."

  rose "Do you stop to think what it costs along the way, Risa?"
  risa "..."
  rose "To be chosen by the Yamato's despite your humble roots, it's nothing short of fantasy."
  rose "To meet your prince, for it to be love at first sight..!"
  rose "Oh wait, that's not quite right, is it?"
  risa dress_worried "Rose-"
  rose "I guess my future with Ren just wasn't meant to be."

  "My mouth runs dry."
  "What can I say? She’s a necessary casualty? She’ll find somebody new?"

  risa "...Don't think I like seeing you two apart."
  
  "Rose's eyes twitch."

  rose neutral "And yet you still toss us aside."
  rose serious "For what? Money?"
  rose "There's plenty of money in the world, but only so many soulmates! Don't you see that?"

  "Pain flares up my hand, my nails digging into my skin."
  "She's not wrong. In fact, if anybody is in the wrong, it's me for being so selfish."
  "For asking so much. And yet..."

  risa "I won't apologize."
  rose "You're sacrificing Ren's future for your own, doesn't that bother you?"
  rose "Don't doom Ren to a loveless life, when you're nothing but a gold digger!"

  "I feel a punch to my gut with her trailing words."
  "She's right. For the sake of my family, I would sacrifice Ren's love with Rose a hundred times over."
  "If it means having the money for a good life..."
  "There is nothing I won’t do."
  "And yet, part of me knows I’m being greedy."
  "No matter how my heart might waver, I won’t falter."
  "Some chances are too precious to let slip by."

  play audio slam
  "A bang shoots out as the door flies open; in the doorway stands Ren, his eyes trained on the ground between us."

  risa dress_neutral "Y-you're back, that didn't take long?"

  "With my words, I unwittingly undo the magic that had bound him to that spot."

  play sound footsteps
  "His eyes regaining focus, he strides towards Rose- No, surely..."

  risa dress_worried "Ren, wait!"

  "I shoot out a hand but he slips by too quickly, until-"
  
  stop sound

  $ channel = renpy.audio.audio.get_channel("music")
  $ channel_volume = channel.context.secondary_volume
  $ renpy.music.set_volume(0)

  scene cg white
  play audio slap
  scene cg slap with Dissolve(2.0)

  $ renpy.music.set_volume(channel_volume, delay=2)

  ren blank "This house doesn't welcome those who would badmouth our family."
  risa dress_worried "Ren, she didn't-"
  ren "You're soon to be part of the Yamato family, Risa."
  ren "That's how things are decided, and no matter what some might wish..."

  "His voice catches slightly in his throat but he continues, forcing the words out."

  ren "No matter what some might wish, that's how it will be."
  ren "I'm sure you can find your way out, Rose, or shall I have Ruth escort you?"

  "The girl clutches her cheek, refusing to let tears spill from her eyes as she stares defiantly back at Ren."
  "In that moment, I can tell she holds a strength that I could never dream of."

  scene bg ren_room with Dissolve(1.0)
  rose blank "I'm sorry, Ren..."
  rose "Goodbye."
  ren blank "...Goodbye."

  "Such are the final words between the two."
  "Rose is gone, never looking back."
  "Unable to see how Ren's eyes follow her departure, or how they shine in the light."
  "I walk to his side, staying a few steps back."
  "He keeps clenching his fist - open, closed, open, closed... But the shaking won’t stop."

  risa dress_worried "I'm sorry - if I'd handled things better-"
  ren "...You too."
  risa "Huh? Ren, what do you..?"
  ren "I have work to finish by tonight. Ruth is relying on me."

  "Even as his eyes refuse to meet mine, the lie in his voice rings loud and clear."

  risa "..."

  "The sight of Ren's back is haunting."
  "Once so strong - so confident - is now shrivelled; his gaze lingering on his stinging hand."

  stop music fadeout 4

  risa "Tomorrow, then."

  "I wait for parting words, or a wave of a hand. When it’s clear there will be no such sign, I leave the room."
  "Wiping the mist from my glasses, I fight the burning in my eyes."

  window hide dissolve
  scene black with Dissolve(1.0)
  
  jump scene7
  return