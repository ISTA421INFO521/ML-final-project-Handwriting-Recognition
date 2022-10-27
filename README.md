## Dataset 

[IAM](https://fki.tic.heia-fr.ch/databases/download-the-iam-handwriting-database)
As dataset is huge, we have uploaded it to google drive. Google Colab will directly read from google drive. 

The IAM Handwriting Database is hierarchically structured into forms (The name of the files correspond to the naming scheme of the LOB Corpus):
Datas:
data/ascii.tgz - Contains summarized meta information in ascii format.
data/formsA-D.tgz data/formsE-H.tgz data/formsI-Z.tgz - Contains form images (example: a01-122.png).
data/lines.tgz - Contains text lines (example: a01/a01-122/a01-122-02.png).
data/sentences.tgz - Contains sentences, one for each line (example: a01/a01-122/a01-122-s01-02.png).
data/words.tgz - Contains words (example: a01/a01-122/a01-122-s01-02.png).
data/xml.tgz - Contains the meta-infornation in XML format (example: a01-122.xml).
   
## Models

Ref: [nanonets](https://nanonets.com/blog/handwritten-character-recognition/)
- Hidden Markov Models(HMM)
- [SVM](https://labelyourdata.com/articles/ai-handwriting-recognition)
- [CNN & RNN](https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5)
- [CNN & seq2seq](https://arxiv.org/abs/2112.13328)
- [LSTM](http://cs231n.stanford.edu/reports/2017/pdfs/810.pdf)
- Multi-dimensional Recurrent Neural Networks 
- Encoder-Decoder and Attention Networks
- Transformer Models
    - [TrOCR](https://utorontomist.medium.com/handwriting-recognition-using-deep-learning-14ec078872b0)
- [CapsNets](https://towardsdatascience.com/https-medium-com-rachelwiles-have-we-solved-the-problem-of-handwriting-recognition-712e279f373b)
    

## IAM dataset related code
- https://keras.io/examples/vision/handwriting_recognition/
- https://github.com/kartikgill/easter2
- https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5

## Notebook
- https://colab.research.google.com/drive/1pHvnla4FJlLKw1mq-_xCkXQsr4byd5ga 



## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── datasets
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── final          <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── docs               <- Code documentation and generated analysis as HTML, PDF, LaTeX, etc.
│   └── images         <- Generated graphics and figures to be used in reporting
|   └── reports        <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
|__ output             <- Temporary Output files
```
## Features
- Commit Message checking via commitlint
- [Local Testing via pre-commit](https://pre-commit.com/)
- Github Integration 
- CI testing via Github actions
- Github CODEOWNERS to automatically add owners to Github PR
- Github pull request remplates for standardizing description

## Requirements:
- [pre-commit](https://pre-commit.com/)
    ```
        pip install pre-commit
    ```
- [commitlint](https://github.com/conventional-changelog/commitlint)
    ```
        npm install -g @commitlint/cli @commitlint/config-conventional
    ```
    for this Nodejs is required. Download and install from here [Nodejs](https://nodejs.org/en/download/)


## Acknowledgments
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
- [pal0064/Sonic](https://github.com/pal0064/Sonic)
