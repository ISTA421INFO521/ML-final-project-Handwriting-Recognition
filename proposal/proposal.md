# Title 
Bulletin: Handwriting To Speech 

# Names
Heba Abdelrazzak, Ani Chitransh, Ankit Pal

# Brief Description
## Background:

Handwriting Recognition is an old ML problem that is still not completely solved because of its complexity. Once properly set up, It can be used to digitize different types of documents like historical texts, patient prescriptions, bank records, etc. In our project, we will be focussing on how we can utilize this technique to help society. We decided to create an application that will help visually impaired people listen to handwritten notes.  


## Why It is Important?

Visually impaired people are dependent on other people to help them read handwritten notes. We want to make this task easier by providing an accessible application that would take an image of a handwritten note and convert it to lifelike speech. This will make it so the task can be done independently. Currently, there's no good free-to-use application that converts handwritten notes to audio. This project has a great social impact and can help many people struggling with accessibility.

## Knowledge Gap(What we know/What we don't Know):
- The main problem we are faced with when creating this application, is ensuring that our training dataset includes all the different handwriting styles, especially cursive handwriting. 
- For this project, we will only be considering simple English text and excluding scientific and mathematical texts to avoid further complicating the model. 
- We may also have to deal with typos and human errors in the handwritten text which we will need to deal with.
- Another challenge we face is that not all images will be clear and taken from a good angle, especially if the user has trouble with vision. Surrounding environment changes will also pose challenges.
- An issue with converting handwritten text to speech is we want to avoid having a robotic voice relay the text, having the voice sound more human-like will be a big challenge.


# Brief description of data required and How would you get such data

We will use images of the handwritten notes as a dataset. We will train our models using multiple datasets to achieve better accuracy. Datasets are listed below:

* https://paperswithcode.com/dataset/iam
* https://paperswithcode.com/dataset/rimes
* https://zenodo.org/record/835489#.YzYv8OzMKrc
* https://cvl.tuwien.ac.at/research/cvl-databases/an-off-line-database-for-writer-retrieval-writer-identification-and-word-spotting/
* https://paperswithcode.com/dataset/brush
* https://www.nist.gov/itl/products-and-services/emnist-dataset
* http://yann.lecun.com/exdb/mnist/

# A list of questions and corresponding analysis tasks you plan to do
1. Which kind of dataset to use to train the model, we could use images of text (words) or characters. We will analyze if we can utilize both.
2. Which model would work best to understand handwritten notes? - We will test different models and see the accuracy of each one.
3. Which TTS model would work best to convert text to lifelike speech? -  We will try to have audio output having a different types of voices(based on emotions or gender).


# References
* https://nanonets.com/blog/handwritten-character-recognition/#challenges-in-handwriting-recognition
* https://arxiv.org/abs/2103.06450
* http://cs231n.stanford.edu/reports/2017/pdfs/810.pdf
* https://www.researchgate.net/publication/325993975_Handwriting_Recognition_of_Historical_Documents_with_Few_Labeled_Data
* https://faculty.eng.ufl.edu/computing-for-life/research/handwriting-recognition/
* https://github.com/0x454447415244/HandwritingRecognitionSystem
* https://medium.com/swlh/learn-and-use-handwritten-line-text-recognition-using-deep-learning-with-tensorflow-b661434b5e3b
* https://riunet.upv.es/bitstream/handle/10251/138465/Pastor%3BCastro-Bleda%3BEspa%C3%B1a%20-%20Handwriting%20recognition%20by%20using%20deep%20learning%20to%20extract%20meaningful....pdf?sequence=7
* https://www.kaggle.com/datasets/constantinwerner/cyrillic-handwriting-dataset 
* https://datacommons.anu.edu.au/DataCommons/item/anudc:6091 
* https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research#Handwriting_and_character_recognition
* https://www.kaggle.com/datasets/landlord/handwriting-recognition 
* https://www.kaggle.com/datasets/vaibhao/handwritten-characters
* https://www.kaggle.com/datasets/fournierp/captcha-version-2-images


