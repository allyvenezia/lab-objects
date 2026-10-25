"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    # users
    a = User('sir_sam_fluffytail')
    b = User('birdfeeder_bandit73')

    # three tweets
    t1 = Tweet(a.username, 'Buried 47 acorns in the backyard today. Remembered where I put 3 of them. #WinterMealPrepping')
    t2 = Tweet(b.username, 'Found a new bird feeder in the garden. #BirdWatching')
    t3 = Tweet(a.username, 'Just spotted a REALLY BIG DOG near the park. #StayAlert')
    t4 = Tweet(b.username, 'The Smiths just refilled their bird feeders, FYI')
    t5 = Tweet(a.username, 'better to find your own acorns than steal from others. #WinterMealPrepping')

    for i in range(10):
        t1.like()
    for i in range(84):
        t2.like()
    for i in range(337):
        t3.like()
    for i in range(1007):
        t4.like()
    for i in range(123):
        t5.like()

    for i in range(998):
        a.follow()
    for i in range(733):
        b.follow()

    for i in range(5):
        t5.unlike()
        a.unfollow()

    users = [a, b]
    posts = [t1, t2, t3, t4, t5]
    return users, posts




def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()

    for user in users:
        print(user)
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()
