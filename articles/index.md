---
layout: default
lang: en
title: Articles
description: "Articles, reflections, memoirs, and archival writings related to Swapna Dutta."
categories: [Project pages]
permalink: /articles/
created: 2026-05-15
---

This section brings together articles, reflections, memoirs, recollections, and other writings connected to the life and memory of Swapna Dutta. The collection includes personal narratives, archival material, translated texts, and essays written across different periods.

Some writings are intimate and autobiographical in nature, while others attempt to place individual experiences within wider emotional, social, and historical contexts. Together, these articles form an evolving archive of remembrance.

<div class="article-tools">

  <input
    type="search"
    id="articleSearch"
    placeholder="Search articles"
    aria-label="Search articles">

  <select id="articleSort" aria-label="Sort articles">

    <option value="oldest">
      Oldest first (Default)
    </option>

    <option value="newest">
      Newest first
    </option>

    <option value="az">
      Title A–Z
    </option>

    <option value="za">
      Title Z–A
    </option>

    <option value="random">
      Random Mode
    </option>

  </select>

</div>

## List of articles

<ul id="articleList" class="article-list">

{% assign english_articles = site.pages
  | where_exp: "item", "item.url contains '/articles/'"
  | where_exp: "item", "item.url != '/articles/'"
  | where_exp: "item", "item.lang != 'bn'" %}

{% assign sorted_articles = english_articles | sort: "originally_created" %}

{% for article in sorted_articles %}

  <li
    class="article-item"
    data-title="{{ article.title | downcase }}"
    data-date="{{ article.originally_created | date: '%Y-%m-%d' }}">

    <h3>
      <a href="{{ article.url | relative_url }}">
        {{ article.title }}
      </a>
    </h3>

    {% if article.description %}
    <p>
      {{ article.description }}
    </p>
    {% endif %}

    {% if article.originally_created %}
    <small>
      Written on: {{ article.originally_created | date: "%-d %B %Y" }}
    </small>
    {% endif %}

  </li>

{% endfor %}

</ul>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const searchInput = document.getElementById('articleSearch');
  const sortSelect = document.getElementById('articleSort');
  const articleList = document.getElementById('articleList');
  const articles = Array.from(articleList.querySelectorAll('.article-item'));

  function filterArticles() {
    const query = searchInput.value.toLowerCase();
    articles.forEach(article => {
      const title = article.dataset.title;
      article.style.display = title.includes(query) ? '' : 'none';
    });
  }

  function sortArticles() {
    const value = sortSelect.value;
    const sorted = [...articles];

    if (value === 'random') {
      // Fisher-Yates Shuffle array variant for unbiased random calculation
      for (let i = sorted.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [sorted[i], sorted[j]] = [sorted[j], sorted[i]];
      }
    } else {
      sorted.sort((a, b) => {
        const titleA = a.dataset.title;
        const titleB = b.dataset.title;
        const dateA = a.dataset.date;
        const dateB = b.dataset.date;

        if (value === 'newest') {
          return dateB.localeCompare(dateA);
        }
        if (value === 'oldest') {
          return dateA.localeCompare(dateB);
        }
        if (value === 'az') {
          return titleA.localeCompare(titleB);
        }
        if (value === 'za') {
          return titleB.localeCompare(titleA);
        }
        return 0;
      });
    }

    sorted.forEach(article => {
      articleList.appendChild(article);
    });
  }

  searchInput.addEventListener('input', filterArticles);
  sortSelect.addEventListener('change', sortArticles);
});
</script>

<style>
  :root {
    --tool-bg: #f9f9f9;
    --tool-text: #222222;
    --tool-border: #dddddd;
  }

  /* This block handles the dark mode overrides perfectly */
  @media (prefers-color-scheme: dark) {
    :root {
      --tool-bg: #1e1e1e;
      --tool-text: #e0e0e0;
      --tool-border: #444444;
    }
    
    /* Explicitly forcing the browser to override default input/select backgrounds */
    .article-tools input,
    .article-tools select {
      background-color: var(--tool-bg) !important;
      color: var(--tool-text) !important;
      border-color: var(--tool-border) !important;
    }
  }

  .article-tools {
    display: flex;
    gap: 12px;
    margin: 20px 0;
    flex-wrap: wrap;
  }

  .article-tools input,
  .article-tools select {
    background-color: var(--tool-bg);
    color: var(--tool-text);
    border: 1px solid var(--tool-border);
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 14px;
    outline: none;
  }

  .article-tools input {
    flex: 1;
    min-width: 200px;
  }
</style>
