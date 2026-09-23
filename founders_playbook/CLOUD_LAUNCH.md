# CLOUD LAUNCH — running this fleet on Qoder Cloud Agents

Written 2026-09-23 while no cloud credential existed on the local machine, so that turning this into
remote execution is one session's work rather than a re-derivation.

**Verified at authoring time:** no QCA MCP server connected in the local session; `QODER_ACCESS_TOKEN`,
`QODER_PAT` and `QCA_MCP_PAT` all unset; `gh` installed but not logged in. **Therefore nothing in this
file has been executed — it is a plan, not a result.** Do not treat any step as confirmed working until
step 1 returns a model list and step 3 returns a session that reaches a terminal state.

## 0. Prerequisites (both are required)

1. **A Qoder PAT**, created in Qoder's account integrations settings and set as a local environment
   variable — `QODER_ACCESS_TOKEN`, without the `Bearer` prefix. Never paste it into a chat or commit
   it. The routes below are QCA HTTP; a token for another host or region is not valid here.
2. **This repository, reachable by the cloud environment.** Already done: pushed to
   `https://github.com/RudraNarayanP/founder-s-play-book`, branch `main`, containing the whole
   evidence base (verified filings, 11 dossiers, the Amazon Stage 1 volumes, all registers). A remote
   agent must clone this; re-searching the web from scratch would discard every audited citation.

Regional endpoints (Global production): Managed HTTP `https://api.qoder.com/api/v1/cloud`,
Forward HTTP `https://api.qoder.com/api/v1/forward`, OpenAPI `https://openapi.qoder.sh`.
Keep account, environment and resource region consistent; on an authentication failure, **do not**
try the same credential against another region.

## 1. Discover, don't assume

```
GET  /models                     # available models and options — read before creating an Agent
```
Then inspect existing Agents/Environments and **reuse** them where they fit. Create nothing that
already exists.

## 2. Environment and Agent

```
POST /environments               # network access + tool configuration for research execution
POST /agents                     # model, system prompt, mcp_servers, skills, file bindings
```
Requirements this project specifically has, to encode in the Agent definition:
- web retrieval and local file read/write (the whole method depends on citing documents it can open);
- the research brief = `founders_playbook/00_METHOD_AND_STYLE.md` + `RESUME_HANDOFF.md` +
  `MASTER_RESEARCH_LOG.md`, read in that order;
- the §14 retrieval rules, which are not optional because each was learned from a failure:
  **write the output file first and append findings as you go**; hard cap of 8 searches and 8 fetches;
  **never delete, move, or tidy any directory, including one you created**; report the output path and
  the record count actually on disk.

## 3. One session per company stage

```
POST /sessions                              # body uses "agent" (HTTP) not "agent_id" (MCP)
POST /sessions/{id}/resources               # attach repo files / uploaded inputs
POST /sessions/{id}/events                  # {"events":[{"type":"user.message","content":[{"type":"text","text":"…"}]}]}
GET  /sessions/{id}                         # status
GET  /sessions/{id}/events                  # history
GET  /sessions/{id}/events/stream           # SSE; without Last-Event-ID it starts at the current tail
POST /sessions/{id}/cancel
```
Per-company message shape: *"Execute <company> Stage <N> per `RESUME_HANDOFF.md` §6 and
`00_METHOD_AND_STYLE.md`. Produce dossiers in `research/`, then the stage volumes, then run all five
audits in `03_quality_control/AUDIT_PROTOCOLS.md`. Commit and push each artifact as it is written."*

**Observe, don't assume completion.** An accepted message is not a finished task. `requires_action`
means paused and waiting for input, not success. Poll to a terminal state or a deadline, then read the
final `agent.message`.

## 4. Parallelization design

- Fan out **one session per company**, not one session per dossier. A company's eleven dossiers share a
  stage boundary; splitting them across independent sessions loses the arbitration that made Amazon's
  Stage 1 coherent (four agents disagreeing about the launch date had to be resolved once, centrally).
- Within a company, keep the **probe-first** rule: a feasibility verdict sets depth before a full fleet
  runs, because 19 of 50 companies are successor/merger entities and 2 have no founder at all.
- Serialize writers on `stage_1.md` — two concurrent agents editing one volume produced conflicts that
  had to be re-applied in order.
- Push after every artifact, so a dead session loses at most one file.

## 5. Recurring work

```
POST /deployments                # scheduled/recurring runs
POST /deployments/{id}/run       # only trigger an immediate run when explicitly asked
```
Creating a schedule does **not** mean running it now.

## 6. Other resources

```
POST /files                      # upload evidence; attach large inputs as files, do not embed datasets in messages
GET  /files/{id}/content         # download via returned signed URL — do not forward QCA Authorization headers to storage
POST /skills , POST /vaults , POST /memory_stores
```
An Agent's `mcp_servers` and Vaults configure **downstream cloud execution**, not this host's link to
QCA. Those credentials are distinct from the QCA PAT.

## 7. What cloud execution cannot fix

Scale is not the constraint here; **evidence density is**. Cloud agents parallelize the wall clock, not
the fact that pre-1970 histories have thin digital archives, that SEC blocks several important Amazon
corporate records from existence, and that a forensic dataset is only as good as its least-verified
claim. Expect the audits to fail on the first pass remotely too — that is the method working, not the
cloud misbehaving.
