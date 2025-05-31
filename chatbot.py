print("Hello, I'm CryptoBuddy. Let's find the right crypto for you.\n")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def get_advice(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Recommended: {recommend}. It has the highest sustainability score."

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"Trending cryptocurrencies: {', '.join(trending)}."

    elif "long-term" in user_query or "growth" in user_query:
        for coin in crypto_db:
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] >= 0.7:
                return f"{coin} is suitable for long-term growth."
        return "No strong long-term options at the moment."

    else:
        return "Try asking about trends, growth, or sustainability."

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("CryptoBuddy: Goodbye.")
        break
    response = get_advice(query)
    print("CryptoBuddy:", response)
