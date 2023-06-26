# Demo-static-analysis-gates

## Docs
[Confluence Doc](https://datadoghq.atlassian.net/wiki/spaces/DE/pages/3061318175/Static+Analysis+Gates+Demo+App)

## Overview:
This project is used to help showcase the static-analysis-gates feature. It is a simplistic project that showcases how the quality gates work within Datadog. 

## Github actions
The project runs off of Github actions to send the staic-analysis and make a determination on if it should pass/fail. This is configured in the .github folder. In addition to this, the static-analysis.datadog.yml file in the root directory is used to determine which rules should be evaluated against

## Setup
Bootstrap the project

1. Create a virtual environment `python -mvenv venv`
2. Use the virtual environment `source venv/bin/activate`
3. Install all dependencies `pip install -r requirements.txt`
4. Init the database `rm -f db.sqlite ;  sqlite3 db.sqlite < init.sql`

Start the project:

```shell
flask --app service run
```
