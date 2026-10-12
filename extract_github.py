import dlt
import requests

@dlt.resource(write_disposition="replace", primary_key="sha")
def get_commits():
    url = "https://api.github.com/repos/duckdb/duckdb/commits?per_page=100"
    response = requests.get(url)
    response.raise_for_status()
    yield response.json()

pipeline = dlt.pipeline(
    pipeline_name="github_pipeline",
    destination="duckdb",
    dataset_name="bronze_layer"
)

if __name__ == "__main__":
    info = pipeline.run(get_commits())
    print(info)