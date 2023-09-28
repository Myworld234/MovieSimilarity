# Import spacy
import spacy

# Load sm
nlp = spacy.load('en_core_web_sm')

# Hulk movie description
description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Tokenization using sm
model_description = nlp(description_to_compare)

# Variables
highest_score = 0
suggested_movie = ""

with open("movies.txt", "r") as file_read:
    # Read movies in a list
    movies = file_read.readlines()
    # Iterate over movies and compare
    for movie in movies:
        movie_description = movie.split(":")
        comparing_similarity = nlp(movie_description[1]).similarity(model_description)
        print(movie_description[0] + " - ", comparing_similarity)
        # Overwrite highest_score with new comparing_similarity value - IF highest_score is less than comparing_similarity
        if highest_score < comparing_similarity:
            highest_score = comparing_similarity
            # Set the suggested movie
            suggested_movie = movie_description[0]

# Print suggest movie           
print(f"Suggested Movie - {suggested_movie}")