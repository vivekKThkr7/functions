def mad_libs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    
    story = f"The {adjective} {noun} likes to {verb} in the forest."
    return story

print(mad_libs())

