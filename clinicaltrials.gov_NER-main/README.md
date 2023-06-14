# Clinicaltrials.gov Natural Language Processing: 

## About the Project
This repository contains relevant code and data for the Clinicaltrials.gov Natural Language Processing Capstone project by the University of Virginia School of Data Science, sponsored by AllenAI. 

## File Descriptions: 

**mod_chia**

*APIpullcode.ipynb*: Jupyter notebook for applying the chia-based spacy model to the entirety of clinicaltrials.gov through the ctg API interface

*base_config.cfg*: base configuration file for training spacy model

*chia_train.ipynb*: preprocessing for spacy model to create training_data.spacy and dev_data.spacy files

*dev_data.spacy*: validation docbin for spacy model training

*relaxed_scorer.ipynb*: scores spacy model by overlap of entitiy span

*stratified_sampling.ipynb*: determines optimal train/dev/test split of chia corpus for training spacy

*strict_scorer.ipynb*: uses spacy.Scorer() to score spacy model

*strict_scorer_custom.ipynb*: scored spacy model by exact match to entity span

*training_data.spacy*: training docbin for spacy model training

### How to replicate Model training: 

1. Download chia's corpus without scope: https://doi.org/10.6084/m9.figshare.11855817

2. Download SciSpacy sm model: https://github.com/allenai/scispacy

3. Use the *chia_train.ipynb* to make the *training_data.spacy* and *dev_data.spacy* files 

4. Change lines in base_config.cfg file:

```
train = '<path to directory>/training_data.spacy'
dev = '<path to directory>/dev_data.spacy'
```
5. In terminal, based in directory where these files are stored, run these lines: 

```
python -m spacy init fill-config base_config.cfg config.cfg
```

```
python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./dev_data.spacy 
```

**streamlit_files**

*api_pull_data_small.csv*: sample of dataframe to demo search within each NCT file, 10000 trials

*entities.csv*: table of entities and their descrtiptions

*ents_spans_small.csv*: sample of dataframe containing all spans marked with each entity label from 10000 trials

**additional files:** 
https://virginia.box.com/s/4ezc8cerqqon4l63aa52yvrq0wu35k2k

*results.csv*: contains dataframe with NCT ID and results of Chia-based NER model for all models availible on clinicaltrials.gov as of 05/19/23
*ents_spans.csv*: contains the spans possible to search within for each entity, for the streamlit app 

## Running the Streamlit application
1. Change existing paths
2. Run app.py
