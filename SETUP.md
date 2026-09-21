# Editing and publishing

## Local editing

Open any `docs/*.md` file in a text editor, VS Code, or GitHub's file editor.
The control tables are normal Markdown tables. Replace the `AUTHOR TODO` text with verified behavior.
Replace screenshots under `docs/images/` while retaining their filenames, or update the image links.

## Build locally

From the directory containing this file:

```bash
python -m pip install -r docs/requirements.txt
python -m sphinx -b html -W --keep-going docs _build/html
python -m http.server --directory _build/html 8000
```

Visit http://localhost:8000. These dependencies build the documentation only. They do not install AIDA.

## Add to GitHub

Copy `docs/` and `.readthedocs.yaml` to the root of your AIDA repository. Merge the ignore rules into any existing `.gitignore`. Do not overwrite the existing README or software files. Do not upload the preview or `_build` directory. The YAML file is hidden on some systems, so enable hidden-file display when copying it.

Add a Documentation link to your repository README after your Read the Docs URL exists.

## Connect Read the Docs

1. Sign in to Read the Docs and connect the GitHub account that owns or can administer the repository.
2. Add/import the AIDA documentation project and select the repository and documentation branch.
3. Confirm the configuration file is `.readthedocs.yaml` at the repository root.
4. Trigger the first build and open the resulting documentation URL.
5. When a tested paper release is ready, tag it using your software's actual version and activate the corresponding documentation version.
6. Set the reader-facing default version to the desired stable release. Keep development documentation separate when the UI changes.

The project name and URL depend on availability. This package does not reserve either.

## Before publication

Complete the author checklist in `docs/editing-guide.md`. Review scientific descriptions, exact button actions, required input columns, output names, Stop/overwrite behavior and paper-specific parameters against the released software. Replace the author-draft notices when the text is verified.

References: https://docs.readthedocs.com/platform/stable/intro/sphinx.html and https://docs.readthedocs.com/platform/latest/versions.html
