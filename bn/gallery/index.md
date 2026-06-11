---
layout: default
lang: bn
title: গ্যালারি
description: "স্বপ্না দত্তকে ঘিরে আলোকচিত্র, ভিডিও ও দৃশ্যভিত্তিক সংরক্ষণমূলক উপাদান।"
categories: [Project pages]
permalink: /bn/gallery/
created: 2026-05-15
---

এই বিভাগে স্বপ্না দত্তকে ঘিরে থাকা আলোকচিত্র, ভিডিও, স্ক্যান করা ছবি, পারিবারিক অ্যালবাম এবং অন্যান্য দৃশ্যভিত্তিক সংরক্ষণমূলক উপাদান একত্র করা হয়েছে।

কিছু ছবি দৈনন্দিন জীবনের সাধারণ মুহূর্তকে ধারণ করে, আবার কিছু গুরুত্বপূর্ণ পারিবারিক ঘটনা, ভ্রমণ, সম্পর্ক এবং সময়ের সাক্ষ্য বহন করে। এই উপকরণগুলি মিলিয়ে এমন এক দৃশ্যমান সংরক্ষণভাণ্ডার তৈরি হয়েছে, যা এই ওয়েবসাইটের অন্যান্য স্মৃতিচর্চামূলক লেখাগুলির পরিপূরক হিসেবে কাজ করে।

এই গ্যালারির উদ্দেশ্য শুধুমাত্র ছবি সংরক্ষণ নয়, বরং সময়ের ভেতর দিয়ে অতিক্রান্ত জীবনের কিছু টুকরো অভিজ্ঞতাকে ধরে রাখার প্রয়াস।

<div class="gallery-tools">

  <input
    type="search"
    id="gallerySearch"
    placeholder="গ্যালারি খুঁজুন"
    aria-label="গ্যালারি খুঁজুন">

  <select id="gallerySort" aria-label="গ্যালারি সাজান">

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

## গ্যালারির তালিকা

<ul id="galleryList" class="gallery-list">

{% assign gallery_items = site.pages
  | where_exp: "item", "item.url contains '/bn/gallery/'"
  | where_exp: "item", "item.url != '/bn/gallery/'" %}

{% assign sorted_gallery = gallery_items | sort: "created" | reverse %}

{% for item in sorted_gallery %}

<li
  class="gallery-item"
  data-title="{{ item.title | downcase }}"
  data-date="{{ item.created | date: '%Y-%m-%d' }}">

  <h3>
    <a href="{{ item.url | relative_url }}">
      {{ item.title }}
    </a>
  </h3>

  {% if item.description %}
  <p>
    {{ item.description }}
  </p>
  {% endif %}

  {% if item.created %}
  <small>
    {{ item.created | date: "%-d %B %Y" }}
  </small>
  {% endif %}

</li>

{% endfor %}

</ul>

<style>
.gallery-tools {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin: 2rem 0;
}

.gallery-tools input,
.gallery-tools select {
  padding: 0.7rem 0.9rem;
  border: 1px solid #d1d5db;
  border-radius: 12px;
  font-size: 0.95rem;
  background: #ffffff;
}

.gallery-tools input {
  flex: 1;
  min-width: 220px;
}

.gallery-list {
  list-style: none;
  padding-left: 0;
}

.gallery-item {
  border-bottom: 1px solid var(--border);
  padding: 1.3rem 0;
}

.gallery-item h3 {
  margin: 0 0 0.5rem;
}

.gallery-item h3 a {
  text-decoration: none;
}

.gallery-item p {
  margin-bottom: 0.6rem;
}

.gallery-item small {
  color: var(--muted);
}

@media (max-width: 768px) {

  .gallery-tools {
    flex-direction: column;
  }

  .gallery-tools input,
  .gallery-tools select {
    width: 100%;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const searchInput =
    document.getElementById('gallerySearch');

  const sortSelect =
    document.getElementById('gallerySort');

  const galleryList =
    document.getElementById('galleryList');

  const items =
    Array.from(galleryList.querySelectorAll('.gallery-item'));

  function filterGallery() {

    const query =
      searchInput.value.toLowerCase();

    items.forEach(item => {

      const title =
        item.dataset.title;

      item.style.display =
        title.includes(query)
          ? ''
          : 'none';
    });
  }

  function sortGallery() {

    const value = sortSelect.value;

    const sorted = [...items];

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

    sorted.forEach(item => {
      galleryList.appendChild(item);
    });
  }

  searchInput.addEventListener('input', filterGallery);

  sortSelect.addEventListener('change', sortGallery);
});
</script>
