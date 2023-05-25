# Multiversal pictures

The repository for final project at [DL course](https://github.com/oseledets/dl2023) at Skoltech - "Multiversal pictures".

The objective of this research addresses the widespread dissemination of misleading information on the internet, which can have significant and irreparable repercussions. The development of technology capable of detecting fake news is necessary to combat this issue. However, existing approaches have limitations, as they rely only on textual information and lack visual evidence.

To address this problem, we propose a new feature called Multiversal pictures, which is based on multimodal evidence. Our hypothesis proposes that pictures can serve as evidence for fake news detection and improve existing methods. We use a technique called Multiverse, which is introduced by Dementieva D. et al., as our baseline and collect multilingual textual data through Google search and supplement it with images obtained using the same method. We utilize the CLIP model to get embeddings for images which are relevant to text of article and BERT to obtain embeddings for these texts. Then cosine similarities are calculated between text and picture embeddings for different languages. This similarity might serve as a powerful feature to distinguish fake news.

We expected that our approach increases the accuracy of fake news detection compared to existing methods.

## Usage
All the losses are implenented in `utils.py` as separate classes. You can find the execution in `experiments.ipynb`.
