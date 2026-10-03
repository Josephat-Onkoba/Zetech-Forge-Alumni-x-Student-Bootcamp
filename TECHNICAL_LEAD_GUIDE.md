# Technical Lead Guide — What to Produce for Your Track

Each track folder needs five files. This explains what goes in each one,
with the exact front matter to use so your pages show up correctly in the
site navigation. Replace `TRACK-SLUG` / `Track Title` with your actual
track, e.g. `cybersecurity` / `Cybersecurity`.

The templates already sitting in your `tracks/<slug>/` folder have this
front matter pre-filled — this guide is the reference for what to write
underneath it.

---

## 1. `index.md` — Track overview

Front matter:
```yaml
---
title: Track Title
nav_order: N
has_children: true
---
```

Content — 2 to 4 paragraphs covering:
- What this track is about and who it's for (what background should a
  participant have?)
- What skills they'll practice or demonstrate
- A short summary of how the competition works for this track (link to
  `rules.md` for the full detail)

---

## 2. `content.md` — Curriculum / pre-event learning content

Front matter:
```yaml
---
title: Content & Curriculum
parent: Track Title
nav_order: 1
---
```

This is the self-study material participants go through *before*
competition day. Structure it as:
- **Learning objectives** — bullet list of what a participant should
  know/be able to do by the end
- **Prerequisite knowledge** — what they should already know coming in
- **Topic breakdown** — organize into modules/sessions, each with a short
  description and estimated time
- **Suggested timeline** — if there's a prep period before the event,
  suggest a pace (e.g. "Week 1: Modules 1-2")

Keep it practical — link out to the actual learning resources in
`resources.md` rather than re-explaining concepts here.

---

## 3. `resources.md` — Curated resources

Front matter:
```yaml
---
title: Curated Resources
parent: Track Title
nav_order: 2
---
```

Curate, don't dump. For each resource, include: title, link, one line on
why it's useful, and whether it's free or paid. Group by category relevant
to your track, e.g.:

| Resource | Type | Free/Paid | Why it's useful |
|---|---|---|---|
| [Example resource](https://example.com) | Reference | Free | One line on why a participant should use this |

Aim for quality over quantity — 5 to 15 well-chosen resources per category
beats 50 generic links.

---

## 4. `rules.md` — Track-specific rules & how to win

Front matter:
```yaml
---
title: Track Rules & How to Compete
parent: Track Title
nav_order: 3
---
```

This is the track's own rulebook. `general-rules.md` already covers team
size, eligibility, and conduct — don't repeat that here. Instead cover
what's specific to your track:

- **Format** — individual deliverable? live demo? submitted repo? CTF-style
  flags?
- **Allowed tools/tech** — any restrictions (e.g. "any language",
  "no pre-built ML models", "no public CVE databases")
- **Submission requirements** — exactly what must be submitted, how, and
  the deadline/time window on the day
- **Judging criteria & weights** — a rubric, e.g.

| Criterion | Weight |
|---|---|
| Functionality / correctness | 40% |
| Code quality / documentation | 20% |
| Creativity / approach | 20% |
| Presentation | 20% |

- **Scoring and tie-breakers**
- **Day-of timeline** specific to your track, if it differs from the
  general schedule

---

## 5. `challenges.md` — The actual challenges

Front matter:
```yaml
---
title: Challenges
parent: Track Title
nav_order: 4
---
```

Design challenges in tiers so teams of different skill levels can engage
(Beginner / Intermediate / Advanced, or sequential stages that unlock). For
**each** challenge include:

- **Title**
- **Scenario / problem statement** — enough context to understand the task
- **Objectives** — what "done" looks like
- **Constraints** — time limit, tech constraints, data provided, etc.
- **Deliverable** — exactly what gets submitted
- **Points value**
- **Challenge-specific judging notes**, if different from the rubric in
  `rules.md`

If your track needs starter files, datasets, or a sandbox environment, put
them in a `tracks/TRACK-SLUG/assets/` subfolder and link to them from here.

---

## Formatting checklist before you open a PR
- [ ] Front matter is present and correct on every page (title, parent,
      nav_order)
- [ ] All links work
- [ ] Tables render correctly
- [ ] You've only edited files inside your own `tracks/<slug>/` folder
