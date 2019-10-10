---
title: "DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting"
collection: publications
permalink: /publication/dual-self-attention-network
excerpt: 'In this paper, we propose a dual self-attention network (DSANet) for highly efficient multivariate time series forecasting.'
date: 2019-11-03
venue: 'Proceedings of CIKM 2019 (Short Paper)'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
citation: 'Siteng Huang, Donglin Wang, Xuehan Wu, Ao Tang. &quot;DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting&quot;. CIKM 2019.'
---

![](https://raw.githubusercontent.com/bighuang624/DSANet/master/docs/DSANet-model-structure.png)

In this paper, we propose a **dual self-attention network (DSANet)** for highly efficient multivariate time series forecasting, especially for dynamic-period or nonperiodic series. DSANet completely dispenses with recurrence and utilizes two parallel convolutional components, called global temporal convolution and local temporal convolution, to capture complex mixtures of global and local temporal patterns. Moreover, DSANet employs a self-attention module to model dependencies between multiple series. To further improve the robustness, DSANet also integrates a traditional autoregressive linear model in parallel to the non-linear neural network. Experiments on real-world multivariate time series data show that the proposed model is effective and outperforms baselines.

Code: [bighuang624/DSANet](https://github.com/bighuang624/DSANet)

<!-- [Download paper here](http://academicpages.github.io/files/paper1.pdf)

Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->