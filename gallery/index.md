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

## Gallery

<div class="photo-gallery">

{% for photo in site.data.gallery %}

  <figure>
    <a href="/assets/images/gallery/{{ photo.file }}">
      <img
        src="/assets/images/gallery/{{ photo.file }}"
        alt="{{ photo.alt_en | default: '' }}"
        loading="lazy">
    </a>

    {% if photo.caption_en %}
      <figcaption>{{ photo.caption_en }}</figcaption>
    {% endif %}
  </figure>

{% endfor %}

</div>

<style>
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.photo-gallery figure {
  margin: 0;
}

.photo-gallery img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.photo-gallery a {
  display: block;
}
</style>