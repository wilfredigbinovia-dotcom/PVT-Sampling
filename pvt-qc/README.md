# PVT data QC: point exclusion for EOS regression

`pvt-qc.html` is a self-contained web page (no install, no internet needed). Open it in any browser.

It checks laboratory PVT data before EOS regression and helps decide which points to exclude:

| Test | Checks |
|---|---|
| CCE | Robust trend on V/Vsat above Psat; V/Vsat ≤ 1 above and ≥ 1 below Psat and rising as P drops; Y-function linearity (oils); P·Vrel and liquid dropout trends (condensates); Z above Psat |
| CVD | Trends on liquid dropout, gas Z and cumulative moles produced; two-phase Z vs p/Z₂ₚₕ = (Pd/Zd)(1 − nₚ); optional Whitson–Torp material balance with back-calculated liquid compositions and a Hoffman plot per stage |
| DL | Rs and Bo falling below Pb; Bo above Pb; Bo vs Rs linearity; oil density, gas Z and gas gravity trends; oil density mass balance from residual oil density, ΔRs and gas gravity |

## How to use

1. Open `pvt-qc.html` and pick pressure/temperature units.
2. On each tab, paste the data table (tab, comma or space separated, header row first) and enter Psat / Pdew / Pb.
3. Flagged points show as red diamonds with the reason. Click a point (or untick it in a table) to exclude or include it. Trends are refitted without excluded points.
4. On **Export weights**, copy the CSV (weight 0 = excluded, 1 = included) and set the excluded points to zero weight in PVTp's regression data.

Column names it recognises: `P`, `Vrel`, `LDO`, `Z`, `Z2ph`, `Np`, `Bo`, `Rs`, `OilDensity`, `GasZ`, `GasGravity`. CVD gas compositions go in a separate table: component, `Feed`, then one column per stage pressure.

Outliers are found with a robust polynomial fit (iteratively re-weighted, Tukey bisquare) and a robust z-score; the threshold is adjustable. A flag is a reason to look at a point, not a verdict.

Data and exclusions are saved in the browser you use; they are not uploaded anywhere.

## Running on Streamlit

The repo root has `streamlit_app.py`, which embeds this page.

- Locally: `pip install -r requirements.txt` then `streamlit run streamlit_app.py`.
- Streamlit Community Cloud: create an app from this repo, branch `main`, main file `streamlit_app.py`.

Inside Streamlit the page sits in a scrollable frame (raise `height` in `streamlit_app.py` if needed). If "Copy CSV" is blocked, the CSV text is selected; press Ctrl/Cmd+C.
