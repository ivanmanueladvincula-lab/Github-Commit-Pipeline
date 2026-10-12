cd C:\Users\acer\github_elt
call venv\Scripts\activate.bat
python extract_github.py
cd transform_layer
dbt run