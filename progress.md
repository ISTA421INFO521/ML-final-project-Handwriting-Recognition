# Final project progress report
### ISTA421/INFO521

-------

Project: Handwriting Recogniition
Names: 
- Heba Abdelrazzak
- Ani Chitransh
- Ankit Pal 

-------


## Instructions

You report should be a short summary of your project progress. This report is relevant to to us, your instructors, and probably to the rest of the class.

Please use this report as a chance to organize your thoughts about what you are trying to do with your project, and to get feedback on your ideas, and the approaches that you have tried so far.

## Submission

Please commit this file to your GitHub repo (progress.md) AND to D2L.


-------

### GitHub repo usage
_Describe the current structure of your repo, the number of commits, and the steps you have taken to ensure the reproducibility of your code_

https://github.com/ISTA421INFO521/final-project-pal0064 

We used [Sonic](https://github.com/pal0064/Sonic) to create the initial structure. We added the resources related to the project. We added colab notebooks of models to the repo. We used same seeds for reproducibility and kept the data and model in google drive. Currently, number of commits are 14. But, we mostly use Colab notebooks for development so number of commits does not define our progress.

### Summarize your data
_Describe the characteristics of your data, any transformations that you have considered, or potential issues that you have faced (e.g. missing data)_

We are using images of the a handwritten notes. Images are of different size. Images are resized and converted into matrix. Extracting words from these images using bounding boxes(cv2 package). x variable is pixels of the words and y-variable is the final word. 


### Describe your initial analysis strategy
_What was your initial plan?_

To read an image of handwritten text and convert it to text, and then convert it to speech (voice). The project aims to help the visually impaired population.

- First we prepared the correct labels. Mapping each images of the word to the text word.
- Transformed the image (resizing and getting features from image) for the model.
- We used word pixels and labels to train the models (CNN/SVM/other models- LSTM and Deep Learning).
- Converting text to speech using python package. 

### What you have tried so far?
_Describe your current implementation_

We tried applying SVM and CNN models for words to text. We used words as "bounding boxes" (labels) but we do not know how to store these many words( too many to work with).We successfully used a package that transforms text to speech. 

### What worked and what did not
_Describe the challenges that you have faced so far and outline a few take-homes from your experience on this project_


- We faced a problem while training the data with the using SVM model on words that the model does not recognize characters and only works by predicting each word. The problem is that there are uncommon words in the training data and we want to use characters instead as the frequency of each character will be much higher.
- Our next step is to train the SVM model on characters instead of words or sentences. Then we will break down the image we want to read into characters by using bounding boxes around each character.
- The problem with finding bounding boxes for characters is that usually handwriting is messy and some letters may be connected, or if the handwriting is cursive then the letters will all be connected. Our workaround is to focus on only reading neat handwriting (properly spaced characters) where each character is separated.
- Finding words (bounding boxes) from the image is also challenging. There are many strategies to do that.

### What you plan to do next...
_Please define explicit goals for each of the remaining weeks (before the presentation is due)_

- Week 1: Text to audio implementation, Improving accuracy with testing different models to present the problem statment along with all possible solutions. 
- Week 2: Prepare project report.
- Week 3: Work on the presentation along with final code review.

### Author contributions
_Describe the contributions of each of the members to the current version of the project_


Student 1: [Ankit Pal]
- [x] Development of question / hypothesis;
- [x] Data research: search for relevant data to contribute to question;
- [x] Literature review;
- [x] Analysis strategy;
- [x] Analysis code;
- [x] Code review;
- [x] Work planning and organization;
- [x] Improving teamwork and collaboration;
- [x] Testing code and procedures;
- [ ] Writing report.
- [ ] Additional comments:

Student 2: [Ani Chitransh]
- [x] Development of question / hypothesis;
- [x] Data research: search for relevant data to contribute to question;
- [x] Literature review;
- [x] Analysis strategy;
- [x] Analysis code;
- [x] Code review;
- [x] Work planning and organization;
- [x] Improving teamwork and collaboration;
- [x] Testing code and procedures;
- [ ] Writing report.
- [ ] Additional comments:

Student 3: Heba Abdelrazzak
- [x] Development of question / hypothesis;
- [x] Data research: search for relevant data to contribute to question;
- [x] Literature review;
- [x] Analysis strategy;
- [x] Analysis code;
- [x] Code review;
- [x] Work planning and organization;
- [x] Improving teamwork and collaboration;
- [x] Testing code and procedures;
- [ ] Writing report.
- [ ] Additional comments:
