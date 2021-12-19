transform topMenu:
  subpixel True
  xalign .5
  on show, replace:
    alpha 0.0 yalign 0.0 yanchor 1.0
    parallel:
      easein 1.0 alpha 1.0
    parallel:
      easein 1.0 yanchor 0.0
  on hide, replaced:
    alpha 1.0 yalign 0.0 yanchor 0.0
    parallel:
      easein 1.0 alpha 0.0
    parallel:
      easein 1.0 yanchor 1.0

transform bottomMenu(time=1.0, delay=0.0):
  subpixel True
  xalign .5
  on show, replace:
    alpha 0.0 yalign 1.0 yanchor 0.0
    time delay
    parallel:
      easein time alpha 1.0
    parallel:
      ease_back time yanchor 1.0
  on hide, replaced:
    alpha 1.0 yalign 1.0 yanchor 1.0
    time delay
    parallel:
      easein time alpha 0.0
    parallel:
      ease_back time yanchor 0.0

transform leftMenu:
  subpixel True
  yalign .5
  on show, replace:
    alpha 0.0 xalign 0.0 xanchor 1.0
    parallel:
      easein 1.0 alpha 1.0
    parallel:
      easein 1.0 xanchor 0.0
  on hide, replaced:
    alpha 1.0 xalign 0.0 xanchor 0.0
    parallel:
      easein 1.0 alpha 0.0
    parallel:
      easein 1.0 xanchor 1.0

transform rightMenu:
  subpixel True
  yalign .5
  on show, replace:
    alpha 0.0 xalign 1.0 xanchor 0.0
    parallel:
      easein 1.0 alpha 1.0
    parallel:
      easein 1.0 xanchor 1.0
  on hide, replaced:
    alpha 1.0 xalign 1.0 xanchor 1.0
    parallel:
      easein 1.0 alpha 0.0
    parallel:
      easein 1.0 xanchor 0.0


transform fadeMenu:
  subpixel True
  on show, replace:
    alpha 0.0 #xzoom 1.2 yzoom 1.2
    easein 1.0 alpha 1.0 #xzoom 1.0 yzoom 1.0
  on hide, replaced:
    easeout 1.0 alpha 0.0 #xzoom 0.8 yzoom 0.8

transform same_transition(old, new):
  old
  new with Dissolve(0.2, alpha=True)



transform mainMenuItem(time=1.0, delay=0.0):
  subpixel True
  yalign .5
  on show, replace:
    alpha 0.0 xpos 100
    time delay
    parallel:
      easein time alpha 1.0
    parallel:
      easein time xpos 0
  on hide, replaced:
    alpha 1.0
    time delay
    parallel:
      easeout time alpha 0.0
    parallel:
      easeout time xpos 100


transform quickMenuItem(time=1.0):
  subpixel True
  xpos 0
  on show:
    alpha 0 xpos 10
    linear 0.3 alpha 1 xpos 0
  on hide:
    alpha 1 xpos 0
    linear 0.3 alpha 0 xpos 10
  on idle:
    linear 0.1 xpos 0
  on hover:
    linear 0.1 xpos 5


transform change_transform(old, new):
  contains:
    old
    alpha 1.0
    linear 0.2 alpha 0.0
  block:
    new
    alpha 0.0
    linear 0.2 alpha 1.0

define config.side_image_change_transform = change_transform