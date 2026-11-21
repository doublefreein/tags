# Doublefree Tags: public passports

The public record behind every Doublefree tag. Each handmade piece carries a
tag whose QR code opens `doublefree.in/p/<ID>`, served from this repository.

| Path | What it holds |
|---|---|
| `passports/<ID>/events/NNNN.json` | The append-only log: one file per event, each carrying the hash of the one before it |
| `passports/<ID>/passport.json` | Summary and the latest (head) hash |
| `media/<sha256>.jpg` | Photos, 1024 px, metadata stripped, named by their SHA-256 |
| `thumbs/<sha256>.jpg` | 720 px display copies of the same photos |
| `p/<ID>/index.html` | The passport page a buyer sees |

This repository holds **no personal contact data**: no phone numbers,
addresses, UPI IDs or ages. Makers appear by first name and district only,
with their consent.

## Check a record yourself

```sh
python3 verify.py                  # every passport
python3 verify.py DF-CRO-26-0001   # one passport
```

It checks that no entry has been changed or removed and that every photo
matches its hash. It needs only Python 3, with no account.

Corrections never rewrite an entry. They are added as new entries that point
to the one they replace.

## Passports

- [DF-CRO-26-0001](p/DF-CRO-26-0001/): striped crochet cardigan, Pune (sample)
