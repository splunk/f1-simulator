# v6 screenshot provenance

Captured 24 September 2026 from collector source commit 89d4cd1 (version 6.0.5), using an isolated Docker instance and the browser screenshot API. Images show the actual UI, not generated mockups.

- Four demo rigs; all driver names are demonstration names.
- HEC delivery used a local mock receiver. Observability was off. No demonstration events were sent to production destinations, and no tokens are displayed.
- The bundled Austria recording was replayed through live UDP at 1× on rig 1 with global recording enabled. First light began capture; Final Classification completed the result and recording. Alex Taylor finished with a 1:07.787 best lap. Rig 2 remained Ready independently.
- `collector.png` shows live collection; `driver-name.png` compares name entry with an assigned driver; `name-validation.png` shows rejected punctuation.
- `saved-files.png` shows the completed recording with the driver name in its filename. `logs.png` shows actual lifecycle messages and the five-column activity table; no repeated entries were fabricated.
- `playback.png` shows the playback form, not an additional playback test. The other images show their named modal or tab.

Refresh images against the release being documented. Keep secrets out of screenshots and preserve visible labels that match the instructions. Existing game-settings screenshots elsewhere remain applicable to F1 25.
