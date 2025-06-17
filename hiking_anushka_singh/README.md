# 🥾 Hiking Comfort Score Mini Project

## 📌 Problem Statement

You're helping a group of friends plan the perfect day to go hiking next week.  
You've been given a week's weather forecast including:

- 🌡️ Temperature
- 💧 Humidity
- 🌬️ Wind Speed

Your job is to analyze this data and **recommend the most comfortable day to go hiking**, using this formula:

Comfort Score = Temperature * 0.4 + Humidity * 0.4 + Wind Speed * 0.2

---

## 📊 Weather Data Used

| Day       | Temperature (°C) | Humidity (%) | Wind Speed (km/h) |
|-----------|------------------|--------------|--------------------|
| Monday    | 25               | 60           | 15                 |
| Tuesday   | 28               | 55           | 10                 |
| Wednesday | 30               | 50           | 20                 |
| Thursday  | 22               | 70           | 10                 |
| Friday    | 26               | 65           | 8                  |
| Saturday  | 27               | 60           | 5                  |
| Sunday    | 24               | 75           | 12                 |

---

output shown on terminal-
PS C:\Users\LENOVO\Documents\hiking-comfort-project> py weather_comfort.py
         Day  Temperature  Humidity  Wind Speed  Comfort Score
0     Monday           25        60          15           37.0
1    Tuesday           28        55          10           35.2
2  Wednesday           30        50          20           36.0
3   Thursday           22        70          10           38.8
4     Friday           26        65           8           38.0
5   Saturday           27        60           5           35.8
6     Sunday           24        75          12           42.0

🏕️ Best day to go hiking: Tuesday

🛠️ Tools Used
1.Python

2.Pandas

3.NumPy

4.VS Code for development

 Author-

Anushka Singh
Mini-Project for ML Summer School 2025 by ACM-W Manipal
GitHub: Nush-jpg2506