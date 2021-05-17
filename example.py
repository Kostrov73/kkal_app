import pandas as pd
import matplotlib.pyplot as plt
# Этап постановки проблемы:
# Сформулируй несколько гипотез.


##   Фильмы определенных режиссеров собирают больший рейтинг.
##   Определенные жанры собирают больше положительных отзывов зритилей.
##   Фильмы, относящиеся к нескольким жанрам, более популярны.
##   Присутствие среди исполнителей определённых актёров повышает рейтинг фильма.

# Этап извлечения данных:
# Здесь должен быть твой код
# Дополнительную информацию о синтаксисе можно найти здесь: https://pandas.pydata.org/docs/
df = pd.read_csv('IMDB-Movie-Data.csv')

# Этап подготовки данных:
# Здесь должен быть твой код
df['Revenue (Millions)'].fillna(0, inplace=True)
df['Metascore'].fillna(0, inplace=True)


# Этап исследования данных:
# Здесь должен быть твой код
def make_genres(genre):
    return len(genre.split(','))
def spl(act):
    return act.split(',')

def make_actors(act):
    if 'Chris Pratt' in act:
        return 'with'
    else:
        return 'without'



df['Genres_score']=df['Genre'].apply(make_genres)
d1=df.groupby(by='Genres_score')['Votes'].max()

df['Actors']=df['Actors'].apply(spl)
df['Avialability']=df['Actors'].apply(make_actors)
d2=df.groupby(by='Avialability')['Rating'].mean()

print(d1)
print(d2)



#print(a[-10:])
# Этап визуализации данных:
# Здесь должен быть твой код
#d1.plot(kind='pie')
d2.plot(kind='bar')
plt.show()

# Этап решения:
# Подготовь презентацию с описанием гипотез и результатами исследования.