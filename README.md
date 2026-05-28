# sarah-s_portfolio
These are projects I created in my AP CSP class

# 🧳 Project 1: Ultimate Travel Packing Todo List

### 📝 Summary
This Python script is an interactive command-line application that helps users manage their clothing packing checklist before a trip. It provides a simple, menu-driven interface to easily track, add, and check off essential travel items.

### ✨ Key Features
* 🕹️ **Interactive Menus:** Easy-to-navigate command-line prompts to guide users through adding items, marking tasks as done, or clearing the entire list.
* 📊 **Dynamic Tracking:** Instantly view separated, real-time lists of tasks you still need to complete and items you've already packed.
* 🛡️ **Error Handling:** Built-in safeguards prevent crashes from accidental typos or blank inputs, keeping your planning session completely smooth.
* 👟 **Preset Defaults:** Starts with a convenient, pre-loaded list of fundamental travel clothing (shirts, pants, shoes, etc.) to jumpstart your packing instantly.

---

# ✈️ Project 2: In-Flight Movie Picker

### 📝 Summary
The In-Flight Movie Picker is a command-line application designed to help travelers find the perfect movie to watch during their flights. By matching user-specified flight durations and preferred genres with an IMDb dataset, the tool ensures your entertainment fits perfectly into your travel window. Additionally, it features an interactive search system that lets users dive deeper into specific movie facts, cast details, and ratings before they fly.

### ✨ Key Features
* ⏱️ **Smart Flight-Time Filtering:** Automatically excludes any movies that are longer than your remaining flight time, preventing your movie from being cut off mid-scene.
* 🧠 **Dynamic Recommendation Engine:** Adapts its output based on how many matches are found—offering top suggestions instantly while giving you the option to expand and view the complete list of matching films.
* 🔍 **Deep-Dive Fact Search:** Allows you to look up any specific movie title to instantly retrieve curated data including the IMDb rating, director, lead star, and a plot overview.
* 🧩 **Crash-Resistant Interface:** Built with integrated error handling (such as data-type validation for flight times) to ensure smooth navigation through the menus without the program crashing.

---

# 🍿 Project 3: Age-Based Movie Rating Evaluator

### 📝 Summary
The Age-Based Movie Rating Evaluator is a quick, interactive Python script that suggests appropriate movie ratings based on a user's entered age. It takes the guesswork out of family movie night by instantly informing users which MPA rating categories (G, PG, PG-13, or R) they are old enough to watch. 

### ✨ Key Features
* 👤 **Interactive Input:** Simple and direct terminal prompts that ask the user to input their exact age.
* 📈 **Tiered Recommendations:** Evaluates age using conditional logic to output a personalized, accurate list of safe movie ratings.
* ⚠️ **Age-Appropriate Warnings:** Reminds users to view certain titles (like PG) with caution if they fall within younger age brackets.

---

# 📉 Project 4: Influencer Scandal Tracker

### 📝 Summary
This project analyzes social media creator data to identify critical financial turning points caused by public controversies. It processes metrics like views, dislikes, subscriber counts, and earnings from a data file to locate the exact timeline of an influencer's career decline. Specifically, the script isolates and extracts the two consecutive months where creator revenue dropped to zero, marking the definitive start of their downfall.

### ✨ Key Features
* 🚨 **Automated Scandal Detection:** Automatically scans dataset arrays to instantly flag and highlight months with total revenue collapse.
* 🎯 **Targeted Data Extraction:** Filters and isolates specific data rows using pandas localization to pin down the exact chronological timeline of the controversy.
* 🗃️ **Multi-Metric Parsing:** Converts raw CSV data into clean, manageable Python lists for a granular analysis of views, dislikes, subscribers, and revenue trends.

---

# 🐾 Project 5: Dog Breed Finder

### 📝 Summary
The Dog Breed Finder is an interactive Python program designed to help users discover the perfect dog breed for their lifestyle. By utilizing a custom dataset, users can easily search for dogs based on size, temperament, visual traits, and historical breeding purposes.

### ✨ Key Features
* 🐕 **Size-Based Recommendations:** Get tailored breed recommendations perfectly suited to your preferred weight class (Tiny, Small, Medium, or Large).
* 🌐 **Trait Discovery & Web Integration:** Search for a specific breed to view its temperament details and instantly trigger your default web browser to open an image of the dog.
* 🛠️ **Purpose Matching:** Enter a specific job or purpose (e.g., hunting, guarding) to instantly discover which breeds were historically developed for those tasks.
* 🗺️ **Interactive Menu:** Navigate through user-friendly prompts to easily switch between search functions or explore multiple breeds in a single session.

---

# 🎭 Project 6: Interactive Python Mad Libs Generator

### 📝 Summary
This project is an interactive, terminal-based Mad Libs game that prompts users for various parts of speech to construct a humorous, randomized campus story. It features a dual-input mechanic where users can either type their own words or enter "random" to let the script select choices from built-in word banks, ensuring a unique narrative every time it runs.

### ✨ Key Features
* 🔀 **Hybrid Input System:** Gives players the complete freedom to fully customize the story with their own words or leverage automated word banks by typing "random" for any prompt.
* 🎲 **Dynamic Story Generation:** Utilizes Python's `random` module to select elements across 15 distinct structural variables, creating thousands of potential story variations.
* 🔤 **Bold Text Formatter:** Implements terminal ANSI escape codes (`\033[1m`) to automatically capitalize and bold user inputs, making the generated words visually pop within the final story block.
* 📦 **Self-Contained Logic:** Designed with structured user prompts and fallback arrays inside a singular, easily executable function for zero-configuration gameplay.
