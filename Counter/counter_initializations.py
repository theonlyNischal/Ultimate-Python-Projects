from collections import Counter

# Using sequence of items
print(Counter(["a", "b", "c", "b", "b"])) 
# Using a dictionary
print(Counter({
    "a": 10,
    "b": 30,
    "c": 20
}))
# Using keyword arguments that map string names to counts
print(Counter(a=10, b=30, c=20))

# Initializing the empty counter and using update to populate it.
c = Counter()
c.update("aaabbdef")
print(c)
c.update({
    "b":5
})
print(c)