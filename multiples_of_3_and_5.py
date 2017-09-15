print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))

# The print command will display the value of what is inside of it.
# The sum command will add up all the integers "i" inside of it and give a value
# Since I only wanted the sum of numbers from 1 to 1000 that are divisble by 3 or 5, I did two more steps.
# I specified that I only wanted i in the range starting at 1 and below 1000
# That would give every number less than 1000 so I put an if command in
# if will only return values if true
# % in the sense that I used it means i (number less than 1000) divided by 3 or 5 has a remainder that equals (==) 0. This gave me only numbers divisble by 3 or 5 less than 1000 and summed them up, printing the result. 
