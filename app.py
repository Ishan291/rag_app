
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("Google API key loaded from environment:", GOOGLE_API_KEY is not None)
