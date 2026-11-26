# Comparable products and differentiation

[← Portfolio](../README.md)

Vendor pages were checked on 2026-11-26. Each fact below comes from the linked vendor page; where a page did not state something, the table says so. No pricing is inferred. This is a design-stage project; every comparable below is a shipping product, which this work is not.

| Product | Senses | Connectivity (as stated) | Actuation (as stated) | Published pricing | Source |
|---|---|---|---|---|---|
| HARDWARIO CHESTER Current | Up to four split-core clamp probes, AC/DC, for utilisation | LTE-M/NB-IoT or LoRaWAN; LoRaWAN server local or cloud | Not stated | None shown | [vendor page](https://www.hardwario.com/products/chester/catalog/current/) |
| Monnit AC current meters | Wireless AC and three-phase current meters | Gateways to the iMonnit cloud | Not stated | No list price | [vendor page](https://www.monnit.com/products/sensors/ac-current-sensors/) |
| MachineMetrics | Machine control data (speed, load, power) and external sensors | Edge device on the machine network | States it can stop a machine or trigger actions on a threshold | None on page | [vendor page](https://machinemetrics.com/condition-monitoring) |
| Tractian | Vibration and ultrasound (not current) | 4G/LTE, no Wi-Fi or Ethernet | Not stated | Quote per asset | [vendor page](https://tractian.com/en/solutions/condition-monitoring/vibration-sensor/pricing) |
| Waites SM7 | Triaxial vibration and temperature | Wireless mesh | Not stated | None | [vendor page](https://waites.net/solutions/sm7-wireless-sensor) |
| KCF SMARTdiagnostics | 4–20 mA input node; motor current signature analysis offered | 2.4 GHz radio to base station, then cloud | Not stated | None | [input node datasheet (2020)](https://kcftech.com/wp-content/uploads/2020/06/IN_Data_Sheet.pdf), [suite page](https://kcftech.com/solutions/smartsensing-suite/) |

None of the vendor pages checked published how stale or offline data is shown to a user. That is an observation about the pages, not evidence that the products lack such handling.

## Differentiation (design intent, not a demonstrated advantage)

- **Read-only by design.** The proposed monitor has no path to machine control. MachineMetrics states its product can stop a machine; that capability is deliberately absent here, and machine safety stays with the site.
- **Published freshness and clock-trust rules.** A reading older than 60 s is shown as stale, and readings with untrusted time are withheld. The rules and their checks are public ([risks and timing](cps-risks-timing.md)); they are tested only on synthetic input.
- **Not differentiated:** clamp-on current sensing for machine state is already offered by HARDWARIO and Monnit. Cost, reliability and support have not been compared because no field deployment exists.

No market size, customer demand, or price advantage is claimed.
