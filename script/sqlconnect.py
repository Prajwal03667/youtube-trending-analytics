import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_",
    database="projects"
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv("youtube_trending.csv")

# Convert date columns to datetime format
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS youtube_trending_data (
        video_id VARCHAR(50) PRIMARY KEY,
        trending_date DATE,
        title TEXT,
        channel_title VARCHAR(255),
        category_id INT,
        publish_date DATETIME,
        time_frame VARCHAR(50),
        published_day_of_week VARCHAR(20),
        publish_country VARCHAR(50),
        tags TEXT,
        views BIGINT,
        likes BIGINT,
        dislikes BIGINT,
        comment_count BIGINT,
        comments_disabled BOOLEAN,
        ratings_disabled BOOLEAN,
        video_error_or_removed BOOLEAN
    )
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO youtube_trending_data (
            video_id, trending_date, title, channel_title, category_id,
            publish_date, time_frame, published_day_of_week, publish_country,
            tags, views, likes, dislikes, comment_count,
            comments_disabled, ratings_disabled, video_error_or_removed
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['video_id'],
        row['trending_date'].date() if pd.notnull(row['trending_date']) else None,
        row['title'],
        row['channel_title'],
        int(row['category_id']),
        row['publish_date'].to_pydatetime() if pd.notnull(row['publish_date']) else None,
        row['time_frame'],
        row['published_day_of_week'],
        row['publish_country'],
        row['tags'],
        int(row['views']),
        int(row['likes']),
        int(row['dislikes']),
        int(row['comment_count']),
        bool(row['comments_disabled']),
        bool(row['ratings_disabled']),
        bool(row['video_error_or_removed'])
    ))

conn.commit()
print("YouTube trending data imported successfully!")
