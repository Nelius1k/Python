
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kev", "Karen", "Jim", "Oscar", "John", "John"]

friends.append("Bob")
friends.insert(1, "Carl")
friends.remove("Oscar")
print(friends)

friends.pop(0) #removes item from a list (can be used with an index)
print(friends)

friends.extend(lucky_numbers) #append a list to another
print(friends)

print(friends.index("Jim")) #prints index where Jim is located

print(friends.count("John"))

lucky_numbers.sort() #sorts a list
print(lucky_numbers) 

lucky_numbers.reverse() #reverses the order of a list
print(lucky_numbers) 