import duckdb

con = duckdb.connect(r'C:\Users\acer\github_elt\github_pipeline.duckdb')

print("--- TABLES IN DATABASE ---")
print(con.sql("SHOW ALL TABLES"))

print("\n--- FINAL GOLD METRICS ---")
print(con.sql("SELECT * FROM silver_commits LIMIT 100"))