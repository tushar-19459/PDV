# End-to-End Job Listings Web Scraping Pipeline

## 📌 Project Overview
This project is an end-to-end web scraping pipeline built using **Scrapy** to collect job listings from multiple job portals.  
The spiders are deployed and scheduled on **Zyte (Scrapy Cloud)** for automated and scalable data extraction.  
The scraped data is cleaned, validated, and stored using multiple custom pipelines for further analysis or downstream applications.

### Targeted Job Portals
- https://www.python.org/jobs/
- https://pythonjobs.github.io/
- https://remote.co/remote-jobs/developer/

---

## 🛠️ Tech Stack
- **Python**
- **Scrapy**
- **Zyte (Scrapy Cloud)**
- **Item Pipelines**
- **Databases** (sqLite3)

---

## 🏗️ Project Architecture
<img width="279" height="537" alt="image" src="https://github.com/user-attachments/assets/00604fbc-fba5-412b-8b65-f0b17cf50834" />

---

## 🕷️ Spiders
Each website has a dedicated Scrapy spider to handle its unique HTML structure and pagination logic.

- `spiderOne.py` – Scrapes jobs from python.org
- `spiderTwo.py` – Scrapes jobs from pythonjobs.github.io
- `spiderThree.py` – Scrapes remote developer jobs from remote.co

---

## 🔄 Pipelines
Multiple pipelines are implemented to ensure data quality and reliability:

### 1. Data Cleaning Pipeline
- Removes HTML tags
- Normalizes text fields
- Handles missing or malformed data

### 2. Deduplication Pipeline
- Prevents duplicate job entries
- Uses job title, company, and URL as unique identifiers

### 3. Database Pipeline
- Stores cleaned job data into the database
- Supports scalable storage for large datasets

---

## ☁️ Zyte (Scrapy Cloud) Integration
- Spiders are deployed to **Zyte**
- Scheduled crawling ensures periodic job data updates
- Built-in logging and monitoring for reliability

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/job-scraping-pipeline.git
cd job-scraping-pipeline
