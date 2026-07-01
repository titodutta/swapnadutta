---
layout: default
lang: bn
title: নিবন্ধ
description: "স্বপ্না দত্তকে ঘিরে স্মৃতিচারণ, প্রবন্ধ, আত্মকথন ও সংরক্ষণমূলক লেখা।"
categories: [Project pages]
permalink: /bn/articles/
created: 2026-05-15
---

এই বিভাগে স্বপ্না দত্তকে ঘিরে লেখা স্মৃতিচারণ, ব্যক্তিগত অভিজ্ঞতা, আত্মকথনধর্মী রচনা, সংরক্ষণমূলক উপাদান এবং বিভিন্ন প্রতিফলনধর্মী লেখাকে একত্র করা হয়েছে। এখানে প্রকাশিত লেখাগুলির কিছু গভীরভাবে ব্যক্তিগত, আবার কিছু বৃহত্তর মানবিক অভিজ্ঞতা, পরিবার, স্মৃতি, শোক এবং সময়ের প্রবাহকে কেন্দ্র করে নির্মিত।

এই সংকলনের উদ্দেশ্য শুধুমাত্র একটি ব্যক্তিগত স্মৃতিভাণ্ডার তৈরি করা নয়, বরং স্মরণ, সম্পর্ক এবং মানবজীবনের ভঙ্গুরতার অভিজ্ঞতাকে নথিবদ্ধ করাও।

<div class="article-tools">

  <input
    type="search"
    id="articleSearch"
    placeholder="নিবন্ধ খুঁজুন"
    aria-label="নিবন্ধ খুঁজুন">

  <select id="articleSort" aria-label="নিবন্ধ সাজান">

    <option value="oldest">
      পুরোনো থেকে নতুন (ডিফল্ট)
    </option>

    <option value="newest">
      নতুন থেকে পুরোনো
    </option>

    <option value="az">
      শিরোনাম: অ-হ
    </option>

    <option value="za">
      শিরোনাম: হ-অ
    </option>

    <option value="random">
      যাদৃচ্ছিক মোড (Random Mode)
    </option>

  </select>

</div>

## প্রবন্ধের তালিকা

<ul id="articleList" class="article-list">

{% assign bangla_articles = site.pages
  | where_exp: "item", "item.url contains '/bn/articles/'"
  | where_exp: "item", "item.url != '/bn/articles/'" %}

{% assign sorted_articles = bangla_articles | sort: "originally_created" %}

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
      রচনার তারিখ: {{ article.originally_created | date: "%-d %B %Y" }}
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
