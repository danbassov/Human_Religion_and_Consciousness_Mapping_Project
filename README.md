# Human_Religion_and_Consciousness_Mapping_Project

This project aims to analyze historical texts spanning from 9600 BC to 2000 AD to identify key themes related to human consciousness and religion. Using Natural Language Processing (NLP) techniques, the project categorizes text into predefined themes, performs sentiment analysis, and visualizes the frequency of these themes over time.

**Project Overview**

**Features:**

Text Processing: Breaks down large historical texts into manageable periods and analyzes them using Spacy's NLP model.

Theme Identification: Detects and categorizes key themes (e.g., Religion, Events, Consciousness) using custom pattern matching.

Sentiment Analysis: Assesses the sentiment of each time period to understand the overall tone.

Frequency Analysis: Tracks the occurrence of each theme over time.

Visualization: Generates time-series graphs to visualize the frequency of each theme.

**How It Works:**

Text Splitting: Historical texts are split into sections corresponding to different time periods.

NLP Processing: Each section is analyzed to identify and categorize key themes based on pre-defined patterns.

Sentiment Analysis: Sentiment polarity and subjectivity are calculated for each section.

Data Visualization: The frequency of each theme is plotted over time.

**Technologies Used:**

Python

Spacy: For NLP processing and pattern matching.

TextBlob: For sentiment analysis.

Matplotlib: For data visualization.


**Installation:**

1) Clone the repository:

git clone https://github.com/2000dann/Human_Religion_and_Consciousness_Mapping_Project.git

2) Navigate to the project directory:

cd human-consciousness-mapping

3) Install the required packages:

Spacy, TexotBlob, Matplotlib

**Usage:**

Prepare your text data in a .txt file.

**Run the main script:**

python Human_Religion_and_Consciousnes_Mapping_Project.py

Don't Forget: View the generated graphs and check the processed data output in processed_output.txt

**File Structure**

Human_Religion_and_Consciousnes_Mapping_Project.pyy: Main script that runs the analysis.

records_9600_to_2000.txt: Sample text file containing historical data.

processed_output.txt: Output file containing the processed data and analysis.

**Contributing**

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**

Special thanks to the open-source community for providing the tools and libraries that made this project possible.
