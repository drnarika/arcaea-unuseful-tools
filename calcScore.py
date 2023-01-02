
#算分器
from time import time



notes = 0

while True:
    note = input('物量')
    if note == '': 
        break
    else:
        notes+=int(note)

far = int(input('far'))
lost = int(input('lost'))
bigpure = int(input('大p,-多少'))
sid = input('歌名')
rating_song= float(input('歌曲定数'))

#Score caculate
fullScore = 10000000
pureOne = fullScore / notes
farOne = -pureOne / 2
lostOne = -pureOne

#clear_type
clear_type=4
if lost == 0:
    clear_type=2
    if far == 0:
        clear_type=3

score = fullScore + far*farOne + lost*lostOne + notes - bigpure
score = round(score)
print(score)

#rating
rating=0.0
exline=9800000
aaline=9500000
if score>=exline:
    rating=rating_song+1+(score-exline)/200000
    if score>fullScore:
        rating=rating_song+2
else:
    rating=rating_song+(score-aaline)/300000

print(
    'update best_score set ',
    'score=',score,
    ',shiny_perfect_count=',notes - far - lost - bigpure,
    ',perfect_count=',notes - far - lost,
    ',near_count=',far,
    ',miss_count=',lost,
    ',health=100',
    ',modifier=2',
    ',time_played=',round(time()),
    ',best_clear_type=',clear_type,
    ',clear_type=',clear_type,
    ',rating=',rating,
    ' where user_id=\'2000001\' and song_id=\'',sid,'\' and difficulty=2;',
    sep='')