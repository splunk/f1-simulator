---
title: "Screens and LED"
linkTitle: "Screens and LED"
weight: 10
type: "docs"
---

The dashboard has two views of the race, and a few screens for before and after it. Press **BOOT** on the board to switch views.

## Race dash {#race-dash}

![Race dash with rev lights, speed, gear, last lap, position, ERS and DRS](../images/hud.webp)

- **Rev lights** across the top: green, then red, then purple at the shift point.
- **Speed** and **RPM** on the left, **gear** in the centre.
- **Last lap**, **position** and **lap** on the right, with the **ERS** mode and **DRS** state below.
- **Throttle** and **brake** bars along the bottom.

## Lap timing {#lap-timing}

![Lap timing view with the current lap, last and best laps, and three sector times](../images/timing.webp)

The lap timing view shows the current lap time, the last and best laps, and each completed sector.

| Colour | Meaning |
| --- | --- |
| Purple | Faster than this driver's best for that sector so far |
| Yellow | Not faster than that best |
| White | No comparison yet, or the lap is invalid |

Sector bests are this driver's own: the collector doesn't send other drivers' sectors. They reset when the dash restarts or stops receiving data.

## Before and after the race {#race-states}

When no data arrives for two seconds, the dash shows **AWAITING DATA** with its Wi-Fi network and the address to enter in the collector.

![Awaiting data screen with the network name and the board's address](../images/waiting.webp)

When the driver crosses the line, the top row shows **AWAITING RESULT** until the game classifies the race. It then shows **RACE COMPLETE**, or **DNF – RACE ENDED** if the driver didn't finish. The result stays on screen until the next race starts.

{{< tabs >}}
{{< tab name="Awaiting result" >}}
![Race dash showing AWAITING RESULT in orange](../images/finishing.webp)
{{< /tab >}}
{{< tab name="Race complete" >}}
![Race dash showing RACE COMPLETE in green](../images/complete.webp)
{{< /tab >}}
{{< tab name="DNF" >}}
![Race dash showing DNF – RACE ENDED in red](../images/dnf.webp)
{{< /tab >}}
{{< /tabs >}}

The board stays on the view the driver chose. In the lap timing view, the result shows the final lap's sectors:

![Lap timing view showing RACE COMPLETE with the final lap's sector times](../images/complete-timing.webp)

## LED colours {#led}

| When | LED |
| --- | --- |
| Race dash | The colour of the rightmost lit rev light |
| Lap timing | The colour of the latest completed sector |
| Awaiting result | Orange. The final sector's colour shows first for three seconds |
| Race complete | Green |
| DNF | Red |

The race result colours apply in both views.
