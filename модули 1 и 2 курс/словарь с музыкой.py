violator_songs = {
    'World in My Eyes' : 4.86,
    'Sweetest Perfection' : 4.63,
    'Personal Jesus' : 4.56,
    'Halo' : 4.9,
    'Waiting for the Night' : 6.07,
    'Enjoy the Silence' : 4.20,
    'Policy of Truth' : 4.76,
    'Blue Dress' : 4.29,
    'Clean' : 5.83
}
songs=[]
kolichestvo=int(input('Сколько песен выбрать? '))
for i in range(kolichestvo):
    a=input('Название песни: ')
    if a in violator_songs:
        b=violator_songs[a]
        songs.append(b)
time=sum(songs)
print('Общее время звучания песен: ', time)