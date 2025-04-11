\newpage

# Chapter I. Work environment

## 1.1. GitHub account

[GitHub Sign-Up](https://github.com/signup)

## 1.2. Template description

```json
// thesis.json
{
  "year": 2024,
  "description": "Informatiō thesis",
  "iso_country": "vat",
  "iso_language": "lat",
  "url_university": "https://thesis.lat/",
  "url_school": "https://thesis.lat/",
  "url_repository": "https://thesis.lat/"
}
```

## 1.3. Generate the PDF document

```bash
# Install packages
make pkgs
# Make doc.pdf
make doc
# Save changes
make save
```