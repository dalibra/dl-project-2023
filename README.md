# Multiversal pictures

The repository for final project at [DL course](https://github.com/oseledets/dl2023) at Skoltech - "Multiversal pictures".

The objective of this research addresses the widespread dissemination of misleading information on the internet, which can have significant and irreparable repercussions. The development of technology capable of detecting fake news is necessary to combat this issue. However, existing approaches have limitations, as they rely only on textual information and lack visual evidence.

To address this problem, we propose a new feature called Multiversal pictures, which is based on multimodal evidence. Our hypothesis proposes that pictures can serve as evidence for fake news detection and improve existing methods. We use a technique called Multiverse, which is introduced by Dementieva D. et al., as our baseline and collect multilingual textual data through Google search and supplement it with images obtained using the same method. We utilize the CLIP model to get embeddings for images which are relevant to text of article. Cosine similarities between picture embeddings for different languages added as features for classification. This similarity might serve as a powerful feature to distinguish fake news.

We expected that our approach increases the accuracy of fake news detection compared to existing methods.

## Usage
You can find the execution in `.ipynb` files in corresponding folders, for example, experiments for web scarping are in `scraper/web_scarping_experiments.ipynb`.

## Main results
<table>
<thead>
  <tr>
    <th> </th>
    <th>Precision</th>
    <th>Recall</th>
    <th>F1-score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Text features (baseline)</b></td>
    <td><b>0.801</b></td>
    <td><b>0.8</b></td>
    <td><b>0.8</b></td>
  </tr>
</tbody>
<tbody>
  <tr>
    <td><b>Text+Image features</b></td>
    <td><b>0.81</b></td>
    <td><b>0.83</b></td>
    <td><b>0.82</b></td>
  </tr>
</tbody>
</table>


## Conclusion
- Image features allow to increase quality of fake news detection
- Results should be validated on more datasets
- CLIP similarities may be added to the feature set


## Team True NLP Detectives:
- Alexander Kharitonov
- Danil Gusak
- Dmitriy Kornilov
- Alina Bogdanova
