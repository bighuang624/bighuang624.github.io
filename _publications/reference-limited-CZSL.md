---
title: "Reference-Limited Compositional Zero-Shot Learning"
collection: publications
permalink: /publication/reference-limited-CZSL
excerpt: '<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/RLCZSL/RLCZSL-setting-comparison.png" /></div> While considerable progress has been made on existing benchmarks, we suspect whether popular compositional zero-shot learning (CZSL) methods can address the challenges of few-shot and few referential compositions, which is common when learning in real-world unseen environments. To this end, we study the challenging **reference-limited compositional zero-shot learning (RL-CZSL)** problem in this paper, *i.e.*, given limited seen compositions that contain only a few samples as reference, unseen compositions of observed primitives should be identified. We propose a novel **Meta Compositional Graph Learner (MetaCGL)** that can efficiently learn the compositionality from insufficient referential information and generalize to unseen compositions. Besides, we build **a benchmark with two new large-scale datasets** that consist of natural images with diverse compositional labels, providing more realistic environments for RL-CZSL. Extensive experiments in the benchmarks show that our method achieves state-of-the-art performance in recognizing unseen compositions when reference is limited for compositional learning.'
date: 2023-02-28
venue: 'Proceedings of the 2023 ACM International Conference on Multimedia Retrieval (ICMR 2023)'
---

[arXiv](https://arxiv.org/abs/2208.10046){: .btn .btn--info}
[github](https://github.com/bighuang624/RL-CZSL){: .btn .btn--info}
[video (Google Drive)](https://drive.google.com/file/d/1_wE_zbyvuGil_LrkmumotkRTLJJEUfCm/view?usp=drive_link){: .btn .btn--info}
[slide](https://kyonhuang.top/files/RLCZSL/ICMR23-RLCZSL-presentation.pdf){: .btn .btn--info}

## Introduction

Compositional zero-shot learning (CZSL) refers to recognizing unseen compositions of known visual primitives, which is an essential ability for artificial intelligence systems to learn and understand the world. While considerable progress has been made on existing benchmarks, we suspect whether popular CZSL methods can address the challenges of few-shot and few referential compositions, which is common when learning in real-world unseen environments. In this paper, our contributions are:

* We introduce a new problem named **reference-limited compositional zero-shot learning (RL-CZSL)**, where given only a few samples of limited compositions, the model is required to generalize to recognize unseen compositions. This offers a more realistic and challenging environment for evaluating compositional learners.

<div align="middle"><img align="middle" style="max-width: 520px; width: 100%" src="https://kyonhuang.top/files/RLCZSL/RLCZSL-setting-comparison.png" /></div>

* We establish **two benchmark datasets with diverse compositional labels and well-designed data splits**, providing the required platform for systematically assessing progress on the task.

<div align="middle"><img align="middle" style="max-width: 540px; width: 100%" src="https://kyonhuang.top/files/RLCZSL/RLCZSL-dataset-stats.png" /></div>

* We propose a novel method, **Meta Compositional Graph Learner (MetaCGL)**, for the challenging RL-CZSL problem. Experimental results show that MetaCGL consistently outperforms popular baselines on recognizing unseen compositions. 

<div align="middle"><img align="middle" style="max-width: 540px; width: 100%" src="https://kyonhuang.top/files/RLCZSL/RLCZSL-main-results.png" /></div>

## BibTex

If you find this work useful in your research, please cite our paper:

<pre>
@inproceedings{Huang2023RLCZSL,
    title={Reference-Limited Compositional Zero-Shot Learning},
    author={Siteng Huang and Qiyao Wei and Donglin Wang},
    booktitle = {Proceedings of the 2023 ACM International Conference on Multimedia Retrieval},
    month = {June},
    year = {2023}
}
</pre>


