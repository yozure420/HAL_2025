from slime import Slime
slimes = [Slime(),Slime()] #スライムをリストで管理
while slimes[0].position <= 10 and slimes[1].position <= 10:#andをorにしてしまった
    for slime in slimes:
        slime.run()
    print('----5----10')