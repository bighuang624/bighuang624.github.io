---
title: "Attributes-Guided and Pure-Visual Attention Alignment for Few-Shot Recognition"
collection: publications
permalink: /publication/attributes-guided-attention-module
excerpt: '![](https://kyonhuang.top/files/AGAM/AGAM-intuition.png) In this paper, we devise an **attributes-guided attention module (AGAM)** to utilize human-annotated attributes and learn more discriminative features for few-shot recognition. This plug-and-play module enables visual contents and corresponding attributes to collectively focus on important channels and regions for support set. And the feature selection is also achieved for query set with only visual information while the attributes are not available. Therefore, representations from both sets are improved in a fine-grained manner. Moreover, an attention alignment mechanism is proposed to distill knowledge from the guidance of attributes to the pure-visual branch for samples without attributes. Extensive experiments and analysis show that our proposed module can significantly improve simple metric-based approaches to achieve state-of-the-art performance on different datasets and settings.'
date: 2021-02-02
venue: 'Proceedings of AAAI 2021'
---

<!-- [paper](https://kyonhuang.top/files/Huang-DSANet.pdf){: .btn .btn--info} 
[poster](https://kyonhuang.top/files/cikm19-DSANet-poster.pdf){: .btn .btn--info}
[slide](https://kyonhuang.top/files/cikm19-DSANet-presentation.pdf){: .btn .btn--info} -->

[arXiv (extended version)](https://arxiv.org/abs/2009.04724){: .btn .btn--info}
[code](https://github.com/bighuang624/AGAM){: .btn .btn--info}

## Abstract

The purpose of few-shot recognition is to recognize novel categories with a limited number of labeled examples in each class. To encourage learning from a supplementary view, recent approaches have introduced auxiliary semantic modalities into effective metric-learning frameworks that aim to learn a feature similarity between training samples (support set) and test samples (query set). However, these approaches only augment the representations of samples with available semantics while ignoring the query set, which loses the potential for the improvement and may lead to a shift between the modalities combination and the pure-visual representation. 

In this paper, we devise an **attributes-guided attention module (AGAM)** to utilize human-annotated attributes and learn more discriminative features. This plug-and-play module enables visual contents and corresponding attributes to collectively focus on important channels and regions for support set. And the feature selection is also achieved for query set with only visual information while the attributes are not available. Therefore, representations from both sets are improved in a fine-grained manner. Moreover, an attention alignment mechanism is proposed to distill knowledge from the guidance of attributes to the pure-visual branch for samples without attributes. Extensive experiments and analysis show that our proposed module can significantly improve simple metric-based approaches to achieve state-of-the-art performance on different datasets and settings.

## Model Overview

![](https://raw.githubusercontent.com/bighuang624/AGAM/master/docs/AGAM-model-structure.png)

<!-- * **Global Temporal Convolution**: First, DSANet applies 1D convolution over all time steps to extract global temporal patterns for univariate time series.
* **Local Temporal Convolution**: Considering that time steps with a shorter relative distance have a larger impact on each other, DSANet uses another 1D convolution with shorter length of filters to model local temporal patterns.
* **Self-attention Module**: To capture the dependencies between different series, a self-attention module inspired by the Transformer ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)) is applied.
* **Autoregressive Component**: To address the drawback that the scale of neural network output is not sensitive to that of input, the final prediction of DSANet is a mixture of the non-linear component and a classical autoregressive model. -->

## Experiment Results

Here we report some experimental results to empirically show the effectiveness of our AGAM. Please check the paper for the details of the experiment settings and further analysis.

### Adapting AGAM into Existing Frameworks

![](https://kyonhuang.top/files/AGAM/adapting-results.png)

### Comparison with State-of-the-Arts

![](https://kyonhuang.top/files/AGAM/sota-CUB.png)

![](https://kyonhuang.top/files/AGAM/sota-SUN.png)

### Visualization Analysis

![](https://kyonhuang.top/files/AGAM/AGAM-Grad-CAM.png)

Gradient-weighted class activation mapping (Grad-CAM) visualization of query samples. Each row is the result of the same query sample, and each column is: (a) Original images. (b) Results of Prototypical Network. (c) Results of AGAM but removing the attention alignment mechanism. (d) Results of the complete AGAM. It is observed that incorporating the complete AGAM helps to attend to more representative local features.

## BibTex

If our paper and codes are helpful for you research, please cite our paper:

<pre>
@inproceedings{Huang2021AGAM,
  author = {Huang, Siteng and Zhang, Min and Kang, Yachen and Wang, Donglin},
  title = {Attributes-Guided and Pure-Visual Attention Alignment for Few-Shot Recognition},
  booktitle = {The 35th AAAI Conference on Artificial Intelligence (AAAI 2021)},
  month = {February},
  year = {2021}
}
</pre>