# Cricket Scorecard Management System

This is a Python-based **Cricket Scorecard Management System** that simulates a two-team cricket match (either IPL-based or user-defined teams), records match data, and stores detailed batting and bowling scorecards in a MySQL database.

---

## 🏏 Features

* Play cricket matches with either IPL or custom teams.
* Tracks ball-by-ball score including runs, outs, 4s, 6s, overs, and wickets.
* Displays formatted scorecards after match completion.
* Stores and retrieves all match data using MySQL.
* Allows viewing previous match records.

---

## ⚙️ Technologies Used

* **Python 3**
* **MySQL**
* `mysql.connector` module
* `random` module

---

## 📁 File Structure

* `Cricket_Scorecard_Management.py` - Main Python script for playing and managing the game.

---

## 🔧 Setup Instructions

### 1. Install MySQL Connector

```bash
pip install mysql-connector-python
```

### 2. Ensure MySQL is Running

Make sure you have MySQL installed and running on `localhost`.

### 3. Run the Script

```bash
python Cricket_Scorecard_Management.py
```

* You will be prompted to enter MySQL `username` and `password`.
* If the `cricket_scorecard_management` database doesn't exist, it will be created automatically.

---

## 🎮 Gameplay Options

* Choose between **IPL teams** or **Create custom teams**.
* Enter team/player names.
* Toss to decide batting or bowling.
* Enter overs and play ball-by-ball.

---

## 📊 Stored Match Data

Each match generates 4 tables in MySQL:

* `matchX_inning1_bat`
* `matchX_inning1_bowl`
* `matchX_inning2_bat`
* `matchX_inning2_bowl`

You can view previous match records using the `Show` option at the start.

---

## ✅ Example IPL Teams Available

* Chennai Super Kings (CSK)
* Delhi Capitals (DC)
* Kolkata Knight Riders (KKR)
* Mumbai Indians (MI)
* Punjab Kings (PK)
* Rajasthan Royals (RR)
* Royal Challengers Bangalore (RCB)
* Sunrisers Hyderabad (SRH)

---

## 📌 Notes

* Only 11 players per team.
* Overs are customizable.
* Includes input validation and replay of previous matches.

---

## 🙌 Credits

Developed by Radhe Tare.

---

## 📄 License

This project is for educational purposes. Modify and use it freely for learning and personal projects.
