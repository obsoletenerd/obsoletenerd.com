---
Title: "Building a personal website using Pelican and Cloudflare"
Date: 2025-07-24 11:33
Modified: 2025-07-24 20:45
Summary: How I built this personal website and static blog with automated build-process and effectively-free hosting, using Pelican/Python, GitHub, and Cloudflare pages.
Category: Projects
Tags: Software, Projects
Status: Published
---

This post will evolve into more of a tutorial/guide later. For now it is a dumping ground for my notes as I build out the site.

## Set up Pelican locally

```bash
uv init obsoletenerd.com
cd obsoletenerd.com
```

Edit `pyproject.toml` and use the following:

```bash
[project]
name = "obsoletenerd-com"
version = "0.1.0"
description = "ObsoleteNerd.com"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pelican[markdown]>=4.11.0",
]

[project.optional-dependencies]
markdown = [
    "pelican>=4.11.0",
]
```

Save, then run the Pelican setup script with `uv run pelican-quickstart`

Answer all the questions and it will create the basic website structure.

Put a quick sample post into `/content/`, using this as an example:

```bash
---
Title: "Welcome to my new website!"
Date: 2025-01-01 13:37
Date: 2025-01-01 13:37
Summary: This is where the summary for this post goes, which will be used in the template where appropriate, eg on the index page where it shows a summary of each post.
Category: [blog]
Tags: [tag1, tag2]
Status: published
---

This is a test post for my new Pelican-based website.
```

Do `uv run pelican` to build the site with the test post, then `uv run pelican -r -l` to spin up a local webserver and have a look at the website. It will show up at `http://127.0.0.1:8000`.

If you keep that server running in the terminal, you can then go edit your posts in your IDE and Pelican will re-build every time it detects a change, letting you iterate on posts/layouts/etc quickly locally before actually uploading anything.

Lastly (and *importantly*) before continuing, type this in the terminal to lock your dependencies for Cloudflare Pages' build process:

`uv pip compile pyproject.toml -o requirements.txt`

Cloudflare pages uses `pip` so we need the `requirements.txt` ready for it to run Pelican on their servers later.

## Set up a Github repository for the website

This assumes you already have a Github account.

Go to [https://repo.new/](https://repo.new/) to create a new repository (it's just a shortcut to the normal page to create repos). Create the repo, then in your terminal in the root folder of the Pelican website, do the following:

```bash
git init
git remote add origin https://github.com/<your-gh-username>/<repository-name>
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

(This is the standard "get a new project going in Github" stuff)

## Configuring Cloudflare Pages to deploy your website

In your Cloudflare dashboard left menu:
- Click on "Compute (Workers)" and then "Workers & Pages".
- Select the "Pages" tab.
- Click on "Import an existing Git repository" and follow the instructions to connect to your Github account and the appropriate repository.
- In the "Build Settings" section choose "Pelican" as the "Frameworks preset".
- Modify the "Build Command" to be this: `pip install -r requirements.txt && pelican content -s publishconf.py`
- Select "Environment variables (advanced)" and add `PYTHON_VERSION = 3.13` (or whatever is current when you do this)
- Continue through the build process.

If all goes well, you should get given a test URL like `https://obsoletenerd-com.pages.dev` to test it all worked.

Next, connect your custom domain to Cloudflare following their instructions ("Custom Domains" in the "Workers & Pages" section)

Voila... you now have the most ridiculously over-engineered static HTML and CSS hosting possible. There's no kill like over-kill.

I miss FTPing files to my ISP.
