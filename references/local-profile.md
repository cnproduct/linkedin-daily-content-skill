# Local profile

- Language: English LinkedIn posts; Chinese delivery summaries.
- Default content: unique drinkware and creative food containers.
- Final directory: `D:\图片文件\Linkedin每日发布`
- Real asset root: `D:\图片文件\LinkedIn真实素材库`
- Staging: `D:\Ai_cache\linkedin_staging\YYYY-MM-DD_theme`
- Schedule: daily 06:00 Asia/Shanghai; existing automation ID `linkedin`.
- External mandatory cleaner: `python D:\Ai_cache\strip_png_metadata.py <absolute-image-path>`.
- Installed skill: `C:\Users\Administrator\.codex\skills\linkedin-daily-content`.
- GitHub repository: https://github.com/cnproduct/linkedin-daily-content-skill
- Owner: cnproduct. Browser for publishing and maintenance: Chrome.
- Only prepare and save social assets. No LinkedIn posting or messaging authorization.

## Strict asset priority

1. `01_真实样品检查`: relevant real employees checking samples, preferably visible faces.
2. `02_真实包装纸箱发货`: relevant real packing, cartons, warehouse, shipping.
3. `03_真实会议订单讨论`: relevant product development or order discussions.
4. `04_真实证书检测报告`: actual readable product-specific documents without private information.
5. `06_独特饮具产品图`, then `07_创意食品容器产品图`, then `05_产品主图`.
6. Built-in imagegen only when there are insufficient suitable authentic assets.

Record photo filenames used in a local source log outside the output folder to prefer unused photos on future runs. Availability must be checked each run; do not permanently assume the source library is empty.

## Output contract

Exactly four PNGs for the day's selected theme plus one caption text file, preserving earlier days. Square source images should be at least 1024px; request higher resolution where supported. Current examples were 1254px square, not a required fixed size.

Source type: 真实照片, 真实产品图, or AI概念示意图. For mixed packages specify each card's type.

Existing original-cleaner backups must not be overwritten. If its backup collision blocks a rerun, preserve the existing backup and use a versioned staged filename; never weaken the PNG validation requirement.

