def generate_brand_voice(adjectives, business_type):
    tone = ", ".join(adjectives).title()
    
    print(f"🎯 Brand Tone: {tone}")
    print()

    print("🧠 Brand Voice Description:")
    print(f"This is a {tone} {business_type} that wants to stand out and connect emotionally. It speaks like a human, not a corporation.")
    print()

    print("📢 Slogan:")
    print(f"{adjectives[0].title()} ideas for {business_type.lower()} people.")
    print()

    print("📱 Social Media Bio:")
    print(f"{business_type.title()} vibes. {tone} content. Built for the bold.")
    print()

    print("📸 First Instagram Caption:")
    print(f"'Not your average {business_type}. This is where {adjectives[1]} meets {adjectives[2]}.' #BrandLaunch #NewVibes")
    print()

    print("🎨 Logo Prompt for Midjourney/DALL·E:")
    print(f"Design a logo for a {business_type} that feels {tone}. Use modern, clean lines with a pop of personality.")
    print()

# Example usage
if __name__ == "__main__":
    sample_adjectives = ["bold", "warm", "curious"]
    sample_business = "indie skincare brand"
    
    generate_brand_voice(sample_adjectives, sample_business)
