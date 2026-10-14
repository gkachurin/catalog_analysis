import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(rating):
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)
print(average_rating(movies))

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return(oldest, newest, average_age)
    
print(catalog_age_stats(movies))
print(type(catalog_age_stats(movies)))

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


print (duration_in_hours(455))

def rating_tier(rating):
    if rating >= 9:
        return "Шедевр"
    elif rating >= 7:
        return "Хорошо"
    elif rating >= 5:
        return "Средне"
    else:
        return "Слабо"  if rating <5 else "Средне"

print(rating_tier(7))

def decade_label(year):
    match year:
        case y if y > 2020:
            return "Новые"
        case y if y >= 2015:
            return "Недавние"
        case _:
            return "Старые"

print(decade_label(2023))

for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

i = 0

while i < len(movies):
    if movies[i]["rating"] > 9:
        print (movies[i]["title"])
        break
    i += 1
else:
    print ("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
print (count_long_movies(movies))

def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        result.append (word[0].upper() + word[1:].lower())
    return " ".join(result)

def make_slug(title):
    words = title.split()
    result = []
    for word in words:
        result.append (word[0:].lower())
    return "-".join(result)

print (normalize_title("жЕНЯ Старший ЭЛЕКТРИК"))
print (make_slug("жЕНЯ Старший ЭЛЕКТРИК"))

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f' "{title}" ({year}) - {rating}/10, {duration}, жанры: {genres}'

print (format_report_line(movies[2]))

def titles_sorted_by_rating(movies):
    movie_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in movie_sorted]
print (titles_sorted_by_rating(movies))

def top_n_by_rating(movies, n=3):
    movie_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in movie_sorted[:n]]
result = top_n_by_rating(movies)

print(result)
print(type(result[0]))

def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts
print (count_by_genre(movies))

filmography = {}
def actor_filmography(movies):
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography
print (actor_filmography(movies))

avg = average_rating(movies)

above_average = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > avg
}
print(above_average)