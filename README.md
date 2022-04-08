# Question Anaswering Based on DistilBert #

Practical NLP project for Question Answering using DistilBERT-based Transformer

This project uses Stanford CS224N 2022 RobustQA track as a starting point (https://github.com/michiyasunaga/robustqa.git)

## Baseline Model - DistilBertQuestionAnswering ##
* Setup environment with ```conda env create -f environment.yml```
* Train a baseline QA system with ```python train.py --do-train --eval-every 2000 --run-name baseline```
* Evaluate the system on test set with ```python train.py --do-eval --sub-file mtl_submission.csv --save-dir save/baseline-01```
* Baseline model dataset:

  | Dataset Type | Dataset Name | N Size |
  | --------------- | --------------- | --------------- |
  | Training Dataset | SQuAD + NewsQA + Natural Questions | 50000 + 50000 + 50000 = 150000 |
  | Validation Dataset for Model Selection | SQuAD + NewsQA + Natural Questions | 10507 + 4212 + 12836 = 27555 |
  | Testing Dataset | DuoRC + RACE + RelationExtraction | 1248 + 419 + 2693 = 4360 |

## Vanilla Fine-tuned Model ##
* Vanilla fine-tuned model starts from the baseline system model above, and fine-tune over out of domain datasets including DuoRC, RACE and RelationExtraction
* Train a vanilla fine-tuned QA system with ```python train.py --do-train --do-vanilla-finetune --eval-every 10  --run-name vanilla-finetune --baseline-model-dir save/baseline-01/checkpoint```
* Evaluate the vanilla fine-tuned QA system on test set with ```python train.py --do-eval --sub-file mtl_submission.csv --save-dir save/vanilla-finetune-01```
* Vanilla fine-tuned model dataset:

  | Dataset Type | Dataset Name | N Size |
  | --------------- | --------------- | --------------- |
  | Training Dataset | DuoRC + RACE + RelationExtraction | 127 + 127 + 127 = 381 |
  | Validation Dataset for Model Selection | DuoRC + RACE + RelationExtraction | 126 + 128 + 128 = 382 |
  | Testing Dataset | DuoRC + RACE + RelationExtraction | 1248 + 419 + 2693 = 4360 |
