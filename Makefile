
.PHONY: install-sys-packages install-python-packages install-python-packages-colab download-data-from-google-drive generate-reports

install-sys-packages:
	sudo apt update && sudo apt install espeak ffmpeg libespeak1

install-python-packages:
	pip install gTTS boto3 scikit-optimize botocore matplotlib numpy opencv_python pandas plotly scikit_learn tabulate easyocr jupyterlab nbconvert

install-python-packages-colab:
	pip install gTTS boto3 scikit-optimize easyocr 

download-data-from-google-drive:
	cp -r /content/drive/MyDrive/iam_dataset /
	rm -rf /words
	mkdir -p /words
	tar xvzf /iam_dataset/words.tgz -C /words
	rm -rf /forms
	mkdir -p /forms
	tar xvzf /iam_dataset/formsA-D.tgz -C /forms
	tar xvzf /iam_dataset/formsE-H.tgz -C /forms
	tar xvzf /iam_dataset/formsI-Z.tgz -C /forms
	rm -rf /words_label
	mkdir -p /words_label
	tar xvzf /iam_dataset/ascii.tgz -C /words_label

generate-reports:
	# install quarto
	quarto convert notebooks/HTR.ipynb
	mv notebooks/HTR.qmd docs/
	python3 -m jupyter nbconvert --to html notebooks/HTR.ipynb
	mv notebooks/HTR.html docs/