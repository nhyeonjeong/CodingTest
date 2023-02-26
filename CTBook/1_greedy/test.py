apply, genre, go_up = map(int, input().split())
genre_list = []
score = [0] * (apply + 1)
for _ in range(genre):
    genre_list = list(input().split())
    for i in range(apply):
        score[int(genre_list[i * 2])] = max(score[int(genre_list[i * 2])], float(genre_list[i * 2 + 1]))
del score[0]
score.sort()
for i in range(apply-go_up):
    del score[i]
print(round(sum(score),1))
