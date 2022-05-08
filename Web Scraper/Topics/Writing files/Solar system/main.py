# create the planets.txt
file_name = "planets.txt"
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune"]
file_context = open(file_name, "w", encoding="utf-8")
file_context.write("\n".join(planets))

file_context.close()
