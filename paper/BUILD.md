# PIFI-3D family manuscript v0.6 — build

Source directory:

`paper/pifi_3d_family/`

Required files:

- `main.tex`
- `references.bib`

Local build:

```bash
cd paper/pifi_3d_family
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

Clean rebuild:

```bash
latexmk -C
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

The manuscript intentionally has no figure-file dependency in v0.6, so the
arXiv source bundle is only the TeX source, bibliography, and README.

The mathematical evidence is external to the TeX build and is frozen in the
result/verifier files listed in the public-release manifest.
