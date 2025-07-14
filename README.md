# FOLIO User Import CLI 

Bulk import users into a FOLIO LSP instance from a TSV (tab-separated values) file.  
Perfect for university/library migrations, automation, and IT support.

## Features

- Authenticate to any FOLIO Okapi with username/password/tenant
- Read user records from a simple `.tsv` file (easy to edit in Excel)
- Import users in batch using the FOLIO `/user-import` API
- Clear error messages and detailed import status
- Works with FOLIO snapshot cloud and local installations

---

## Quick Start

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare your users.tsv data file  (this is fake dummy data)
Format (header required):

```tsv
username	externalSystemId	barcode	patronGroup	lastName	firstName	email	phone	addressLine1	addressLine2	city	postalCode	region	expirationDate
azlanmusa	100100001	950000000011	undergrad	Musa	Azlan	azlan.musa1@example.com	013-1000001	21 Jalan Damai	Taman Sentosa	Kuala Lumpur	50050	WP	2027-12-31
linatan	100100002	950000000012	undergrad	Tan	Lina	lina.tan2@example.com	013-1000002	15 Jalan Indah	Taman Melati	Petaling Jaya	46200	Selangor	2028-01-15
...
```

You can export from Excel as "Text (Tab delimited) *.txt" and rename as .tsv.

### 3. Run the CLI

```bash
python bulk_user_import_tsv.py users.tsv \
  --okapi-url https://folio-snapshot-okapi.dev.folio.org \
  --tenant diku \
  --username diku_admin \
  --password (required)
```

Change values as needed for your own FOLIO instance.

https://docs.folio.org/docs/getting-started/

### Arguments

| Argument      | Description                 | Default |
|---------------|-----------------------------|---------|
| `tsv_file`    | Path to TSV user file       | (Required) |
| `--okapi-url` | FOLIO Okapi API endpoint    | https://folio-snapshot-okapi.dev.folio.org |
| `--tenant`    | FOLIO tenant                | diku |
| `--username`  | FOLIO admin username        | diku_admin |
| `--password`  | FOLIO admin password        | (required) —  |

### Example Output

```text
Authenticating as diku_admin@diku ...
Token acquired.
Importing 10 users...
Import response: 200
{
  "message" : "Users were imported successfully.",
  "createdRecords" : 10,
  ...
}
```

If an error occurs, details will be shown in the output.

### Troubleshooting

- Make sure every patronGroup matches exactly with one defined in FOLIO (Settings > Users > User Groups).
- If login fails or you get Token missing, the FOLIO server may be initializing—wait and try again.
- If import fails, check that all columns are present and data is valid.

---

## Sample users.tsv

See the provided users.tsv in this repository for the correct format.

## Contributing

Pull requests are welcome!

Please open an issue for feature requests or bug reports.

Suggestions for web UI, CSV mapping, or error reporting are encouraged.



## Contributing

Pull requests are welcome. For any pull request, please make sure to either:
- Create a new branch, **or**
- Submit a pull request to the `staging` branch.

Please include a brief description of the changes introduced in the pull request.


## License

MIT License (see LICENSE file)

Made in 🇲🇾 with ❤️ (HafizSRL)

