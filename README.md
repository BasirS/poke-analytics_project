# Pokémon Analytics Project in Python

This project explores the evolution of Pokémon games' popularity using Python and integrates data from the VGChartz dataset and PokeAPI. By leveraging programming, analytics techniques, and Object-Oriented Programming (OOP) principles, this project aims to analyze Pokémon games' global sales and uncover the elements contributing to the franchise's enduring success.

## Project Overview

The objective of this project is to:
  1. Analyze the global sales data of Pokémon games using the VGChartz dataset.
  2. Examine Pokémon-specific traits (e.g., types, abilities) through the PokeAPI    to explore their impact on the games' success.
  3. Demonstrate skills in Python programming, data visualization, and modular       code design via OOP principles.

The tools and techniques used include:
  + Python Libraries: pandas, matplotlib, requests
  + Visualization Platforms: matplotlib, Tableau
  + Object-Oriented Programming: Encapsulation of functionality into reusable        classes.

## Key Hypotheses
### Dataset Hypothesis
The commercial success of Pokémon games is significantly influenced by key attributes like platform availability, regional sales trends, and franchise timelines. Games released during peak franchise moments (e.g., new generation launches) or on widely adopted platforms (like Nintendo DS) outperform others globally.

### API Hypothesis
The success of Pokémon games is deeply rooted in internal elements like the design of iconic Pokémon (e.g., Pikachu), their abilities, and type combinations. Pokémon with unique traits or pivotal roles in the storyline significantly boost their games’ appeal and popularity.

## Getting Started: Setting Up the Project
### 1. Install Prerequisites
To run this project locally, you must have the following installed:
  - Python 3.8 or later
  - pip (Python package manager)
  - Required Python libraries:
    ```bash
      pip install pandas matplotlib requests

### 2. Clone the Repository
  - Clone the repository to your local machine using the following command:
    ```bash
    git clone https://github.com/BasirS/poke-analytics_project

### 3. Set Up API Keys
  - PokeAPI Access:
    PokeAPI is freely accessible, and no API key is required. You can directly       make requests to its endpoints to retrieve Pokémon data.
    - An example API Endpoint for Pikachu:
      ```bash
      https://pokeapi.co/api/v2/pokemon/pikachu
    - For more information on endpoints and data structures, visit the PokeAPI Documentation <a href="https://pokeapi.co/docs/v2" title="Official PokeAPI Documentation" target="_blank">here</a>.

  - Config File for Other APIs (optional):
    If you use additional APIs for your project which require keys, make             sure to store them in a file named config.py in the following format:
    ```bash
    OTHER_API_KEY = "your_other_api_key_here"

## Data Sources and Connection
### VGChartz Dataset
  - Source: The VGChartz dataset provides global sales data for video games,         including Pokémon titles.
  - Connection: The dataset is the foundation for analyzing Pokémon game sales       and identifying trends across regions and platforms.

### PokeAPI
  - Purpose: PokeAPI offers comprehensive data on individual Pokémon, including      stats, types, and abilities.
  - Connection: By combining game sales data with Pokémon-specific attributes        from PokeAPI, we aim to understand how Pokémon design and abilities              contribute to a game’s success. (e.g., iconic Pokémon like Charizard—            Fire/Flying type, popular starter evolution—may attract more players).

## Data Visualizations and Interpretations
### 1. Global Sales by Pokémon Game
### 2. Pokémon Traits and Success

## Complications

## Conclusion

## Future Enhancements

## Your Suggestions
How can I further enhance this analysis? Feel free to contribute or share ideas via GitHub!
