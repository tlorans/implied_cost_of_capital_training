# Implied Cost of Capital Training Course

This repository contains course materials for learning about the Implied Cost of Capital, built with Sphinx and deployed to GitHub Pages.

## Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Local Development

### 1. Install uv

If you haven't already installed uv:

```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Set up the environment

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install sphinx sphinx-rtd-theme myst-parser
```

### 3. Build the documentation locally

```bash
# Build HTML documentation
sphinx-build -b html docs docs/_build/html

# Or use the make command (if you have make installed)
cd docs
make html
```

### 4. View the documentation

Open `docs/_build/html/index.html` in your web browser.

## GitHub Pages Deployment

This repository is configured to automatically deploy to GitHub Pages using GitHub Actions.

### Setup Steps:

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Initial Sphinx setup"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository settings
   - Navigate to "Pages" in the left sidebar
   - Under "Build and deployment", select "GitHub Actions" as the source

3. **Automatic Deployment:**
   - Every push to the `main` branch will trigger the workflow
   - The workflow builds the Sphinx documentation and deploys it to GitHub Pages
   - Your site will be available at: `https://<your-username>.github.io/<repository-name>/`

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions workflow for deployment
├── docs/
│   ├── _static/             # Static files (CSS, images, etc.)
│   │   └── custom.css       # Custom styling
│   ├── exercises/           # Exercise materials
│   │   └── exercises.rst
│   ├── modules/             # Course modules
│   │   ├── module1.rst
│   │   └── module2.rst
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Main page
│   └── introduction.rst     # Introduction page
├── .gitignore
├── pyproject.toml           # Project dependencies
└── README.md
```

## Adding Content

### Creating New Pages

1. Create a new `.rst` file in the appropriate directory
2. Add the file to the `toctree` in [docs/index.rst](docs/index.rst)
3. Build and preview locally before pushing

### Markdown Support

This setup includes `myst-parser`, so you can also write content in Markdown (`.md` files):

```markdown
# My New Page

This is a markdown file that Sphinx will render.

## Section

- List item 1
- List item 2
```

### Adding Math Equations

Use Sphinx's math directive:

```rst
.. math::

   e^{i\pi} + 1 = 0
```

Or inline: `:math:`a^2 + b^2 = c^2``

## Customization

- **Theme**: Modify `html_theme` in [docs/conf.py](docs/conf.py)
- **Styling**: Edit [docs/_static/custom.css](docs/_static/custom.css)
- **Configuration**: Adjust settings in [docs/conf.py](docs/conf.py)

## Troubleshooting

### Build Errors

If you encounter build errors:

```bash
# Clean build directory
rm -rf docs/_build

# Rebuild
sphinx-build -b html docs docs/_build/html
```

### GitHub Actions Failing

Check the Actions tab in your GitHub repository for detailed error logs.

## Contributing

Feel free to submit issues or pull requests to improve the course materials.

## License

[Add your license here]
