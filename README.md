# OTT Streaming Content Trend Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive exploratory data analysis (EDA) of Netflix and Amazon Prime content libraries to identify trends in genre popularity, content ratings, release patterns, and regional content distribution.

##   Project Report

For a complete overview of the project, including methodology, findings, and recommendations, see **[PROJECT_REPORT.md](PROJECT_REPORT.md)**.

##  📋 Project Overview

This project analyzes streaming content from two major OTT platforms (Netflix and Amazon Prime) to derive actionable insights for content acquisition strategies. The analysis covers:

- **Genre Popularity**: Most common content categories across platforms
- **Content Ratings**: Distribution of maturity ratings (TV-MA, PG-13, etc.)
- **Release Trends**: Content production patterns over time
- **Regional Mix**: Geographic distribution of content production
- **Duration Analysis**: Movie lengths and TV show season counts

## 🎯 Objectives

1. Analyze content libraries of Netflix and Amazon Prime
2. Identify trending genres and content types
3. Understand regional content distribution patterns
4. Provide data-driven recommendations for content acquisition

## 🛠️ Tools & Technologies

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Seaborn**: Statistical data visualization
- **Matplotlib**: Plotting and graphing
- **SQL**: Database queries for aggregations
- **Spyder/Jupyter Notebook**: Analysis environment

## 📁 Project Structure

```
ott-streaming-analysis/
│
├── ott_analysis.py                 # Main Python script (for Spyder/IDE)
├── sql_queries.sql                  # SQL queries for core aggregations
├── CONTENT_STRATEGY_MEMO.md        # Strategic recommendations
├── PROJECT_REPORT.md               # Comprehensive project report
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── netflix_titles.csv              # Netflix content dataset (8,807 titles)
├── amazon_prime_titles.csv        # Amazon Prime content dataset (~10,000 titles)
│
└── [Generated PNG files]           # Visualizations created after running
    ├── content_type_distribution.png
    ├── top_genres.png
    ├── rating_distribution.png
    ├── release_year_trends.png
    ├── country_distribution.png
    ├── duration_analysis.png
    └── genre_heatmap.png
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ott-streaming-analysis.git
cd ott-streaming-analysis
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import pandas; import seaborn; import plotly; print('All packages installed successfully!')"
```

## 📊 Running the Analysis

### Prerequisites

1. **Install Python 3.8+** from https://www.python.org/downloads/
2. **Install required packages**:
```bash
pip install -r requirements.txt

Run the python code
```

## 📈 Visualizations

The analysis generates 8 key visualizations:

1. **Content Type Distribution**: Movies vs TV Shows comparison
2. **Top 10 Content Genres**: Most popular genre categories
3. **Content Rating Distribution**: Rating breakdown by platform
4. **Release Year Trends**: Content production over time (2010-2023)
5. **Regional Content Distribution**: Top 10 countries by content
6. **Content Duration Analysis**: Movie length and TV show seasons
7. **Genre Heatmap**: Genre trends over time
8. **Country Rating Analysis**: Average content rating by country

## 🔍 Key Findings

### Content Distribution
- **Total Titles Analyzed**: ~18,800+ (8,807 Netflix, ~10,000 Amazon Prime)
- **Netflix**: ~70% Movies, ~30% TV Shows (actual numbers from analysis)
- **Amazon Prime**: ~80% Movies, ~20% TV Shows (actual numbers from analysis)

### Top Genres
1. International TV Shows
2. Dramas
3. Action & Adventure
4. TV Comedies
5. Sci-Fi & Fantasy

### Regional Analysis
- **United States**: Leading content producer (45% of total)
- **United Kingdom**: Strong presence in dramas and mysteries
- **India**: Growing market for crime and action content
- **South Korea**: Viral potential in thriller genre
- **Emerging Markets**: Turkey, Brazil showing growth

### Rating Distribution
- **TV-MA**: 35% of content (mature audiences)
- **TV-14**: 25% of content (teens)
- **PG-13**: 18% of content (family-friendly)
- **R**: 12% of content (restricted)

### Release Trends
- **Peak Production**: 2018-2021
- **Recent Surge**: International content acquisitions (2020-2023)
- **COVID Impact**: Visible shift in content strategy during pandemic

## 💡 Strategic Recommendations

Based on the analysis, three key recommendations for content acquisition:

### 1. Invest in International Non-English Content
- Allocate 40% of acquisition budget to international titles
- Focus on Korean, Turkish, and Indian content
- Target: Viral potential and emerging market growth

### 2. Focus on Limited Series (2-3 Seasons)
- Shift to 70% limited series format
- Higher completion rates and lower production costs
- Target: Binge-able, self-contained stories

### 3. Expand Family-Friendly Content
- Currently only 18% of catalog is family-friendly
- High weekend viewing demand
- Target: Multi-generational household subscriptions

*See [CONTENT_STRATEGY_MEMO.md](CONTENT_STRATEGY_MEMO.md) for detailed recommendations.*

## 🗄️ SQL Queries

The `sql_queries.sql` file contains 10 core SQL queries for:
- Content count by platform and type
- Top 10 most common genres
- Content rating distribution
- Release trends by year
- Country-wise content analysis
- Duration statistics
- Genre trends over time
- Platform-specific analysis
- Content addition timeline
- Rating distribution by country

These queries can be adapted for use with MySQL, PostgreSQL, or SQLite databases.

## 📝 Dataset Information

### Netflix Dataset
- **Source**: Kaggle (Netflix Movies and TV Shows by Shivamb)
- **URL**: https://www.kaggle.com/datasets/shivamb/netflix-shows
- **Records**: 8,807 titles
- **Columns**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

### Amazon Prime Dataset
- **Source**: Kaggle (Amazon Prime Movies and TV Shows by Shivamb)
- **URL**: https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows
- **Records**: ~10,000 titles
- **Columns**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

### Data Cleaning Performed
- Duration column cleaned to extract numeric values
- Date_added converted to datetime format
- Missing values handled appropriately
- Genre extraction from comma-separated lists

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
---


