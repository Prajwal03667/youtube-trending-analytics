-- Data Analyst Queries

-- 1. Most Viewed Videos
SELECT 
    video_id, title, channel_title, views
FROM youtube_trending_data
ORDER BY views DESC
LIMIT 10;

-- 2. Daily Trending Volume
SELECT 
    trending_date,
    COUNT(*) AS videos_trending
FROM youtube_trending_data
GROUP BY trending_date
ORDER BY trending_date;

-- 3. Category Popularity by Views
SELECT 
    category_id,
    SUM(views) AS total_views,
    COUNT(*) AS video_count
FROM youtube_trending_data
GROUP BY category_id
ORDER BY total_views DESC;

-- 4. Publish Day Performance
SELECT 
    published_day_of_week,
    ROUND(AVG(views), 2) AS avg_views,
    ROUND(AVG(likes), 2) AS avg_likes
FROM youtube_trending_data
GROUP BY published_day_of_week
ORDER BY avg_views DESC;

-- Business Analyst Queries

-- 5. Country-wise Engagement
SELECT 
    publish_country,
    ROUND(AVG(likes), 2) AS avg_likes,
    ROUND(AVG(comment_count), 2) AS avg_comments
FROM youtube_trending_data
GROUP BY publish_country
ORDER BY avg_likes DESC;

-- 6. Videos with Disabled Comments or Ratings
SELECT 
    video_id, title, channel_title,
    comments_disabled, ratings_disabled
FROM youtube_trending_data
WHERE comments_disabled = TRUE OR ratings_disabled = TRUE;

-- 7. Top Tags by Popularity
SELECT 
    tags,
    SUM(views) AS total_views
FROM youtube_trending_data
GROUP BY tags
ORDER BY total_views DESC
LIMIT 10;

-- 8. Content Effectiveness Score (Custom Metric)
SELECT 
    video_id,
    title,
    ROUND((likes + comment_count) / views * 100, 2) AS engagement_score
FROM youtube_trending_data
WHERE views > 0
ORDER BY engagement_score DESC
LIMIT 10;
