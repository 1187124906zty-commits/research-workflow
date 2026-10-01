# Property figure QA

Output: `ammt-property-continuations.pdf`, editable-text SVG, 600 dpi PNG; script `plot_properties.py`;27-row `property-table-source-data.csv`; curve values `property-continuation-curves.csv`; contract `property-figure-contract.json`. The figure is an original plot of the actual executed inputs and deterministic continuation rules, with no new PDE.

Physical size is180×95 mm. Panels share the25–2200 °C axis with equal axes bounds and aligned labels/ticks. Gray interpolation and source knots, blue L and orange dashed H remain distinguishable by geometry as well as color. Ts/Tl shading and both actual endpoint values are explicit. The latent addition4666.7 J kg−1 K−1 is separate from sensible cp.

Final checks:

- Render-time nature-figure panel-alignment gate passed; record `ammt-property-continuations.alignment.json`.
- Source validator ready=true,20 passes,0 failures. One nonblocking warning notes the requested PNG preview has no TIFF submission raster. PDF/SVG are the delivery vector formats, so no TIFF was added.
- Final PDF text audit:80 text runs, minimum8.1 pt, no below5 pt text and no warnings.
- Final PDF collision audit:0 failures,0 warnings; verdictPASS. Endpoint and phase reference lines are finite vertical guides, and the phase shade has no stroke through annotations. No opaque masking was used.
- Final rendered PNG inspected for legibility, labels, endpoints, curve direction, shared x range and legend separation. Native PDF page dimensions verified against180×95 mm.
- All27 input rows compare exactly with the frozen evidence table; property values are positive and input temperatures strictly increasing. Source data below25 °C remain available and contribute to interpolation at25 °C.

Machine reports: `property-source-audit.json`, `property-text-audit.json`, `property-collision-audit.json` and optional collision overlay. No manuscript compilation is part of this figure QA; canonical compilation belongs to the coordinator.
