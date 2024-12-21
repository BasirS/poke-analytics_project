# Pokémon Analytics Project in Python

This project explores the evolution of Pokémon games' popularity using Python and integrates data from the VGChartz dataset and PokeAPI. By leveraging programming, analytics techniques, and Object-Oriented Programming (OOP) principles, this project aims to analyze Pokémon games' sales figures across different platforms and explore related data to uncover the franchise's enduring success.

---

## Project Overview

The objective of this project is to:

1. Analyze the global sales data of Pokémon games using the VGChartz dataset.  
2. Examine prominent Pokémon-specific base stats through the PokeAPI to explore their impact on the games' success.
3. Demonstrate skills in Python programming, data visualization techniques, and modular code design via OOP principles.

### Tools and Techniques Used:
- **Python Libraries**: `pandas`, `NumPy`, `matplotlib`, `seaborn`, `requests`, `Beautiful Soup`, `python-pptx`, `Pillow` 
- **Visualization**: Python (matplotlib, seaborn) with integrated images from a Tableau presentation.
- **Object-Oriented Programming**: Encapsulation of functionality into reusable classes (e.g., PokeAPI).

---

## Key Hypotheses

### 1. Dataset Hypothesis  
This analysis will quantitatively explore the relationship between global sales of Pokémon games and factors such as platform availability, regional sales trends, and franchise timeline. The idea is to investigate whether games released during periods of heightened franchise interest or on widely adopted platforms exhibit higher global sales.

### 2. API Hypothesis  
This exploration will qualitatively examine how intrinsic Pokémon characteristics might contribute to the appeal and popularity of the games they are featured in. The analysis will consider how Pokémon with pivotal roles in the storyline may influence player engagement and game reception.

---

## Getting Started: Setting Up the Project

### 1. Install Prerequisites  
To run this project locally, you must have the following installed:
- Python 3.8 or later  
- pip (Python package manager)  

**Setting up the Virtual Environment (Recommended):**

It's highly recommended to create a virtual environment to isolate your project's dependencies. This prevents conflicts with other Python projects.

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv .venv  # On Windows, use: py -3 -m venv .venv
    ```

2.  **Activate the virtual environment:**

    *   **On macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

    *   **On Windows:**

        ```bash
        .venv\Scripts\activate
        ```

**Installing Required Libraries:**

Once the virtual environment is activated, install the required Python libraries using the `requirements.txt` file (which should be included in your repository):

```bash
pip install -r requirements.txt
```

### 2. Clone the Repository  
Clone the repository to your local machine using the following command:  

```bash
git clone https://github.com/BasirS/poke-analytics_project
```

### 3. Set Up API Keys

#### PokeAPI Access  
PokeAPI is freely accessible, and no API key is required. You can directly make requests to its endpoints to retrieve Pokémon data.  

- An example API Endpoint for Bulbasaur:  

```bash
https://pokeapi.co/api/v2/pokemon/bulbasaur
```
<p align="center">OR</p>

```bash
https://pokeapi.co/api/v2/pokemon/1
```

- For more information on endpoints and data structures, visit the PokeAPI Documentation <a href="https://pokeapi.co/docs/v2" title="Official PokeAPI Documentation" target="_blank">here</a>.

#### Config File for Other APIs (optional)  
If you use additional APIs for your project which require keys, make sure to store them in a file named `config.py` in the following format:

```python
OTHER_API_KEY = "your_other_api_key_here"
```

---

## Data Sources

### VGChartz Dataset  
- **Source**: The VGChartz dataset provides global sales data for video games, including Pokémon titles.  
- **Purpose**: This dataset serves as the foundation for analyzing Pokémon game sales and identifying trends across regions and platforms.  

### PokeAPI  
- **Purpose**: PokeAPI offers comprehensive data on individual Pokémon, including stats, types, and abilities.  
- **Usage**: In this project, PokeAPI is used to retrieve and visualize the *base stats* of selected Pokémon.
  *Example*: Starter Pokémon are an important part of the player experience, and their design can be a significant factor in a game's initial appeal.

---

## Data Visualizations and Interpretations

### 1. Global Sales by Pokémon Game 
---
#### Insight 1: What makes the top-selling Pokémon games so successful?

![Global Sales Distribution (Bar Chart)](resources/1st_output_barplot.png)
* Our first bar chart highlights global sales data for Pokémon games, with **Pokémon Red/Blue** leading at 31.37 million units sold. Its success is rooted in its innovative gameplay, accessibility on the Game Boy, and the introduction of features like link cable trading, alongside a robust multimedia campaign that established Pokémon as a global phenomenon.

* Following closely, **Pokémon Gold/Silver** sold 23.10 million units, driven by enhancements like day-night cycles, 100 new Pokémon, and two regions to explore, which expanded on the original's appeal. Iterative improvements and innovative mechanics ensured these titles retained and grew their audience.

* Games like **Ruby/Sapphire** and **Diamond/Pearl** reflect the series' adaptability, leveraging new hardware capabilities to introduce features like Pokémon Abilities and online trading, maintaining high engagement. The chart emphasizes the franchise's mastery of blending nostalgia with innovation across generations.

![Top-Selling Pokémon Games' Success (Bar Plot)](resources/2nd_output_barplot.png)
* Now, the second bar chart showcases the global sales data for the top 10 best-selling Pokémon games. It highlights the enormous popularity of **Pokémon Red/Blue**, leading the list with an impressive **31.37** million units sold, followed by **Pokémon Gold/Silver** at **23.10 million units**. This significant gap indicates how the first-generation games established the foundation for the franchise's enduring success. Factors such as the novelty of the Pokémon concept, the introduction of link cable trading, and the nostalgia associated with these titles may have contributed to their monumental success.

* Other high-ranking entries like **Pokémon Diamond/Pearl** and **Ruby/Sapphire** reflect how iterative improvements, new mechanics, and fresh regions continued to engage audiences over the years. The consistent sales across newer titles suggest that nostalgia, coupled with innovations, plays a critical role in maintaining Pokémon’s dominance in the gaming industry.
---

#### Insight 2: How do sales trends correlate with the platform used and the release year?

![Global Sales by Platform (Line Plot)](resources/3rd_output_lineplot.png)
* The line chart analyzes global sales trends across various platforms, illustrating the pivotal role hardware plays in the franchise's success. The **Nintendo DS (DS)** emerges as the most successful platform, generating over **80 million units** in sales, reflecting its broad market penetration and compatibility with multiple Pokémon titles. Similarly, platforms like the **Game Boy (GB)** and **Game Boy Advance (GBA)** sustain the trend of high sales during their respective peaks.

* However, the chart also reveals dips in sales for platforms like the **GameCube (GC)** and **Mobile**, emphasizing the importance of accessible and popular hardware in driving game success. The spike in sales for the **Nintendo Switch (NS)** highlights the impact of modern hybrid gaming experiences, reflecting Pokémon’s ability to adapt and thrive with changing player preferences.

![Yearly Global Sales of Games on All Platforms(Pie Chart)](tableau/slide1_image.png)
* This Tableau visualization depicts a pie chart that provides an overview of Pokémon game sales across various platforms and release years. From the visualization, it's evident that earlier platforms like the **Game Boy (GB)** and **Game Boy Advance (GBA)** played a foundational role in establishing Pokémon as a blockbuster franchise, with combined sales exceeding **79 million units (79M)** and **49 million units (49M)**, respectively. These platforms represent the franchise's formative years, where games like *Pokémon Red*, *Blue*, and *Emerald* capitalized on the novelty of portable gaming and simple yet immersive mechanics.

* In contrast, newer platforms like the **Nintendo Switch (NS)** and **3DS** reflect Pokémon’s ability to stay relevant by evolving with technology. The Nintendo Switch alone boasts sales of over **25 million units** for Pokémon titles in **2022**, which correlates with its versatility as both a handheld and docked console. Similarly, the 3DS saw sales spikes during its peak years in **2013 (14.35M)** and **2016 (15.17M)**, coinciding with the release of highly anticipated titles like *Pokémon X/Y* and *Pokémon Sun/Moon*.

* The timeline reveals that platform adoption and hardware capabilities heavily influence game sales. For example, the **GameCube** and **Nintendo 64** had lower contributions to Pokémon sales due to their limited portable appeal, compared to handheld-focused devices that align better with the franchise's design philosophy. Additionally, the dominance of mobile platforms in **2019** (with the release of Pokémon GO) shows how Pokémon successfully leveraged emerging trends in casual and mobile gaming to expand its audience.

![Global Sales by Top 5 Nintendo Platforms(Donut Chart)](tableau/slide2_image.png)
* Following up with the above one is another Tableau visualization, which reinforces the significance of the **Game Boy (GB)** and **DS**, which together account for a significant share of the total **329.6 million (M)** global sales. The **DS (76.7M)**, for example, demonstrates the success of innovative features like dual screens and Wi-Fi connectivity, which were instrumental in the popularity of games like *Pokémon Diamond/Pearl* and *HeartGold/SoulSilver*.

* The transition to the **3DS (66.6M)** showcases a natural progression, with Nintendo capitalizing on backward compatibility and improved hardware, ensuring a seamless shift in player loyalty. Similarly, the **GBA (49M)** served as a pivotal platform for Pokémon's evolution, introducing fan-favorite titles like Ruby/Sapphire while setting the stage for later advancements.

* The **Nintendo Switch (58.3M)** marks a new era of Pokémon games, offering HD visuals and open-world exploration that appeals to both nostalgic fans and newer audiences. This aligns with broader gaming trends, where hybrid consoles appeal to diverse player preferences, from casual to competitive.



### 2. Pokémon Traits and Success  
*TBD*  

---

## Complications  
*TBD*  

---

## Conclusion  
*TBD*  

---

## Future Enhancements  
*TBD*  

---

## Your Suggestions  

How can I further enhance this analysis? Feel free to contribute or share ideas via GitHub!
