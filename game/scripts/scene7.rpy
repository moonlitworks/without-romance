label scene7:
  # SCENE 7:

  $ renpy.pause(2)
  
  scene bg ren_room with Dissolve(2.0)
  window show dissolve

  play music the_end fadein 2 fadeout 2

  "The house is quiet."
  "For such a large estate that might not be so unusual, but still I take pause as I step inside on my daily visit."
  "Is it worth my time? I’m not sure."
  "For days, I’ve not heard a sound from Ren."
  "The sound of his hand... I rub my arm, a chill running through my body."

  "{i}\"-sa?\"{/i}"

  "If only I'd thought things through more..!"

  ruth stare_open "Risa, are you okay?"
  risa dress_neutral "Eh?"

  "Standing before me, Ruth regards me with a good deal of confusion. When did she..?"
  "Forget it. It doesn’t matter. What am I doing, turning up only to space out?"

  risa "Oh it's you Ruth. Sorry, I've a lot on my mind lately."

  "Ruth flashes me an understanding smile."
  "Even though she hadn't been party to the events surrounding Rose's departure, she’s watched over Ren for long enough to pick up the signs."

  ruth "I take it you're here for Ren today, too?"
  risa "Is he taking visitors?"

  "The past couple of visits I’ve arrived only to pace outside Ren's study."
  "Seeing him sitting alone... Whatever words I'd wanted to give him had vanished from my mind."
  "Would he even want to see me? That fear had kept me distant, even as he suffered."
  "She turns her head, glancing towards what could only be Ren's location. Gears turn over and over before she lets out a steadying breath."

  ruth "It seems I've forgotten. Whatever had he said..."
  risa "Ruth?"
  ruth "I'm sure he said {i}something{/i} but... Oh dear, how unlike me."
  ruth "It would seem in all the extra work I have it slipped my mind."

  "Ruth hangs her head in shame. She smiles as she spins her back to me, pacing away into the depths of the estate."

  risa dress_smile "Thank you, Ruth!"
  ruth "For forgetting my duties? For a future member of the Yamato's, you'd do better to chastise me, Risa."

  "The usually composed Ruth unceremoniously waves her hand in parting."
  "She’s a mystery all of her own - but one I’ll have to unravel another day."
  "In that case..."

  risa dress_neutral "She looked toward the study, right?"

  "I turn to follow where Ruth's eyes had pointed moments ago."
  "There is only one room where Ren would be; the very room I’ve hesitated to enter ever since that day."
  
  risa "Really, causing her so much trouble..."

  "I’ll have to complain on Ruth’s behalf when I see him. To make her worry is utterly unfair of him."
  "A familiar doorway looms before me. My fingers curl away from the handle as I reach toward it, my heart jumping in my chest."

  risa "This won't be like last time..."

  "I open the door as quietly as I can, taking great care to close it behind me."
  "Across the room, a lonely back faces me."
  "One step. Two."
  "On my third, I am made to pause."

  ren neutral "Ruth, do you need something? I'm busy, surely whatever it is can wait."

  "His eyes briefly move from the ground of the garden to the clouds scrolling by above."
  "Through our silence he regards them with what I can only imagine is a great indifference."

  ren "And I thought I'd told her I didn't want guests. How bothersome."
  risa "You're lucky to have her by your side. Do you intend to turn me away?"
  ren "...No."
  ren "In a way, I'm glad to see you."
  ren "This house has felt terribly empty of late."

  "I close the distance between us as his eyes return to rest on his lap once more."
  
  scene cg end with Dissolve(1.0)
  "Sitting beside Ren, their target becomes clear."

  ren neutral "I made it hard for you to talk to me recently."
  ren "I'm sorry for that, Risa. To have acted so pathetically... it's unlike me."

  "His fingertips curl with his words."

  risa dress_neutral "If anybody should apologize, it should be me. If it weren't for my suggestion, this would never-"
  ren "Do you really think you can absolve me of my mistakes?"
  ren "No, Risa. I did what I did to protect the Yamato name."
  ren "You're soon to be a Yamato, just as I am. To tolerate such belittlement..."

  "Ren's voice cracks."

  risa "But at the price of your own happiness?"
  risa dress_worried "I can't just accept that, Ren!"
  risa "But even when I tried to help, I just drove you further apart."

  "A chuckle breaks forth from Ren’s lips. How can he find this funny?"

  ren smile "You're my bride-to-be."
  ren "Wouldn't you say you were just doing your job? Magnificently, at that."
  risa "But I'm only here for my own gain! I can never give you the future that Rose could."

  "Ren's hand twitches at her name."

  ren neutral "You're right. But is there anything wrong with that?"
  
  "He turns his gaze on me, his eyes peering into the depths of mine."

  ren "Our union... "
  extend "It's a business transaction."
  ren "Nothing more, nothing less. Something of benefit to both parties."
  ren "So you're right, Risa."
  ren "I can't imagine I'll ever come to love you as I did Rose."
  ren "But I can provide you with a home, and your family with security. And in turn..."
  risa dress_neutral "...I'll carry on the Yamato lineage."
  ren "See? A fair trade to my eyes."
  ren "So don't let anybody speak of you that way again."
  ren "To run your name through the dirt is to disgrace the Yamato's. To disgrace {i}your{/i} family."

  "A wry grin comes my way; one I can’t resist returning."
  "It’s so laughable. Yet, with this, my family’s future is assured. They’ll never have to worry again."

  "I laugh."
  "All that talk as a child of a prince to whisk me away to happiness..."
  "Will my parents be proud? Or will they condemn me for putting them first?"
  "A family for a family."
  "To protect my own, I will carry on on the Yamato bloodline."

  "If my life were told as a fairy tale, what form would it take?"
  "Would it commend me for my dedication?"
  "Celebrate my sacrifices, in the name of the greater good?"
  "Or would I be a cautionary tale; a fable against throwing away your future?"
  "Only time would tell how the story of the selfish princess might unfold."
  "Of the girl who gave herself to a loveless life."
  "A future"
  extend " without romance."

  # blur before end
  window hide dissolve
  
  jump end
  return