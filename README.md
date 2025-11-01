# LLM_BLOGGING_APP — Streamlit blog generator

This is a small Streamlit app that uses LangChain + a Hugging Face model endpoint to generate blog posts.

Quick notes to deploy on Heroku

1. Do NOT commit your `.env` file. Remove any tokens from git history if already committed.

2. Add your Hugging Face token to Heroku config vars:

```bash
heroku login
heroku create your-app-name
heroku config:set HUGGINGFACEHUB_API_TOKEN=hf_xxx
git push heroku main
heroku ps:scale web=1
```

3. Files provided for Heroku
- `Procfile` — runs streamlit on the dyno
- `requirements.txt` — dependencies (Heroku will pip install)
- `runtime.txt` — python version

4. Build command

No explicit build command is required for this Streamlit app. If you need custom steps, add a `bin/post_compile` script and make it executable.

Local testing

1. Create a `.env` file for local testing (not committed):

```
HUGGINGFACEHUB_API_TOKEN='hf_xxx'
```

2. Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

If you run into issues, check logs on Heroku with `heroku logs --tail`.
