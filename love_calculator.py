# Simple Love Percentage Calculator ❤️

def love_calculator(name1, name2):
    # Combine both names and convert to lowercase
    combined = (name1 + name2).lower()
    
    # Calculate a "love score" based on character count (fun & basic method)
    love_score = 0
    for char in combined:
        love_score += ord(char)  # Use ASCII value of each character
    
    # Get percentage between 0-100
    love_percentage = (love_score % 101)  # 0 to 100
    
    # Make it more fun with special cases
    if love_percentage < 30:
        message = "Maybe just friends? 💔"
    elif love_percentage < 60:
        message = "There's some spark! 🔥"
    elif love_percentage < 85:
        message = "Great match! 💕"
    else:
        message = "True Love! Soulmates forever! ❤️‍🔥"
    
    print(f"\n💖 Love Calculator Result 💖")
    print(f"{name1} ❤️ {name2}")
    print(f"Love Percentage: {love_percentage}%")
    print(message)
    print("-" * 40)


# === How to use ===
if __name__ == "__main__":
    print("❤️ Welcome to Love Percentage Calculator ❤️\n")
    
    name1 = input("Enter first person's name: ").strip()
    name2 = input("Enter second person's name: ").strip()
    
    if name1 and name2:
        love_calculator(name1, name2)
    else:
        print("Please enter both names!")
