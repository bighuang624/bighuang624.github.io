---
title: "VoP: Text-Video Co-operative Prompt Tuning for Cross-Modal Retrieval"
collection: publications
permalink: /publication/text-video-cooperative-prompt-tuning
excerpt: '<div align="middle"><img align="middle" style="max-width: 560px; width: 100%" src="https://kyonhuang.top/files/VoP/VoP-comparison.png" /></div> In this work, we propose the **VoP**: Text-**V**ideo C**o**-operative **P**rompt Tuning for efficient tuning on the text-video retrieval task. The proposed VoP is an end-to-end framework with both video & text prompts introducing, which can be regarded as a powerful baseline with only **0.1%** trainable parameters. Further, based on the spatio-temporal characteristics of videos, we develop three novel video prompt mechanisms to improve the performance with different scales of trainable parameters. The basic idea of the VoP enhancement is to model the frame position, frame context, and layer function with specific trainable prompts, respectively. Extensive experiments show that compared to full finetuning, the enhanced VoP achieves a **1.4%** average R@1 gain across five text-video retrieval benchmarks with **6×** less parameter overhead.'
date: 2023-05-01
venue: 'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2023 (CVPR 2023)'
---

[arXiv](https://arxiv.org/abs/2211.12764){: .btn .btn--info}
[github](https://github.com/bighuang624/VoP){: .btn .btn--info}
[video (Youtube)](https://www.youtube.com/watch?v=ymdkiSSuOmI){: .btn .btn--info}
[poster](https://kyonhuang.top/files/VoP/CVPR23-VoP-poster.pdf){: .btn .btn--info}
[slide](https://kyonhuang.top/files/VoP/CVPR23-VoP-presentation.pdf){: .btn .btn--info}
[ModelScope](https://modelscope.cn/models/damo/cv_vit-b32_retrieval_vop/summary){: .btn .btn--info}

<!-- ![](https://img.shields.io/badge/arXiv-2211.12764-B31B1B?style=flat) -->

## Background

<div align="middle"><img align="middle" style="max-width: 560px; width: 100%" src="https://kyonhuang.top/files/VoP/VoP-comparison.png" /></div>

<!-- In this paper, we introduce prompt tuning to address the challenges that limit the transferability and generalizability. Keeping the backbone frozen and only tuning a few extra parameters prepended to the input, prompt tuning has been widely applied as a flexible and light-weight fine-tuning protocol. Compared to uni-modal applications, text-video cross-modal retrieval requires more parameters to support the dualbranch structure, making it logical to benefit from the parameter-efficient tuning strategy. In addition, different from text descriptions that compose sequential information from words, video-understanding requires summarizing information in both the spatial and temporal dimensions. Therefore, we assume that designing nontrivial video prompts further contributes to prompting both branches for mutual promotion. -->
Many recent studies leverage the pre-trained CLIP for text-video cross-modal retrieval by tuning the backbone with additional heavy modules, which not only brings huge computational burdens with much more parameters, but also leads to the knowledge forgetting from upstream models. In this paper, we continue the vein of prompt tuning to transfer pre-trained CLIP for text-video retrieval with both effectiveness and efficiency. Main contributions are:
<!-- We first devise a simple but competitive baseline VoP, which achieves promising performance with only 0.1% trainable parameters by prompting all layers of both textual and visual encoders. To increase the revenue of VoP, we further explore three video prompts to model different video-specific information. Different combinations of our video prompts can be selected depending on the strictness of the limits on parameter overhead, and achieve at most 1.4% average relative improvement with much fewer trainable parameters compared to full fine-tuning.  -->

1. We propose the VoP as a strong baseline that effectively adapts CLIP to text-video retrieval with only 0.1% trainable parameters.

2. To exploit video-specific information, we further develop three video prompts respectively conditioned on the frame position, frame context, and layer function. To the best of our knowledge, this is the first work that explores video-specific prompts.

3. Extensive experiments on five text-video retrieval benchmarks demonstrate that various combinations of our video prompts effectively enhance VoP, achieving at most 1.4% average relative improvement with much fewer trainable parameters compared to full fine-tuning.

## Model Overview

![](https://kyonhuang.top/files/VoP/VoP-overview.png)

We propose the **VoP**: Text-**V**ideo C**o**-operative **P**rompt Tuning to simultaneously introduce tunable prompts in both textual and visual encoders. Also, different from existing related efforts that only insert prompt vectors into the input textual sequences, we find that preparing prompts for every layer of both encoders can further close the gap to full fine-tuning. To exploit essential video-specific information, we further design three novel video prompts from different perspectives, which can seamlessly replace conventional visual prompts in VoP. Specifically, 

1. **position-specific** video prompts model the information shared between frames at the same relative position. 
2. Generated **context-specific** video prompts integrate injected contextual message from the frame sequence into the intra-frame modeling. 
3. And **function-specific** video prompts adaptively assist to learn intra- or inter-frame affinities by sensing the transformation of layer functions.

By exploring video-specific prompts, VoP offers a new way to transfer pre-trained foundation models to the downstream video domain.

## Experiment Results

Here we report some experimental results to empirically show the effectiveness and efficiency of our VoP series. Please check the paper for the details of the experiment settings and further analysis.

### Main Results

The following results are obtained with a pre-trained CLIP (ViT-B/32). More experimental results can be found in the paper.

*t2v* and *v2t* retrieval results on MSR-VTT-9k dataset:

![](https://kyonhuang.top/files/VoP/VoP-MSRVTT9k-results.png)

*t2v* relative results on all datasets:

<div align="middle"><img align="middle" style="max-width: 560px; width: 100%" src="https://kyonhuang.top/files/VoP/VoP-t2v-results.png" /></div>

### Qualitative Results

![](https://kyonhuang.top/files/VoP/VoP-qualitative-results.png)

<!-- We represent the retrieval results of four tuning methods: Full, Partial, VoP, and VoP<sup>F+C</sup>.  -->

* In the **top left** example, Full and our proposed methods can retrieve the correct video while Partial matches an unrelated one, which shows the inferiority of existing efficient tuning protocols. 
* In the **top right** example, Full fails to recognize a “Japanese” book while parameter-efficient tuning methods succeed by capturing visual clues of Japanese characters and related English words like “Tokyo”, indicating that updating all parameters might be an unsatisfactory strategy as more knowledge from large-scale text-image pre-training is forgotten. 
* In the **bottom left** example, by fine-tuning all parameters with video datasets or designing specialized prompting solutions for videos, Full and VoP<sup>F+C</sup> can understand the whole event represented by sequenced frames. Even if some textual elements like “priest” are not visually present, the methods overcome such minor semantic misalignments and select more relevant candidates from a global view. 
* In the **bottom right** example, understanding the concept of “tail” and capturing the interaction of “playing with”, VoP<sup>F+C</sup> can distinguish the correct video from hard negative candidates while all the other three methods fail.

## BibTex

If you find this work useful in your research, please cite our paper:

<pre>
@inproceedings{Huang2023VoP,
    title={VoP: Text-Video Co-operative Prompt Tuning for Cross-Modal Retrieval},
    author={Siteng Huang and Biao Gong and Yulin Pan and Jianwen Jiang and Yiliang Lv and Yuyuan Li and Donglin Wang},
    booktitle = {Proceedings of the {IEEE/CVF} Conference on Computer Vision and Pattern Recognition 2023},
    month = {June},
    year = {2023}
}
</pre>