init -20 python:
  import discord_rpc
  import requests
  import time

  start = time.time()
  _preferences.mobile_rollback_side = "left"

  # Menu image for smooth fade
  menu_image = "cg/end.png"
  menu_image_blur_value = 1.0
  renpy.image("menu_image", Image(menu_image))
  renpy.image("menu_image_blur", im.Blur(menu_image, menu_image_blur_value))

  def readyCallback(current_user):
    print(current_user)
    print('Our user: {}'.format(current_user))

  def disconnectedCallback(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
      codeno, codemsg
    ))

  def errorCallback(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(
      errno, errmsg
    ))

python early:
  show_text_during_trans=True

### Characters
define risa = Character(_("Risa"), image="risa_sprite")
define rachel = Character(_("Rachel"), image="rachel_sprite")
define ruth = Character(_("Ruth"), image="ruth_sprite")
define rose = Character(_("Rose"), image="rose_sprite")
define ren = Character(_("Ren"), image="ren_sprite")
define roger = Character(_("Roger"))

### Sprites
image side risa_sprite dress_neutral = im.FactorScale("risa/risa_dress_neutral.png", 0.6)
image side risa_sprite dress_smile = im.FactorScale("risa/risa_dress_smile.png", 0.6)
image side risa_sprite dress_worried = im.FactorScale("risa/risa_dress_worried.png", 0.6)
image side risa_sprite toga_neutral = im.FactorScale("risa/risa_toga_neutral.png", 0.6)
image side risa_sprite toga_smile = im.FactorScale("risa/risa_toga_smile.png", 0.6)
image side risa_sprite toga_worried = im.FactorScale("risa/risa_toga_worried.png", 0.6)

image side rachel_sprite smile_closed = im.FactorScale("rachel/rachel_smile_closed.png", 0.6)
image side rachel_sprite smile_open = im.FactorScale("rachel/rachel_smile_open.png", 0.6)
image side rachel_sprite worried = im.FactorScale("rachel/rachel_worried.png", 0.6)

image side ren_sprite neutral = im.FactorScale("ren/ren_neutral.png", 0.6)
image side ren_sprite smile = im.FactorScale("ren/ren_smile.png", 0.6)
image side ren_sprite serious = im.FactorScale("ren/ren_serious.png", 0.6)
image side ren_sprite blank = im.FactorScale("ren/ren_blank.png", 0.6)

image side rose_sprite smile_open = im.FactorScale("rose/rose_smile_open.png", 0.6)
image side rose_sprite smile_closed = im.FactorScale("rose/rose_smile_closed.png", 0.6)
image side rose_sprite serious = im.FactorScale("rose/rose_serious.png", 0.6)
image side rose_sprite neutral = im.FactorScale("rose/rose_neutral.png", 0.6)
image side rose_sprite blush = im.FactorScale("rose/rose_blush.png", 0.6)
image side rose_sprite blank = im.FactorScale("rose/rose_blank.png", 0.6)

image side ruth_sprite stare_open = im.FactorScale("ruth/ruth_open.png", 0.6)
image side ruth_sprite stare_closed = im.FactorScale("ruth/ruth_closed.png", 0.6)

### CGs
image cg flashback = "cg/flashback.png"
image cg kiss_open = "cg/kiss_open.png"
image cg kiss_closed = "cg/kiss_closed.png"
image cg hangout = "cg/hangout.png"
image cg slap = "cg/slap.png"
image cg white = "cg/white.png"
image cg end = "cg/end.png"
image cg end_blur = im.Blur("cg/end.png", 1.0)

### BGs
image bg logo = "bg/moonlit.png"
image bg ren_room = "bg/ren_room.png"
image bg graduation = "bg/graduation.png"
image bg ruth_room = "bg/ruth_room.png"

### OSTs
define audio.the_end = "audio/The End.ogg"
define audio.dissidence = "audio/Dissidence.ogg"
define audio.unresolved_feelings = "audio/Unresolved Feelings.ogg"

### SFXs
define audio.slam = "audio/slam.mp3"
define audio.slap = "audio/slap.mp3"
define audio.crowd = "audio/crowd.mp3"
define audio.footsteps_wood = "<from 0 to 5>audio/footsteps_wood.mp3"
define audio.footsteps = "<from 0 to 3>audio/footsteps.mp3"
define audio.shutter = "audio/shutter.mp3"
define audio.slidingdoor = "audio/slidingdoor.mp3"

screen prestart_screen:
  timer 1.0 action Start()

label prestart_label:
  scene menu_image_blur
  $ renpy.call_screen("prestart_screen")
  return

label splashscreen:
  play music the_end
  scene bg logo with Dissolve(1)
  $ renpy.pause(1.0)
  scene menu_image_blur with Dissolve(1)
  return

label before_main_menu:
  python:
    callbacks = {
      'ready': readyCallback,
      'disconnected': disconnectedCallback,
      'error': errorCallback,
    }
    discord_rpc.initialize('721882249825353791', callbacks=callbacks, log=False)
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    discord_rpc.update_presence(
      **{
        'details': 'Testing',
        'large_image_key': 'logo',
        'start_timestamp': start
      }
    )
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
  return


label start:
  python:
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    discord_rpc.update_presence(
      **{
        'details': 'Testing',
        'large_image_key': 'logo',
        'start_timestamp': start
      }
    )
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()

  # unblur before start
  scene menu_image_blur
  scene menu_image with Dissolve(2.0)
  window show dissolve
  jump scene0
  return

label end:
  scene menu_image_blur with Dissolve(2.0)
  $ renpy.full_restart()
  return