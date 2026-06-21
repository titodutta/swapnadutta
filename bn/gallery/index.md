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
        {% when "01" %}{% assign month_name = "জানুয়ারি" %}
        {% when "02" %}{% assign month_name = "ফেব্রুয়ারি" %}
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
    {% endif %}

    {% if photo.people %}
      <div class="photo-meta">
        👥 {% for person_id in photo.people %}{% assign person = site.data.people[person_id] %}{% unless forloop.first %}, {% endunless %}{{ person.bn }}{% endfor %}
      </div>
    {% endif %}

    {% if photo.location %}
      <div class="photo-meta">
        📍 {% for location_id in photo.location %}{% assign location = site.data.locations[location_id] %}{% unless forloop.first %}, {% endunless %}{{ location.bn }}{% endfor %}
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
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.photo-gallery figure {
  margin: 0;
  display: flex;
  flex-direction: column;
}

.photo-gallery a {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  background-color: var(--surface-soft); /* Flips cleanly to dark surface */
  border: 1px solid var(--border);       /* Flips cleanly to dark border */
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
  line-height: 1.4;
}

.photo-meta {
  margin-top: 0.25rem;
  font-size: 0.9rem;
  color: var(--muted); /* Becomes legible silver-grey in dark mode */
  text-align: center;
  line-height: 1.5;    /* Gives breathing room to Bengali script loops */
}
</style>
