# [Bootcamp Name] — Tracks Repo

Source repo for the [Bootcamp Name] competition site, published via GitHub
Pages at: `https://<org>.github.io/<repo>/` (update this link once Pages is
enabled in Settings).

## What's in here
- `general-rules.md` — organizer-owned general competition rules (team size,
  eligibility, conduct — applies to every track).
- `tracks/` — one folder per track, each owned by a Technical Lead:
  - Software Development
  - Web3 & Blockchain
  - IoT & Robotics
  - Machine Learning & Data Science
  - Cybersecurity
- `_config.yml` — site config (Jekyll + Just the Docs theme), used to render
  this repo as a navigable site via GitHub Pages.
- `.github/` — CODEOWNERS, PR/issue templates, and the automated check that
  keeps each Technical Lead inside their own track folder.

## Roles
- **Organizer** — owns `general-rules.md`, `_config.yml`, and does final
  review/merge on every pull request.
- **Technical Leads** — each owns one `tracks/<slug>/` folder end-to-end:
  curriculum, curated resources, track-specific rules, and challenges.

## For Technical Leads
Start with [`TECHNICAL_LEAD_GUIDE.md`](TECHNICAL_LEAD_GUIDE.md) for *what* to
write, and [`CONTRIBUTING.md`](CONTRIBUTING.md) for the Git/PR workflow.

## Access control
This repo uses CODEOWNERS + branch protection + an automated "Track Path
Guard" check (`.github/workflows/path-guard.yml`) so each Technical Lead's
pull requests are reviewed by, and restricted to, their own track folder.
Edit `.github/CODEOWNERS` and `.github/track-owners.yml` to assign real
GitHub usernames to each track.
