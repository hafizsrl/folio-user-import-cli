import csv
import requests
import re

# get credential here https://docs.folio.org/docs/getting-started/ (Snapshot Server)
okapi = "https://folio-snapshot-okapi.dev.folio.org"
tenant = "diku"
username = "diku_admin"
password = "required"
tsv_file = "users.tsv"   # Your TSV file path

# === LOGIN ===
resp = requests.post(
    f"{okapi}/authn/login-with-expiry",
    headers={
        "Content-Type": "application/json",
        "x-okapi-tenant": tenant
    },
    json={"username": username, "password": password},
)
# Extract token from cookies or Set-Cookie header
token = resp.cookies.get("folioAccessToken")
if not token:
    set_cookie = resp.headers.get("Set-Cookie", "")
    match = re.search(r'folioAccessToken=([^;]+)', set_cookie)
    token = match.group(1) if match else None

print("Token:", "Token acquired")
if not token:
    print("No token found. Login failed or server not ready.")
    exit(1)

# === READ USERS FROM TSV ===
users = []
with open(tsv_file, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        user = {
            "username": row["username"],
            "externalSystemId": row["externalSystemId"],
            "barcode": row["barcode"],
            "active": True,
            "patronGroup": row["patronGroup"],
            #"departments": [row["department"]],
            "personal": {
                "lastName": row["lastName"],
                "firstName": row["firstName"],
                "email": row["email"],
                "phone": row["phone"],
                "addresses": [
                    {
                        "addressLine1": row["addressLine1"],
                        "addressLine2": row["addressLine2"],
                        "city": row["city"],
                        "postalCode": row["postalCode"],
                        "region": row["region"],
                        "addressTypeId": "Home",   # Set as appropriate or map if needed
                        "primaryAddress": True
                    }
                ]
            },
            "expirationDate": row["expirationDate"]
        }
        users.append(user)

if not users:
    print("No users found in TSV.")
    exit(1)

payload = {
    "users": users,
    "totalRecords": len(users),
    "deactivateMissingUsers": False,
    "updateOnlyPresentFields": True
}

# === IMPORT TO FOLIO ===
resp2 = requests.post(
    f"{okapi}/user-import",
    headers={
        "Content-Type": "application/json",
        "x-okapi-tenant": tenant,
        "x-okapi-token": token
    },
    json=payload
)

print("Import response:", resp2.status_code)
print(resp2.text)
