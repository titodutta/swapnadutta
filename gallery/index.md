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
  <div class="photo-caption">{{ photo.caption_en }}</div>
{% endif %}

{% assign metadata = "" %}

{% if photo.date %}
  {% assign date_parts = photo.date | split: "-" %}
  {% assign year = date_parts[0] %}
  {% assign month = date_parts[1] %}
  {% assign day = date_parts[2] %}

  {% case month %}
    {% when "01" %}{% assign month_name = "January" %}
    {% when "02" %}{% assign month_name = "February" %}
    {% when "03" %}{% assign month_name = "March" %}
    {% when "04" %}{% assign month_name = "April" %}
    {% when "05" %}{% assign month_name = "May" %}
    {% when "06" %}{% assign month_name = "June" %}
    {% when "07" %}{% assign month_name = "July" %}
    {% when "08" %}{% assign month_name = "August" %}
    {% when "09" %}{% assign month_name = "September" %}
    {% when "10" %}{% assign month_name = "October" %}
    {% when "11" %}{% assign month_name = "November" %}
    {% when "12" %}{% assign month_name = "December" %}
  {% endcase %}

  {% assign metadata = day | append: " " | append: month_name | append: " " | append: year %}
{% endif %}

{% if photo.people %}
  <div class="photo-meta">
    👥 {% for person_id in photo.people %}{% assign person = site.data.people[person_id] %}{% unless forloop.first %}, {% endunless %}{{ person.en }}{% endfor %}
  </div>
{% endif %}

{% if photo.location %}
  <div class="photo-meta">
    📍 {% for location_id in photo.location %}{% assign location = site.data.locations[location_id] %}{% unless forloop.first %}, {% endunless %}{{ location.en }}{% endfor %}
  </div>
{% endif %}

{% if photo.date %}
  <div class="photo-meta">
    📅 {{ day }} {{ month_name }} {{ year }}
  </div>
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
.photo-caption {
  margin-top: 0.5rem;
  font-weight: 600;
  text-align: center;
}

.photo-meta {
  margin-top: 0.25rem;
  font-size: 0.9rem;
  color: #444;
  text-align: center;
}
</style>