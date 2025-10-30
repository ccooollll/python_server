# python_server

1. Launch a virtual environment (optional):
    1. Create a virtual environment:
        - `python3 -m venv venv`
    2. Activate the virtual environment:
        - `source venv/bin/activate`
2. Install the required libraries by running:
    - `pip3 install -r requirements.txt`
3. Run the script using:
    - `python3 main.py`


Call the script with the following command as example
```bash
curl --location --request POST 'http://localhost:5001/api/ping' \
--header 'Content-Type: application/json' \
--data '{
    "version":"0.0.1"
}'
```

```bash
curl --location --request GET 'http://localhost:5001/api/ping'
```