# Contributing as a Technical Lead

Thanks for leading a track! This doc covers the day-to-day workflow. For
*what* to actually write, see
[`TECHNICAL_LEAD_GUIDE.md`](TECHNICAL_LEAD_GUIDE.md).

## Your role
You own one track end-to-end:

```
tracks/<your-track>/{index,content,resources,rules,challenges}.md
```

You decide the curriculum, curate the resources, write the track-specific
rules and judging criteria, and design the challenges. The organizer owns
the general rules (team size, eligibility, code of conduct) in
`general-rules.md` — you don't need to touch that file.

## One-time setup
1. Accept the collaborator invite you received by email/GitHub notification.
2. Clone the repo:
   ```bash
   git clone https://github.com/<org>/<repo>.git
   cd <repo>
   ```
3. Confirm your GitHub username is listed under your track in
   `.github/track-owners.yml` and `.github/CODEOWNERS`. If it's missing, open
   an issue or ping the organizer — the automated check below won't work
   without it.

## Making changes
1. Create a branch off `main`, named after your track:
   ```bash
   git checkout -b track/<your-track>/short-description
   ```
2. Edit only files inside `tracks/<your-track>/`.
3. Commit and push:
   ```bash
   git add tracks/<your-track>/
   git commit -m "Cybersecurity: add web-exploitation challenge tier"
   git push origin track/<your-track>/short-description
   ```
4. Open a pull request into `main`. Fill in the PR template.
5. Two automated things happen:
   - **CODEOWNERS** requests your review (and the organizer's) automatically.
   - **Track Path Guard**, a GitHub Action, checks that you only touched
     your own track folder, and fails the PR check if not.
6. The organizer reviews and merges. Note: GitHub doesn't allow approving
   your own pull request, so even though you're the code owner for your
   track, the organizer (or another admin) still has to approve it — that's
   intentional. It's the quality checkpoint before anything goes live on the
   site.

## Formatting your pages
Every page needs a small front-matter block at the top so the site
navigation picks it up correctly and nests it under the right track.
Templates are already in place in your track folder with this front matter
filled in — just write your content underneath it and don't remove the
front matter block. See `TECHNICAL_LEAD_GUIDE.md` for exactly what's
expected in each file.

## Previewing locally (optional)
```bash
gem install bundler jekyll
bundle exec jekyll serve
```
Or skip this — once your PR is merged, the live site on GitHub Pages
rebuilds automatically within a minute or two.
