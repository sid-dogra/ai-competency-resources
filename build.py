from pathlib import Path
from html import escape
from datetime import date
import json

ROOT = Path(__file__).resolve().parent
resources = json.loads((ROOT / 'resources.json').read_text())
reading = json.loads((ROOT / 'papers.json').read_text())
updated = date.fromisoformat(resources['last_updated'])
updated_label = f'{updated.strftime("%B")} {updated.day}, {updated.year}'


def e(text):
    return escape(str(text), quote=True)


def link(url, label):
    if not url.startswith('https://'):
        raise ValueError('Resource links must use HTTPS')
    return f'<a href="{e(url)}">{e(label)}</a>'


category_titles = ['General Programming', 'AI/ML', 'Radiology AI']
resource_html = ''
for title, group in zip(category_titles, resources['groups'], strict=True):
    resource_html += f'<details class="category"><summary>{e(title)}</summary><ul class="resource-list">'
    for item in group['resources']:
        resource_html += f'<li>{link(item["url"], item["title"])}<p class="citation">{e(item["detail"])}</p>'
        if item.get('extra'):
            resource_html += f'<p class="additional-link">{link(item["extra"]["url"], item["extra"]["label"])}</p>'
        resource_html += '</li>'
    resource_html += '</ul></details>'

paper_html = ''
paper_count = 0
for theme in reading['themes']:
    paper_html += f'<details class="category" id="{e(theme["id"])}"><summary>{e(theme["title"])}</summary><ul class="paper-list">'
    for paper in theme['papers']:
        paper_count += 1
        paper_html += f'<li>{link(paper["url"], paper["title"])}<p class="citation">{e(paper["citation"])}</p></li>'
    paper_html += '</ul></details>'

html = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Selected resources for developing AI competency: programming, AI and machine learning, radiology AI, and nontechnical competencies.">
  <meta name="theme-color" content="#ffffff">
  <title>How to Gain AI Competency</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#resources">Skip to resources</a>
  <main>
    <header>
      <h1>How to Gain AI Competency</h1>
      <p class="subtitle">Beginner resources initially presented at SABI 2026</p>
    </header>
    <div id="resources">
      <details class="resource-menu" id="build">
        <summary>Building Radiology AI Models</summary>
        <div class="categories">RESOURCES</div>
      </details>
      <details class="resource-menu" id="reading">
        <summary>Nontechnical AI Competencies</summary>
        <div class="categories">PAPERS</div>
        <p class="framework">Curriculum framework: <a href="https://doi.org/10.1016/j.jacr.2025.07.024">Artificial Intelligence Integration Into Residency Training: How, What, and When?</a> Dogra S, Recht MP. <em>JACR.</em> 2026.</p>
      </details>
    </div>
    <footer>Curated by Sid Dogra, MD <span aria-hidden="true">·</span> <span>Last updated <time datetime="UPDATED_ISO">UPDATED_LABEL</time></span></footer>
  </main>
  <script>
    function revealHash() {
      const target = document.getElementById(location.hash.slice(1));
      if (!target) return;
      let parent = target;
      while (parent) {
        if (parent.tagName === 'DETAILS') parent.open = true;
        parent = parent.parentElement;
      }
    }
    window.addEventListener('hashchange', revealHash);
    revealHash();
    const menus = [...document.querySelectorAll('details')];
    window.addEventListener('beforeprint', () => {
      menus.forEach(menu => { menu.dataset.wasOpen = menu.open; menu.open = true; });
    });
    window.addEventListener('afterprint', () => {
      menus.forEach(menu => { menu.open = menu.dataset.wasOpen === 'true'; });
    });
  </script>
</body>
</html>
'''.replace('RESOURCES', resource_html).replace('PAPERS', paper_html).replace('UPDATED_ISO', e(resources['last_updated'])).replace('UPDATED_LABEL', e(updated_label))
(ROOT / 'index.html').write_text(html)
print(f'Built index.html with {sum(len(g["resources"]) for g in resources["groups"])} learning resources and {paper_count} paper entries.')
