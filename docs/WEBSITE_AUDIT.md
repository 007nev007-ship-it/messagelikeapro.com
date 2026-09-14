# Message Like A Pro: baseline and completion record

Date: 14 September 2026. Baseline commit: `40371c9e9dfeb6f8e1418f8f9d2f2b9e16b834bb`.
Branch: `website/sales-readiness`. This is a prepared change set, not a deployed release.

## Audit scope and evidence

Inspected the complete tracked-file inventory, all 15 HTML pages, shared CSS, embedded research-page CSS, image inventory and dimensions, README, CNAME, ignore file and placeholder text file. No build system, JavaScript, analytics integration or deployment workflow is present in the repository. No AGENTS.md is present. Public text retrieval succeeded for the homepage and all 14 linked pages. All seven distinct Gumroad product URLs returned product titles, but no product-body text. This verifies destination identity, not price, contents or checkout operation.

The browser permission check rejected live-site visual inspection. No browser workaround was attempted. Desktop/mobile rendering, interactive checkout, console errors and actual loading timings remain unverified. Public robots/sitemap retrieval failed; their absence was confirmed in the repository, not by interpreting that retrieval failure as a live 404.

## Commercial findings and disposition

| Priority | Baseline finding | Action/status |
|---|---|---|
| Critical | Homepage purchase route ends in email on book.html although Gumroad products exist | Both flagship purchase links now use the existing Gumroad destination. Homepage differentiates product exploration from buying. |
| Critical | App described as in development but buttons say buy now | Labels now accurately offer an app-access enquiry. No availability, pricing or release promise invented. |
| Critical | Hidden-checkbox navigation is not keyboard-operable through its label | Replaced with native details/summary navigation; labelled landmark, active-page marker, skip link and visible focus. Browser checks outstanding. |
| Critical | No first-party visitor/click collection or verified sale attribution | Added static UTM labels to 17 purchase links. No scripts, accounts, cookies or personal-data collection added. Gumroad reporting verification still required. |
| Critical | Bundle states US$99.99 and save over 38%; Gumroad body unavailable | Existing price and saving remain unchanged. Must verify both against current listings before release. |
| Important | Product titles differ from destination titles | Aligned On Track, Off Script and Professional Communication System with returned Gumroad titles. Updated flagship cover to the current image already used in the catalogue. |
| Important | App promotion interrupts the six-book catalogue | Preserved and moved app section after all books. Added a situation-based six-book chooser near the top and a persistent browse-books link. |
| Important | FAQ omits buying guidance | Added buying, selection, bundle, format, app-access and order-support answers using existing site information. No invented refund policy or delivery guarantee. |
| Important | Large PNGs impose unnecessary transfer weight | Added WebP derivatives, intrinsic dimensions and below-hero lazy loading. All original PNGs preserved. |
| Important | Missing canonical, image-sharing and discovery metadata | Added canonical URLs, Open Graph fields where missing, social image, locale, Twitter card, favicon, robots.txt and sitemap for 15 pages. Existing page descriptions preserved. |
| Important | Logo is an H1 on every page | Logo is now a styled paragraph; one principal H1 per page. |
| Important | Repeated sentence injected into every authority heading via CSS | Removed injected repetition while retaining all source paragraphs and sections. |
| Important | About page does not identify an author; research claims have no source links | Content retained. Source-backed author information and explicit research attribution remain to be verified before new claims are published. |
| Important | Privacy/terms describe generic future services | Policy substance unchanged. Actual Gumroad/payment handling and any future measurement must be reflected accurately; no legal-compliance claim made. |
| Optional | Duplicate/unused legacy images and overlapping explanatory pages | Preserved. Deleting assets or consolidating substantive pages is unnecessary for this repair. |

No missing local HTML/image/CSS destinations were found in the baseline. No new system, publishing account, price change or spending was introduced.

## Existing product destinations

| Product | Existing Gumroad path |
|---|---|
| On Track | https://messagelikeapro.gumroad.com/l/on-track |
| At Work | https://messagelikeapro.gumroad.com/l/at-work |
| Off Script | https://messagelikeapro.gumroad.com/l/off-script |
| In Conflict | https://messagelikeapro.gumroad.com/l/in-conflict |
| Under Pressure | https://messagelikeapro.gumroad.com/l/under-pressure |
| Professional Communication System | https://messagelikeapro.gumroad.com/l/professional-communication-system |
| Complete Professional Communication Series | https://messagelikeapro.gumroad.com/l/complete-series |

## Performance evidence

Sum of distinct referenced image files per page, excluding favicon/social metadata images. This is a file-size comparison, not measured browser transfer or a speed score.

| Page | Before | Prepared | Reduction |
|---|---:|---:|---:|
| Homepage | 725,125 bytes | 38,130 bytes | 94.7% |
| Flagship book | 1,400,646 bytes | 148,368 bytes | 89.4% |
| Products | 50,346,793 bytes | 923,486 bytes | 98.2% |
| App | 8,786,223 bytes | 442,028 bytes | 95.0% |

Six-book banner: 18,616,485 bytes to 143,674 bytes. Original artwork retained. One empty derivative was detected, regenerated and checked before completion.

## Verification completed

- `python scripts/check_site.py`: all 15 pages and 17 Gumroad links pass local file/anchor, allowed-product destination, attribution, heading, language, landmark, metadata, image-attribute and sitemap checks.
- `identify images/*.webp images/mlap-social.jpg`: all derivative images decode successfully.
- `git diff --check`: no whitespace errors.
- All original PNG assets remain byte-for-byte unchanged in git.

These checks do not constitute a screen-reader audit, real-device test, checkout transaction or proof of sales reporting.

## Remaining execution sequence

1. Obtain GitHub connection for publishing the branch/PR. Read-only public clone succeeded; write access is not confirmed.
2. With browser access permitted, verify desktop and mobile layout, keyboard menu/focus behaviour, product-listing contents, price/saving consistency and purchase flow up to payment. No paid test is authorised.
3. Verify actual Gumroad reporting fields and existing sales baseline. Determine whether the prepared UTM values appear in reports before relying on them. If visitor denominators are unavailable, do not report a conversion rate.
4. Obtain only the missing source-backed author/research details necessary for credibility content. Do not manufacture claims or repurpose an unfinished research project as validation.
5. Prepare any necessary factual policy updates based on actual services. Review the concrete release changes with Nev before consequential publication; merge/deploy only with appropriate authority.
6. Verify the deployed revision and destination links. Begin a small organic traffic experiment only after readiness is established.

## Measurement and later traffic work

Prepared outbound tags use source `messagelikeapro.com`, medium `referral`, campaign `website`, and page/placement content labels. They contain no personal identifiers, and normal anchor navigation works without JavaScript. Tags alone do not collect visits, clicks or completed purchases.

The first traffic experiment should address one concrete teacher communication problem and link to the most relevant existing book. Use existing authorised channels, without paid advertising or unsolicited messaging. Record the publication, destination, reporting window, attributable sales and revenue where actually available. Compare evidence before expanding. No promotion has been published and no ongoing automation is running.

## Rollback

The repair is isolated from main. Original content and PNGs remain in git history. Before publication, discard the repair branch to return to baseline. After a reviewed merge, revert the merge or relevant repair commit through the repository's normal workflow; do not reset or force-push shared history.
