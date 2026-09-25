# Stage-3 source-id re-key map

My merge wrote four dossiers' `S3001…S3022` blocks into `sources.csv` on top of each other, so 22 ids each
named three different documents. Re-keyed to a single canonical block **S3001–S3081 in application order**
(ST3_A, then B, then C, then D). **Consequence the next pass must respect:** a pending row citing bare
`S3001` is now ambiguous by history — it may have meant A's S-8, B's FY1998 10-K or C's FY1997 10-K405.
Resolution is by content, never by position; irreducible references are held, not guessed.

| Dossier | Old id | Canonical id | Source (truncated) |
|---|---|---|---|
| ST3_A | S3001 | `S30001` | Form S-8 File No. 333-28763 registering the 1997 Stock Optio |
| ST3_A | S3002 | `S30002` | Form 10-Q for the quarter ended June 30 1997 |
| ST3_A | S3003 | `S30003` | Form 10-Q for the quarter ended September 30 1997 EX-10.1 Le |
| ST3_A | S3004 | `S30004` | Form 8-K event 1997-11-07 |
| ST3_A | S3005 | `S30005` | Form 10-K405 for the fiscal year ended December 31 1997 |
| ST3_A | S3006 | `S30006` | Form 8-K event 1998-04-17 Item 9 Regulation S |
| ST3_A | S3007 | `S30007` | Form DEF 14A 1998 proxy statement |
| ST3_A | S3008 | `S30008` | Form DEF 14A 1999 proxy statement |
| ST3_A | S3009 | `S30009` | Form 10-K for the fiscal year ended December 31 1998 |
| ST3_A | S3010 | `S30010` | Form 10-Q for the quarter ended June 30 1999 |
| ST3_A | S3011 | `S30011` | Form 10-Q for the quarter ended September 30 1999 |
| ST3_A | S3012 | `S30012` | Form ARS 1997 annual report to shareholders |
| ST3_A | S3013 | `S30013` | Form ARS 1998 annual report to shareholders |
| ST3_A | S3014 | `S30014` | Form SC 13G for Jeffrey Bezos |
| ST3_A | S3015 | `S30015` | Form SC 13G for Jacklyn Gise Bezos and Miguel A. Bezos |
| ST3_A | S3016 | `S30016` | Form S-4 File No. 333-55943 with S-4/A No. 1 and POS AM Nos. |
| ST3_A | S3017 | `S30017` | Form S-3 File No. 333-65091 with S-3/A No. 1 and POS AM No.  |
| ST3_A | S3018 | `S30018` | Form 10-Q for the quarter ended March 31 1999 |
| ST3_A | S3019 | `S30019` | Form 8-K event 1999-02-03 |
| ST3_A | S3020 | `S30020` | Form 8-K event 1999-03-30 |
| ST3_A | S3021 | `S30021` | Form 8-K events 1998-04-24 and 1998-05-05 |
| ST3_A | S3022 | `S30022` | Form S-4 File No. 333-56723 with S-4/A No. 1 and the 424B2 o |
| ST3_A | S3023 | `S30023` | Forms 8-K events 1998-08-03 and 1998-08-12 and 1998-08-27 wi |
| ST3_A | S3024 | `S30024` | Forms 8-K events 1999-04-26 (two accessions) and 1999-05-14  |
| ST3_A | S3025 | `S30025` | Signature blocks and powers of attorney across the eight 10- |
| ST3_A | S3026 | `S30026` | Form 424B1 final prospectus |
| ST3_A | S3027 | `S30027` | Form 8-A12G Exchange Act registration of the common stock |
| ST3_A | S3028 | `S30028` | Stage 2 chronology and organisation dossier section STAGE BO |
| ST3_A | S3029 | `S30029` | Form 10-K FY1998 EX-10.13 Lease Agreement dated December 14  |
| ST3_A | S3030 | `S30030` | Stage-3 intake manifest and the evidence cache's Stage-3 int |
| ST3_B | S3001 | `S30031` | Form 10-K for fiscal year 1998, Amazon.com, Inc. |
| ST3_B | S3002 | `S30032` | Form 10-K405 for fiscal year 1997, Amazon.com, Inc. |
| ST3_B | S3003 | `S30033` | Form 8-K, fourth quarter and fiscal 1998 results |
| ST3_B | S3004 | `S30034` | Form 8-K, third quarter 1999 results |
| ST3_B | S3005 | `S30035` | DEF 14A proxy statement, meeting 1999-05-20 |
| ST3_B | S3006 | `S30036` | DEF 14A proxy statement, meeting 1998-05-28 |
| ST3_B | S3007 | `S30037` | Schedule 13G for Jeffrey P. Bezos |
| ST3_B | S3008 | `S30038` | Schedule 13G for Jacklyn Gise Bezos & Miguel Bezos |
| ST3_B | S3009 | `S30039` | Form 424B2 final prospectus, Reg. No. 333-56723 |
| ST3_B | S3010 | `S30040` | Form 8-K Item 5, event 1997-11-07 |
| ST3_B | S3011 | `S30041` | Form 8-K Item 5, event 1999-02-03 |
| ST3_B | S3012 | `S30042` | Form 10-Q for the quarter ended 1999-03-31 |
| ST3_B | S3013 | `S30043` | Form 10-Q for the quarter ended 1999-09-30 |
| ST3_B | S3014 | `S30044` | Form S-8, File No. 333-74419 |
| ST3_B | S3015 | `S30045` | Form S-3, File No. 333-78797 |
| ST3_B | S3016 | `S30046` | Form S-3, File No. 333-74435 |
| ST3_B | S3017 | `S30047` | Form 424B3 final prospectus, Reg. No. 333-65091 |
| ST3_B | S3018 | `S30048` | Form 8-K Item 9 Regulation S, event 1998-04-17 |
| ST3_B | S3019 | `S30049` | Form 10-K FY1998, Pro Forma Information |
| ST3_B | S3020 | `S30050` | ARS 1997 and ARS 1998 annual reports to shareholders |
| ST3_B | S3021 | `S30051` | Forms 8-K, events 1998-10-28 and 1999-01-05 |
| ST3_B | S3022 | `S30052` | Corpus scan of all 80+ archived filings against the 1997 reg |
| ST3_C | S3001 | `S30053` | Amazon.com FY1997 Form 10-K405 |
| ST3_C | S3002 | `S30054` | Amazon.com FY1998 Form 10-K |
| ST3_C | S3003 | `S30055` | 8-K event 1998-04-27 with Q1-1998 results release |
| ST3_C | S3004 | `S30056` | Amazon.com Q2-1998 Form 10-Q |
| ST3_C | S3005 | `S30057` | Amazon.com Form S-4 File No 333-55943 |
| ST3_C | S3006 | `S30058` | 8-K events 1998-08-12 and 1998-08-27 (Junglee; PlanetAll) |
| ST3_C | S3008 | `S30059` | ARS 1997 annual report to shareholders |
| ST3_C | S3009 | `S30060` | Amazon.com Q1-1999 Form 10-Q with Exhibits 10.1-10.6 |
| ST3_C | S3010 | `S30061` | 8-K event 1999-03-30 (Auctions launch release) |
| ST3_C | S3011 | `S30062` | Amazon.com Q2-1998 Form 10-Q Item 1 Legal Proceedings |
| ST3_C | S3012 | `S30063` | Amazon.com Q1-1999 10-Q Note 7 and FY1998 10-K Item 3 |
| ST3_C | S3013 | `S30064` | Amazon.com Q2-1999 Form 10-Q |
| ST3_C | S3014 | `S30065` | Amazon.com Q3-1999 Form 10-Q |
| ST3_C | S3015 | `S30066` | 8-K event 1999-10-28 (Q3-1999 results release) |
| ST3_C | S3016 | `S30067` | DEF14A 1999 proxy statement |
| ST3_C | S3017 | `S30068` | ARS 1998 annual report to shareholders |
| ST3_C | S3018 | `S30069` | 424B3 final prospectus and supplement |
| ST3_C | S3019 | `S30070` | Stage 3 intake manifest |
| ST3_C | S3020 | `S30071` | HistoryLink essay Amazon: The Early Years 1995-1999 |
| ST3_D | S3D-001 | `S30072` | Form 10-K405 for the fiscal year ended December 31 1997 |
| ST3_D | S3D-002 | `S30073` | Form 10-K for the fiscal year ended December 31 1998 |
| ST3_D | S3D-003 | `S30074` | Form 10-Q quarterly period ended March 31 1999 including EX- |
| ST3_D | S3D-004 | `S30075` | Form 10-K for the fiscal year ended December 31 1999 |
| ST3_D | S3D-005 | `S30076` | Form 10-Q quarterly period ended September 30 1999 |
| ST3_D | S3D-006 | `S30077` | Form 8-K event July 21 1999 (Amazon.co.uk premises release) |
| ST3_D | S3D-007 | `S30078` | Form 8-K event 1998-08-27 (Junglee and PlanetAll merger note |
| ST3_D | S3D-008 | `S30079` | Forms S-8 File Nos. 333-63311 333-74419 333-78651 333-78653  |
| ST3_D | S3D-009 | `S30080` | Annual Report to Shareholders 1997 (ARS) |
| ST3_D | S3D-010 | `S30081` | Form 10-K FY1999 and FY1998 comparative tables; split histor |
