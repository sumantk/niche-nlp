# https://github.com/sumantk/nlp-accelerator

from gensim.summarization.summarizer import summarize
text = '''Rice Pudding - Poem by Alan Alexander Milne
... What is the matter with Mary Jane?
... She's crying with all her might and main,
... And she won't eat her dinner - rice pudding again -
... What is the matter with Mary Jane?
... What is the matter with Mary Jane?
... I've promised her dolls and a daisy-chain,
... And a book about animals - all in vain -
... What is the matter with Mary Jane?
... What is the matter with Mary Jane?
... She's perfectly well, and she hasn't a pain;
... But, look at her, now she's beginning again! -
... What is the matter with Mary Jane?
... What is the matter with Mary Jane?
... I've promised her sweets and a ride in the train,
... And I've begged her to stop for a bit and explain -
... What is the matter with Mary Jane?
... What is the matter with Mary Jane?
... She's perfectly well and she hasn't a pain,
... And it's lovely rice pudding for dinner again!
... What is the matter with Mary Jane?'''
print(summarize(text))
