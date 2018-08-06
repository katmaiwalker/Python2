import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien plane",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.show_trailer()

blood_diamond = media.Movie("Blood Diamond",
                            "Diamonds mined in war zones and sold to finance conflicts",
                            "https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg",
                            "https://www.youtube.com/watch?v=yknIZsvQjG4")

#blood_diamond.show_trailer()

movies = [toy_story,avatar,blood_diamond]
fresh_tomatoes.open_movies_page(movies)
