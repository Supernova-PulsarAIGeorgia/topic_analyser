from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer
import logging
import pickle
import torch

logging.basicConfig(level=logging.INFO)

max_length = 128 
class Classification:
    def __init__(self,model_path) -> None:
        logging.info('Loading model.')
        self.model = XLMRobertaForSequenceClassification.from_pretrained(model_path)
        logging.info('Model loaded.')

        logging.info('Loading tokenizer.')
        self.tokenizer = XLMRobertaTokenizer.from_pretrained(model_path)
        logging.info('Tokenizer loaded.')


    
    def classify(self,sentences):
        with open(f'model/classLabel.pickle', 'rb') as handle:
            classLabel = pickle.load(handle)
        output = []
        for word in sentences:
            tokenized = self.tokenizer([word], padding='max_length', truncation=True, max_length=max_length)
            input_ids = torch.LongTensor(tokenized['input_ids'])
            attention_mask = torch.FloatTensor(tokenized['attention_mask'])

            label_idx = self.model.forward(input_ids, attention_mask).logits.argmax()

            label = classLabel.int2str([label_idx])
            output.append(label)
        return output
