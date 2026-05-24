# plg_robots_meta

Samostatný plugin pro řízení `<meta name="robots">` ve frontend hlavičce.

## Metadata

| Pole | Hodnota |
| :--- | :--- |
| Typ | `plugin` |
| Verze | `0.1.0` |
| Vendor | `klucon` |
| Extension ID | `klucon/plg_robots_meta` |
| Kategorie | `seo` |
| Licence | MIT |
| Core minimum | `0.2.15` |
| Python | `>=3.12` |
| Entry point | `src.plugins.plg_robots_meta` |
| Repository | `https://github.com/klucon/plg_robots_meta` |
| Admin URL | `-` |

## Účel

Plugin generuje pouze robots meta tag. Výchozí hodnota je prázdná, takže po instalaci nic nevkládá do hlavičky, dokud se v administraci nenastaví konkrétní obsah, například `index,follow` nebo `noindex,nofollow`.

## Struktura

```text
src/**/plg_robots_meta/
├── manifest.json
├── __init__.py
├── plugin.py
└── ...
```

## Balíčkování

Release ZIP se staví z `src/plugins/plg_robots_meta/manifest.json` pomocí GitHub Actions workflow `.github/workflows/release-package.yml`.

## Instalace

1. Publikuj ZIP a metadata do marketplace serveru.
2. V CMS otevři `/admin/marketplace`.
3. Vyber `plg_robots_meta` a instaluj verzi `0.1.0`.
4. V nastavení pluginu vyplň hodnotu robots podle požadovaného chování stránky.

## Poznámky k verzi

První verze odděluje robots metadata od obecného SEO meta pluginu.
