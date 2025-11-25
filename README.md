
# 🌤️ Wheatea Checker

A clean and lightweight weather forecasting web app built using **Django** and **OpenWeather API**.
Users can search any city and instantly view real-time temperature, sky condition, weather icons, and the current date.
The project also supports **Google Custom Search API** for city background images (optional).

---

## 🚀 Features

* 🔍 **Search weather by city name**
* 🌡️ **Live Temperature (°C)**
* ☁️ **Sky Description (clear sky, haze, mist, clouds, etc.)**
* 🖼️ **Dynamic city background using Google Images API**
* 🛟 **Graceful error handling (invalid city fallback)**
* 🔁 **Auto-reload on code changes**
* 🧩 **Clean and modular Django structure**

---

## 🛠️ Tech Stack

**Backend:** Django (Python)
**API:** OpenWeather API
**Optional:** Google Custom Search Image API
**Frontend:** HTML, CSS

---

## 🔑 API Keys Used

You need to generate and add your own keys:

* **OpenWeather API Key:** [https://openweathermap.org/api](https://openweathermap.org/api)
* **Google Custom Search Engine ID (optional)**

---

## 📦 Project Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/wheatea-checker.git
cd wheatea-checker
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 📁 Project Structure

```
weatherproject/
│── weatherproject/
│   ├── settings.py
│   ├── urls.py
│── weatherapp/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       └── index.html
│── static/
│── manage.py
```

---

## 🚦 How It Works

### ▶ Input

User enters a **city name** in the search bar.

### ▶ Processing

The app calls:
`https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY`

### ▶ Output

* Temperature
* Weather description
* Icon
* Date
* (Optional) Background image fetched from Google Search API

---

## ⚠️ Error Handling

If an invalid city is entered:

* Shows a fallback message
* Displays default weather of Indore
* No app crash

---

## 📌 Future Enhancements

* 7-day weather forecast
* Theme change based on weather
* Hourly updates
* Weather alerts
* API caching for speed

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and enhance the project.

---

## 📜 License

This project is licensed under the **MIT License**.
