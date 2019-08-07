blogs = dict()

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items(): # (blog_name, Blog), (blog_name_Blog)
        print(' - {}'.format(blog))
