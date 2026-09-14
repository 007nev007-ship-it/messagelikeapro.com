# Sales-readiness release verification — 14 September 2026

Continues the existing implementation; this is not a new audit.

## Recovery and publication

- Recovered branch: `website/sales-readiness`.
- Original implementation: `1cf21ea16b55eafe80bb4fea45c8246aed98d015`.
- Original handover: `f3fd19155d7de6161d871c4c9179f32649ec0f28`.
- Remote main matched prerequisite `40371c9e9dfeb6f8e1418f8f9d2f2b9e16b834bb` at recovery and continuation.
- Terminal push has no credential path. Authenticated GitHub connector writes are available. Connector-created commits have new identifiers; original file hashes and tree hashes are checked to preserve the recovered implementation exactly.
- User explicitly authorised verified publication and deployment in this conversation. No additional spending, paid purchase, new publishing service or force push.

## Completed commercial checks

The seven public Gumroad listings were inspected in the browser. All six individual books are English PDF downloads. Listing values with US Dollars selected:

| Book | Price (USD) | Pages |
| --- | ---: | ---: |
| On Track | 16.99 | 37 |
| At Work | 19.99 | 57 |
| Off Script | 19.99 | 100 |
| In Conflict | 24.99 | 95 |
| Under Pressure | 29.99 | 131 |
| Professional Communication System | 49.99 | 464 |

Individual total: US$161.94. Complete series: US$99.99. Saving: US$61.95 (approximately 38.25%). Bundle listing confirms all six PDFs.

The bundle checkout reached its payment form and showed the correct bundle. No payment details, personal information or payment were submitted. Display currency initially defaulted to Vietnamese dong; buyers can choose a currency. Payment completion, email receipt and file delivery were not tested.

## Follow-on implementation

- Added verified prices, formats and page counts to the existing book chooser.
- Made the bundle saving amount explicit without changing its price.
- Updated factual privacy wording to distinguish website links, campaign labels and Gumroad checkout.
- Added purchase guidance to the existing terms page, directing buyers to the product listing and final checkout total.
- Static checks for 15 pages and 17 Gumroad links continue to pass.

## Remaining work

- Confirm deployment and browser navigation on the released revision.
- Desktop and mobile visual checks remain outstanding. The browser could visit the live website but blocked the local preview address.
- Gumroad dashboard reporting and sales baseline remain unverified. Do not infer zero sales or calculate conversion rates without the necessary data. Campaign tags alone do not collect visits, clicks or sales.
- Author credentials and research-source additions require supporting material; do not manufacture these or imply that unfinished research validates the products.
- No promotional messages have been sent. Organic promotion follows readiness and requires an authorised channel. No recurring automation is running.
