---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<!-- ref: https://github.com/RayeRen/rayeren.github.io/tree/main/_pages/includes -->

<span class='anchor' id='about-me'></span>

{% include_relative includes/intro.md %}

<!-- {% include_relative includes/research_interests.md %} -->

{% include_relative includes/news.md %}

<!-- {% include_relative includes/pub.md %} -->

{% include_relative includes/pub_short.md %}

{% include_relative includes/work_experience.md %}

{% include_relative includes/services.md %}

{% include_relative includes/misc.md %}