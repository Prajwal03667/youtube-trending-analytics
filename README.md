# 📊 YouTube Trending Video Analytics

Analyze YouTube trending videos across multiple regions to discover patterns in popularity, sentiment, and category performance.
This project delivers a complete pipeline: data cleaning, sentiment analysis, SQL insights, visual dashboards, and a final storytelling report.

---

## 🚀 Project Overview

This project focuses on:

* Cleaning and standardizing YouTube trending datasets
* Sentiment analysis on titles & tags
* Ranking categories based on views using SQL
* Time-series evaluation of trending duration
* Visual storytelling using Tableau & Python

---

## 📁 Repository Structure

```
youtube-trending-analytics/
│
├── data/
│   ├── raw/           # raw country datasets
│   └── processed/     # cleaned & standardized outputs
│
├── notebooks/         # exploratory analysis (Jupyter)
│
├── src/               # python scripts
│   ├── etl.py
│   ├── cleaning.py
│   ├── sentiment.py
│   ├── features.py
│   └── viz.py
│
├── sql/               # SQL queries for ranking & category analysis
│
├── tableau/           # dashboard files
│
├── reports/           # final storytelling PDF
│
├── requirements.txt
└── README.md
```

---

## 🧹 Data Cleaning & Standardization

Performed inside `cleaning.py`:

* Normalize dates (`publishedAt`, `trending_date`)
* Standardize column names across regions
* Clean titles & tags (lowercase, remove noise)
* Explode tags into lists
* Map `categoryId` → category name
* Remove duplicates using `video_id + region + trending_date`

---

## 😃 Sentiment Analysis (title + tags)

Tools used:

* VADER / TextBlob (baseline)
* Optional: Transformer model (`distilbert-base-uncased-finetuned-sst-2`)

Outputs added:

* `title_sentiment_score`
* `title_sentiment_label`
* `tags_sentiment_score`
* `subjectivity`

---

## 🗂 SQL Analytics

Example query to rank categories by avg views:

```sql
SELECT
  region,
  category_name,
  ROUND(AVG(views), 0) AS avg_views
FROM trending
GROUP BY region, category_name
ORDER BY region, avg_views DESC;
```

More SQL queries included in `/sql`.

---

## 📈 Time-Series & Trending Duration

Computed per video:

```python
df.groupby(['region','video_id']).agg(
    first_trend=('trending_date','min'),
    last_trend=('trending_date','max')
)
```

Visualizations:

* Histogram of trending duration
* Day-0 aligned view trajectory
* Trending survival curve (region-wise)

---

## 📊 Tableau Dashboard

Dashboard includes:

* Most popular genres (views + video count)
* Sentiment patterns by region
* Region-wise category comparison
* Trending video lifecycle
* Filters: Region, category, sentiment level

---

## 🎯 Final Deliverables

✔ Cleaned processed dataset
✔ Python scripts & notebooks
✔ SQL ranking queries
✔ Tableau dashboard
✔ Final storytelling report (PDF)

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Running ETL

```bash
python src/etl.py --input_dir data/raw --output_dir data/processed
```

---

## 🔧 Requirements (main)

```
pandas
numpy
matplotlib
seaborn
nltk
textblob
sqlalchemy
transformers
torch
tableauserverclient

```
