def add_full_name(user: dict) -> None:
  # write your code here
  user["full_name"] = f"{user['first_name']} {user['last_name']}"

  print(user)

# {
#   "first_name": "Ivan",
#   "last_name": "Vasylchenko",
# }

user = {
  "first_name": "Roman",
  "last_name": "Vasylchenko",
}

add_full_name(user)
# some test changes
