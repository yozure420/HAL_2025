from slime import Slime
# slimes[0] には '○' と '=' を使う
slime1 = Slime(head='○', body='=')
# slimes[1] には '★' と '~' を使う
slime2 = Slime(head='★', body='~')

slimes = [slime1, slime2]

while slimes[0].position <= 10 and slimes[1].position <= 10:
    for slime in slimes:
        slime.run()
    print('----5----0')