# Implied Cost of Capital Training Course

A comprehensive course on Implied Cost of Capital, built with Sphinx and automatically deployed to GitHub Pages. Write your course content in Markdown, see changes instantly with live reload, and publish with a single `git push`.

## 🚀 Quick Start (5 minutes)

### 1. Install uv (if not already installed)

```powershell
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Set up the project

```powershell
# Clone and enter the repository
cd implied_cost_of_capital_training

# Create virtual environment and install dependencies
uv venv
uv pip install sphinx sphinx-rtd-theme myst-parser sphinx-autobuild
```

### 3. Start the live development server

```powershell
# Option 1: Use the convenience script
.\serve.ps1

# Option 2: Run directly
.venv\Scripts\sphinx-autobuild.exe docs docs/_build/html --open-browser --port 8000
```

**That's it!** Your browser will open at http://127.0.0.1:8000 and automatically refresh when you save any changes.

## 📝 Daily Workflow

### Writing Content

1. **Edit any `.md` file** in the `docs/` folder
2. **Save the file** - the browser refreshes automatically
3. **Keep editing** - changes appear instantly

**Example:** Open `docs/modules/module1.md` and try changing some text!

### Project Structure

```
docs/
├── index.md              # Home page - edit to change main landing page
├── introduction.md       # Course introduction
├── modules/
│   ├── module1.md       # First module - edit to add your content
│   ├── module2.md       # Second module
│   └── module3.md       # Add new modules here...
├── exercises/
│   └── exercises.md     # Practice problems and projects
├── _static/
│   └── custom.css       # Custom styles (colors, fonts, etc.)
└── conf.py              # Sphinx settings (usually don't need to touch)
```

### Adding a New Page

1. **Create the file:**
   ```powershell
   New-Item docs/modules/module3.md
   ```

2. **Add content:**
   ```markdown
   # Module 3: Advanced Analysis
   
   Your content here...
   ```

3. **Add to navigation** - Edit `docs/index.md`:
   ```markdown
   ```{toctree}
   :maxdepth: 2
   
   introduction
   modules/module1
   modules/module2
   modules/module3    # Add this line
   exercises/exercises
   ```
   ```

4. **Save** - it appears automatically in your browser!

## 📖 Markdown Syntax Guide

### Headings & Text
```markdown
# Main Heading
## Sub Heading
### Smaller Heading

**Bold text**
*Italic text*
```

### Math Equations
```markdown
Inline math: $r = \frac{D_1}{P_0} + g$

Block equation:
$$r = \frac{D_1}{P_0} + g$$
```

### Code Blocks
````markdown
```python
def calculate_icc(dividend, price, growth):
    return (dividend / price) + growth
```
````

### Callout Boxes
````markdown
```{note}
This is an informational note.
```

```{tip}
This is a helpful tip!
```

```{warning}
This is a warning message.
```
````

### Tables
```markdown
| Company | Price | Dividend | Growth |
|---------|-------|----------|--------|
| A Corp  | $100  | $3.00    | 5%     |
| B Inc   | $75   | $2.50    | 7%     |
```

### Lists
```markdown
* Bullet point 1
* Bullet point 2

1. Numbered item 1
2. Numbered item 2
```

### Images
```markdown
# Place image in docs/_static/ folder
![Alt text](_static/my-image.png)
```

## 🌐 Deploy to GitHub Pages

### First-Time Setup

1. **Push to GitHub:**
   ```powershell
   git add .
   git commit -m "Initial course setup"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repo on GitHub
   - Click **Settings** → **Pages**
   - Under "Source", select **GitHub Actions**
   - Done! GitHub will build and deploy automatically

3. **View your site:**
   - Wait 2-3 minutes for the first build
   - Visit: `https://<your-username>.github.io/implied_cost_of_capital_training/`

### Every Update After That

```powershell
# Make your changes to .md files
# Then just:
git add .
git commit -m "Updated module 1 content"
git push

# Site rebuilds and deploys automatically in ~2 minutes!
```

You can check deployment status in the **Actions** tab of your GitHub repository.

## 🎨 Customization

### Change Colors & Fonts
Edit `docs/_static/custom.css`:
```css
/* Change primary color */
.rst-content table.docutils th {
    background-color: #e74c3c;  /* Red theme */
}
```

### Change Theme
Edit `docs/conf.py`:
```python
html_theme = 'alabaster'  # or 'sphinx_book_theme', etc.
```

### Change Course Title
Edit `docs/conf.py`:
```python
project = 'Your Course Name Here'
author = 'Your Name'
```

## 🛠️ Common Tasks

### Build without live reload
```powershell
.venv\Scripts\sphinx-build.exe -b html docs docs/_build/html
Start-Process docs\_build\html\index.html
```

### Clean build (fixes most issues)
```powershell
Remove-Item -Recurse -Force docs/_build
.venv\Scripts\sphinx-build.exe -b html docs docs/_build/html
```

### Stop the development server
Press `Ctrl+C` in the terminal running sphinx-autobuild

### Add Python packages
```powershell
uv pip install package-name
```

## 🆘 Troubleshooting

### Server won't start
```powershell
# Make sure you're in the right directory
cd c:\DBD\implied_cost_of_capital_training

# Activate virtual environment
.venv\Scripts\activate

# Try starting again
.\serve.ps1
```

### Changes not showing
1. Check the terminal - it should show "Detected change in..."
2. Hard refresh browser: `Ctrl+Shift+R`
3. Clean rebuild: `Remove-Item -Recurse -Force docs/_build`

### Build errors
- Check your Markdown syntax (especially code blocks and callouts)
- Look at the terminal output for the error line number
- Common issue: Unclosed code blocks (need three backticks)

### GitHub Actions failing
- Go to your repo's **Actions** tab
- Click on the failed workflow
- Check the error message in the build logs

## 📚 What's Included

- ✅ **Sphinx** - Professional documentation generator
- ✅ **Read the Docs theme** - Clean, responsive design
- ✅ **Markdown support** - Write in familiar syntax
- ✅ **Math equations** - LaTeX-style formatting
- ✅ **Live reload** - See changes instantly
- ✅ **GitHub Actions** - Automatic deployment
- ✅ **Custom CSS** - Easy styling
- ✅ **Code highlighting** - Syntax highlighting for Python, etc.

## 📖 Learn More

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Markdown Guide](https://myst-parser.readthedocs.io/)
- [Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/)

## 💡 Tips

- **Save often** - Changes appear instantly with auto-reload
- **Use callouts** - `{note}`, `{tip}`, `{warning}` make content clearer
- **Add examples** - Code blocks with actual calculations help students learn
- **Test locally first** - Always preview before pushing to GitHub
- **Commit frequently** - Small commits are easier to track and debug

## 📄 License

[Add your license here]
