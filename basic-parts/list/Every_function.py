musics = ["video-games", "born-to-die", "radio", "dark-paradise", "chandelier", "bad-guy", "psycho"]

print(musics[0].title())
print(musics[1].lower())
print(musics[2].upper())
print(musics[3].title())
print(musics[4].lower())
print(musics[5].upper())
print(musics[6].title())


musics.append('stiches')
print(musics)

musics.insert(0, 'thank-u-next')
print(musics)

del musics[4]
print(musics)

favourite_M = musics.pop(2)
print(musics)
print(f"\n{favourite_M.title()} is my favourite in this list.")

musics.remove('stiches')
print(musics)

by_maisie = 'psycho'
musics.remove(by_maisie)
print(musics)


print(sorted(musics))
print(sorted(musics, reverse=True))
print(musics)


musics.sort()
print(musics)

musics.sort(reverse=True)
print(musics)

musics.sort()
print(musics)

musics.reverse()
print(musics)

print(len(musics))
print(musics[-1])






