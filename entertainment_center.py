import media  # module needed to create movie objects
import fresh_tomatoes  # module needed to generate HTML file

# creating movie objects, with movie title, synopsis, poster image, and trailer
hangover = media.Movie(
    "The Hangover",
    "Two days before his wedding, Doug and three friends drive to Las Vegas \
    for a wild and memorable stag party. In fact, when the three groomsmen \
    wake up the next morning, they can't remember a thing; nor can they find \
    Doug. With little time to spare, the three hazy pals try to re-trace \
    their steps and find Doug so they can get him back to Los Angeles in time \
    to walk down the aisle.",
    "http://www.gstatic.com/tv/thumb/movieposters/192248/p192248_p_v8_an.jpg",
    "https://www.youtube.com/watch?v=vhFVZsk3XEs")

get_out = media.Movie(
    "Get Out",
    "Now that Chris and his girlfriend, Rose, have reached the \
    meet-the-parents milestone of dating, she invites him for \
    a weekend getaway upstate with Missy and Dean. At first, Chris reads the \
    family's overly accommodating behavior as nervous \
    attempts to deal with their daughter's interracial relationship, but as \
    the weekend progresses, a series of increasingly disturbing discoveries \
    lead him to a truth that he never could have imagined.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=sRfnevzM9kQ")

the_prestige = media.Movie(
    "The Prestige",
    "An illusion gone horribly wrong pits two 19th-century magicians, \
    Alfred Borden and Rupert Angier, against each other in a bitter battle \
    for supremacy. Terrible consequences loom when the pair escalate their \
    feud, each seeking not just to outwit -- but to destroy -- the other man.",
    "https://images-na.ssl-images-amazon.com/images/I/41I9XGrG88L.jpg",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI")

the_illusionist = media.Movie(
    "The Illusionist",
    "A master magician named Eisenheim vies with Crown Prince Leopold of \
    Vienna for the hand of noblewoman Sophie, the girl he once loved. He \
    brings his considerable powers to bear on the prince, as she is about to \
    be named royal fiancee. However, a police inspector named \
    Uhl (Paul Giamatti) tries to warn Eisenheim that he is playing a \
    very dangerous game.",
    "http://www.gstatic.com/tv/thumb/movieposters/161007/p161007_p_v8_at.jpg",
    "https://www.youtube.com/watch?v=zuFGKcOSUfM")

o_brother = media.Movie(
    "O Brother Where Art Thou?",
    "Ulysses Everett McGill is having difficulty adjusting to his hard-labor \
    sentence in Mississippi. He scams his way off the chain gang with simple \
    Delmar and maladjusted Pete, then the trio sets out to pursue freedom and \
    the promise of a fortune in buried treasure. With nothing to lose and \
    still in shackles, their hasty run takes them on an incredible \
    journey of awesome experiences and colorful characters.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQgU9Ju96z4deYcNGfyNzM0mOD5qtNHhu5sQ4Pmfnfs1xzklPs0",  # noqa
    "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

shawshank = media.Movie(
    "The Shawshank Redemption",
    "Andy Dufresne is sentenced to two consecutive life terms in prison for \
    the murders of his wife and her lover and is sentenced to a tough prison. \
    However, only Andy knows he didn't commit the crimes. While there, he \
    forms a friendship with Red, experiences brutality of prison life, \
    adapts, helps the warden, etc., all in 19 years.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",  # noqa
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

# create movie array
movies = [hangover, get_out, the_prestige, the_illusionist, o_brother,
          shawshank]

# create HTML file with movies
fresh_tomatoes.open_movies_page(movies)
