# order matters in lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# prints first item
print(states_of_america[0])

# prints last item
print(states_of_america[-1])

# alters second item
states_of_america[1] = "Pencilvania"
print(states_of_america)

# adds item to the end of the list
states_of_america.append("Angelaland")
print(states_of_america)

# extends the list by adding items to the end
states_of_america.extend(["Angelaland", "Jack Bauer"])
print(states_of_america)
