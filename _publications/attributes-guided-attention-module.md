---
title: "Attributes-Guided and Pure-Visual Attention Alignment for Few-Shot Recognition"
collection: publications
permalink: /publication/attributes-guided-attention-module
excerpt: 'In this paper, we devise an **attributes-guided attention module (AGAM)** to utilize human-annotated attributes and learn more discriminative features for few-shot recognition. This plug-and-play module enables visual contents and corresponding attributes to collectively focus on important channels and regions for support set. And the feature selection is also achieved for query set with only visual information while the attributes are not available. Therefore, representations from both sets are improved in a fine-grained manner. Moreover, an attention alignment mechanism is proposed to distill knowledge from the guidance of attributes to the pure-visual branch for samples without attributes. Extensive experiments and analysis show that our proposed module can significantly improve simple metric-based approaches to achieve state-of-the-art performance on different datasets and settings.'
date: 2020-12-03
venue: 'Proceedings of AAAI 2021'
---

<!-- [paper](https://kyonhuang.top/files/Huang-DSANet.pdf){: .btn .btn--info} 
[poster](https://kyonhuang.top/files/cikm19-DSANet-poster.pdf){: .btn .btn--info}
[slide](https://kyonhuang.top/files/cikm19-DSANet-presentation.pdf){: .btn .btn--info} -->

[arXiv (extended version)](https://arxiv.org/abs/2009.04724){: .btn .btn--info}
[code](https://github.com/bighuang624/AGAM){: .btn .btn--info}

## Abstract

The purpose of few-shot recognition is to recognize novel categories with a limited number of labeled examples in each class. To encourage learning from a supplementary view, recent approaches have introduced auxiliary semantic modalities into effective metric-learning frameworks that aim to learn a feature similarity between training samples (support set) and test samples (query set). However, these approaches only augment the representations of samples with available semantics while ignoring the query set, which loses the potential for the improvement and may lead to a shift between the modalities combination and the pure-visual representation. In this paper, we devise an **attributes-guided attention module (AGAM)** to utilize human-annotated attributes and learn more discriminative features. This plug-and-play module enables visual contents and corresponding attributes to collectively focus on important channels and regions for support set. And the feature selection is also achieved for query set with only visual information while the attributes are not available. Therefore, representations from both sets are improved in a fine-grained manner. Moreover, an attention alignment mechanism is proposed to distill knowledge from the guidance of attributes to the pure-visual branch for samples without attributes. Extensive experiments and analysis show that our proposed module can significantly improve simple metric-based approaches to achieve state-of-the-art performance on different datasets and settings.

## Model Overview

![](https://raw.githubusercontent.com/bighuang624/AGAM/master/docs/AGAM-model-structure.png)

<!-- * **Global Temporal Convolution**: First, DSANet applies 1D convolution over all time steps to extract global temporal patterns for univariate time series.
* **Local Temporal Convolution**: Considering that time steps with a shorter relative distance have a larger impact on each other, DSANet uses another 1D convolution with shorter length of filters to model local temporal patterns.
* **Self-attention Module**: To capture the dependencies between different series, a self-attention module inspired by the Transformer ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)) is applied.
* **Autoregressive Component**: To address the drawback that the scale of neural network output is not sensitive to that of input, the final prediction of DSANet is a mixture of the non-linear component and a classical autoregressive model.

## Experiment Results

We conduct our experiments on a large multivariate time series dataset, which contains the daily revenue of geographically close gas stations. Data visualization analysis is performed to ensure that the data set does not contain distinct repetitive patterns. Please check the paper for the details of the experiment settings and further analysis.

### Evaluation Results

Each row in the table compares the results of all methods in a particular metric with a specific window-horizon pair, and each column shows the results of a specific method in all cases. Boldface indicates the best result of each row in a particular metric. 

With *window* = 32:

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/exp_results_window_32.png)

With *window* = 64:

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/exp_results_window_64.png)

With *window* = 128:

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/exp_results_window_128.png)

### Ablation Study

To justify the efficiency of our architecture design, we conduct a careful ablation study. Specifically, we remove each of the components one at a time in our DSANet model:

* **DSAwoGlobal**: Remove the global temporal convolution branch.
* **DSAwoLocal**: Remove the local temporal convolution branch.
* **DSAwoAR**: Remove the autoregressive component.

With *window* = 32:

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/ablation_RRSE.png)

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/ablation_MAE.png)

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/ablation_CORR.png)

**Observations**:

1. The best result on each window-horizon pair is obtained by complete DSANet, showing all components have contributed to the effectiveness and robustness of the whole model. 
2. The performance of DSAwoAR significantly drops, showing that the AR component plays a crucial role. The reason is that AR is generally robust to the scale changing in data according to [Lai et al. (2018)](https://dl.acm.org/citation.cfm?id=3210006). 
3. DSAwoGlobal and DSAwoLocal also suffer from performance loss but less than removing the AR component. This is because features learned by the two branches coincide. In other words, when one branch is removed, some of the lost features can be obtained from the other branch. -->

## BibTex

If our paper and codes are helpful for you research, please cite our paper:

<pre>
@inproceedings{Huang2021AGAM,
  author = {Huang, Siteng and Zhang, Min and Kang, Yachen and Wang, Donglin},
  title = {Attributes-Guided and Pure-Visual Attention Alignment for Few-Shot Recognition},
  booktitle = {The Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI 2021)},
  month = {February},
  year = {2021}
}
</pre>