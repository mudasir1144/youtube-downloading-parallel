# 🎬 YouTube Parallel Downloader (Flask + Threading)

A simple beginner-friendly web project that demonstrates **parallel computing using Python threading** by downloading multiple YouTube videos at the same time using `yt-dlp`.


# 📌 Project Overview

This project allows users to:

* Paste multiple YouTube video links in a web interface
* Start downloading all videos at once
* Use Python threading for parallel downloads

It is designed as a **class project** to demonstrate:

* Web development basics (HTML + Flask)
* Python backend programming
* Parallel computing (threading)

---

# ⚙️ Technologies Used

* Python
* Flask
* yt-dlp (YouTube downloader library)
* HTML (frontend)
* CSS (styling)
* Python Threading (parallel execution)

---

# 📁 Project Structure

```
youtube_parallel_downloader/
│
├── app.py                 # Main Flask backend
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # Styling
└── downloads/            # Downloaded videos folder
```

---

# 🚀 Features

✔ Download multiple YouTube videos at once
✔ Parallel downloading using threading
✔ Simple and clean web interface
✔ Automatic download folder creation
✔ Beginner-friendly code structure

---

# 📦 Installation Requirements

Install required Python libraries:

```bash
pip install flask yt-dlp
```

---

# ▶️ How to Run the Project

### Step 1: Open VS Code

Open the project folder in VS Code.

---

### Step 2: Run Flask App

```bash
python app.py
```

---

### Step 3: Open Browser

Go to:

```
http://127.0.0.1:5000
```

---

### Step 4: Paste Links

* Paste multiple YouTube links (one per line)
* Click **Download Videos**

---

### Step 5: Check Downloads

All videos will be saved in:

```
downloads/
```

---

# 🧠 How Parallel Computing Works

Normally, videos download one after another (sequential execution).

But in this project:

* Each video is assigned a separate thread
* All threads run simultaneously
* Multiple downloads happen at the same time

This demonstrates **parallel computing using Python threading**.

---

# ⚠️ Important Notes

* Make sure you have a stable internet connection
* Some YouTube videos may take longer due to size or network speed
* Do not close the terminal while downloading

---

# 🎯 Learning Outcome

After completing this project, you will understand:

* How web apps work (frontend + backend)
* How Python handles multithreading
* How real-world download managers work internally

---

# 👨‍🎓 Author Notes (For Class Presentation)

> "This project demonstrates parallel computing using Python threading where multiple YouTube videos are downloaded simultaneously instead of sequentially, improving efficiency and showcasing concurrency concepts."

---

# ✅ End of Project
