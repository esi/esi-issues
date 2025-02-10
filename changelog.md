Historical reference of endpoint additions and changes made in ESI.

Dates in the future are upcoming scheduled changes.

# 2025-02-10
- **REMOVAL**:
  - `/characters/{character_id}/bookmarks/`
  - `/characters/{character_id}/bookmarks/folders/`
  - `/corporations/{corporation_id}/bookmarks/`
  - `/corporations/{corporation_id}/bookmarks/folders/`
    * Removed `esi-bookmarks` as announced in [this blog post](https://developers.eveonline.com/blog/deprecation-and-impending-removal-of-esi-opportunities-and-esi-bookmarks).

# 2025-02-03
- **DEPRECATION**:
  - `/characters/{character_id}/opportunities/`
  - `/opportunities/groups/`
  - `/opportunities/groups/{group_id}/`
  - `/opportunities/tasks/`
  - `/opportunities/tasks/{task_id}/`
    * Deprecated `esi-opportunities` as announced in [this blog post](https://developers.eveonline.com/blog/deprecation-and-impending-removal-of-esi-opportunities-and-esi-bookmarks).

# 2024-07-16
- **FIX**:
  - `/v6/characters/{character_id}/notifications/`
  - `/v5/characters/{character_id}/notifications/`
    * Add new notification types: StructureLowReagentsAlert and StructureNoReagentsAlert
- **FIX**:
  - `/v1/universe/races/`
    * Fixed the maxItems limit that would cause this endpoint to fail unnecessarily.

# 2024-07-11
- **ENHANCEMENT**:
  - `/v1/route/{origin}/{destination}/`
    * Add stargates for Intaki-Amygnon and Athounon-Samanuni, bump the security status for the Intaki system to `0.6`, as per [this PR](https://github.com/esi/esi-routes/pull/12).
- **ENHANCEMENT**:
  - `/v1/universe/races/`
    * Add the Jove and Triglavian races to the list of returned races.
- **ENHANCEMENT**:
  - `/v1/markets/{region_id}/types/`
    * Update the Swagger spec to indicate a possible 404 response when requests are made to regions that do not exist.
- **ENHANCEMENT**:
  - `/v4/corporations/{corporation_id}/wallets/{division}/journal/`
  - `/v5/corporations/{corporation_id}/wallets/{division}/journal/`
  - `/v6/characters/{character_id}/wallet/journal/`
  - `/v7/characters/{character_id}/wallet/journal/`
    - Add new wallet journal ref types: `under_construction`, `allignment_based_gate_toll`, `project_payouts`, `insurgency_corruption_contribution_reward`, `insurgency_suppression_contribution_reward`, `daily_goal_payouts`, `daily_goal_payouts_tax`, `cosmetic_market_component_item_purchase`, `cosmetic_market_skin_sale_broker_fee`, `cosmetic_market_skin_purchase`, `cosmetic_market_skin_sale`, `cosmetic_market_skin_sale_tax` & `cosmetic_market_skin_transaction`.
- **ENHANCEMENT**:
  - `/v5/characters/{character_id}/notifications/`
  - `/v6/characters/{character_id}/notifications/`
     * Add new notification types `LPAutoRedeemed`, `SPAutoRedeemed`, `SkinSequencingCompleted`, `SkyhookOnline`, `SkyhookLostShields`, `SkyhookUnderAttack`, `SkyhookDestroyed` & `SkyhookDeployed`.
- **ENHANCEMENT**:
  - `/v5/characters/{character_id}/assets/`
  - `/v5/corporations/{corporation_id}/assets/`
    * Add new location flags `InfrastructureHangar` & `MoonMaterialBay`. 
- **ENHANCEMENT**:
  - `/v2/characters/{character_id}/roles/`
  - `/v3/characters/{character_id}/roles/`
  - `/v1/corporations/{corporation_id}/roles/history/`
  - `/v2/corporations/{corporation_id}/roles/history/`
  - `/v1/corporations/{corporation_id}/roles/`
  - `/v2/corporations/{corporation_id}/roles/`
  - `/v1/corporations/{corporation_id}/titles/`
  - `/v2/corporations/{corporation_id}/titles/`
     * Adds corporation `BrandManager` role. 

# 2024-01-25
- **ENHANCEMENT** `/v6/characters/{character_id}/notifications`
  * Adds new notification types: `CorporationGoalNameChange` & `CorporationLeft`.
- **ENHANCEMENT**:
  - `/v2/characters/{character_id}/roles/`;
  - `/v3/characters/{character_id}/roles/`;
  - `/v1/corporations/{corporation_id}/roles/history/`;
  - `/v2/corporations/{corporation_id}/roles/history/`;
  - `/v1/corporations/{corporation_id}/roles/`;
  - `/v2/corporations/{corporation_id}/roles/`;
  - `/v1/corporations/{corporation_id}/titles/`;
  - `/v2/corporations/{corporation_id}/titles/`;
     * Adds corporation `ProjectManager` role. 

# 2023-01-23
- Updates to `/characters/{character_id}/fw/stats`
  * characters that have delisted from factional warfare will still return their statistics from their time of service

# 2023-01-19
- Lowered the cache timer on public character get responses back to 24 hours
  * Please not that it will take a full week for the currently cached records to expire

# 2023-01-13
- Raised the cache timer on public character get responses to full seven days.

# 2023-01-09
- **TEMPORARY REMOVAL** esi-characters/{character_id}/corporationhistory/
  * Routes will return empty lists rather than corporation history once the request cache has expired
  * This affects all versions of endpoint: legacy, dev, latest, v1 and v2

# 2022-07-12
- **REMOVAL** /search
    * Use /characters/{character_id}/search instead to authenticate your search queries
    * `character_id` should be the ID of the character performing the query

# 2022-06-21
- **ENHANCEMENT** /v5/corporations/{corporation_id}/assets/ & /v5/characters/{character_id}/assets/
    * Added new location_flag enum values:
        - "StructureDeedBay";
        - "SpecializedIceHold";
        - "SpecializedAsteroidHold";

# 2021-11-26
- **ENHANCEMENT** /v6/characters/{character_id}/wallet/journal/ & /v4/corporations/{corporation_id}/wallets/{division}/journal/
    * Adds following wallet journal entry ref types to enum:
        - "external_trade_freeze";
        - "external_trade_thaw";
        - "external_trade_delivery";
        - "season_challenge_reward";
        - "skill_purchase";
        - "item_trader_payment";
        - "flux_ticket_sale";
        - "flux_payout";
        - "flux_tax";
        - "flux_ticket_repayment";
        - "redeemed_isk_token";
        - "daily_challenge_reward";
        - "market_provider_tax";
        - "ess_escrow_transfer";
        - "milestone_reward_payment".

# 2021-10-21
- **REMOVAL** /v4/characters/{character_id} (legacy)
    * _The only difference between `v4` and `v5` is the fact that `v4` contains as an optional field `ancestry_id`._

# 2021-09-21
- ~~**REMOVAL** /v4/characters/{character_id} (legacy)~~
    * ~~_The only difference between `v4` and `v5` is the fact that `v4` contains as an optional field `ancestry_id`._~~ **POSTPONED**

# 2021-09-15
- **REMOVAL** /v3/characters/{character_id} (legacy)
- **DEPRECATION** /v4/characters/{character_id} (latest->legacy)
- **PROMOTION** /v5/characters/{character_id} (dev->latest)
    * _The only change introduced by `v5` is removal of an optional field `ancestry_id` so it shouldn't cause problems for any application._

# 2021-07-30
- **NEW** /v5/characters/{character_id} (dev)
  * 'ancestry_id' field removed from response as it's being deprecated / meaningless in the game. 
  * 'v4' stays as 'latest' and will stay so for some time, the deprecation will be announced in advance. 

# 2021-03-22
- **ENHANCEMENT** /v5/characters/{character_id}/notifications/ & /v6/characters/{character_id}/notifications/
  * Added new `type` enum values:
    - "ExpertSystemExpiryImminent"
    - "ExpertSystemExpired"

# 2020-12-16
- **REMOVAL** /characters/{character_id}/stats/
  * Removing esi-characterstats (annoncment made on 20.08.2020 in tweetfleet)

# 2020-12-01
- **ENHANCEMENT** /v1/route/{origin}/{destination}/
  * Updates map data to include changes introduced after Triglavian region remapping.

# 2020-11-25
- **ENHANCEMENT** /v4/corporations/{corporation_id}/wallets/{division}/journal/
  * Added new `ref_type` enum values:
     - "skill_purchase"
     - "item_trader_payment"
     - "ess_escrow_transfer"
     
# 2020-11-09
- **ENHANCEMENT** /v5/characters/{character_id}/notifications/ & /v6/characters/{character_id}/notifications/
  * Added new `type` enum values:
     - "IndustryOperationFinished"
     - "ESSMainBankLink"
- **ENHANCEMENT** /v6/characters/{character_id}/wallet/joiurnal/
  * Added new `ref_type` enum values:
     - "skill_purchase"
     - "item_trader_payment"
     - "ess_escrow_transfer"

# 2020-10-26
- **ENHANCEMENT** /v5/characters/{character_id}/notifications/ & /v6/characters/{character_id}/notifications/
  * Added new `type` enum values:
     - "InvasionSystemStart"
     - "InvasionCompletedMsg"
     - "MissionCanceledTriglavian"
     - "AgentRetiredTrigravian"
     - "StructureImpendingAbandonmentAssetsAtRisk"
     - "OfficeLeaseCanceledInsufficientStandings"
     - "ContractRegionChangedToPochven"
  
# 2020-06-10
- **REMOVAL** /v2/alliance/{alliance_id} (legacy)
- **REMOVAL** GET /v2/characters/{character_id}/calendar/{event_id} (legacy)
- **REMOVAL** PUT /v2/characters/{character_id}/calendar/{event_id} (legacy)

# 2020-05-06
- **REMOVAL** /v1/fw/systems (legacy)
- **REMOVAL** /v1/characters/{character_id}/location (legacy)

# 2020-05-01
**CHANGE OF POLICY ON BREAKING CHANGES**  
_Extending attribute `enums` no longer treated as an endpoint breaking change._

- Starting from now (2020/05/01) spec changes limited to extending enumerations won't be treated as breaking changes and therefore won't require a version bump.  
- We will announce those in the changelog as existing route version _ENHANCEMENT_ and the changes will be made with just one day of prior notice.
- Please adjust your applications to treat all `string` attributes accompanied with enumerations simply as `string`. 

# 2020-04-08

- **REMOVAL** of scopes from SSO:
   - esi-corporations.read_outposts.v1;
   - esi-corporations.write_structures.v1.
   
*These scopes do not serve any purpose for a long time now but we see that some applications still request them. If those applications won't be fixed, they will break after scopes removal.* 

# 2020-04-08
- **REMOVAL** /v3/characters/{character_id}/assets/ (legacy)
- **DEPRECATION** /v4/characters/{character_id}/assets/ (latest->legacy)
- **PROMOTION** /v5/characters/{character_id}/assets/ (dev->latest)
- **REMOVAL** /v3/corporations/{corporation_id}/assets/ (legacy)
- **DEPRECATION** /v4/corporations/{corporation_id}/assets/ (latest->legacy)
- **PROMOTION** /v5/corporations/{corporation_id}/assets/ (dev->latest)

# 2020-03-26
- **REVERSAL** /v3/characters/{character_id}/assets/
  * Removed new location_flag enum value: FrigateEscapeBay.
- **REVERSAL** /v4/characters/{character_id}/assets/
  * Removed new location_flag enum value: FrigateEscapeBay.
- **REVERSAL** /v3/corporations/{corporation_id}/assets/
  * Removed new location_flag enum value: FrigateEscapeBay.
- **REVERSAL** /v4/corporations/{corporation_id}/assets/
  * Removed new location_flag enum value: FrigateEscapeBay.
- **NEW** /v5/characters/{character_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.
- **NEW** /v5/corporations/{corporation_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.

# 2020-03-25
- **ENHANCEMENT** /v3/characters/{character_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.
- **ENHANCEMENT** /v4/characters/{character_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.
- **ENHANCEMENT** /v3/corporations/{corporation_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.
- **ENHANCEMENT** /v4/corporations/{corporation_id}/assets/
  * Added new location_flag enum value: FrigateEscapeBay.
  
# 2020-03-17
- **NEW** /v2/alliances/{alliance_id}/icons (dev)
  * 'New image server URL paths. 
- **NEW** /v2/corporations/{corporation_id}/icons	 (dev)
  * 'New image server URL paths. 
- **NEW** /v2/characters/{character_id}/potrait (dev)
  * 'New image server URL paths. 
  
# 2020-03-02

- **REMOVAL** /v2/corporations/{corporation_id}/assets/
- **DEPRECATION** /v3/corporations/{corporation_id}/assets/ (latest->legacy)
- **PROMOTION** /v4/corporations/{corporation_id}/assets/ (dev->latest)
- **REMOVAL** /v2/characters/{character_id}/assets/
- **DEPRECATION** /v3/characters/{character_id}/assets/ (latest->legacy)
- **PROMOTION** /v4/characters/{character_id}/assets/ (dev->latest)

- **DEPRECATION** /v4/characters/{character_id}/notifications/ (latest->legacy)
- **PROMOTION** /v5/characters/{character_id}/notifications/ (dev->latest)

# 2020-01-23
- **NEW** /v4/corporations/{corporation_id}/assets/
  * 'item' location type was added to `location_type` enum
- **NEW** /v4/characters/{character_id}/assets/
  * 'item' location type was added to `location_type` enum
  
# 2020-01-14
- **REMOVAL** Singularity server removed as data source.
  * https://developers.eveonline.com/blog/article/removing-datasource-singularity

# 2019-11-25 
- **DEPRECATION** /characters/{character_id}/bookmarks/
- **DEPRECATION** /characters/{character_id}/bookmarks/folders/
- **DEPRECATION** /corporations/{corporation_id}/bookmarks/
- **DEPRECATION** /corporations/{corporation_id}/bookmarks/folders/
  * All Bookmarks routes are deprecated as a result of the new Bookmark system. They will return only an empty list.
  * New bookmark endpoints not yet released.
  * https://developers.eveonline.com/blog/article/temporary-blackout-of-esi-bookmarks

# 2019-11-21
- **CHANGE** /v4/characters/{character_id}/
  * Cache timer changed to 24hrs. 
  * Emergency change due to server instability caused by scraping.
  * Did not result in a version change.

# 2019-08-13
- **ENHANCEMENT** /v5/characters/{character_id}/notifications/
  * Added support for new notification types.
  
# 2019-07-15
- **REMOVAL** /v2/characters/{character_id}/search/
- **REMOVAL** /v1/search/

# 2019-07-10
- **REMOVAL** /v3/characters/{character_id}/notifications/
- **DEPRECATION** /v4/characters/{character_id}/notifications/ (latest->legacy)
- **PROMOTION** /v5/characters/{character_id}/notifications/ (dev->latest)

# 2019-06-19
- **ENHANCEMENT** /v5/characters/{character_id}/notifications/
  * Added support for new war and invasion notifications

# 2019-06-06
- **BUGFIX** /v1/universe/planets/{planet_id}/
  * Fixed a bug making the endpoint return data about a star if star ID was set instead of planet ID. 

# 2019-05-23
- **BUGFIX** /v3/characters/{character_id}/search/
  * Fixed "internal error" when searching some unicode strings
- **BUGFIX** /v2/search/
  * Fixed "internal error" when searching some unicode strings

# 2019-05-20
- **ENHANCEMENT** /v2/characters/{character_id}/skillqueue/
  * Added extra doc to better explain how finish_date works
- **NEW** /v5/characters/{character_id}/notifications/ (dev)
  * Added support for notifications relating to war system iterations

# 2019-05-15
- **REMOVAL** /v4/characters/{character_id}/wallet/journal/
- **DEPRECATION** /v5/characters/{character_id}/wallet/journal/ (latest->legacy)
- **PROMOTION** /v6/characters/{character_id}/wallet/journal/ (dev->latest)

# 2019-04-10
- **ENHANCEMENT** GET /v4/characters/{character_id}/
  * Add individual title if applicable, as per definition here: https://support.eveonline.com/hc/en-us/articles/203218352-Titles

# 2019-04-09
- **BUGFIX** PUT /v1/fleets/{fleet_id}/members/{member_id}/
    * Fix issues relating to moving people into the squad commander role: https://github.com/esi/esi-issues/issues/690
    * More specific errors if an invalid combination of wing id's, squad id's and roles is passed into the endpoint
- **BUGFIX** POST /v1/fleets/{fleet_id}/members/
    * Same as above
- **NEW** GET /v2/characters/{character_id}/fleet
    * Adds support for returning the current fleet boss, allowing discovery of the new fleet boss in cases of mass disconnects

# 2019-03-20
- **NEW** /v6/characters/{character_id}/wallet/journal/ (dev)
  * add support for skill_purchase journal entry
  * add support for item_trader_payment journal entry

# 2019-03-18
- **DEPRECATION** GET /v1/characters/{character_id}/fittings/ (latest->legacy)
- **PROMOTION** GET /v2/characters/{character_id}/fittings/ (dev->latest)
- **DEPRECATION** POST /v1/characters/{character_id}/fittings/ (latest->legacy)
- **PROMOTION** POST /v2/characters/{character_id}/fittings/ (dev->latest)

# 2019-03-11
- **REMOVAL** POST /v1/universe/names/
- **DEPRECATION** POST /v2/universe/names/ (latest->legacy)
- **PROMOTION** POST /v3/universe/names/ (dev->latest)

# 2019-01-28
- **NEW** GET /v2/characters/{character_id}/fittings/ (dev)
  * Add enum for slot/bay flags
- **NEW** POST /v2/characters/{character_id}/fittings/ (dev)
  * Add enum for slot/bay flags

# 2019-01-24
- **REMOVAL** POST /v1/ui/autopilot/waypoint/
- **PROMOTION** POST /v2/ui/autopilot/waypoint/ (latest->latest+legacy)
- **NEW** POST /v3/universe/names/ (dev)
  * Add support for factions

# 2019-01-22
- **BUGFIX** /v1/markets/{region_id}/types/ - No longer returns duplicate type ids
- **BUGFIX** /v1/universe/constellations/{constellation_id}/ - No longer 500 errors if an invalid constellation ID is given
- **BUGFIX** /v3/corporations/{corporation_id}/structures/ - No longer 500 errors if results contain a recently updated flex structure

# 2019-01-21
- **BUGFIX** /v1/corporations/{corporation_id}/customs_offices/ - No longer 500 errors if results contain an unconfigured customs office

# 2019-01-18
- GET /v1/characters/{character_id}/implants/ Cache lowered to 120 seconds
- GET /v1/characters/{character_id}/attributes/ Cache lowered to 120 seconds
- POST /v1/universe/ids/ -> MaxItems in both request and response lowered to 500
  * Note: technically this is a breaking change, but this endpoint errored for requests larger than 500 anyway, so this simply formalises reality. 

# 2019-01-14
- **PROMOTION** GET /v3/corporations/{corporation_id}/structures/ (dev -> latest)
- **DEPRECATION** GET /v2/corporations/{corporation_id}/structures/ (latest -> legacy)
- **REMOVAL** GET /v1/corporations/{corporation_id}/structures/
- **PROMOTION** GET /v5/characters/{character_id}/wallet/journal/  (dev -> latest)
- **PROMOTION** GET /v4/corporations/{corporation_id}/wallets/{division}/journal/  (dev -> latest)
- **DEPRECATION** GET /v4/characters/{character_id}/wallet/journal/ (latest -> legacy)
- **DEPRECATION** GET /v3/corporations/{corporation_id}/wallets/{division}/journal/ (latest -> legacy)

# 2018-12-11
- **PROMOTION** GET /v4/characters/{character_id}/notifications/ (dev -> latest)
- **DEPRECATION** GET /v3/characters/{character_id}/notifications/ (latest -> legacy)
- **REMOVAL** GET /v2/characters/{character_id}/notifications/
- **ENHANCEMENT** GET /v4/corporations/{corporation_id}/
  - add war_eligible bool
- **ENHANCEMENT** GET /v1/universe/structures/
  - add "market" and "manufacturing_basic" service filters
  
# 2018-12-10
- **BUGFIX** GET /v1/corporations/{corporation_id}/industry/jobs/
  - Fix for https://github.com/esi/esi-issues/issues/1053
- **BUGFIX** GET /v1/characters/{character_id}/industry/jobs/
  - Fix for https://github.com/esi/esi-issues/issues/1053

# 2018-11-29
- GET /v3/corporations/{corporation_id}/structures/
    - Attribute reinforce_weekday became optional.
    - [New structure state type](https://github.com/esi/eve-glue/commit/1f20a5eaba85179031f0848316ccb4f3f2922f05#diff-00a0945a33de4aa1d938a32af65496bcR23)

# 2018-11-21
- GET /v5/characters/{character_id}/wallet/journal/ (dev)
    - [New wallet journal ref type](https://github.com/esi/eve-glue/commit/f98efea05b9cc906754a9d989a2f29915cce958c#diff-9587688122f96b612670ae031fb74f75R133) added.
- GET /v4/corporations/{corporation_id}/wallets/{division}/journal/ (dev)
    - [New wallet journal ref type](https://github.com/esi/eve-glue/commit/f98efea05b9cc906754a9d989a2f29915cce958c#diff-9587688122f96b612670ae031fb74f75R133) added.

# 2018-10-30
- GET /v4/characters/{character_id}/notifications/ (dev)
    - [New notification types](https://github.com/esi/eve-glue/commit/6d8c2caf2ba4feacae95bc6b72f915345c5c330c#diff-ae236f83a42263e6217db24918f8d0c9R203) added.

# 2018-10-10
- GET /v1/markets/structures/{structure_id}/
    - Pagination maxItems dropped from 5000 -> 1000

# 2018-09-14

- **PROMOTION** GET /v3/characters/{character_id}/notifications/ (dev -> latest)
- **DEPRECATION** GET /v2/characters/{character_id}/notifications/ (latest -> legacy)
- **REMOVAL** GET /v1/characters/{character_id}/notifications/

# 2018-08-23

- GET /v1/contracts/public/{region_id}/ (dev, latest, legacy)
- GET /v1/contracts/public/bids/{contract_id}/ (dev, latest, legacy)
- GET /v1/contracts/public/items/{contract_id}/ (dev, latest, legacy)

# 2018-08-03

- GET /v3/characters/{character_id}/notifications/ (dev)
    - [New notification types](https://github.com/esi/eve-glue/commit/d1c8ba8142cf59cb4115707d2cdc126420c1c2c2#diff-ae236f83a42263e6217db24918f8d0c9R204) added.

# 2018-07-08
- **PROMOTION** GET /v2/universe/structures/{structure_id}/ (dev -> latest)
- **PROMOTION** GET /v4/universe/systems/{system_id}/ (dev -> latest)
- **PROMOTION** GET /v2/corporations/{corporation_id}/orders/history/ (dev -> latest)
- **PROMOTION** GET /v3/corporations/{corporation_id}/orders/ (dev -> latest)
- **DEPRECATION** GET /v1/universe/structures/{structure_id}/ (latest -> legacy)
- **DEPRECATION** GET /v3/universe/systems/{system_id}/ (latest -> legacy)
- **DEPRECATION** GET /v1/corporations/{corporation_id}/orders/history/ (latest -> legacy)
- **DEPRECATION** GET /v2/corporations/{corporation_id}/orders/ (latest -> legacy)
- **REMOVAL** GET /v2/universe/systems/{system_id}/
- **REMOVAL** GET /v1/corporations/{corporation_id}/orders/
- **REMOVAL** GET /v1/corporations/{corporation_id}/outposts/
- **REMOVAL** GET /v1/corporations/{corporation_id}/outposts/{outpost_id}/

# 2018-06-27

- **PROMOTION** GET /v2/fw/systems/ (dev -> latest)
- **DEPRECATION** GET /v1/fw/systems/ (latest -> legacy)

# 2018-06-21
- **REMOVAL** GET /v1/alliances/names/
- **REMOVAL** GET /v2/alliances/names/

# 2018-06-18

- **REMOVAL** GET /v1/characters/names/
- **REMOVAL** GET /v1/corporations/names/
- **REMOVAL** GET /v2/corporations/names/
- **REMOVAL** GET /v2/corporations/{corporation_id}/wallet/journal/
- **REMOVAL** GET /v3/characters/{character_id}/wallet/journal/

# 2018-06-07

- **PROMOTION** GET /v2/alliances/{alliance_id}/contacts/ (dev -> latest)
- **PROMOTION** GET /v2/characters/{character_id}/contacts/ (dev -> latest)
- **PROMOTION** GET /v2/corporations/{corporation_id}/contacts/ (dev -> latest)
- **PROMOTION** POST /v2/characters/{character_id}/contacts/ (dev -> latest)
- **PROMOTION** PUT /v2/characters/{character_id}/contacts/ (dev -> latest)

# 2018-05-29

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

# 2018-05-22

- GET /v1/corporations/{corporation_id}/killmails/recent/
    - Remove `max_kill_id` query parameter.
    - X-pages pagination added.


- GET /v1/characters/{character_id}/killmails/recent/
    - Remove `max_kill_id` and `max_count` query parameters.
    - X-pages pagination added.

# 2018-05-18

- **REMOVAL** GET /v1/characters/{character_id}/chat_channels/

# 2018-05-16

- GET /v2/fw/systems/ (dev)

# 2018-05-15

- GET /v1/markets/{region_id}/orders/ -- maxItems dropped from 10,000 -> 1,000

# 2018-05-04

- GET /v2/universe/stations/{station_id}/ -- Cache time changed to daily at 11:05

# 2018-04-27

- **DEPRECATION** GET /v1/characters/{character_id}/chat_channels/ (latest -> legacy)

# 2018-04-26

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

# 2018-04-06

- GET /latest/universe/asteroid_belts/{asteroid_belt_id}/ (v1)

**Updates to existing endpoints:**

- `system_id` added to `/v1/markets/{region_id}/orders/`
- `asteroid_belts` added to `planets` object in response from `/v3/universe/systems/{system_id}/`

# 2018-04-03

- **REMOVAL** GET /legacy/corporations/{corporation_id}/assets/ (v1)
- **PROMOTION** GET /latest/corporations/{corporation_id}/assets/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/notifications/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/blueprints/ (v2)
- **PROMOTION** GET /latest/corporations/{corporation_id}/containers/logs/ (v2)

# 2018-03-15

- GET /dev/characters/{character_id}/wallet/journal/ (v4)
- GET /dev/corporations/{corporation_id}/wallets/{division}/journal/ (v3)

# 2018-03-08

- **PROMOTION** GET /latest/corporations/{corporation_id}/orders/ (v2)
- **PROMOTION** GET /latest/characters/{character_id}/orders/ (v2)

# 2018-02-27

- **REMOVAL** PUT /v1/corporations/{corporation_id}/structures/{structure_id}/

# 2018-02-20

- GET /dev/corporations/{corporation_id}/containers/logs/ (v2)
- GET /dev/corporations/{corporation_id}/blueprints/ (v2)
- GET /dev/characters/{character_id}/notifications/ (v2)
- GET /dev/corporations/{corporation_id}/assets/ (v3)

# 2018-02-13

- GET /latest/corporations/{corporation_id}/structures/ (v2)

# 2018-02-07

- GET /latest/universe/ancestries/ (v1)

# 2018-01-25

- GET /dev/corporations/{corporation_id}/orders/ (v2)
- GET /dev/characters/{character_id}/orders/ (v2)
- GET /latest/corporations/{corporation_id}/orders/history/ (v1)
- GET /latest/characters/{character_id}/orders/history/ (v1)

# 2017-12-28

- **PROMOTION** GET /latest/characters/{character_id}/stats/ (v2)

# 2017-12-20

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

# 2017-12-19

- POST /latest/universe/ids/ (v1)

# 2017-11-21

- GET /latest/corporations/{corporation_id}/outposts/{outpost_id}/ (v1)
- GET /latest/corporations/{corporation_id}/outposts/ (v1)

# 2017-11-16

- GET /dev/characters/{character_id}/assets/ (v2)

# 2017-11-02

- GET /latest/universe/factions/ (v2)
- GET /latest/characters/{character_id}/wallet/journal/ (v3)
- GET /latest/ corporations/{corporation_id}/wallets/{division}/journal/ (v2)
- GET /latest/corporations/{corporation_id}/fw/stats/ (v1)
- GET /latest/characters/{character_id}/fw/stats/ (v1)

# 2017-10-31

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

# 2017-10-24

- GET /latest/corporation/{corporation_id}/mining/observers/{observer_id}/ (v1)
- GET /latest/corporation/{corporation_id}/mining/observers/ (v1)
- GET /latest/characters/{character_id}/mining/ (v1)
- GET /latest/characters/{character_id}/bookmarks/folders/ (v2)
- GET /latest/characters/{character_id}/bookmarks/ (v2)

# 2017-10-17

- GET /latest/corporations/{corporation_id}/containers/logs/ (v1)

# 2017-10-12

- GET /latest/corporations/{corporation_id}/orders/ (v1)
- GET /latest/corporations/{corporation_id}/industry/jobs/ (v1)
- GET /latest/corporations/{corporation_id}/standings/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/{contract_id}/bids/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/{contract_id}/items/ (v1)
- GET /latest/corporations/{corporation_id}/contracts/ (v1)
- POST /latest/corporations/{corporation_id}/assets/locations/ (v1)
- POST /latest/corporations/{corporation_id}/assets/names/ (v1)

# 2017-10-10

- GET /latest/corporations/{corporation_id}/bookmarks/folders/ (v1)
- GET /latest/corporations/{corporation_id}/bookmarks/ (v1)
- GET /dev/characters/{character_id}/bookmarks/folders/ (v2)
- GET /dev/characters/{character_id}/bookmarks/ (v2)

# 2017-10-06

- GET /latest/characters/{character_id}/wallet/journal (v2)
- GET /latest/universe/types/{type_id} (v3)
- GET /latest/characters/{character_id}/blueprints/ (v2)

# 2017-09-25

- GET /latest/corporations/{corporation_id}/titles (v1)
- POST /latest/characters/{character_id}/assets/locations (v1)
- POST /latest/characters/{character_id}/assets/names (v1)

# 2017-09-21

- GET /latest/corporations/{corporation_id}/blueprints (v1)

# 2017-09-19

- GET /latest/characters/{character_id}/calendar/{event_id}/attendees (v1)

# 2017-09-13

- GET /latest/corporations/{corporation_id}/wallets/{division}/transactions (v1)
- GET /latest/corporations/{corporation_id}/assets (v1)
- GET /latest/characters/{character_id}/assets (v1, **spec breaking**) Migrate to a pagination style

# 2017-09-07

- GET /latest/corporations/{corporation_id}/contacts (v1)
- GET /latest/corporations/{corporation_id}/members/limit (v1)
- GET /latest/corporations/{corporation_id}/divisions/ (v1)

# 2017-09-05

- GET /dev/characters/{character_id}/blueprints/ (v2)

# 2017-09-01

- GET /latest/universe/systems/{system_id}/ (v3)

# 2017-08-30

- GET /latest/corporations/{corporation_id}/wallets/{division}/journal (v1)
- GET /latest/corporations/{corporation_id}/killmails/recent (v1)

# 2017-08-29

- GET /dev/characters/{character_id}/roles/ (v2)
- GET /latest/characters/{character_id}/notifications/contacts/ (v1)

# 2017-08-25

- GET /latest/characters/{character_id}/planets/{planet_id}/ (v3)

# 2017-08-23

- GET /latest/corporations/{corporation_id}/wallets/ (v1)
- GET /latest/corporations/{corporation_id}/membertracking/ (v1)
- GET /dev/alliances/{alliance_id}/ (v3)
- GET /latest/fw/systems/ (v1)
- GET /latest/fw/leaderboards/corporations/ (v1)
- GET /latest/fw/leaderboards/characters/ (v1)
- GET /latest/fw/leaderboards/ (v1)

# 2017-08-03

- GET /latest/fw/stats/ (v1)
- GET /latest/fw/wars/ (v1)

# 2017-08-02

- **REMOVAL** GET /legacy/universe/types/{type_id} (v1)
- **REMOVAL** GET /legacy/characters/{character_id}/clones/ (v1)
- GET /latest/universe/system_kills/ (v2)
- GET /latest/dogma/effects/{effect_id} (v2)
- **REMOVAL** GET /legacy/characters/{character_id}/wallets/journal (v1)
- **REMOVAL** GET /legacy/characters/{character_id}/wallets (v1)

# 2017-07-20

- GET /latest/characters/{character_id}/fatigue (v1)
- GET /latest/corporations/{corporation_id}/alliancehistory/ (v2)
- GET /dev/characters/{character_id}/clones (v3)
- GET /dev/universe/types/{type_id} (v3) Add `packaged_volume` (#125)
- GET /latest/characters/{character_id}/implants (v1)

# 2017-07-04

- GET /dev/dogma/effects/{effect_id} (v2) Make `domain` optional
- GET /latest/characters/{character_id}/wallet/transactions (v1)
- GET /latest/characters/{character_id}/wallet/journal (v1) Moved from /wallets/journal
- GET /latest/characters/{character_id}/wallet (v1) Moved from /wallets
- GET /dev/characters/{character_id}/skills (v4) Add `unallocated_sp`
- GET /latest/characters/{character_id}/attributes (v1)

# 2017-06-21

- GET /dev/corporations/names (v2)
- GET /dev/alliances/names (v2)

# 2017-06-20

- GET /dev/characters/{character_id}/skills/ (v4)
- GET /latest/characters/{character_id}/wallets/journal (v1)
- GET /latest/characters/{character_id}/contracts/{contract_id}/bids (v1)
- GET /latest/characters/{character_id}/contracts/{contract_id}/items (v1)
- GET /latest/characters/{character_id}/contracts (v1)

# 2017-06-13

- GET /dev/characters/{character_id}/online/ (v2) #424

# 2017-05-16

- GET /dev/dogma/effects/{effect_id}/ (v2)

# 2017-05-09

- GET /latest/characters/{character_id}/blueprints (v1)
- GET /latest/characters/{character_id}/industry/jobs (v1)
- GET /latest/characters/{character_id}/orders (v1)

# 2017-04-11

- GET /latest/status/ (v1) #88

# 2017-03-30

- GET /latest/universe/system_kills (v1)
- GET /latest/universe/system_jumps (v1)
- GET /latest/sovereignty/map (v1)
- GET /latest/characters/{character_id}/agents_research (v1)
- GET /latest/characters/{character_id}/standings (v1)
- GET /latest/characters/{character_id}/medals (v1)
- GET /latest/characters/{character_id}/chat_channels (v1)

# 2017-03-01

- GET /dev/universe/types/{type_id} (v3) #276
- GET /latest/markets/groups/{group_id} (v1) #156
- GET /latest/markets/groups (v1) #156

# 2017-02-23

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

# 2017-02-20

- /latest/characters/{character_id}/loyalty/points/ (v1)
- /latest/loyalty/stores/{corporation_id}/offers/ (v1)

# 2017-02-14

- /latest/universe/systems/{system_id}/ (v2)
- /latest/universe/stations/{station_id}/ (v2)

# 2017-02-07

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

# 2017-01-31

- /latest/universe/bloodlines/ (v1)
- /latest/universe/names/ (v2) #186
- /latest/characters/<char_id>/ (v4) #221

# 2017-01-26

- /latest/universe/factions/ (v1)

# 2017-01-24

- /dev/characters/<char_id>/ (v4) #221
- /latest/wars/ (v1, spec breaking change) #228
- /latest/universe/races/ (v1) #147

# 2016-11-30

- GET /dev/corporations/{corporation_id}/assets/ (v2)
- GET /dev/characters/{character_id}/assets/ (v3)
- **PROMOTION** GET /latest/characters/{character_id}/assets/ (v2)
