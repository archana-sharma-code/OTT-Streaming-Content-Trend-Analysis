"""
OTT Streaming Content Trend Analysis
Netflix vs Amazon Prime Content Analysis

This script performs exploratory data analysis on Netflix and Amazon Prime 
content libraries to identify trends in genre popularity, content ratings, 
release patterns, and regional content distribution.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Suppress warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("="*60)
print("OTT STREAMING CONTENT TREND ANALYSIS")
print("="*60)

# ============================================
# Load Datasets
# ============================================
print("\n[1/10] Loading datasets...")

# Load Netflix data
netflix_df = pd.read_csv('netflix_titles.csv')
netflix_df['platform'] = 'Netflix'

# Load Amazon Prime data
prime_df = pd.read_csv('amazon_prime_titles.csv')
prime_df['platform'] = 'Amazon Prime'

# Combine datasets
combined_df = pd.concat([netflix_df, prime_df], ignore_index=True)

print(f"   Netflix Titles: {len(netflix_df):,}")
print(f"   Amazon Prime Titles: {len(prime_df):,}")
print(f"   Total Titles: {len(combined_df):,}")

# ============================================
# Data Overview
# ============================================
print("\n[2/10] Data overview...")
print("\nFirst 5 rows:")
print(combined_df.head())

print("\n" + "="*60)
print("DATA TYPES AND MISSING VALUES")
print("="*60)
print(combined_df.info())

# ============================================
# Data Cleaning
# ============================================
print("\n[3/10] Data cleaning...")

# Check for missing values
print("\nMissing values:")
print(combined_df.isnull().sum())

# Clean duration column - extract numeric values
def clean_duration(duration):
    if pd.isna(duration):
        return None
    duration = str(duration)
    if 'min' in duration:
        return int(duration.split(' ')[0])
    elif 'Season' in duration:
        return int(duration.split(' ')[0])
    return None

combined_df['duration_numeric'] = combined_df['duration'].apply(clean_duration)

# Clean date_added
combined_df['date_added'] = pd.to_datetime(combined_df['date_added'], errors='coerce')
combined_df['year_added'] = combined_df['date_added'].dt.year

print("Data cleaning completed.")

# ============================================
# Visualization 1: Content Type Distribution
# ============================================
print("\n[4/10] Creating content type distribution...")

type_counts = combined_df.groupby(['platform', 'type']).size().unstack()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Netflix
type_counts.loc['Netflix'].plot(kind='pie', ax=axes[0], autopct='%1.1f%%', 
                                   colors=['#ff6b6b', '#4ecdc4'], explode=(0.05, 0))
axes[0].set_title('Netflix: Movies vs TV Shows', fontsize=14, fontweight='bold')
axes[0].set_ylabel('')

# Amazon Prime
type_counts.loc['Amazon Prime'].plot(kind='pie', ax=axes[1], autopct='%1.1f%%',
                                        colors=['#45b7d1', '#96ceb4'], explode=(0.05, 0))
axes[1].set_title('Amazon Prime: Movies vs TV Shows', fontsize=14, fontweight='bold')
axes[1].set_ylabel('')

plt.tight_layout()
plt.savefig('content_type_distribution.png', dpi=300, bbox_inches='tight')
print("   Saved: content_type_distribution.png")

print("\nContent Type Distribution:")
print(type_counts)

# ============================================
# Visualization 2: Top 10 Content Genres
# ============================================
print("\n[5/10] Creating genre analysis...")

# Extract genres from listed_in column
all_genres = []
for genres in combined_df['listed_in']:
    if pd.notna(genres):
        all_genres.extend([g.strip() for g in genres.split(',')])

genre_counts = pd.Series(all_genres).value_counts().head(10)

# Create visualization
plt.figure(figsize=(12, 6))
genre_counts.plot(kind='barh', color='#e74c3c')
plt.title('Top 10 Content Genres Across Platforms', fontsize=16, fontweight='bold')
plt.xlabel('Count', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_genres.png', dpi=300, bbox_inches='tight')
print("   Saved: top_genres.png")

print("\nTop 10 Genres:")
print(genre_counts)

# ============================================
# Visualization 3: Content Rating Distribution
# ============================================
print("\n[6/10] Creating rating distribution...")

# Rating distribution by platform
rating_counts = combined_df.groupby(['platform', 'rating']).size().unstack().fillna(0)

# Select top ratings
top_ratings = combined_df['rating'].value_counts().head(8).index
rating_counts = rating_counts[top_ratings]

fig, ax = plt.subplots(figsize=(14, 6))
rating_counts.T.plot(kind='bar', ax=ax, color=['#e74c3c', '#3498db'])
plt.title('Content Rating Distribution by Platform', fontsize=16, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Platform', loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('rating_distribution.png', dpi=300, bbox_inches='tight')
print("   Saved: rating_distribution.png")

print("\nRating Distribution:")
print(rating_counts.T)

# ============================================
# Visualization 4: Release Year Trends
# ============================================
print("\n[7/10] Creating release year trends...")

# Release year distribution
release_year_counts = combined_df.groupby(['platform', 'release_year']).size().unstack().fillna(0)

# Filter for recent years (2010 to max year in data)
max_year = combined_df['release_year'].max()
recent_years = range(2010, max_year + 1)
available_years = [year for year in recent_years if year in release_year_counts.columns]
release_year_counts = release_year_counts[available_years]

fig, ax = plt.subplots(figsize=(14, 6))
release_year_counts.T.plot(kind='line', ax=ax, marker='o', linewidth=2, markersize=8)
plt.title(f'Content Release Trends ({min(available_years)}-{max(available_years)})', fontsize=16, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.legend(title='Platform', loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('release_year_trends.png', dpi=300, bbox_inches='tight')
print("   Saved: release_year_trends.png")

print("\nRelease Year Distribution:")
print(release_year_counts.T)

# ============================================
# Visualization 5: Regional Content Distribution
# ============================================
print("\n[8/10] Creating country distribution...")

# Country distribution
country_counts = combined_df['country'].value_counts().head(10)

plt.figure(figsize=(12, 6))
country_counts.plot(kind='bar', color='#9b59b6')
plt.title('Top 10 Countries by Content Production', fontsize=16, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('country_distribution.png', dpi=300, bbox_inches='tight')
print("   Saved: country_distribution.png")

print("\nTop 10 Countries:")
print(country_counts)

# ============================================
# Visualization 6: Content Duration Analysis
# ============================================
print("\n[9/10] Creating duration analysis...")

# Duration analysis by content type
movie_durations = combined_df[combined_df['type'] == 'Movie']['duration_numeric'].dropna()
tv_durations = combined_df[combined_df['type'] == 'TV Show']['duration_numeric'].dropna()

if len(movie_durations) > 0 or len(tv_durations) > 0:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Movie durations
    if len(movie_durations) > 0:
        axes[0].hist(movie_durations, bins=30, color='#e74c3c', alpha=0.7, edgecolor='black')
        axes[0].set_title('Movie Duration Distribution', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Duration (minutes)', fontsize=12)
        axes[0].set_ylabel('Frequency', fontsize=12)
        axes[0].axvline(movie_durations.mean(), color='black', linestyle='--', linewidth=2, 
                       label=f'Mean: {movie_durations.mean():.0f} min')
        axes[0].legend()
    else:
        axes[0].text(0.5, 0.5, 'No movie duration data', ha='center', va='center', 
                    transform=axes[0].transAxes)
        axes[0].set_title('Movie Duration Distribution', fontsize=14, fontweight='bold')
    
    # TV Show seasons
    if len(tv_durations) > 0:
        axes[1].hist(tv_durations, bins=20, color='#3498db', alpha=0.7, edgecolor='black')
        axes[1].set_title('TV Show Season Count Distribution', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Number of Seasons', fontsize=12)
        axes[1].set_ylabel('Frequency', fontsize=12)
        axes[1].axvline(tv_durations.mean(), color='black', linestyle='--', linewidth=2, 
                       label=f'Mean: {tv_durations.mean():.1f} seasons')
        axes[1].legend()
    else:
        axes[1].text(0.5, 0.5, 'No TV show season data', ha='center', va='center', 
                    transform=axes[1].transAxes)
        axes[1].set_title('TV Show Season Count Distribution', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('duration_analysis.png', dpi=300, bbox_inches='tight')
    print("   Saved: duration_analysis.png")
    
    if len(movie_durations) > 0:
        print(f"\nMovie Duration Statistics:")
        print(f"   Mean: {movie_durations.mean():.2f} minutes")
        print(f"   Median: {movie_durations.median():.2f} minutes")
        print(f"   Min: {movie_durations.min()} minutes")
        print(f"   Max: {movie_durations.max()} minutes")
    
    if len(tv_durations) > 0:
        print(f"\nTV Show Season Statistics:")
        print(f"   Mean: {tv_durations.mean():.2f} seasons")
        print(f"   Median: {tv_durations.median():.2f} seasons")
        print(f"   Min: {tv_durations.min()} seasons")
        print(f"   Max: {tv_durations.max()} seasons")
else:
    print("   No duration data available for analysis")

# ============================================
# Additional Analysis: Genre Mix by Release Year
# ============================================
print("\n[10/10] Creating genre heatmap...")

# Genre trends over time
genre_year_data = []
for idx, row in combined_df.iterrows():
    if pd.notna(row['listed_in']) and pd.notna(row['release_year']):
        genres = [g.strip() for g in row['listed_in'].split(',')]
        for genre in genres:
            genre_year_data.append({
                'genre': genre,
                'year': row['release_year'],
                'platform': row['platform']
            })

genre_year_df = pd.DataFrame(genre_year_data)

# Filter for recent years and top genres
top_5_genres = genre_year_df['genre'].value_counts().head(5).index
max_year_genre = genre_year_df['year'].max()
genre_year_filtered = genre_year_df[
    (genre_year_df['genre'].isin(top_5_genres)) & 
    (genre_year_df['year'] >= 2015) &
    (genre_year_df['year'] <= max_year_genre)
]

# Create heatmap
genre_pivot = genre_year_filtered.pivot_table(
    index='genre', 
    columns='year', 
    values='platform', 
    aggfunc='count'
).fillna(0)

plt.figure(figsize=(12, 6))
sns.heatmap(genre_pivot, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=0.5)
min_year_genre = genre_pivot.columns.min()
max_year_genre = genre_pivot.columns.max()
plt.title(f'Genre Trends Over Time ({min_year_genre}-{max_year_genre})', fontsize=16, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.tight_layout()
plt.savefig('genre_heatmap.png', dpi=300, bbox_inches='tight')
print("   Saved: genre_heatmap.png")

print("\nGenre-Year Heatmap Data:")
print(genre_pivot)

# ============================================
# Summary Statistics
# ============================================
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)

print(f"\n1. Total Content Titles: {len(combined_df):,}")
print(f"   - Netflix: {len(netflix_df):,} titles")
print(f"   - Amazon Prime: {len(prime_df):,} titles")

print(f"\n2. Content Type Distribution:")
for platform in ['Netflix', 'Amazon Prime']:
    platform_data = combined_df[combined_df['platform'] == platform]
    movies = len(platform_data[platform_data['type'] == 'Movie'])
    tv_shows = len(platform_data[platform_data['type'] == 'TV Show'])
    print(f"   {platform}:")
    print(f"     - Movies: {movies} ({movies/len(platform_data)*100:.1f}%)")
    print(f"     - TV Shows: {tv_shows} ({tv_shows/len(platform_data)*100:.1f}%)")

print(f"\n3. Top 5 Genres:")
for i, (genre, count) in enumerate(genre_counts.head(5).items(), 1):
    print(f"   {i}. {genre}: {count} titles")

print(f"\n4. Top 5 Countries:")
for i, (country, count) in enumerate(country_counts.head(5).items(), 1):
    print(f"   {i}. {country}: {count} titles")

print(f"\n5. Release Year Range: {combined_df['release_year'].min()} - {combined_df['release_year'].max()}")
print(f"   Most common year: {combined_df['release_year'].mode()[0]}")

print(f"\n6. Content Duration:")
if len(movie_durations) > 0:
    print(f"   - Average movie duration: {movie_durations.mean():.1f} minutes")
else:
    print(f"   - Movie duration data not available")
if len(tv_durations) > 0:
    print(f"   - Average TV show seasons: {tv_durations.mean():.1f} seasons")
else:
    print(f"   - TV show season data not available")

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print("\nGenerated Visualizations:")
print("  1. content_type_distribution.png")
print("  2. top_genres.png")
print("  3. rating_distribution.png")
print("  4. release_year_trends.png")
print("  5. country_distribution.png")
print("  6. duration_analysis.png")
print("  7. genre_heatmap.png")
print("\nAll files saved in current directory.")
