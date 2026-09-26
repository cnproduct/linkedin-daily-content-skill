# Maintenance and GitHub synchronization

The user authorized publishing this reusable skill and future skill improvements to https://github.com/cnproduct/linkedin-daily-content-skill using Chrome.

## What to maintain

Update the installed skill when real usage reveals a useful reusable correction: novel theme coverage, stronger source selection, improved typography, duplicate detection, product-structure checks, metadata verification, or recovery behavior. Preserve the user's actual requirements. Do not generate arbitrary changes just to produce activity.

## Synchronization

- Authoritative local folder: `C:\Users\Administrator\.codex\skills\linkedin-daily-content`.
- Remote folder: repository root (copy the repository into a local folder named `linkedin-daily-content`).
- Publish only SKILL.md, agents metadata, references, scripts, and necessary package documentation.
- Never upload daily images, caption archives, source library, employee/customer photos, credentials, local automation files, browser state, private logs, or personal data.
- Validate with the installed skill-creator quick_validate script. For cleaner changes exercise actual pixel equality and invalid-PNG rejection.
- Track last synchronized SHA-256 hashes in `D:\Ai_cache\linkedin_skill_sync_state.json`, outside the repository. Compare files each scheduled run. If no change, stop quietly.
- Open the repository in Chrome; compare changed remote files before overwriting to avoid losing external edits. If remote has changed since last sync, merge compatible edits locally and validate; otherwise report a conflict without overwriting it.
- Use GitHub's browser add/upload/edit files UI, preserve directory layout, and commit a concise description of the actual improvement.
- Verify the resulting GitHub commit/file listing before updating sync state. If authentication, CAPTCHA, conflicting edits, or browser availability prevents completion, preserve local changes and report the blocker. Do not claim success.
- The scheduled sync checks for existing changes; it does not authorize generating new posts, accessing unrelated repositories, publishing social content, modifying credentials, or deleting remote files.
- Chrome file uploads must follow the available browser file-upload documentation.

## Recurring integration

The daily automation should invoke this installed skill. After an improvement it should attempt synchronization; a separate daily sync heartbeat can catch changes made between content runs. Existing automation schedule and status should be preserved. The computer/browser must be available for scheduled browser operations.

## Installation

Copy the repository into `~/.codex/skills/linkedin-daily-content/` and install Pillow from the normal Python package environment. The local profile contains user-specific paths and can be adapted for another installation. Built-in imagegen is required only for AI fallback; authentic-photo preparation does not require image generation.
