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

<!-- {% include_relative includes/join_us.md %} -->

{% include_relative includes/news.md %}

<style>
.pub-toggle {
  display: inline-flex;
  gap: 8px;
  margin: 8px 0 12px;
}
.pub-toggle-btn {
  border: 1px solid #999;
  background: #fff;
  color: #224b8d;
  padding: 4px 10px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 120ms ease, color 120ms ease, border-color 120ms ease;
}
.pub-toggle-btn.is-active {
  background: #224b8d;
  color: #fff;
  border-color: #224b8d;
}
.pub-toggle-btn:hover {
  background: #224b8d;
  color: #fff;
  border-color: #224b8d;
}
.pub-panel.is-hidden {
  display: none;
}
</style>

# 📝 Publications

<div class="pub-toggle" role="group" aria-label="Publications view">
  <button type="button" class="pub-toggle-btn is-active" data-target="pub-all" aria-pressed="true">Show by All</button>
  <button type="button" class="pub-toggle-btn" data-target="pub-selected" aria-pressed="false">Show by Topic</button>
</div>

<div id="pub-all" class="pub-panel" markdown="1">
{% include_relative includes/pub_short.md %}
</div>

<div id="pub-selected" class="pub-panel is-hidden" markdown="1">
{% include_relative includes/pub.md %}
</div>

<script>
(function () {
  var buttons = document.querySelectorAll(".pub-toggle-btn");
  if (!buttons.length) return;
  var panels = {
    "pub-all": document.getElementById("pub-all"),
    "pub-selected": document.getElementById("pub-selected")
  };
  function activate(targetId) {
    Object.keys(panels).forEach(function (key) {
      if (!panels[key]) return;
      panels[key].classList.toggle("is-hidden", key !== targetId);
    });
    buttons.forEach(function (btn) {
      var isActive = btn.getAttribute("data-target") === targetId;
      btn.classList.toggle("is-active", isActive);
      btn.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  }
  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      activate(btn.getAttribute("data-target"));
    });
  });
})();
</script>

{% include_relative includes/experience.md %}

{% include_relative includes/services.md %}

{% include_relative includes/misc.md %}
