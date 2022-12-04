## Introduction
    Handwriting Recognition is an old ML problem that is still not completely solved because of its complexity. Once properly set up, It can be used to digitize different types of documents like historical texts, patient prescriptions, bank records, etc. In our project, we will be focussing on how we can utilize this technique to help society. We decided to create an application that will help visually impaired people listen to handwritten notes.

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
   
## Used Models
    [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
    [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
    [SVM](https://en.wikipedia.org/wiki/Support_vector_machine)
    [Random Forest](https://en.wikipedia.org/wiki/Random_forest)

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make install-python-packages` or `make download-data-from-google-drive`
├── README.md          <- Introduction of repository
├── docs               <- Presentations
├── notebooks          <- Final report created using Jupyter notebook(Google Colab)
├── requirements.txt   <- Python packages requirement file
├── src                <- Source code
|   |____ python       <- All python related code
          |__ datasets <- datasets specific code
              |__ iam   <- iam dataset related preprocessing and predicton code
          |__ ml            <- ML models related common code e.g. model tuning, testing, visualizing performance (Not specific to the handwriting recognition)
          |__ processing    <- Common processing code
              |__ image     <- image related processing code e.g resize, thresholding, getting bounding box for words 
              |__ audio     <- Audio related processing code e.g. converting text to audio

```
## Features
- Commit Message checking via commitlint
- [Local Testing via pre-commit](https://pre-commit.com/)
- Github Integration 
- CI testing via Github actions
- Github CODEOWNERS to automatically add owners to Github PR
- Github pull request templates for standardizing description

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


## Notebook


## References:

- [nanonets](https://nanonets.com/blog/handwritten-character-recognition/)
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
    

## Acknowledgments
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
- [pal0064/Sonic](https://github.com/pal0064/Sonic)
