# Grey Star Action Assistant v1.1.6 Release Notes

This release moves Grey Star to its own default localhost ports so it can run beside Lone Wolf Action Assistant Redux without a port collision.

## Changed

- Grey Star web app default port changed from `8797` to `8897`.
- Grey Star embedded CLI WebSocket default port changed from `8798` to `8898`.
- Grey Star now launches against `127.0.0.1` by default to avoid localhost IPv4/IPv6 ambiguity on Windows.
- The PowerShell launcher, Python launcher, web server, CLI bridge, assistant startup text, README, install docs, FAQ, and public release guide now point to the new ports.
- The assistant ignores an old saved `8798` CLI bridge port preference and falls back to `8898` unless a `wsPort` query parameter is provided.

## Notes

Custom ports still work:

```powershell
.\Launch-GreyStar.ps1 -HttpPort 9001 -WsPort 9002
```

Project Aon book files are still not included in the release package.

## Verified

- Confirmed local ports `8897` and `8898` were free before the change.
- Python compile check passed.
- Server smoke test passed at `http://127.0.0.1:8897/api/state`.
- CLI bridge smoke test listened on `127.0.0.1:8898`.
- Release package check confirmed no Project Aon book files were included.
