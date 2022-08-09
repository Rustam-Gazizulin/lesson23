class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'user #{self.id}'

    def __repr__(self):
        return self.__str__()


class Blog:
    def __init__(self, id, subscriber_ids):
        self.id = id
        self.subscriber_ids = subscriber_ids


users = [User(1, 'Alex'), User(2, 'sergey')]
blogs = [Blog(1, [1, 2]), Blog(2, [2, 3, 4])]

res = {'<blog_id>': ['user']}


def attach_users(blogs, users):
    users_dict = {u.id: u for u in users}
    # for u in users:
    #     users_dict[u.id] = u

    blogs_dict = {}
    for b in blogs:
        blog_users = [users_dict[subscriber_id] for subscriber_id in b.subscriber_ids if subscriber_id in users_dict]
        # for subscriber_id in b.subscriber_ids:
        #     if subscriber_id in users_dict:
        #         blog_users.append(users_dict[subscriber_id])
        blogs_dict[b.id] = blog_users

    return blogs_dict


print(attach_users(blogs, users))
