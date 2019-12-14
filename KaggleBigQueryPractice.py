#https://www.kaggle.com/dansbecker/getting-started-with-sql-and-bigquery
from google.cloud import bigquery

bq = bigquery.Client()
print("imported: ", bq)
dataset_ref = bq.dataset("hacker_news", project="bigquery-public-data")

dataset = bq.get_dataset(dataset_ref)


tables = list(bq.list_tables(dataset))

print (tables.table_id)

table_ref = dataset_ref.table("full")

table = bq.get_table(table_ref)


table.schema


bq.list_rows(table, max_results=5).to_dataframe()



client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()

