# Retained Wayback CDX evidence (probe-tesla, 2026-09-26)

Two CDX calls this session answered 504 Gateway Time-out or the Internet Archive
"Temporarily Offline" HTML page; those raw bodies are kept verbatim in this directory
with `.meta.json` sidecars as NEGATIVE ARTEFACTS (UNANSWERED, not nulls).

One CDX call DID answer, at 2026-09-26T01:19Z (approx.), `url=www.tesla.com` (which CDX
normalises to the `tesla.com` urlkey), returning exactly these rows:

    [["timestamp","original","statuscode","length"],
     ["20021125165605","http://tesla.com:80/","200","1119"],
     ["20030209014400","http://tesla.com:80/","200","1116"],
     ["20030214143552","http://tesla.com:80/","200","1113"],
     ["20060209024141","http://tesla.com:80/","302","394"]]

Provenance: response text retained from this session's terminal transcript, not re-fetched;
the bytes above are transcribed, so treat as a LEAD for re-verification, and treat the
504/offline files as the authoritative held bytes of the failed attempts.
