import requests

url = ["https://datasets.imdbws.com/title.basics.tsv.gz","https://datasets.imdbws.com/title.ratings.tsv.gz"]
for u in url:
    filename = u.split("/")[-1]
    with open(f"/opt/airflow/dags/{filename}", "wb") as f:
        r = requests.get(u)
        f.write(r.content)