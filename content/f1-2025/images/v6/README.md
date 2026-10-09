# v6 screenshot provenance

Captured 9 October 2026 from collector source commit a887f44 (version 6.0.6), using an isolated Docker instance and the browser screenshot API. Images show the actual UI, not generated mockups. The viewport is 1440×900.

- Four demo rigs; all driver names are demonstration names.
- HEC delivery used a local mock receiver. Observability was off. No demonstration events were sent to production destinations, and no tokens are displayed.
- The public-address lookup was blocked, so the IP pill reads Unavailable. Use the host LAN address for local rigs.
- The Game pill and the Event tab show F1 2025. The Game list was left closed.
- The bundled Austria recording was replayed through live UDP at 1× on rig 1 with global recording enabled. First light began capture; Final Classification completed the result. Alex Taylor finished with a 1:07.787 best lap. Rig 2 remained Ready independently.
- `collector.webp` shows live collection. `driver-name.webp` compares name entry with an assigned driver and the saved result. `name-validation.webp` shows rejected punctuation.
- `saved-files.webp` shows the bundled Austria recordings. `logs.webp` shows the race lifecycle in the activity table. `playback.webp` shows the playback form, not an additional playback test. The other images show their named modal or tab.

Refresh images against the release being documented. Keep secrets out of screenshots and preserve visible labels that match the instructions. Existing game-settings screenshots elsewhere remain applicable to F1 25.
