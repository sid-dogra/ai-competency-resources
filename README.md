# How to Gain AI Competency

Beginner resources initially presented at SABI 2026.

[Browse the resources](https://sid-dogra.github.io/ai-competency-resources/)

Repository: [sid-dogra/ai-competency-resources](https://github.com/sid-dogra/ai-competency-resources).

The page contains programming and model-building resources from the talk and selected papers organized around six nontechnical AI curriculum themes.

Two nested, clickable menus reveal the model-building categories and nontechnical competencies. The page uses a plain white background, and paper titles link to journal articles through their DOIs.

## Editing the resource list

- Learning resources: `resources.json`
- Selected papers: `papers.json`
- Layout and styling: `build.py` and `styles.css`

Run `python3 build.py` after updating the resource lists. The resulting `index.html` is the static page served by GitHub Pages.

GitHub Pages serves the repository root on the `main` branch. Push the generated page and styles alongside the resource lists to publish updates.

Update `last_updated` in `resources.json` when revising the resource list. The date appears alongside the author credit at the bottom of the page.

Each paper entry contains `title`, `url`, and `citation`. Optional fields are `description`, `topics`, and `full_text`. Set `complete` to `true` in `papers.json` when the selected paper list is ready for publication.

Paper links point to the publisher, PubMed, or a legitimate full-text source. The site does not host copies of articles.

## Curriculum framework

Dogra S, Recht MP. Artificial Intelligence Integration Into Residency Training: How, What, and When? *Journal of the American College of Radiology*. 2026;23(3):371–374. https://doi.org/10.1016/j.jacr.2025.07.024
