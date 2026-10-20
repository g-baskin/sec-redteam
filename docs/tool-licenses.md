# Tool license review

Reviewed 2026-10-19 against upstream license files. This is an engineering inventory, not legal clearance or a complete dependency audit. No listed tool source or binary has been copied into this repository. Pin and re-review the exact version, dependencies, assets and notices before shipping an integration or image.

| Component | Observed license | Integration implications and evidence |
| --- | --- | --- |
| Reconmap | MIT on current `main`; Apache-2.0 on legacy `master` | Preserve the actual selected revision's notices. [main license](https://github.com/reconmap/reconmap/blob/main/LICENSE), [legacy license](https://github.com/reconmap/reconmap/blob/master/LICENSE). Other Reconmap repositories require their own review. |
| Faraday community | GPL v3 text | Preserve GPL terms for upstream portions and provide required Corresponding Source when distributing. GPLv3 section 13 permits combinations with AGPLv3 without erasing the GPL terms on those portions. [license](https://github.com/infobyte/faraday/blob/master/LICENSE). Exact file grants and commercial features remain separate. |
| Faraday plugins | GPL v3 text | [COPYING](https://github.com/infobyte/faraday_plugins/blob/master/COPYING). Same distribution/source review needed. |
| Faraday agent dispatcher | GPL v3 text | [COPYING](https://github.com/infobyte/faraday_agent_dispatcher/blob/master/COPYING). Same distribution/source review needed. |
| reNgine | GPL v3 text | [license](https://github.com/yogeshojha/rengine/blob/master/LICENSE). Review bundled tools independently. |
| DefectDojo community | BSD-3-Clause | Retain copyright, conditions and disclaimer; do not imply endorsement. Commercial edition not included. [license](https://github.com/DefectDojo/django-DefectDojo/blob/master/LICENSE.md). |
| ZAP core | Apache-2.0 | Include license, relevant notices and modification notices. Add-ons and container contents need separate inventory. [license](https://github.com/zaproxy/zaproxy/blob/main/LICENSE). Preferred first integration. |
| Hashcat | MIT | Preserve copyright/license; its `docs/license_libs/` covers additional dependencies. [license](https://github.com/hashcat/hashcat/blob/master/docs/license.txt). |
| John the Ripper jumbo | GPL-2.0-or-later plus OpenSSL/unRAR exception and component-specific terms | Preserve relevant grants and source availability. [license](https://github.com/openwall/john/blob/bleeding-jumbo/LICENSE). |
| Aircrack-ng | GPL v2 text; examined core source grants GPL-2.0-or-later with OpenSSL exception | Do not infer a single grant for every file or dependency. [license](https://github.com/aircrack-ng/aircrack-ng/blob/master/LICENSE), [core source grant](https://github.com/aircrack-ng/aircrack-ng/blob/master/src/aircrack-ng/aircrack-ng.c). |
| Nmap | NPSL 0.95 on examined master | NOT plain GPL. Section 3 expressly addresses purpose-built execution/parsing wrappers and helpers. Separate-process or user-installed execution is not automatic compatibility clearance. Section 6 requires attribution for applicable external deployments. Npcap/Windows redistribution has separate restrictions. Hold integration/bundling pending exact-use review or upstream permission. [license](https://github.com/nmap/nmap/blob/master/LICENSE), [policy](https://nmap.org/npsl/). |
| Burp Suite and examined Montoya API repository | Proprietary PortSwigger terms | The API repository's LICENSE is the Burp Suite Professional Licence Agreement, not a permissive open-source grant. Do not copy/relicense/bundle it as AGPL. Review extension and edition-specific automation terms; licensed user-operated integration is a proposal, not clearance. [API license](https://github.com/PortSwigger/burp-extensions-montoya-api/blob/main/LICENSE), [terms](https://portswigger.net/burp/eula). |
| Kali Linux | Mixed package licenses; Kali-specific infrastructure/integration is GPLv3 | Not one blanket permission for all tools. Review each package and non-free redistribution permissions. Prefer a separately managed worker environment. [official policy](https://www.kali.org/docs/policy/kali-linux-open-source-policy/). |

## Our code

The owner authorized AGPL-3.0-only for original project code and confirmed licensing authority on 2026-10-19. Third-party materials retain their original terms. Public availability and separate repositories/processes do not themselves resolve compatibility.

AGPL permits commercial use. Section 13 requires modified network-interactive versions to prominently offer their Corresponding Source to interacting users. A public repository alone does not establish that every deployed version's source offer is complete. Include a visible source/license link in the UI and maintain source/build instructions for actual releases. Do not publish credentials or collected target data as source.

## Release gate

Before distributing binaries or containers: pin revisions/digests; inventory transitive dependencies, add-ons, fonts and assets; preserve license/NOTICE files; record changes and source availability; review any uncertain combined-work boundary with qualified counsel. This preliminary review does not certify a future release.
