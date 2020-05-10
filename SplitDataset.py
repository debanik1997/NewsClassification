import json
import pprint

import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

data = []

with open('News_Category_Dataset.json') as f:
    for line in f:
        json_dict = json.loads(line)
        current_line = [json_dict['category'],
                        json_dict['headline'],
                        json_dict['short_description'],
                        json_dict['link'],
                        json_dict['date']]
        data.append(current_line)

df = pd.DataFrame(data, columns=['category', 'headline', 'short_description', 'link', 'date'])

smallestCategorySize = df['category'].value_counts().sort_values(ascending=True)[0]

categories = df['category'].unique().tolist()

counts = {i: 0 for i in categories}

merged_classes = {'EDUCATION': 'ART & EDUCATION',
                  'CULTURE & ARTS': 'ART & EDUCATION',
                  'LATINO VOICES': 'SPECIAL INTEREST',
                  'COLLEGE': 'ART & EDUCATION',
                  'ENVIRONMENT': 'CURRENT EVENTS',
                  'ARTS & CULTURE': 'ART & EDUCATION',
                  'GOOD NEWS': 'ENTERTAINMENT',
                  'FIFTY': 'SPECIAL INTEREST',
                  'ARTS': 'ART & EDUCATION',
                  'MONEY': 'BUSINESS',
                  'TECH': 'BUSINESS',
                  'TASTE': 'ENTERTAINMENT',
                  'WORLD NEWS': 'CURRENT EVENTS',
                  'SCIENCE': 'ART & EDUCATION',
                  'STYLE': 'WELLNESS',
                  'RELIGION': 'HOME',
                  'WORLDPOST': 'CURRENT EVENTS',
                  'GREEN': 'CURRENT EVENTS',
                  'WEIRD NEWS': 'ENTERTAINMENT',
                  'MEDIA': 'ENTERTAINMENT',
                  'CRIME': 'CURRENT EVENTS',
                  'DIVORCE': 'HOME',
                  'IMPACT': 'BUSINESS',
                  'WOMEN': 'SPECIAL INTEREST',
                  'WEDDINGS': 'HOME',
                  'THE WORLDPOST': 'CURRENT EVENTS',
                  'PARENTS': 'HOME',
                  'HOME & LIVING': 'HOME',
                  'BLACK VOICES': 'SPECIAL INTEREST',
                  'SPORTS': 'ENTERTAINMENT',
                  'COMEDY': 'ENTERTAINMENT',
                  'BUSINESS': 'BUSINESS',
                  'FOOD & DRINK': 'ENTERTAINMENT',
                  'QUEER VOICES': 'SPECIAL INTEREST',
                  'HEALTHY LIVING': 'WELLNESS',
                  'PARENTING': 'HOME',
                  'STYLE & BEAUTY': 'WELLNESS',
                  'TRAVEL': 'ENTERTAINMENT',
                  'ENTERTAINMENT': 'ENTERTAINMENT',
                  'WELLNESS': 'WELLNESS',
                  'POLITICS': 'CURRENT EVENTS'}

with open('News_Category_Dataset_UNDERSAMPLED.json', 'w') as f:
    for index, row in df.iterrows():
        if counts[row.category] < smallestCategorySize:
            counts[row.category] += 1
            jsonifySeries = json.dumps(row.to_dict())
            f.write(jsonifySeries)
            f.write("\n")


with open('News_Category_Dataset_CATEGORIZED.json', 'w') as f:
    for index, row in df.iterrows():
        categorizedRow = row
        row.category = merged_classes[row.category]
        jsonifySeries = json.dumps(row.to_dict())
        f.write(jsonifySeries)
        f.write("\n")

