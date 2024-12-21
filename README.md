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
*TBD*  

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
