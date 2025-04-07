from pebbleflow import task, flow


@task
def extract():
    return "raw_data"


@task
def transform(data):
    return data.upper()


@task
def load(data):
    print(f"Loaded: {data}")


@flow
def etl_pipeline():
    raw = extract()
    processed = transform(raw)
    load(processed)


etl_pipeline.run()

