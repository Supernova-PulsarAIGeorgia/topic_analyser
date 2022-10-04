<p align="center">
<img width="200" height="200" src="https://media-exp1.licdn.com/dms/image/C4D0BAQFxBa6W6H46_Q/company-logo_200_200/0/1655455167248?e=2147483647&v=beta&t=9APBEwiZiKz4a9CAZ7-QeS7UE3Ill9e7ZwITaAG0e5o">
</p>

# topic_analyser
Topic analyser is an intent classification model created by Supernova-PulsarAIGeorgia.

The model is trained for topics like "პოლიტიკა და ომი", "სპორტი", "ეკონომიკა", "კოვიდ-19" with 85% of Accuracy.

## Usage
The model is divided into two parts: model training and model inference.

In intent_classification folder you have all necassery files to train a model

In topic_analyser_api, the folder with the name "model" contains neccessary files for model inferenece.

## Installation
to use API you should run docker file

commands:
```sh
sudo docker build -t dockerfile .
```
```sh
sudo docker run -p 8000:8000 dockerfile
```

## Work with us

You are welcomed to contribute to this repository

## License

MIT

