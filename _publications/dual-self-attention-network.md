---
title: "DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting"
collection: publications
permalink: /publication/dual-self-attention-network
excerpt: 'In this paper, we propose a dual self-attention network (DSANet) for highly efficient multivariate time series forecasting, especially for dynamic-period or nonperiodic series. '
date: 2019-11-03
venue: 'Proceedings of CIKM 2019 (Short Paper, Oral)'
---

[paper](https://kyonhuang.top/files/Huang-DSANet.pdf){: .btn .btn--info} 
[code](https://github.com/bighuang624/DSANet){: .btn .btn--info}

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/DSANet-model-structure.png)

In this paper, we propose a **dual self-attention network (DSANet)** for highly efficient multivariate time series forecasting, especially for dynamic-period or nonperiodic series. DSANet completely dispenses with recurrence and utilizes two parallel convolutional components, called global temporal convolution and local temporal convolution, to capture complex mixtures of global and local temporal patterns. Moreover, DSANet employs a self-attention module to model dependencies between multiple series. To further improve the robustness, DSANet also integrates a traditional autoregressive linear model in parallel to the non-linear neural network. Experiments on real-world multivariate time series data show that the proposed model is effective and outperforms baselines.

## BibTex

If our paper and codes are helpful for you research, please cite our paper:

<pre>
@inproceedings{Huang2019DSANet,
  author = {Huang, Siteng and Wang, Donglin and Wu, Xuehan and Tang, Ao},
  title = {DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting},
  booktitle = {The 28th ACM International Conference on Information and Knowledge Management (CIKM ’19)},
  month = {November},
  year = {2019},
  address = {Beijing, China}
}
</pre>
