import spacy
from spacy.matcher import Matcher
from textblob import TextBlob
import matplotlib.pyplot as plt
nlp = spacy.load('en_core_web_sm')


class TextProcessor:
    def __init__(self, nlp_model, patterns):
        self.nlp = nlp_model
        self.matcher = Matcher(self.nlp.vocab)
        self._add_patterns(patterns)

    def _add_patterns(self, patterns):
        for pattern in patterns:
            self.matcher.add(pattern['label'], [pattern['pattern']])
            print(f"Added patternL {pattern['label']} -> {pattern['pattern']}")
    
    def load_and_split_text(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content.split('\n\n')
    
    def process_text(self, text):
        doc = nlp(text)
        matches = self.matcher(doc)

        categories = {
            "RELIGION": [],
            "CONSCIOUSNESS": []

        }

        print(f"Processing text: {text[:100]}...")  # Print the beginning of the text being processed

        for match_id, start, end in matches:
            span = doc[start:end]
            label = self.nlp.vocab.strings[match_id]

            if label in categories:
                categories[label].append(span.text)
                print(f"Matched '{span.text}' as '{label}'")  # Debugging print statement
            else:
                print(f"Label '{label}' not found in categories")

        # Print the content of each category to verify it is capturing correctly
        for category, items in categories.items():
            print(f"Category '{category}' has {len(items)} items: {items}")

        sentiment = TextBlob(text).sentiment
        print(f"Sentiment: {sentiment}")
    
        if categories and sentiment:
            return categories, sentiment
        else:
            return None, None


class FrequencyAnalyzer:
    def __init__(self):
        self.frequency_analysis = {}

    def update_frequencies(self, period, categories):
        for theme, items in categories.items():
            if theme not in self.frequency_analysis:
                self.frequency_analysis[theme] = {}
            self.frequency_analysis[theme][period] = len(items)
            print(f"Updated {theme} for period {period}: {len(items)}")

    def get_frequencies(self):
        return self.frequency_analysis
    
class Visualizer:
    def plot_frequencies(self, frequency_analysis):
        for theme, data in frequency_analysis.items():
            periods = list(data.keys())
            frequencies = list(data.values())
            print(f"Plotting {theme}: {frequencies}")

            if any(frequencies):
                plt.plot(periods, frequencies, label = theme)

            plt.plot(periods,frequencies)
            # plt.title('Themes Over Time')
            plt.title(f'{theme} Over Time')
            plt.xlabel('Time Period')
            plt.ylabel('Frequency')
            plt.xticks(rotation=90)
            plt.legend()
            plt.show()


class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    
    def categorize_sentiment(self, polarity):
        if polarity>0:
            return "Positive"
        elif polarity<0:
            return "Negative"
        else:
            return "Neutral"

class Main:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.patterns = [
            
            {"label": "RELIGION", "pattern": [{"LEMMA": "spiritual"}]}, 
            {"label": "RELIGION", "pattern": [{"LEMMA": "belief"}]},      
            {"label": "RELIGION", "pattern": [{"LEMMA": "ritual"}]},      
            {"label": "RELIGION", "pattern": [{"LEMMA": "faith"}]},       
            {"label": "RELIGION", "pattern": [{"LEMMA": "worship"}]},     
            {"label": "RELIGION", "pattern": [{"LEMMA": "religion"}]},    
            {"label": "RELIGION", "pattern": [{"LEMMA": "worship"}]},
            {"label": "RELIGION", "pattern": [{"LEMMA": "spiritual"}, {"LEMMA": "belief"}]},
            {"label": "RELIGION", "pattern": [{"LEMMA": "ritual"}, {"LEMMA": "practice"}]},     
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "collective"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "thought"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "mental"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "emotion"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "collective"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "conscience"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "self"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "conscious"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "consciousness"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "ancient"}]},
            {"label": "CONSCIOUSNESS", "pattern": [{"LEMMA": "collective"}, {"LEMMA": "thought"}]},
            
        ]

        self.text_processor = TextProcessor(self.nlp, self.patterns)
        self.frequency_analyzer = FrequencyAnalyzer()
        self.visualizer = Visualizer()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.time_period_outputs = {}

    def load_data(self, file_path):
        self.texts = self.text_processor.load_and_split_text(file_path)
        self.periods = [f"{9600-i*100} BC" for i in range(96)] + [f"{0+i*100} AD" for i in range(21)] 

    def process_data(self):
        for period, text in zip(self.periods, self.texts):
            categories, sentiment = self.text_processor.process_text(text)

            if categories is None or sentiment is None:
                print(f"Skipping period {period} due to missing data.")
                continue

            self.time_period_outputs[period] = categories
            
            if sentiment:
            
                polarity, subjectivity = sentiment.polarity, sentiment.subjectivity
                sentiment_category = self.sentiment_analyzer.categorize_sentiment(polarity)
                self.time_period_outputs[period]["SENTIMENT"] = {
                    "Polarity": polarity,
                    "Subjectivity": subjectivity,
                    "Category": sentiment_category
                }
            
            
            
            self.frequency_analyzer.update_frequencies(period, categories)

        polarity, subjectivity = self.sentiment_analyzer.analyze_sentiment(text)
        sentiment_category = self.sentiment_analyzer.categorize_sentiment(polarity)
        self.time_period_outputs[period]["SENTIMENT"] = {
            "Polarity": polarity,
            "Subjectivity": subjectivity,
            "category": sentiment_category
        }
    
        self.frequency_analyzer.update_frequencies(period, categories)

    def save_output(self, output_path):
        with open(output_path,"w", encoding = "utf-8") as file:
            for period, categories in self.time_period_outputs.items():
                file.write(f"Time Period: {period}\n")

                for theme, items in categories.items():
                    if theme != "SENTIMENT":
                        file.write(f"{theme}: \n")
                        if items:
                            for item in items:
                                file.write(f"  - {item}\n")
                        else:
                            file.write("  - None\n")
                    else:
                        file.write(f"Sentiment Analysis:\n")
                        file.write(f"  - Polarity: {categories['SENTIMENT'].get('Polarity', 'N/A')}\n")
                        file.write(f"  - Subjectivity: {categories['SENTIMENT'].get('Subjectivity', 'N/A')}\n")
                        file.write(f"  - Category: {categories['SENTIMENT'].get('Category', 'N/A')}\n")
                file.write("---------\n")               # Delimeter between time periods
    
    def visualize_data(self):
        frequency_analysis = self.frequency_analyzer.get_frequencies()
        print(f"Final frequency analysis: {frequency_analysis}")
        self.visualizer.plot_frequencies(frequency_analysis)

    def run(self, file_path, output_path):
        self.load_data(file_path)
        self.process_data()
        self.save_output(output_path)
        self.visualize_data()

if __name__ == "__main__":
    main_program = Main()
    main_program.run("records_9600_to_2000.txt", "processed_output.txt")