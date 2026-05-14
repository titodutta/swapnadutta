---
layout: default
lang: bn
title: প্রবন্ধ
description: "স্বপ্না দত্তকে ঘিরে স্মৃতিচারণ, প্রবন্ধ, আত্মকথন ও সংরক্ষণমূলক লেখা।"
categories: [Project pages]
permalink: /bn/articles/
created: 2026-05-15
---

# প্রবন্ধ

এই বিভাগে স্বপ্না দত্তকে ঘিরে লেখা স্মৃতিচারণ, ব্যক্তিগত অভিজ্ঞতা, আত্মকথনধর্মী রচনা, সংরক্ষণমূলক উপাদান এবং বিভিন্ন প্রতিফলনধর্মী লেখাকে একত্র করা হয়েছে। এখানে প্রকাশিত লেখাগুলির কিছু গভীরভাবে ব্যক্তিগত, আবার কিছু বৃহত্তর মানবিক অভিজ্ঞতা, পরিবার, স্মৃতি, শোক এবং সময়ের প্রবাহকে কেন্দ্র করে নির্মিত।

এই সংকলনের উদ্দেশ্য শুধুমাত্র একটি ব্যক্তিগত স্মৃতিভাণ্ডার তৈরি করা নয়, বরং স্মরণ, সম্পর্ক এবং মানবজীবনের ভঙ্গুরতার অভিজ্ঞতাকে নথিবদ্ধ করাও।

<div class="article-tools">

  <input
    type="search"
    id="articleSearch"
    placeholder="প্রবন্ধ খুঁজুন"
    aria-label="প্রবন্ধ খুঁজুন">

  <select id="articleSort" aria-label="প্রবন্ধ সাজান">

    <option value="newest">
      নতুন থেকে পুরোনো
    </option>

    <option value="oldest">
      পুরোনো থেকে নতুন
    </option>

    <option value="az">
      শিরোনাম: অ-হ
    </option>

    <option value="za">
      শিরোনাম: হ-অ
    </option>

  </select>

</div>

## প্রবন্ধের তালিকা

<ul id="articleList" class="article-list">

{% assign bangla_articles = site.pages
  | where_exp: "item", "item.url contains '/bn/articles/'"
  | where_exp: "item", "item.url != '/bn/articles/'" %}

{% assign sorted_articles = bangla_articles | sort: "created" | reverse %}

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
