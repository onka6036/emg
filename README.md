# JBM Corporate Training LLC Website

## Overview
This project is a production-ready Flask web application for JBM Corporate Training LLC. It includes marketing pages, course catalog, training booking, authentication, admin dashboard, and a SQLite-backed database.

## Features
- Responsive modern corporate website
- Flask login and registration
-- No database: app has been converted to use in-memory fixtures for static/export mode
- Training booking workflow
- Admin dashboard for bookings and contact messages
- SEO-friendly page structure

## Setup
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the app:
   `python app.py`
3. Open http://localhost:5000

## Notes
The app uses SQLite by default and can be switched to MySQL or PostgreSQL by updating the database URI in config.py.
