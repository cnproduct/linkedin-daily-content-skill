---
name: linkedin-daily-content
description: Prepare diverse daily B2B LinkedIn image and caption packages for unique drinkware and creative food containers, including authentic-photo selection, AI concept fallback, theme rotation, and verified PNG metadata cleanup. Use for daily material preparation or maintaining this workflow; publishing requires separate authorization.
---

# LinkedIn Daily B2B Content

Prepare one coherent theme, four high-resolution square PNGs, and a ready-to-post English caption for overseas brands, importers, retailers, gift buyers, and distributors.

Read [local-profile.md](references/local-profile.md) for this user's paths and recurring schedule. For a different business, establish its profile without inheriting company claims or credentials. Read [theme-library.md](references/theme-library.md) when choosing a theme and [maintenance.md](references/maintenance.md) when improving or synchronizing the skill.

## Daily preparation

1. Resolve today's date in Asia/Shanghai. Inspect final files and the last 14 days of captions, including semantic theme overlap. Use `python scripts/history.py "<output-directory>" --date YYYY-MM-DD`. If today's complete package passes validation, return its paths. If incomplete, finish only missing work. A user request to change a theme authorizes a new version; archive existing outputs outside the final folder.
2. Choose one product structure × use scenario × buyer angle. Prefer novelty over merely changing colors. Rotate product families, content angles, compositions, and buyer audiences. Keep four cards coherent rather than presenting four unrelated products. Avoid ordinary plates, bowls, cutlery, or generic lunch boxes unless a specific innovation is visible.
3. Inventory real assets in the strict priority order in the profile. Select relevant, clear, previously unused images where possible. Empty or unsuitable folders permit AI concept fallback; do not misclassify unrelated factory pictures as product evidence.
4. Prepare four cards and copy. A useful sequence is overview → structure → use scenario → buyer discussion, but a four-direction comparison is also valid. Keep text short and readable on phones. Use actual source resolution and request high-resolution square generation; never describe simple upscaling as added detail.
5. Validate each image visually: correct English, plausible product joins and closures, no malformed objects, clear layout, adequate contrast. Redo or discard failed images. Preserve originals.
6. Clean every final PNG from decoded pixels. For the configured local workflow run the exact external cleanup command in the profile on every final image; otherwise use the bundled `scripts/strip_png_metadata.py`. Independently validate with `python scripts/strip_png_metadata.py --verify <files...>`. Cleanup must preserve dimensions, mode, and pixel bytes, remove EXIF and caBX/JUMBF/C2PA, and leave only IHDR/IDAT/IEND chunks. Invalid final images must be moved outside the final directory and reported as failed.
7. Save `YYYY-MM-DD_theme_01.png` through `_04.png` and `YYYY-MM-DD_theme_caption.txt`. Caption file includes theme, four-image order, source type, English caption, and generation prompts when AI was used. Keep any logs, backups, source files, and receipts outside the final directory.
8. Report theme, material type, and all five absolute paths. This skill prepares material; it does not publish, comment, send messages, or imply that a post went live.

## Authenticity and claims

- Prefer relevant real employee sample checks, packing/shipping, development meetings, real product-specific certificates/reports, and real product photographs, in that order.
- Real photographs may receive deterministic cropping, resizing, and typography. Do not generatively redraw faces, premises, certificates, or product structure.
- Use readable certificates/reports only when actually present and matching the product. Never invent, repair, infer, or modify certificate names, IDs, conclusions, marks, or results. Exclude images containing private customer or personal information.
- AI images are **AI概念示意图 / AI concept visuals**. Never put the letters "AI" or the words "artificial intelligence" or "人工智能" in final image pixels, including generated artwork and overlaid text. A neutral visible label such as "CONCEPT VISUAL" is suitable. Disclose AI origin explicitly in the caption file and use concept, idea, or direction in public copy. Do not represent concepts as existing company products, real samples, factories, employees, meetings, certificates, customer cases, or validated designs.
- Do not invent MOQ, fees, delivery times, materials, safety, sealing, temperature resistance, certifications, patents, performance, production status, or customer endorsements. Discuss questions to evaluate instead.
- Use built-in imagegen by default, one call per distinct card; do not silently substitute CLI/API generation. For real-photo deterministic layouts, Pillow is appropriate. Use AI edits only for concept visuals and explicitly authorized image changes.

## English copy

Write a short buyer-facing opening, two or three useful observations about visible structure or development decisions, and one relevant discussion question. Use a few specific hashtags. Concepts require an explicit disclosure and a concise development/testing caveat. Avoid generic sales superlatives and unverified capabilities.

## Recurring runs and improvements

Daily runs use the schedule configured by the user (06:00 Asia/Shanghai here). On a demonstrated workflow improvement, update the installed skill, validate changes, and synchronize only skill code/documentation to its configured GitHub repository through Chrome. Read maintenance guidance. Preserve schedule and user authorization boundaries. An unattended browser failure is a failed sync, never a successful publish.
