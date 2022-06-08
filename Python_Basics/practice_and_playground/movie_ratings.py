num_of_movies = int(input())
max_rating = -100
min_rating = 100
max_rating_name = ''
min_rating_name = ''
sum_of_ratings = 0

for i in range(num_of_movies):
    movie_name = input()
    movie_rating = float(input())
    sum_of_ratings += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rating_name = movie_name

    elif movie_rating < min_rating:
        min_rating = movie_rating
        min_rating_name = movie_name

average_ratings = sum_of_ratings / num_of_movies
print(f"{max_rating_name} is with highest rating: {max_rating}")
print(f"{min_rating_name} is with lowest rating: {min_rating}")
print(f"Average rating: {average_ratings:.1f}")



