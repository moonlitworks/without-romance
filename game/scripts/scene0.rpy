label scene0:
  $ achievement.register("WITHOUT_ROMANCE", steam="WITHOUT_ROMANCE")
  $ achievement.steam_position = "bottom right"
  $ achievement.sync()
  # SCENE 0: Prologue
  "An outsider would likely not believe it."
  "I can still barely believe it myself."
  "If I wake up and realize this is all just a dream, I won't be surprised."
  "A fairy tale."
  "That's the only way I can describe it."
  "I loved those stories as a kid."
  "Fantasizing about being one of the many princesses."
  "And now, here I sit."
  "Enjoying the view with Prince Charming by my side."
  "Just like how those stories end."
  "Except"
  extend ", love is not our happy ending."

  window hide dissolve
  scene black with Dissolve(1.0)
  jump scene1
  return