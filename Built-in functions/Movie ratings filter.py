ratings = [9.2, 5.8, 7.6, 8.9, 4.3, 6.5, 9.8]

good_ratings = list(filter(lambda x: x >= 7, ratings))

updated_ratings = list(map(lambda x: round(x + 0.1, 1), good_ratings))

print("Final Ratings:", updated_ratings)
print("Recommended Movies:", len(updated_ratings))
