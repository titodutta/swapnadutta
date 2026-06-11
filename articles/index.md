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

    <option value="newest">
      Newest first
    </option>

    <option value="oldest">
      Oldest first
    </option>

    <option value="az">
      Title A–Z
    </option>

    <option value="za">
      Title Z–A
    </option>

  </select>

</div>

## List of articles

<ul id="articleList" class="article-list">

{% assign english_articles = site.pages
  | where_exp: "item", "item.url contains '/articles/'"
  | where_exp: "item", "item.url != '/articles/'"
  | where_exp: "item", "item.lang != 'bn'" %}

{% assign sorted_articles = english_articles | sort: "created" | reverse %}

{% for article in sorted_articles %}

  <li
    class="article-item"
    data-title="{{ article.title | downcase }}"
    data-date="{{ article.created | date: '%Y-%m-%d' }}">

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

    {% if article.created %}
    <small>
      {{ article.created | date: "%-d %B %Y" }}
    </small>
    {% endif %}

  </li>

{% endfor %}

</ul>

<style>
.article-tools {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin:
    2rem
    0;
}

.article-tools input,
.article-tools select {
  padding:
    0.7rem
    0.9rem;

  border: 1px solid #d1d5db;

  border-radius: 12px;

  font-size: 0.95rem;

  background: #ffffff;
}

.article-tools input {
  flex: 1;
  min-width: 220px;
}

.article-list {
  list-style: none;
  padding-left: 0;
}

.article-item {
  border-bottom: 1px solid var(--border);
  padding:
    1.3rem
    0;
}

.article-item h3 {
  margin:
    0
    0
    0.5rem;
}

.article-item h3 a {
  text-decoration: none;
}

.article-item p {
  margin-bottom: 0.6rem;
}

.article-item small {
  color: var(--muted);
}

@media (max-width: 768px) {

  .article-tools {
    flex-direction: column;
  }

  .article-tools input,
  .article-tools select {
    width: 100%;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const searchInput =
    document.getElementById('articleSearch');

  const sortSelect =
    document.getElementById('articleSort');

  const articleList =
    document.getElementById('articleList');

  const articles =
    Array.from(articleList.querySelectorAll('.article-item'));

  function filterArticles() {

    const query =
      searchInput.value.toLowerCase();

    articles.forEach(article => {

      const title =
        article.dataset.title;

      article.style.display =
        title.includes(query)
          ? ''
          : 'none';
    });
  }

  function sortArticles() {

    const value = sortSelect.value;

    const sorted =
      [...articles];

    sorted.sort((a, b) => {

      const titleA =
        a.dataset.title;

      const titleB =
        b.dataset.title;

      const dateA =
        a.dataset.date;

      const dateB =
        b.dataset.date;

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

    sorted.forEach(article => {
      articleList.appendChild(article);
    });
  }

  searchInput.addEventListener(
    'input',
    filterArticles
  );

  sortSelect.addEventListener(
    'change',
    sortArticles
  );
});
</script>
