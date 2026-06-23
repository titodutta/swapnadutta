---
layout: default
lang: bn
title: গ্যালারি
description: "স্বপ্না দত্তকে ঘিরে আলোকচিত্র, ভিডিও ও দৃশ্যভিত্তিক সংরক্ষণমূলক উপাদান।"
categories: [Project pages]
permalink: /bn/gallery/
created: 2026-05-15
---

এই বিভাগে স্বপ্না দত্তকে ঘিরে থাকা আলোকচিত্র, ভিডিও, স্ক্যান করা ছবি, পারিবারিক অ্যালবাম এবং অন্যান্য দৃশ্যভিত্তিক সংরক্ষণমূলক উপাদান একত্র করা হয়েছে।

কিছু ছবি দৈনন্দিন জীবনের সাধারণ মুহূর্তকে ধারণ করে, আবার কিছু গুরুত্বপূর্ণ পারিবারিক ঘটনা, ভ্রমণ, সম্পর্ক এবং সময়ের সাক্ষ্য বহন করে। এই উপকরণগুলি মিলিয়ে এমন এক দৃশ্যমান সংরক্ষণভাণ্ডার তৈরি হয়েছে, যা এই ওয়েবসাইটের অন্যান্য স্মৃতিচর্চামূলক লেখাগুলির পরিপূরক হিসেবে কাজ করে।

এই গ্যালারির উদ্দেশ্য শুধুমাত্র ছবি সংরক্ষণ নয়, বরং সময়ের ভেতর দিয়ে অতিক্রান্ত জীবনের কিছু টুকরো অভিজ্ঞতাকে ধরে রাখার প্রয়াস।

## ছবিসমূহ

<div class="photo-gallery">

{% for photo in site.data.gallery %}
  <figure class="gallery-item">
    <div class="photo-container">
      <a href="/assets/images/gallery/{{ photo.file }}">
        <img
          src="/assets/images/gallery/{{ photo.file }}"
          alt="{{ photo.alt_bn | default: photo.caption_bn | default: '' }}"
          loading="lazy">
      </a>
    </div>

    <div class="gallery-details">
      {%- if photo.caption_bn -%}
        <div class="photo-caption">{{ photo.caption_bn }}</div>
      {%- endif -%}

      {%- if photo.people_bn and photo.people_bn.size > 0 -%}
        <div class="photo-meta">👥 {{ photo.people_bn | join: ", " }}</div>
      {%- endif -%}

      {%- if photo.location_bn -%}
        <div class="photo-meta">📍 {{ photo.location_bn }}</div>
      {%- endif -%}

      {%- if photo.date -%}
        {%- assign date_parts = photo.date | split: "-" -%}
        {%- assign year = date_parts[0] -%}
        {%- assign month = date_parts[1] -%}
        {%- assign day = date_parts[2] -%}

        {%- assign day = day
          | replace: "0", "০" | replace: "1", "১" | replace: "2", "২" | replace: "3", "৩"
          | replace: "4", "৪" | replace: "5", "৫" | replace: "6", "৬" | replace: "7", "৭"
          | replace: "8", "৮" | replace: "9", "৯" -%}

        {%- assign year = year
          | replace: "0", "০" | replace: "1", "১" | replace: "2", "২" | replace: "3", "৩"
          | replace: "4", "৪" | replace: "5", "৫" | replace: "6", "৬" | replace: "7", "৭"
          | replace: "8", "৮" | replace: "9", "৯" -%}

        {%- case month -%}
          {%- when "01" -%}{% assign month_name = "জানুয়ারি" %}
          {%- when "02" -%}{% assign month_name = "ফেব্রুয়ারি" %}
          {%- when "03" -%}{% assign month_name = "মার্চ" %}
          {%- when "04" -%}{% assign month_name = "এপ্রিল" %}
          {%- when "05" -%}{% assign month_name = "মে" %}
          {%- when "06" -%}{% assign month_name = "জুন" %}
          {%- when "07" -%}{% assign month_name = "জুলাই" %}
          {%- when "08" -%}{% assign month_name = "আগস্ট" %}
          {%- when "09" -%}{% assign month_name = "সেপ্টেম্বর" %}
          {%- when "10" -%}{% assign month_name = "অক্টোবর" %}
          {%- when "11" -%}{% assign month_name = "নভেম্বর" %}
          {%- when "12" -%}{% assign month_name = "ডিসেম্বর" %}
        {%- endcase -%}

        <div class="photo-meta">
          📅 {% if photo.date contains "-" %}{{ day }} {{ month_name }} {{ year }}{% else %}{{ photo.date }}{% endif %}
        </div>
      {%- endif -%}

      {%- if photo.time -%}
        {%- assign bn_time = photo.time 
          | replace: "0", "০" | replace: "1", "১" | replace: "2", "২" | replace: "3", "৩"
          | replace: "4", "৪" | replace: "5", "৫" | replace: "6", "৬" | replace: "7", "৭"
          | replace: "8", "৮" | replace: "9", "৯" -%}
        <div class="photo-meta compact-text">
          🕒 সময়: {{ bn_time }} আইএসটি (IST)
        </div>
      {%- endif -%}

      {%- if photo.camera -%}
        <div class="photo-meta compact-text">
          📷 ডিভাইস: {{ photo.camera }}
        </div>
      {%- endif -%}

      {%- if photo.coordinates -%}
        <div class="photo-meta compact-text">
          🌐 ওপেনস্ট্রিটম্যাপে <a href="https://www.openstreetmap.org/?mlat={{ photo.coordinates[0] }}&mlon={{ photo.coordinates[1] }}#map=17/{{ photo.coordinates[0] }}/{{ photo.coordinates[1] }}" rel="noopener">স্থানটি দেখুন</a>
        </div>
      {%- endif -%}
    </div>
  </figure>
{% endfor %}

</div>

<style>
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  grid-auto-rows: min-content; /* CRITICAL: Snaps row tracks tightly to the content height */
  gap: 2rem;
  margin: 2rem 0;
}

.gallery-item {
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Forces content up and removes huge row gaps */
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

.gallery-details {
  padding: 0.5rem 0;
}

.photo-caption {
  margin-top: 0.5rem;
  font-weight: 600;
  text-align: center;
  line-height: 1.4;
}

.photo-meta {
  margin-top: 0.25rem;
  font-size: 0.95rem;
  text-align: center;
  line-height: 1.5;
}

/* ক্যামেরা এবং ম্যাপের বিষয়ের জন্য নিবিড় ৯০% ফন্ট স্কেলিং */
.compact-text {
  font-size: 0.85rem !important; 
  color: var(--muted);
}

.compact-text a {
  color: inherit;
  text-decoration: underline;
}
</style>