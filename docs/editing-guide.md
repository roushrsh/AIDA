# Author editing guide

## What is ready

The navigation, nine tab pages, source screenshots, build configuration and editable reference structure are in place. Screenshots are evidence for visible labels, not for hidden algorithmic behavior.

## What to complete

Search all `.md` files for **AUTHOR TODO**. Fill in exact input schemas, control behavior, defaults, output filenames and tested examples. Verify labels against the release you will publish. Add screenshots of successful results, not just empty input screens.

## Recommended editing order

1. Complete Installation and a runnable Quick start example.
2. Verify Main and Database Generator against the code/application.
3. Complete Advanced settings, including interactions between flags.
4. Verify Offline Search and Post Run Script file relationships.
5. Add a worked Gradient Cal and Transfer Learn example.
6. Confirm Run-tab behavior and finish the output map.
7. Fill in paper recipes, citation, release and license details.

## Button description pattern

**Control name:** Describe what it changes. Give accepted values and units, the actual default, when to change it, interactions with other settings and its effect on output.

For Run/Start/Stop controls, explain validation, progress, completion, cancellation and partial-file behavior.

## Adding or rearranging pages

Create a `.md` file under `docs/` and add its name to the appropriate `toctree` in `index.md`. Use normal Markdown links and tables. Store images under `docs/images/` and reference them with relative paths.

## Draft to publication

After verifying the text, remove the draft notices and author TODOs, update `release` in `conf.py`, and remove this editing-guide page from the public navigation if desired. Build with warnings treated as errors before uploading.

The included `SETUP.md` explains local preview and Read the Docs connection. This project does not publish automatically until you connect it to your repository and hosting account.
