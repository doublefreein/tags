# Doublefree Tags

The public record behind every Doublefree tag. Each handmade piece carries a
tag whose QR code opens `doublefree.in/tags/<ID>`, served from this repository.

| Path | What it holds |
|---|---|
| `passports/<ID>/events/NNNN.json` | The append-only log: one file per event, each carrying the hash of the one before it |
| `passports/<ID>/passport.json` | Summary and the latest (head) hash |
| `media/<sha256>.jpg` | Photos, 1024 px, metadata stripped, named by their SHA-256 |
| `thumbs/<sha256>.jpg` | 720 px display copies of the same photos |
| `<ID>/index.html` | The passport page a buyer sees, at `doublefree.in/tags/<ID>` |

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

## Keeping tag addresses working

Every printed tag points to `doublefree.in/tags/<ID>`, so that address must
never change. It works because GitHub Pages serves this repository under
the custom domain of the account's main site, `doublefreein.github.io`
(whose `CNAME` is `doublefree.in`). This repository has no domain settings
of its own.

- **Never rename this repository.** The name `tags` is the `/tags/` in every
  printed address. Renaming it breaks every tag in circulation.
- **Never add a `CNAME` file here.** It would replace the inherited
  `doublefree.in/tags/` address.
- **The main site must keep `doublefree.in` as its custom domain.** If that
  changes, every passport moves with it.
- **Nothing else on doublefree.in may use `/tags/`.** This repository hides
  any page at that path on the main site. The blog's tag archive lives at
  `/blog/tags/` for this reason.
- **Mirrors don't inherit this.** A Codeberg or self-hosted copy needs its
  own setup to serve the same `/tags/<ID>` paths before DNS can be pointed
  at it.

## Passports

- [DF-CRO-26-0001](DF-CRO-26-0001/): striped crochet cardigan, Pune (sample)
