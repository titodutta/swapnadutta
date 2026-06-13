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

## গ্যালারি

<div class="photo-gallery">

{% for photo in site.data.gallery %}

  <figure>
    <a href="/assets/images/gallery/{{ photo.file }}">
      <img
        src="/assets/images/gallery/{{ photo.file }}"
        alt="{{ photo.alt_bn | default: '' }}"
        loading="lazy">
    </a>

{% if photo.caption_bn %}
  <div class="photo-caption">{{ photo.caption_bn }}</div>
{% endif %}

{% assign metadata = "" %}

{% if photo.date %}
  {% assign date_parts = photo.date | split: "-" %}
  {% assign year = date_parts[0] %}
  {% assign month = date_parts[1] %}
  {% assign day = date_parts[2] %}

  {% assign day = day
  | replace: "0", "০"
  | replace: "1", "১"
  | replace: "2", "২"
  | replace: "3", "৩"
  | replace: "4", "৪"
  | replace: "5", "৫"
  | replace: "6", "৬"
  | replace: "7", "৭"
  | replace: "8", "৮"
  | replace: "9", "৯" %}

{% assign year = year
  | replace: "0", "০"
  | replace: "1", "১"
  | replace: "2", "২"
  | replace: "3", "৩"
  | replace: "4", "৪"
  | replace: "5", "৫"
  | replace: "6", "৬"
  | replace: "7", "৭"
  | replace: "8", "৮"
  | replace: "9", "৯" %}

  {% case month %}
    {% when "01" %}{% assign month_name = "জানুয়ারি" %}
    {% when "02" %}{% assign month_name = "ফেব্রুয়ারি" %}
    {% when "03" %}{% assign month_name = "মার্চ" %}
    {% when "04" %}{% assign month_name = "এপ্রিল" %}
    {% when "05" %}{% assign month_name = "মে" %}
    {% when "06" %}{% assign month_name = "জুন" %}
    {% when "07" %}{% assign month_name = "জুলাই" %}
    {% when "08" %}{% assign month_name = "আগস্ট" %}
    {% when "09" %}{% assign month_name = "সেপ্টেম্বর" %}
    {% when "10" %}{% assign month_name = "অক্টোবর" %}
    {% when "11" %}{% assign month_name = "নভেম্বর" %}
    {% when "12" %}{% assign month_name = "ডিসেম্বর" %}
  {% endcase %}

  {% assign metadata = day | append: " " | append: month_name | append: " " | append: year %}
{% endif %}

{% if photo.people_bn.size > 0 %}
  <div class="photo-meta">
    👥 {{ photo.people_bn | join: ", " }}
  </div>
{% endif %}

{% if photo.location_bn %}
  <div class="photo-meta">
    📍 {{ photo.location_bn }}
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