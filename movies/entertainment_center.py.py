import media
import fresh_tomatoes
# create different instances for different movies

bahubali =\
    media.Movie("Bahubali",
                "A story about king of mahehmati",
                "https://bit.ly/2u4rvOD",
                "https://www.youtube.com/watch?v=G62HrubdD6o")
yeh_jawaani_hai_deewani =\
    media.Movie("Yeh Jawaani Hai Deewani",
                "This movies is about a man and his friends",
                "https://bit.ly/2m2mdyX",
                "https://www.youtube.com/watch?v=Rbp2XUSeUNE")
sky_high =\
    media.Movie("Sky High",
                "American superhero comedy film about an \
                airborne school for teenage superheroes",
                "https://bit.ly/2NyY5Am",
                "https://www.youtube.com/watch?v=G7aMWVN1ThM")
hunger_games =\
    media.Movie("Hunger games",
                "The Hunger Games film series consists of \
                four science fiction dystopian adventure \
                films based on The Hunger Games trilogy of\
                novels, by the American author Suzanne Collins.",
                "https://bit.ly/2N1tbPY",
                "https://www.youtube.com/watch?v=4S9a5V9ODuY")
avengers_infinity_war =\
    media.Movie("Avengers: Infinity War",
                "Iron Man, Thor, the Hulk and the rest of the Avengers\
                unite to battle their most powerful enemy yet \
                -- the evil Thanos",
                "https://bit.ly/2L4zlOL",
                "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
doctor_strange =\
    media.Movie("Doctor Strange",
                "Doctor Stephen Vincent Strange is a fictional superhero\
                appearing in American comic books published by Marvel Comics",
                "https://bit.ly/2L2qi0X",
                "https://www.youtube.com/watch?v=Lt-U_t2pUHI")

# create an object list to store all the movies
movies = [bahubali, yeh_jawaani_hai_deewani, sky_high, hunger_games,
          avengers_infinity_war, doctor_strange]
# using open_movies_page under frest tomatoes file
fresh_tomatoes.open_movies_page(movies)
