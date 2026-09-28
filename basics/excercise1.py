# favorite_movies = ("movie1", "movie2", "movie3", "movie2")
# print(favorite_movies)
# list_movies = len(favorite_movies)
# print(list_movies)
# favorite_movies1 = ("movie5")
# movies = favorite_movies + (favorite_movies1,)
# print(movies)

# new_movies = input("Enter your favorite movie: ")
# if new_movies in favorite_movies:
#     print("Your favorite movie is already in the list.")
# else:
#     favorite_movies = favorite_movies + (new_movies,)
#     print("Updated list of favorite movies:", favorite_movies)
# print("User added movies:", favorite_movies)

# servers = ("server1", "server2", "server3", "server4", "server5")
# print(servers)
# new_server = input("Enter a new server name: ")
# if new_server in servers:
#     print("The server name is already in the list.")
# else:
#     servers = servers + (new_server,)
#     print("Updated list of servers:", servers)
# print("User added servers:", servers)      

# for server in servers:
#     print("Server:", server)

my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print(my_list)
#del my_list[3]
my_list.pop(4)
print(my_list)
my_list[2] = 100
print(my_list)
count = len(my_list)
print("Total elements in the list:", count)
    