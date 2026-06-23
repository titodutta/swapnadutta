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
  <div class="gallery-item">
    <div class="photo-container">
      <a href="/assets/images/gallery/{{ photo.file }}">
        <img
          src="/assets/images/gallery/{{ photo.file }}"
          alt="{{ photo.alt_en | default: photo.caption_en | default: '' }}"
          loading="lazy">
      </a>
    </div>

    <div class="gallery-details">
      {%- if photo.caption_en -%}
        <div class="photo-caption">{{ photo.caption_en }}</div>
      {%- endif -%}

      {%- if photo.people_en and photo.people_en.size > 0 -%}
        <div class="photo-meta">
          👥 {% for person_id in photo.people_en %}{% assign person = site.data.people[person_id] %}{% unless forloop.first %}, {% endunless %}{{ person.en }}{% endfor %}
        </div>
      {%- endif -%}

      {%- if photo.location_en and photo.location_en.size > 0 -%}
        <div class="photo-meta">
          📍 {% for location_id in photo.location_en %}{% assign location = site.data.location[location_id] | default: site.data.locations[location_id] %}{% unless forloop.first %}, {% endunless %}{{ location.en }}{% endfor %}
        </div>
      {%- endif -%}

      {%- if photo.date -%}
        <div class="photo-meta">
          📅 {% if photo.date contains "-" %}{{ photo.date | date: "%-d %B %Y" }}{% else %}{{ photo.date }}{% endif %}
        </div>
      {%- endif -%}

      {%- if photo.time -%}
        <div class="photo-meta compact-text">
          🕒 {{ photo.time }} IST
        </div>
      {%- endif -%}

      {%- if photo.camera -%}
        <div class="photo-meta compact-text">
          📷 Shot on {{ photo.camera }}
        </div>
      {%- endif -%}

      {%- if photo.coordinates -%}
        <div class="photo-meta compact-text">
          🌐 <a href="https://www.openstreetmap.org/?mlat={{ photo.coordinates[0] }}&mlon={{ photo.coordinates[1] }}#map=17/{{ photo.coordinates[0] }}/{{ photo.coordinates[1] }}" rel="noopener">Location</a> on OpenStreetMap
        </div>
      {%- endif -%}
    </div>
  </div>
{% endfor %}

</div>

<style>
/* Main clean auto-fit layout area */
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  grid-auto-rows: min-content; /* Keeps the grid rows tightly bound to actual content */
  grid-row-gap: 3.5rem;        /* Generous, clean breathing room between rows */
  grid-column-gap: 2rem;       /* Perfect spacing between columns */
  margin: 2rem 0;
}

/* Base structural blocks */
.gallery-item {
  display: flex;               /* Forces uniform vertical layout column bounds */
  flex-direction: column;
  margin: 0;
  padding: 0;
  background: transparent;
}

.photo-container {
  display: block;
  width: 100%;
}

.photo-container a {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  background-color: var(--surface-soft);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}

.photo-container img {
  display: block;
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

/* Label content adjustments */
.gallery-details {
  display: block;
  padding: 0.75rem 0 0 0;      /* Clean top spacing above layout text strings */
  margin: 0;
}

.photo-caption {
  margin-top: 0.25rem;
  font-weight: 600;
  text-align: center;
  line-height: 1.4;
}

.photo-meta {
  margin-top: 0.35rem;         /* Balanced line gaps for clean scannability */
  font-size: 0.95rem;
  text-align: center;
  line-height: 1.5;
}

/* Explicit 90% size scaling for camera hardware, time, and map elements */
.compact-text {
  font-size: 0.85rem !important; 
  color: var(--muted);
}

.compact-text a {
  color: inherit;
  text-decoration: underline;
}

/* Mobile responsive layout safety block overrides */
@media (max-width: 480px) {
  .photo-gallery {
    grid-template-columns: 1fr;
    grid-row-gap: 3rem;        /* Relaxed list tracking rows for smaller mobile screens */
  }
  .photo-container a {
    height: 280px;             /* Balanced display container framework proportions on mobile views */
  }
}
</style>