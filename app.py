# Mindful Feed - Smart Content Redirection System

# Categories and limits set by user
limits = {
    "entertainment": 60,   # minutes
    "learning": 999,
    "gaming": 30,
    "shopping": 40
}

# Productivity score values
scores = {
    "learning": 10,
    "productivity": 8,
    "entertainment": 2,
    "gaming": 1,
    "shopping": 3
}

# Sample content data (simulated)
usage_data = [
    {"app": "YouTube", "category": "learning", "time": 30},
    {"app": "Instagram", "category": "entertainment", "time": 50},
    {"app": "PUBG", "category": "gaming", "time": 40},
    {"app": "Amazon", "category": "shopping", "time": 20},
]

total_score = 0

print("----- Mindful Feed Report -----")

for item in usage_data:
    app = item["app"]
    category = item["category"]
    time = item["time"]

    print(f"\nApp: {app}")
    print(f"Category: {category}")
    print(f"Time Used: {time} minutes")

    # Calculate productivity score
    total_score += scores.get(category, 0)

    # Check limits
    if time > limits.get(category, 999):
        print("⚠ Limit exceeded!")

        if category == "entertainment":
            print("Suggestion: Watch educational videos instead.")
        elif category == "gaming":
            print("Suggestion: Try learning apps or coding practice.")
        elif category == "shopping":
            print("Suggestion: Focus on productive tasks.")

print("\nTotal Productivity Score:", total_score)

# Productivity evaluation
if total_score > 25:
    print("Excellent productive day!")
elif total_score > 15:
    print("Moderately productive day.")
else:
    print("Try to improve productivity tomorrow.")