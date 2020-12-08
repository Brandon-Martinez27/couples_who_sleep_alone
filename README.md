# Couples Who Sleep Alone

### Goals
- Find what factors influence a couple to sleep in separate beds
- Build a classification model to predict whether a couple will sleep in separate beds
- Explore the possiblity of marketing separate beds to couple's that tend to sleep separately

### Background
>In 1927, the Motion Picture Association of America issued “The Don’ts and Be Carefuls.” Item No. 19 in the “be careful” section of the list was “man and woman in bed together” — a scene the organization thought could risk “vulgarity and suggestiveness.” Even decades later on TV, Lucy and Ricky were always shown in separate beds in “I Love Lucy” despite being married offscreen, as well as on it.

>Times have changed. It doesn’t take a data journalist to work out that the chances of you having seen a couple sharing a bed onscreen is high. But the reality of what’s happening offscreen is harder to gauge, tucked away in bedrooms. After all, Anonymous, how many people have you told about your sleeping arrangements?

<p style='text-align: right;'>FiveThirtyEight</p>

### Deliverables
- Github Repo w/ Final Notebook and README
- Class Presentation + Slide Deck

### Acknowledgments
- [FiveThirtyEight Article](https://fivethirtyeight.com/features/dear-mona-how-many-couples-sleep-in-separate-beds/)
- [Data](https://github.com/fivethirtyeight/data/tree/master/sleeping-alone-data)

## Data Dictionary
Describe the columns in your final dataset. Use [this link](https://www.tablesgenerator.com/markdown_tables) to easily create markdown tables.

| Feature Name | Description                                                                        |
|--------------|------------------------------------------------------------------------------------|
| rel_length   | Length of relationship in years                                                    |
| separate_bed | Target variable, 1: couple sleeps in same bed, 0: couple doesn't sleep in same bed |
| occupation   | The field in which person who reported is currently employed in                    |
| age          | The age group of respondent                                                        |
| education    | The highest level of education a respondent recieved                               |
| location     | The census region within the U.S.                                                  |
| married      | Married or not                                                                     |
| male         | Male or female                                                                     |
| long_term    | Relationship is 11-20 years                                                        |
| young        | Age group is 18-29                                                                 |
| hs_or_less   | Highest level of education is HS degree or less                                    |
| regional     | Region is either East South Central, Mountain, and South Atlantic                  |
| esc_610      | Region is East South Central and relationship length is 6-10 years                 |
| ma_1620      | Region is Middle Atlantic and relationship length is 16-20 years                   |
| mt_1115      | Region is Mountain and relationship length is 11-15 years                          |
| midage_hs    | Age group is 30-44 and education level is HS degree or less                        |
| esc_bac      | Region is East South Central and education level is Bachelor's degree              |
| pac_hs       | Region is Pacific and education level is High School or less                       |

## Initial Thoughts & Hypotheses
### Thoughts
- Do couples in longer relationships sleep in separate beds?
- Do older couples end up sleeping in separate beds?
- Are people with higher degrees sleeping separately?
- Which census region are couples more likely to sleep seperately?
- Are people with stressful jobs sleeping separately? *Note: need to do a lot of cleaning for the occupation category. May require NLP to categorize 'Other' reponses. Will do after project is done if time permits*
### Hypotheses
I used a Chi$^2$ Test to determine a relationship between my features and my target. All features were categorical
```
Null hypothesis: Sleeping in separate beds is independent of {key features}
```

## Project Steps
### Acquire
Using pandas, I read the data from a csv locally to a dataframe. The data can be found in the acknowledments section. Use 'ISO-8859-1' as the argument for encoding or the data may not be read correctly. See `wrangle.py` for code sample.
### Prepare
- Dropped the date columns and columns with less than 1000 non-null values
- Lowercased columns
- Renamed columns. Final column names are in the data dictionary
- Created and combined values within columns to reduce categories
- Encoded gender
- Split the data into train, validate, test
- Created variables with feature engineering
### Explore
Looked at the countplot of each variable and the distribution of separate beds or not.
Answered initial hypothesis question
Ran Chi^2 test for each variable
### Model
- Set baseline to mean of most frequent (sleep in same beds)
- Did cross validation to find optimal hyperparameters for models
- Ran 3 models
  - Logistic Regression 
  - Random Forest
  - Decision Tree
### Conclusions
<b>Summary</b>: None of the models I trained/tested beat the baseline. This leads me to believe that the current features don't have great predictive potential.

<b>Next Steps</b>:
It may be helpful to explore the occupation feature and decipher the "Other" category. There is data that indicated the specific response to this selection and further condensing this category may be useful.
Its usually helpful to collect and use more data. Running a survey with more descriptive questions and including some quantitative data may contribute as well.
Follow up questions like, "What are the reasons that you sleep in separate beds? Please select all that apply," were excluded due to several null values. Perhaps exploring these as additional variables and making these survey questions mandatory can eliminate a lot of preparation and be useful for analysis.

### Tools & Requirements
Python latest version

## License
Standard

## Creators
Brandon Martinez
