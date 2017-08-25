import media
import fresh_tomatoes

# To create just by ("moviename","description","image_url","trailer_url")
arjun_reddy = media.Movie("arjunreddy",
                          "This is a story about a medico and his"
                          "lovestory with a great attitude",
                          "http://c.jollyhoo.com"
                          "/19/Arjun-Reddy-Telugu-Movie"
                          ".jpg",
                          "https://www.youtube.com/watch?v=aozErj9NqeE")


# arjun_reddy.show_trailer()

paisa_vasool = media.Movie("paisa vasool",
                           "This is a story about a gangstar"
                           "with a suspense about his doing things",
                           "https://encrypted-tbn0.gstatic.com/images?q=t"
                           "bn:ANd9GcTMSQz7U0qCDJkb_IYEFBBOsoUJoIVd7ZMTt8alO"
                           "yaX6dWt32TaokpXhfJW",
                           "https://www.youtube.com/watch?v=nGsP1hlFIhM")


raja_great = media.Movie("raja the great",
                         "This is a story of a blind person"
                         "tackling with his dreams",
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:"
                         "ANd9GcQ5fDO5Cp1rxxahZxWQmty4sXRhDAbH1x66"
                         "PY-J2MDwXH3l8IPEUA",
                         "https://www.youtube.com/watch?v=FfxjvqJnfqA")

badri_dulhania = media.Movie("Badri ki dulhania",
                             "This is a story of a rich kid and a girl",
                             "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                             ":ANd9GcRXZZiZRCXd2RFZBuatimvjd6QceP2Z08_dDS_W"
                             "6j0BgF4Q7hPuQq-9iTQ5",
                             "https://www.youtube.com/watch?v=ztX-iGlZ_Ug")

mahanu_bavudu = media.Movie("Mahanubavudu",
                            "This is a story of a guy with over neatness",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                            ":ANd9GcSC0HBIc2MSMejeEiuEDI_hxO1TaXVFA42WNKRgtX7K"
                            "M91TDWch-sN_tq6Q",
                            "https://www.youtube.com/watch?v=pEjKXISdiWo")

majnu = media.Movie("Majnu",
                    "This is a story of a guy who loves two girls",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:"
                    "ANd9GcTxMQ63rpuCdGFN4z59aX2ri4uObPVG-GQO8fyqv0uc"
                    "T9Eu80JpzBy9DUzF",
                    "https://www.youtube.com/results?search_query=majnu+"
                    "trailer"
                    )

# This is the list all the instances 
movies = [arjun_reddy, paisa_vasool, raja_great, majnu, mahanu_bavudu,
          badri_dulhania]

# This passes the list of arguments of movies
fresh_tomatoes.open_movies_page(movies)
