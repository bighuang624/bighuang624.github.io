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

1. We propose a novel Multi-Path paradigm for CZSL with VLMs, which explicitly constructs vision-language alignments for the state, object, and composition. The paradigm is flexible enough to derive new approaches.

2. Based on the paradigm, we implement a model named Troika that effectively aligns the branch-specific prompt representations and decomposed visual features.

3. We further design a Cross-Modal Traction module for Troika that adaptively adjusts the prompt representation depending on the visual content.

4. We conduct extensive experiments on three CZSL benchmark datasets to show that Troika achieves the SOTA performance on both closed-world and open-world settings.

## Generalizing in Multi-Path Paradigm

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-paradigm-comparison.png" /></div>

## Troika: Our Implementation

![](https://kyonhuang.top/files/Troika/Troika-overview.png)

### Instantiations

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-prompt-comparison.png" /></div>

### Cross-Modal Traction

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/Troika/Troika-CMT.png" /></div>

<!-- We propose the **VoP**: Text-**V**ideo C**o**-operative **P**rompt Tuning to simultaneously introduce tunable prompts in both textual and visual encoders. Also, different from existing related efforts that only insert prompt vectors into the input textual sequences, we find that preparing prompts for every layer of both encoders can further close the gap to full fine-tuning. To exploit essential video-specific information, we further design three novel video prompts from different perspectives, which can seamlessly replace conventional visual prompts in VoP. Specifically, 

1. **position-specific** video prompts model the information shared between frames at the same relative position. 
2. Generated **context-specific** video prompts integrate injected contextual message from the frame sequence into the intra-frame modeling. 
3. And **function-specific** video prompts adaptively assist to learn intra- or inter-frame affinities by sensing the transformation of layer functions.

By exploring video-specific prompts, VoP offers a new way to transfer pre-trained foundation models to the downstream video domain. -->

## Experiment Results

Here we report some experimental results to empirically show the effectiveness of our Troika. Please check the paper for the details of the experiment settings and further analysis.

### Main Results

The following results are obtained with a pre-trained CLIP (ViT-L/14). More experimental results can be found in the paper.

![](https://kyonhuang.top/files/Troika/Troika-SOTA.png)

<!-- <div align="middle"><img align="middle" style="max-width: 560px; width: 100%" src="https://kyonhuang.top/files/VoP/VoP-t2v-results.png" /></div> -->

### Qualitative Results

![](https://kyonhuang.top/files/Troika/Troika-qualitative-results.png)

<!-- We represent the retrieval results of four tuning methods: Full, Partial, VoP, and VoP<sup>F+C</sup>.  -->

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