---
title: "Troika: Multi-Path Cross-Modal Traction for Compositional Zero-Shot Learning"
collection: publications
permalink: /publication/Troika
excerpt: '<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-paradigm-comparison.png" /></div> With a particular focus on the universality of the solution, in this work, we propose a novel **Multi-Path paradigm** for VLM-based CZSL models that establishes three identification branches to jointly model the state, object, and composition. The presented **Troika** is an outstanding implementation that aligns the branch-specific prompt representations with decomposed visual features. To calibrate the bias between semantically similar multi-modal representations, we further devise a **Cross-Modal Traction module** into Troika that shifts the prompt representation towards the current visual content. Experiments show that on the closed-world setting, Troika exceeds the current state-of-the-art methods by up to **+7.4%** HM and **+5.7%** AUC. And on the more challenging open-world setting, Troika still surpasses the best CLIP-based method by up to **+3.8%** HM and **+2.7%** AUC.'
date: 2023-03-28
venue: 'arXiv preprint arXiv:2303.15230'
---

[arXiv](https://arxiv.org/abs/2303.15230){: .btn .btn--info}
[github](https://github.com/bighuang624/Troika){: .btn .btn--info}

## Background

Recent compositional zero-shot learning (CZSL) methods adapt pre-trained vision-language models (VLMs) by constructing trainable prompts only for composed state-object pairs. Relying on learning the joint representation of seen compositions, these methods ignore the explicit modeling of the state and object, thus limiting the exploitation of pre-trained knowledge and generalization to unseen compositions. In this paper, our contributions are:

1. We propose a novel **Multi-Path** paradigm for CZSL with VLMs, which explicitly constructs vision-language alignments for the state, object, and composition. The paradigm is flexible enough to derive new approaches.

2. Based on the paradigm, we implement a model named **Troika** that effectively aligns the branch-specific prompt representations and decomposed visual features.

3. We further design a **Cross-Modal Traction** module for Troika that adaptively adjusts the prompt representation depending on the visual content.

4. We conduct extensive experiments on three CZSL benchmark datasets to show that Troika achieves the SOTA performance on both closed-world and open-world settings.

## Generalizing in Multi-Path Paradigm

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-paradigm-comparison.png" /></div>

Crucially, our proposed Multi-Path paradigm requires a recognition branch for each of the three semantic components, *i.e.*, state, object, and composition. These branches are essentially cross-modal alignments that independently unearth specific knowledge from large-scale vision-language pre-training. Specifically, during training, three branches can collectively optimize the parameters in a multi-task learning manner. And for inference, the prediction results of state and object can be incorporated to assist the composition branch, thereby mitigating the excessive bias towards seen compositions. Without further implementation constraints, the flexibility of the \MP paradigm allows for the derivation of new methods, which can freely exploit various multi-modal features extracted by the powerful VLMs.

## Troika: Our Implementation

![](https://kyonhuang.top/files/Troika/Troika-overview.png)

### Instantiations

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-prompt-comparison.png" /></div>

**Learning Prompt Representations.** As the semantic roles of the target classes on each branch are different, it is natural to introduce different priors through special contexts. Therefore, while maintaining the same primitive vocabulary as a cue of semantic compositionality, we employ an independent prompt prefix for each branch of Troika. The constructed fully trainable prompts are then fed into the text encoder to obtain the prompt representation for each branch.

**Learning Visual Representations.** While existing methods directly apply the frozen image encoder, we first introduce Adapter to adapt the image encoder without updating its original parameters. Then, to establish cross-modal alignment on each branch, specific visual features for the composition, state, and object should be extracted. Still treating the image representation as the composition visual representation, we introduce the state disentangler and object disentangler, implemented with two individual MLPs, to decompose the state and object visual features.

**Training.** In each branch, the cross-entropy loss encourages the model to explicitly recognize the corresponding semantic role. And weighting coefficients balance the influences of different losses in the overall training loss.

**Inference.** During inference, the primitive predictions are combined to complement the composition prediction, thus promoting a more robust recognition system.

### Cross-Modal Traction

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-CMT.png" /></div>

Although inheriting the rich cross-modal understanding of VLMs, discrepancies may still exist between semantically similar vision-language representations. Given the same semantic concept, the static and monotonous prompt representation naturally fails to be commonly optimal for all input images that come from a plentiful distribution. This issue becomes more serious in the additional state and object branches, as the visual content of the same primitive changes considerably when paired with different primitives. Therefore, we further develop a Cross-Modal Traction module for Troika. The module adaptively shifts the prompt representation to accommodate the content diversity and diminish the cross-modal discrepancies. In this process, relevant patch features serve as the guidance to avoid noise from semantic-agnostic sub-regions interfering with the traction.

## Experiment Results

Here we report some experimental results to empirically show the effectiveness of our Troika. Please check the paper for the details of the experiment settings and further analysis.

### Main Results

![](https://kyonhuang.top/files/Troika/Troika-SOTA.png)

The above results are obtained with a pre-trained CLIP (ViT-L/14). More experimental results can be found in the paper.

### Qualitative Results

![](https://kyonhuang.top/files/Troika/Troika-qualitative-results.png)


We report the predictions of the complete Troika and the models that remove the Multi-Path paradigm or the Cross-Modal Traction module. Benefiting from both two innovations, Troika recognizes the compositions with higher accuracy. Taking the 5th case in the top row as an example, while the incomplete methods may be confused by the color and material presented by the object, the complete Troika can focus on details such as shape, surface texture, and even local regions containing lens for comprehensive reasoning.

We also show some failure cases, where the entanglement of visual features places extreme demands on combinatorial understanding. However, the proposed Multi-Path paradigm enables the complete Troika to correctly identify part of the contained primitives. For the cases of complete prediction errors, although different from the provided labels, we find that the predictions can also interpret the content of these images. This indicates the effectiveness of our Troika from another perspective beyond the metrics.

## BibTex

If you find this work useful in your research, please cite our paper:

<pre>
@article{Huang2023Troika,
    title={Troika: Multi-Path Cross-Modal Traction for Compositional Zero-Shot Learning},
    author={Siteng Huang and Biao Gong and Yutong Feng and Yiliang Lv and Donglin Wang},
    journal={arXiv preprint arXiv:2303.15230},
    year={2023}
}
</pre>