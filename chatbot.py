# chatbot.py

# 1. Design the Chatbot’s Personality
bot_name = "CryptoBuddy"
bot_tone = "Hey there! Let’s find you a green and growing crypto!"

# 2. Predefined Crypto Data
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
    },
    "Solana": { # Added for more variety
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 5/10
    },
    "Ripple": { # Added for more variety
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    }
}

# 3. Chatbot Logic and 4. Add Advice Rules
def get_crypto_advice(user_query):
    user_query = user_query.lower()

    # Disclaimer
    disclaimer = "Disclaimer: Crypto is risky—always do your own research! This is not financial advice."

    # Profitability advice
    if "trending up" in user_query or "long-term growth" in user_query or "profitable" in user_query or "buy" in user_query:
        profitable_options = []
        for crypto, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                profitable_options.append(crypto)
        if profitable_options:
            return f"{bot_name}: For profitability and long-term growth, consider {' and '.join(profitable_options)}. They are trending up with high market caps! 🚀 {disclaimer}"
        else:
            return f"{bot_name}: Currently, I don't see any cryptocurrencies with both a rising trend and high market cap in my data. {disclaimer}"

    # Sustainability advice
    elif "sustainable" in user_query or "eco-friendly" in user_query or "green" in user_query:
        sustainable_recommendations = []
        best_score = -1
        for crypto, data in crypto_db.items():
            if data["energy_use"] == "low" and data["sustainability_score"] > 7/10:
                sustainable_recommendations.append(crypto)
            if data["sustainability_score"] > best_score:
                best_score = data["sustainability_score"]
                most_sustainable_coin = crypto

        if sustainable_recommendations:
            return f"{bot_name}: Invest in {' and '.join(sustainable_recommendations)}! 🌱 They are eco-friendly with long-term potential! (The highest scoring is {most_sustainable_coin} with a score of {crypto_db[most_sustainable_coin]['sustainability_score']*10}/10). {disclaimer}"
        else:
            return f"{bot_name}: Based on my current data, I'm recommending {most_sustainable_coin} as the most sustainable option with a score of {crypto_db[most_sustainable_coin]['sustainability_score']*10}/10. {disclaimer}"

    # General trends (e.g., "what's stable?")
    elif "stable" in user_query:
        stable_coins = [crypto for crypto, data in crypto_db.items() if data["price_trend"] == "stable"]
        if stable_coins:
            return f"{bot_name}: Cryptocurrencies with a stable price trend include: {', '.join(stable_coins)}. {disclaimer}"
        else:
            return f"{bot_name}: I don't have information on stable coins at the moment. {disclaimer}"

    # Specific crypto information (basic lookup)
    elif any(crypto.lower() in user_query for crypto in crypto_db):
        for crypto_name, data in crypto_db.items():
            if crypto_name.lower() in user_query:
                return (f"{bot_name}: Here's what I know about {crypto_name}:\n"
                        f"  Price Trend: {data['price_trend']}\n"
                        f"  Market Cap: {data['market_cap']}\n"
                        f"  Energy Use: {data['energy_use']}\n"
                        f"  Sustainability Score: {data['sustainability_score']*10}/10\n{disclaimer}")

    # General greetings/farewells
    elif "hello" in user_query or "hi" in user_query:
        return f"{bot_name}: {bot_tone} How can I help you with your crypto investment today?"
    elif "bye" in user_query or "goodbye" in user_query:
        return f"{bot_name}: Goodbye! Happy investing (and researching!)."

    # Default response
    else:
        return f"{bot_name}: I'm sorry, I can only provide advice based on profitability (price trends, market cap) and sustainability (energy use, sustainability score). Try asking about 'trending up', 'sustainable coins', or specific crypto names. {disclaimer}"

# 5. Test Your Bot (Interactive Session)
if __name__ == "__main__":
    print(f"{bot_name}: {bot_tone} Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = get_crypto_advice(user_input)
        print(response)
