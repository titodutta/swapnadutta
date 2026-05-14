---
layout: default
lang: en
title: Gallery
description: "Photographs, videos, and visual archival material related to Swapna Dutta."
categories: [Project pages]
permalink: /gallery/
created: 2026-05-15
---

# Gallery

This section brings together photographs, videos, scanned images, family albums, and other visual materials connected to the life and memory of Swapna Dutta.

Some images document ordinary moments of everyday life, while others preserve important family occasions, travels, relationships, and periods that acquired meaning only in retrospect. Together, these materials form a visual archive that complements the written recollections published elsewhere on this website.

The gallery is intended not merely as a collection of images, but as an attempt to preserve fragments of lived experience across time.

<div class="gallery-tools">

  <input
    type="search"
    id="gallerySearch"
    placeholder="Search gallery"
    aria-label="Search gallery">

  <select id="gallerySort" aria-label="Sort gallery">

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

## Gallery items

<ul id="galleryList" class="gallery-list">

{% assign gallery_items = site.pages
  | where_exp: "item", "item.url contains '/gallery/'"
  | where_exp: "item", "item.url != '/gallery/'"
  | where_exp: "item", "item.lang != 'bn'" %}

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
