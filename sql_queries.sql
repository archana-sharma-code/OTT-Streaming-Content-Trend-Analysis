-- OTT Streaming Content Analysis - SQL Queries
-- This file contains SQL queries for core aggregations as required by the project

-- ============================================
-- TABLE STRUCTURE ASSUMPTIONS
-- ============================================
-- Table: content_library
-- Columns: 
--   - id (INT)
--   - platform (VARCHAR) - 'Netflix' or 'Amazon Prime'
--   - type (VARCHAR) - 'Movie' or 'TV Show'
--   - title (VARCHAR)
--   - director (VARCHAR)
--   - cast (VARCHAR)
--   - country (VARCHAR)
--   - date_added (DATE)
--   - release_year (INT)
--   - rating (VARCHAR)
--   - duration (VARCHAR)
--   - listed_in (VARCHAR) - genres
--   - description (TEXT)

-- ============================================
-- QUERY 1: Content Count by Platform and Type
-- ============================================
SELECT 
    platform,
    type,
    COUNT(*) as total_titles,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY platform), 2) as percentage
FROM content_library
GROUP BY platform, type
ORDER BY platform, type DESC;

-- ============================================
-- QUERY 2: Top 10 Most Common Genres
-- ============================================
SELECT 
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(listed_in, ',', numbers.n), ',', -1)) as genre,
    COUNT(*) as count
FROM content_library
JOIN (
    SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL 
    SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6
) numbers ON CHAR_LENGTH(listed_in) - CHAR_LENGTH(REPLACE(listed_in, ',', '')) >= numbers.n - 1
WHERE listed_in IS NOT NULL
GROUP BY genre
ORDER BY count DESC
LIMIT 10;

-- ============================================
-- QUERY 3: Content Rating Distribution by Platform
-- ============================================
SELECT 
    platform,
    rating,
    COUNT(*) as title_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY platform), 2) as percentage
FROM content_library
WHERE rating IS NOT NULL
GROUP BY platform, rating
ORDER BY platform, title_count DESC;

-- ============================================
-- QUERY 4: Content Release Trends by Year and Platform
-- ============================================
SELECT 
    release_year,
    platform,
    COUNT(*) as titles_released
FROM content_library
WHERE release_year >= 2010
GROUP BY release_year, platform
ORDER BY release_year DESC, platform;

-- ============================================
-- QUERY 5: Top 10 Countries by Content Production
-- ============================================
SELECT 
    country,
    COUNT(*) as total_titles,
    COUNT(DISTINCT platform) as platforms_available
FROM content_library
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- ============================================
-- QUERY 6: Average Content Duration by Type
-- ============================================
-- For Movies (in minutes)
SELECT 
    platform,
    AVG(CAST(REPLACE(duration, ' min', '') AS UNSIGNED)) as avg_duration_minutes,
    MIN(CAST(REPLACE(duration, ' min', '') AS UNSIGNED)) as min_duration,
    MAX(CAST(REPLACE(duration, ' min', '') AS UNSIGNED)) as max_duration
FROM content_library
WHERE type = 'Movie' 
    AND duration LIKE '%min%'
GROUP BY platform;

-- For TV Shows (in seasons)
SELECT 
    platform,
    AVG(CAST(REPLACE(REPLACE(duration, ' Seasons', ''), ' Season', '') AS UNSIGNED)) as avg_seasons,
    MIN(CAST(REPLACE(REPLACE(duration, ' Seasons', ''), ' Season', '') AS UNSIGNED)) as min_seasons,
    MAX(CAST(REPLACE(REPLACE(duration, ' Seasons', ''), ' Season', '') AS UNSIGNED)) as max_seasons
FROM content_library
WHERE type = 'TV Show' 
    AND duration LIKE '%Season%'
GROUP BY platform;

-- ============================================
-- QUERY 7: Genre Analysis by Release Year (Recent Trends)
-- ============================================
SELECT 
    release_year,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(listed_in, ',', numbers.n), ',', -1)) as genre,
    COUNT(*) as title_count
FROM content_library
JOIN (
    SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL 
    SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6
) numbers ON CHAR_LENGTH(listed_in) - CHAR_LENGTH(REPLACE(listed_in, ',', '')) >= numbers.n - 1
WHERE release_year >= 2015 
    AND listed_in IS NOT NULL
GROUP BY release_year, genre
HAVING title_count > 2
ORDER BY release_year DESC, title_count DESC;

-- ============================================
-- QUERY 8: Platform-Specific Content Analysis
-- ============================================
-- Netflix Exclusive Analysis
SELECT 
    country,
    COUNT(*) as netflix_titles,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
FROM content_library
WHERE platform = 'Netflix' AND country IS NOT NULL
GROUP BY country
ORDER BY netflix_titles DESC
LIMIT 10;

-- Amazon Prime Exclusive Analysis
SELECT 
    country,
    COUNT(*) as prime_titles,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
FROM content_library
WHERE platform = 'Amazon Prime' AND country IS NOT NULL
GROUP BY country
ORDER BY prime_titles DESC
LIMIT 10;

-- ============================================
-- QUERY 9: Content Added Over Time
-- ============================================
SELECT 
    YEAR(date_added) as year_added,
    platform,
    COUNT(*) as titles_added
FROM content_library
WHERE date_added IS NOT NULL
GROUP BY YEAR(date_added), platform
ORDER BY year_added DESC, platform;

-- ============================================
-- QUERY 10: Rating Distribution by Country
-- ============================================
SELECT 
    country,
    rating,
    COUNT(*) as title_count
FROM content_library
WHERE country IS NOT NULL 
    AND rating IS NOT NULL
GROUP BY country, rating
HAVING title_count > 1
ORDER BY country, title_count DESC;
