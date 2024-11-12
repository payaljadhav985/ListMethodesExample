"append()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.append("ferrari")
print(cars)

"insert()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.insert(3,"porsche")
print(cars)

"clear()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.clear()
print(cars)

"sort()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.sort()
print(cars)

"remove()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.remove("audi")
print(cars)

"index()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
print(cars.index("mustang"))

"extend()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1 = ["tesla","nissan"]
cars.extend(cars1)
print(cars)

"pop()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
print(cars.pop(-1))

"count()"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
print(cars.count("bmw"))

"append multiple cars"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
c = ["jaguar","fiat"]
cars.extend(c)
print(cars)

"insert multiple cars"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.insert(2,"volva")
cars.insert(3,"honda")
print(cars)

"clear if empty"
cars = []
if not cars:
    print("list is empty")

"sort in dessending order"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.sort(reverse=True)
print(cars)

"remove all occurance of bmw"
cars = ["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.remove("bmw")
print(cars)

