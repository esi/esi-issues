Historical reference of endpoint additions and changes made in ESI.

Dates in the future are upcoming scheduled changes.

# July 8th, 2018
- **PROMOTION** GET /v2/universe/structures/{structure_id}/ (dev -> latest)
- **PROMOTION** GET /v4/universe/systems/{system_id}/ (dev -> latest)
- **PROMOTION** GET /v2/corporations/{corporation_id}/orders/history/ (dev -> latest)
- **PROMOTION** GET /v3/corporations/{corporation_id}/orders/ (dev -> latest)
- **DEPRECATION** GET /v1/universe/structures/{structure_id}/ (latest -> legacy)
- **DEPRECATION** GET /v3/universe/systems/{system_id}/ (latest -> legacy)
- **DEPRECATION** GET /v1/corporations/{corporation_id}/orders/history/ (latest -> legacy)
- **DEPRECATION** GET /v2/corporations/{corporation_id}/orders/ (latest -> legacy)
- **REMOVAL** GET /v2/universe/systems/{system_id}
- **REMOVAL** GET /v1/corporations/{corporation_id}/orders/

# June 27, 2018

- **PROMOTION** GET /v2/fw/systems/ (dev -> latest)
- **DEPRECATION** GET /v1/fw/systems/ (latest -> legacy)

# June 7, 2018

- **PROMOTION** GET /v2/alliances/{alliance_id}/contacts/ (dev -> latest)
- **PROMOTION** GET /v2/characters/{character_id}/contacts/ (dev -> latest)
- **PROMOTION** GET /v2/corporations/{corporation_id}/contacts/ (dev -> latest)
- **PROMOTION** POST /v2/characters/{character_id}/contacts/ (dev -> latest)
- **PROMOTION** PUT /v2/characters/{character_id}/contacts/ (dev -> latest)

# May 29th, 2018

**New routes**
- GET /v1/dogma/dynamic/items/{type_id}/{item_id}/ (dev, latest, legacy)
- GET /v2/universe/structures/{structure_id}/ (dev)
    - Add `owner_id` as required attribute
- GET /v4/universe/systems/{system_id}/ (dev)
    - Change attributes `star_id` and `planets` to be optional
- GET /v2/corporations/{corporation_id}/orders/history/ (dev)
    - Add required attribute `issued_by`
- GET /v3/corporations/{corporation_id}/orders/ (dev)
    - Add required attribute `issued_by`

**Changes to existing routes**
- GET /v3/corporations/{corporation_id}/assets/ (dev, latest)
    - Add optional `is_blueprint_copy` attribute
- GET /v3/characters/{character_id}/assets/ (dev, latest)
    - Add optional `is_blueprint_copy` attribute

# May 22nd, 2018

- GET /v1/corporations/{corporation_id}/killmails/recent/
    - Remove `max_kill_id` query parameter.
    - X-pages pagination added.


- GET /v1/characters/{character_id}/killmails/recent/
    - Remove `max_kill_id` and `max_count` query parameters.
    - X-pages pagination added.

# May 18, 2018

- **REMOVAL** GET /v1/characters/{character_id}/chat_channels/

# May 16th, 2018

- GET /v2/fw/systems/ (dev)

# May 15th, 2018

- GET /v1/markets/{region_id}/orders/ -- maxItems dropped from 10,000 -> 1,000

# May 4th, 2018

- GET /v2/universe/stations/{station_id}/ -- Cache time changed to daily at 11:05

# Apr 27, 2018

- **DEPRECATION** GET /v1/characters/{character_id}/chat_channels/ (latest -> legacy)

# Apr 26, 2018

**New routes**

- [GET /v1/alliances/{alliance_id}/contacts/labels/](https://esi.evetech.net/ui/#/Contacts/get_alliances_alliance_id_contacts_labels)
- [GET /v1/corporations/{corporation_id}/contacts/labels/](https://esi.evetech.net/ui/#/Contacts/get_corporations_corporation_id_contacts_labels)

**New versions of existing routes**

- GET /v2/alliances/{alliance_id}/contacts/
- GET /v2/characters/{character_id}/contacts/
- GET /v2/corporations/{corporation_id}/contacts/
- POST /v2/characters/{character_id}/contacts/
- PUT /v2/characters/{character_id}/contacts/
- DELETE /v2/characters/{character_id}/contacts/

**Route promotions and removals**

- **PROMOTION** GET /latest/characters/{character_id}/wallet/journal/ (v4)
- **PROMOTION** GET /latest/corporations/{corporation_id}/wallets/{division}/journal/ (v3)
- **REMOVAL** GET /v2/characters/{character_id}/wallet/journal/
- **REMOVAL** GET /v1/corporations/{corporation_id}/wallets/{division}/journal/

# Apr 6, 2018

- GET /latest/universe/asteroid_belts/{asteroid_belt_id}/ (v1)

**Updates to existing endpoints:**

- `system_id` added to `/v1/markets/{region_id}/orders/`
- `asteroid_belts` added to `planets` object in response from `/v3/universe/systems/{system_id}/`

# Apr 3, 2018

- **REMOVAL** GET /legacy/corporations/{corporation_id}/assets/ (v1)
- **PROMOTION** GET /latest/corporations/{corporation_id}/assets/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/notifications/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/blueprints/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/containers/logs/ (v2)

# Mar 15, 2018

- GET /dev/characters/{character_id}/wallet/journal/ (v4)
- GET /dev/corporations/{corporation_id}/wallets/{division}/journal/ (v3)

# Mar 8, 2018

- **PROMOTION** GET /latest/corporations/{corporation_id}/orders/ (v2)
- **PROMOTION** GET /latest/characters/{character_id}/orders/ (v2)

# Feb 27, 2018

- **REMOVAL** PUT /v1/corporations/{corporation_id}/structures/{structure_id}/

# Feb 20, 2018

- GET /dev/corporations/{corporation_id}/containers/logs/ (v2)
- GET /dev/corporations/{corporation_id}/blueprints/ (v2)
- GET /dev/characters/{character_id}/notifications/ (v2)
- GET /dev/corporations/{corporation_id}/assets/ (v3)

# Feb 13, 2018

- GET /latest/corporations/{corporation_id}/structures/ (v2)

# Feb 7, 2018

- GET /latest/universe/ancestries/ (v1)

# Jan 25, 2018

- GET /dev/corporations/{corporation_id}/orders/ (v2)
- GET /dev/characters/{character_id}/orders/ (v2)
- GET /latest/corporations/{corporation_id}/orders/history/ (v1)
- GET /latest/characters/{character_id}/orders/history/ (v1)

# Dec 28, 2017

- **PROMOTION** GET /latest/characters/{character_id}/stats/ (v2)

# Dec 20, 2017

- **PROMOTION** GET /latest/search/ (v2)
- **PROMOTION** POST /latest/corporations/{corporation_id}/assets/locations/ (v2)
- **PROMOTION** GET /latest/corporations/names/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/wallets/{division}/journal/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/members (v3)
- **PROMOTION** GET /latest/corporations/{corporation_id}/assets/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/ (v4)
- **PROMOTION** DELETE /latest/characters/{character_id}/contacts/ (v2)
- **PROMOTION** POST /latest/characters/{character_id}/cspa/ (v4)
- **PROMOTION** POST /latest/characters/{character_id}/assets/locations/ (v2)
- **PROMOTION** GET /latest/characters/{character_id}/wallet/journal/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/skills/ (v4)
- **PROMOTION** GET /latest/characters/{character_id}/search/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/roles/ (v2)
- **PROMOTION** GET /latest/characters/{character_id}/online/ (v2)
- **PROMOTION** GET /latest/characters/{character_id}/clones/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/assets/ (v3)
- **PROMOTION** GET /latest/alliances/names/ (v2)
- **PROMOTION** GET /latest/alliances/{alliance_id}/ (v3)

# Dec 19, 2017

- POST /latest/universe/ids/ (v1)

# Nov 21, 2017

- GET /latest/corporations/{corporation_id}/outposts/{outpost_id}/ (v1)
- GET /latest/corporations/{corporation_id}/outposts/ (v1)

# Nov 16, 2017

- GET /dev/characters/{character_id}/assets/ (v2)

# Nov 2, 2017

- GET /latest/universe/factions/ (v2)
- GET /latest/characters/{character_id}/wallet/journal/ (v3)
- GET /latest/ corporations/{corporation_id}/wallets/{division}/journal/ (v2)
- GET /latest/corporations/{corporation_id}/fw/stats/ (v1)
- GET /latest/characters/{character_id}/fw/stats/ (v1)

# Oct 31, 2017

- GET /latest/alliances/{alliance_id}/contacts/ (v1)
- GET /latest/corporations/{corporation_id}/members/titles/ (v1)
- GET /latest/corporations/{corporation_id}/starbases/{starbase_id}/ (v1)
- GET /latest/corporations/{corporation_id}/starbases/ (v1)
- GET /latest/corporations/{corporation_id}/roles/history/ (v1)
- GET /latest/corporations/{corporation_id}/medals/issued/ (v1)
- GET /latest/corporations/{corporation_id}/medals/ (v1)
- GET /latest/corporations/{corporation_id}/facilities/ (v1)
- GET /latest/corporations/{corporation_id}/customs_offices/ (v1)
- GET /latest/characters/{character_id}/titles/ (v1)

# Oct 24, 2017

- GET /latest/corporation/{corporation_id}/mining/observers/{observer_id}/ (v1)
- GET /latest/corporation/{corporation_id}/mining/observers/ (v1)
- GET /latest/characters/{character_id}/mining/ (v1)
- GET /latest/characters/{character_id}/bookmarks/folders/ (v2)
- GET /latest/characters/{character_id}/bookmarks/ (v2)

# Oct 17, 2017

- GET /latest/corporations/{corporation_id}/containers/logs/ (v1)

# Oct 12, 2017

- GET /latest/corporations/{corporation_id}/orders/ (v1)
- GET /latest/corporations/{corporation_id}/industry/jobs/ (v1)
- GET /latest/corporations/{corporation_id}/standings/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/{contract_id}/bids/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/{contract_id}/items/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/ (v1)
- POST /latest/corporations/{corporation_id}/assets/locations/ (v1)
- POST /latest/corporations/{corporation_id}/assets/names/ (v1)

# Oct 10, 2017

- GET /latest/corporations/{corporation_id}/bookmarks/folders/ (v1)
- GET /latest/corporations/{corporation_id}/bookmarks/ (v1)
- GET /dev/characters/{character_id}/bookmarks/folders/ (v2)
- GET /dev/characters/{character_id}/bookmarks/ (v2)

# Oct 6, 2017

- GET /latest/characters/{character_id}/wallet/journal (v2)
- GET /latest/universe/types/{type_id} (v3)
- GET /latest/characters/{character_id}/blueprints/ (v2)

# Sep 25, 2017

- GET /latest/corporations/{corporation_id}/titles (v1)
- POST /latest/characters/{character_id}/assets/locations (v1)
- POST /latest/characters/{character_id}/assets/names (v1)

# Sep 21, 2017

- GET /latest/corporations/{corporation_id}/blueprints (v1)

# Sep 19, 2017

- GET /latest/characters/{character_id}/calendar/{event_id}/attendees (v1)

# Sep 13, 2017

- GET /latest/corporations/{corporation_id}/wallets/{division}/transactions (v1)
- GET /latest/corporations/{corporation_id}/assets (v1)
- GET /latest/characters/{character_id}/assets (v1, **spec breaking**) Migrate to a pagination style

# Sep 7, 2017

- GET /latest/corporations/{corporation_id}/contacts (v1)
- GET /latest/corporations/{corporation_id}/members/limit (v1)
- GET /latest/corporations/{corporation_id}/divisions/ (v1)

# Sep 5, 2017

- GET /dev/characters/{character_id}/blueprints/ (v2)

# Sep 1, 2017

- GET /latest/universe/systems/{system_id}/ (v3)

# Aug 30, 2017

- GET /latest/corporations/{corporation_id}/wallets/{division}/journal (v1)
- GET /latest/corporations/{corporation_id}/killmails/recent (v1)

# Aug 29, 2017

- GET /dev/characters/{character_id}/roles/ (v2)
- GET /latest/characters/{character_id}/notifications/contacts/ (v1)

# Aug 25, 2017

- GET /latest/characters/{character_id}/planets/{planet_id}/ (v3)

# Aug 23, 2017

- GET /latest/corporations/{corporation_id}/wallets/ (v1)
- GET /latest/corporations/{corporation_id}/membertracking/ (v1)
- GET /dev/alliances/{alliance_id}/ (v3)
- GET /latest/fw/systems/ (v1)
- GET /latest/fw/leaderboards/corporations/ (v1)
- GET /latest/fw/leaderboards/characters/ (v1)
- GET /latest/fw/leaderboards/ (v1)

# Aug 3, 2017

- GET /latest/fw/stats/ (v1)
- GET /latest/fw/wars/ (v1)

# Aug 2, 2017

- **REMOVAL** GET /legacy/universe/types/{type_id} (v1)
- **REMOVAL** GET /legacy/characters/{character_id}/clones/ (v1)
- GET /latest/universe/system_kills/ (v2)
- GET /latest/dogma/effects/{effect_id} (v2)
- **REMOVAL** GET /legacy/characters/{character_id}/wallets/journal (v1)
- **REMOVAL** GET /legacy/characters/{character_id}/wallets (v1)

# Jul 20, 2017

- GET /latest/characters/{character_id}/fatigue (v1)
- GET /latest/corporations/{corporation_id}/alliancehistory/ (v2)
- GET /dev/characters/{character_id}/clones (v3)
- GET /dev/universe/types/{type_id} (v3) Add `packaged_volume` (#125)
- GET /latest/characters/{character_id}/implants (v1)

# Jul 4, 2017

- GET /dev/dogma/effects/{effect_id} (v2) Make `domain` optional
- GET /latest/characters/{character_id}/wallet/transactions (v1)
- GET /latest/characters/{character_id}/wallet/journal (v1) Moved from /wallets/journal
- GET /latest/characters/{character_id}/wallet (v1) Moved from /wallets
- GET /dev/characters/{character_id}/skills (v4) Add `unallocated_sp`
- GET /latest/characters/{character_id}/attributes (v1)

# Jun 21, 2017

- GET /dev/corporations/names (v2)
- GET /dev/alliances/names (v2)

# Jun 20, 2017

- GET /dev/characters/{character_id}/skills/ (v4)
- GET /latest/characters/{character_id}/wallets/journal (v1)
- GET /latest/characters/{character_id}/contracts/{contract_id}/bids (v1)
- GET /latest/characters/{character_id}/contracts/{contract_id}/items (v1)
- GET /latest/characters/{character_id}/contracts (v1)

# Jun 13, 2017

- GET /dev/characters/{character_id}/online/ (v2) #424

# May 16, 2017

- GET /dev/dogma/effects/{effect_id}/ (v2)

# May 9, 2017

- GET /latest/characters/{character_id}/blueprints (v1)
- GET /latest/characters/{character_id}/industry/jobs (v1)
- GET /latest/characters/{character_id}/orders (v1)

# Apr 11, 2017

- GET /latest/status/ (v1) #88

# Mar 30, 2017

- GET /latest/universe/system_kills (v1)
- GET /latest/universe/system_jumps (v1)
- GET /latest/sovereignty/map (v1)
- GET /latest/characters/{character_id}/agents_research (v1)
- GET /latest/characters/{character_id}/standings (v1)
- GET /latest/characters/{character_id}/medals (v1)
- GET /latest/characters/{character_id}/chat_channels (v1)

# Mar 1, 2017

- GET /dev/universe/types/{type_id} (v3) #276
- GET /latest/markets/groups/{group_id} (v1) #156
- GET /latest/markets/groups (v1) #156

# Feb 23, 2017

- GET /latest/universe/graphics/{graphic_id}/ (v1)
- GET /latest/universe/graphics/ (v1)
- PUT /latest/corporations/{corporation_id}/structures/{structure_id} / (v1)
- GET /latest/corporations/{corporation_id}/structures/ (v1)
- GET /latest/dogma/effects/{effect_id}/ (v1)
- GET /latest/dogma/effects/ (v1)
- GET /latest/dogma/attributes/{attribute_id}/ (v1)
- GET /latest/dogma/attributes/ (v1)
- GET /latest/corporations/{corporation_id}/ (v3)
- GET /latest/characters/{character_id}/planets/{planet_id}/ (v2)

# Feb 20, 2017

- /latest/characters/{character_id}/loyalty/points/ (v1)
- /latest/loyalty/stores/{corporation_id}/offers/ (v1)

# Feb 14, 2017

- /latest/universe/systems/{system_id}/ (v2)
- /latest/universe/stations/{station_id}/ (v2)

# Feb 7, 2017

- /dev/universe/stations/{station_id}/ (v2)
- /latest/universe/stargates/{stargate_id}/ (v1)
- /latest/universe/planets/{planet_id}/ (v1)
- /latest/universe/moons/{moon_id}/ (v1)
- /dev/universe/systems/{system_id}/ (v2)
- /latest/universe/systems/ (v1)
- /latest/universe/constellations/{constellation_id}/ (v1)
- /latest/universe/constellations/ (v1)
- /latest/universe/regions/{region_id}/ (v1)
- /latest/universe/regions/ (v1)

# Jan 31, 2017

- /latest/universe/bloodlines/ (v1)
- /latest/universe/names/ (v2) #186
- /latest/characters/<char_id>/ (v4) #221

# Jan 26, 2017

- /latest/universe/factions/ (v1)

# Jan 24, 2017

- /dev/characters/<char_id>/ (v4) #221
- /latest/wars/ (v1, spec breaking change) #228
- /latest/universe/races/ (v1) #147

# Nov 30, 2016

- GET /dev/corporations/{corporation_id}/assets/ (v2)
- GET /dev/characters/{character_id}/assets/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/assets/ (v2)
