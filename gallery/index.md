---
layout: default
lang: en
title: Gallery
description: "Photographs, videos, and visual archival material related to Swapna Dutta."
categories: [Project pages]
permalink: /gallery/
created: 2026-05-15
---

This section brings together photographs, videos, scanned images, family albums, and other visual materials connected to the life and memory of Swapna Dutta.

Some images document ordinary moments of everyday life, while others preserve important family occasions, travels, relationships, and periods that acquired meaning only in retrospect. Together, these materials form a visual archive that complements the written recollections published elsewhere on this website.

The gallery is intended not merely as a collection of images, but as an attempt to preserve fragments of lived experience across time.

## Media

<div class="photo-gallery">

{% for photo in site.data.gallery %}
  <figure>
    <a href="/assets/images/gallery/{{ photo.file }}">
      <img
        src="/assets/images/gallery/{{ photo.file }}"
        alt="{{ photo.alt_en | default: photo.caption_en | default: '' }}"
        loading="lazy">
    </a>

    {% if photo.caption_en %}
      <div class="photo-caption">{{ photo.caption_en }}</div>
    {% endif %}

    {% if photo.people_en and photo.people_en.size > 0 %}
      <div class="photo-meta">
        👥 {{ photo.people_en | join: ", " }}
      </div>
    {% endif %}

    {% if photo.location_en %}
      <div class="photo-meta">
        📍 {{ photo.location_en }}
      </div>
    {% endif %}

    {% if photo.date %}
      <div class="photo-meta">
        📅 {% if photo.date contains "-" %}{{ photo.date | date: "%-d %B %Y" }}{% else %}{{ photo.date }}{% endif %}
      </div>
    {% endif %}

    {% if photo.camera %}
      <div class="photo-meta">
        📷 Shot on {{ photo.camera }}
      </div>
    {% endif %}

    {% if photo.coordinates %}
      <div class="photo-meta">
        🗺️ <a href="https://www.openstreetmap.org/?mlat={{ photo.coordinates[0] }}&mlon={{ photo.coordinates[1] }}#map=17/{{ photo.coordinates[0] }}/{{ photo.coordinates[1] }}" rel="noopener">View on Map</a>
      </div>
    {% endif %}
  </figure>
{% endfor %}

</div>

<style>
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.photo-gallery figure {
  margin: 0;
  display: flex;
  flex-direction: column;
}

/* Updated container box to dynamically adjust with your main theme tokens */
.photo-gallery a {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  background-color: var(--surface-soft); /* Follows theme variable maps */
  border: 1px solid var(--border);       /* Follows theme variable maps */
  border-radius: 8px;
  overflow: hidden;
}

.photo-gallery img {
  display: block;
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.photo-caption {
  margin-top: 0.5rem;
  font-weight: 600;
  text-align: center;
}

.photo-meta {
  margin-top: 0.25rem;
  font-size: 0.9rem;
  color: var(--muted); /* Adapts automatically for clean reading contrast */
  text-align: center;
}
</style>
