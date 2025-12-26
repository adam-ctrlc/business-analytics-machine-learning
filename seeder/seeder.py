# Seed data for social media posts

import pandas as pd
import numpy as np

titles = [
    "How to cook", "Travel tips for", "AI is changing", "My daily routine in", 
    "Best tech for", "Top 10 secrets of", "Why I moved to", "The future of", 
    "Life hacks for", "A beginner's guide to", "Budget friendly", "Mastering"
]

locations = [
    "Paris", "New York", "London", "Tokyo", "Berlin", "Dubai", "Singapore", 
    "Bali", "San Francisco", "Sydney", "Rome", "Toronto", "Seoul", "Mexico City"
]

topics = [
    "coding", "fitness", "cooking", "finance", "gaming", "sustainability", 
    "mental health", "minimalism", "photography", "crypto", "career growth", 
    "interior design", "skincare", "productivity"
]
data = []


rows = 100

for i in range(1, rows + 1):
    title = f"{np.random.choice(titles)} {np.random.choice(locations)}"
    desc = f"A deep dive into {np.random.choice(topics)} while visiting {np.random.choice(locations)}."
    hour = np.random.randint(0, 24)
    has_img = np.random.choice([0, 1])
    likes = (has_img * 100) + (hour * 5) + np.random.randint(10, 50)
    data.append([i, title, desc, hour, has_img, likes])

df = pd.DataFrame(data, columns=['post_id', 'title', 'description', 'hour_posted', 'has_image', 'likes'])

df.to_excel('./excel/data.xlsx', index=False)
print(f"File 'social_media_data.xlsx' has been created with {rows} rows!")