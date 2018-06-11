---
title: CREST to ESI Migration
---

# CREST to ESI Migration

See also [XML to ESI Migration](https://docs.esi.evetech.net/docs/XML_to_ESI)


# Table of Contents

  * [bloodlines](#bloodlines)
    * [/bloodlines/](#bloodlines-1)
    * [/bloodlines/\{bloodlineID:integerType\}/](#bloodlinesbloodlineidintegertype)
  * [decode](#decode)
    * [/decode/](#decode-1)
  * [factions](#factions)
    * [/factions/\{factionID:integerType\}/](#factionsfactionidintegertype)
  * [graphicids](#graphicids)
    * [/graphicids/](#graphicids-1)
    * [/graphicids/\{graphicID:integerType\}/](#graphicidsgraphicidintegertype)
  * [insurance](#insurance)
    * [/insuranceprices/](#insuranceprices)
  * [loyaltypoints](#loyaltypoints)
    * [/loyaltypoints/\{corporationID:corporationIdType\}/](#loyaltypointscorporationidcorporationidtype)
  * [races](#races)
    * [/races/](#races-1)
    * [/races/\{raceID:integerType\}/](#racesraceidintegertype)
  * [time](#time)
    * [/time/](#time-1)
  * [alliances](#alliances)
    * [/alliances/](#alliances-1)
    * [/alliances/\{allianceID:integerType\}/](#alliancesallianceidintegertype)
  * [characters](#characters)
    * [/characters/](#characters-1)
    * [/characters/\{characterID:characterIdType\}/](#characterscharacteridcharacteridtype)
  * [contacts](#contacts)
    * [/characters/\{characterID:characterIdType\}/contacts/](#characterscharacteridcharacteridtypecontacts)
    * [/characters/\{characterID:characterIdType\}/contacts/\{contactID:integerType\}/](#characterscharacteridcharacteridtypecontactscontactidintegertype)
  * [fittings](#fittings)
    * [/characters/\{characterID:characterIdType\}/fittings/](#characterscharacteridcharacteridtypefittings)
    * [/characters/\{characterID:characterIdType\}/fittings/\{fittingID:integerType\}/](#characterscharacteridcharacteridtypefittingsfittingidintegertype)
  * [location](#location)
    * [/characters/\{characterID:characterIdType\}/location/](#characterscharacteridcharacteridtypelocation)
  * [loyaltypoints](#loyaltypoints-1)
    * [/characters/\{characterID:characterIdType\}/loyaltypoints/](#characterscharacteridcharacteridtypeloyaltypoints)
  * [opportunities](#opportunities)
    * [/characters/\{characterID:characterIdType\}/opportunities/](#characterscharacteridcharacteridtypeopportunities)
  * [ship](#ship)
    * [/characters/\{characterID:characterIdType\}/ship/](#characterscharacteridcharacteridtypeship)
  * [ui](#ui)
    * [/characters/\{characterID:characterIdType\}/ui/openwindow/contract/](#characterscharacteridcharacteridtypeuiopenwindowcontract)
    * [/characters/\{characterID:characterIdType\}/ui/openwindow/marketdetails/](#characterscharacteridcharacteridtypeuiopenwindowmarketdetails)
    * [/characters/\{characterID:characterIdType\}/ui/openwindow/newmail/](#characterscharacteridcharacteridtypeuiopenwindownewmail)
    * [/characters/\{characterID:characterIdType\}/ui/openwindow/ownerdetails/](#characterscharacteridcharacteridtypeuiopenwindowownerdetails)
    * [/characters/\{characterID:characterIdType\}/ui/autopilot/waypoints/](#characterscharacteridcharacteridtypeuiautopilotwaypoints)
  * [corporations](#corporations)
    * [/corporations/\{corporationID:corporationIdType\}/](#corporationscorporationidcorporationidtype)
    * [/corporations/\{corporationID:corporationIdType\}/structures/](#corporationscorporationidcorporationidtypestructures)
    * [/corporations/\{corporationID:corporationIdType\}/loyaltystore/](#corporationscorporationidcorporationidtypeloyaltystore)
    * [/corporations/npccorps/](#corporationsnpccorps)
  * [dogma](#dogma)
    * [/dogma/attributes/](#dogmaattributes)
    * [/dogma/attributes/\{attributeID:integerType\}/](#dogmaattributesattributeidintegertype)
    * [/dogma/effects/](#dogmaeffects)
    * [/dogma/effects/\{effectID:integerType\}/](#dogmaeffectseffectidintegertype)
  * [fleets](#fleets)
    * [/fleets/\{fleetID:integerType\}/](#fleetsfleetidintegertype)
    * [/fleets/\{fleetID:integerType\}/members/](#fleetsfleetidintegertypemembers)
    * [/fleets/\{fleetID:integerType\}/members/\{memberID:characterIdType\}/](#fleetsfleetidintegertypemembersmemberidcharacteridtype)
    * [/fleets/\{fleetID:integerType\}/wings/](#fleetsfleetidintegertypewings)
    * [/fleets/\{fleetID:integerType\}/wings/\{wingID:integerType\}/](#fleetsfleetidintegertypewingswingidintegertype)
    * [/fleets/\{fleetID:integerType\}/wings/\{wingID:integerType\}/squads/](#fleetsfleetidintegertypewingswingidintegertypesquads)
    * [/fleets/\{fleetID:integerType\}/wings/\{wingID:integerType\}/squads/\{squadID:integerType\}/](#fleetsfleetidintegertypewingswingidintegertypesquadssquadidintegertype)
  * [incursions](#incursions)
    * [/incursions/](#incursions-1)
  * [industry](#industry)
    * [/industry/facilities/](#industryfacilities)
    * [/industry/systems/](#industrysystems)
  * [inventory](#inventory)
    * [/inventory/categories/](#inventorycategories)
    * [/inventory/categories/\{categoryID:integerType\}/](#inventorycategoriescategoryidintegertype)
    * [/inventory/groups/](#inventorygroups)
    * [/inventory/groups/\{groupID:integerType\}/](#inventorygroupsgroupidintegertype)
    * [/inventory/types/](#inventorytypes)
    * [/inventory/types/\{typeID:integerType\}/](#inventorytypestypeidintegertype)
  * [killmails](#killmails)
    * [/killmails/\{killID:integerType\}/\{killHash:stringType\}/](#killmailskillidintegertypekillhashstringtype)
  * [market](#market)
    * [/market/groups/](#marketgroups)
    * [/market/groups/\{groupID:integerType\}/](#marketgroupsgroupidintegertype)
    * [/market/types/](#markettypes)
    * [/market/types/\{marketTypeID:integerType\}/](#markettypesmarkettypeidintegertype)
    * [/market/\{regionID:integerType\}/history/](#marketregionidintegertypehistory)
    * [/market/\{regionID:integerType\}/orders/all/](#marketregionidintegertypeordersall)
    * [/market/\{regionID:integerType\}/orders/](#marketregionidintegertypeorders)
    * [/market/\{regionID:integerType\}/orders/buy/](#marketregionidintegertypeordersbuy)
    * [/market/\{regionID:integerType\}/orders/sell/](#marketregionidintegertypeorderssell)
    * [/market/prices/](#marketprices)
  * [opportunities](#opportunities-1)
    * [/opportunities/groups/](#opportunitiesgroups)
    * [/opportunities/groups/\{groupID:integerType\}/](#opportunitiesgroupsgroupidintegertype)
    * [/opportunities/tasks/](#opportunitiestasks)
    * [/opportunities/tasks/\{taskID:integerType\}/](#opportunitiestaskstaskidintegertype)
  * [sovereignty](#sovereignty)
    * [/sovereignty/campaigns/](#sovereigntycampaigns)
    * [/sovereignty/structures/](#sovereigntystructures)
  * [structures](#structures)
    * [/structures/\{structID:integerType\}/](#structuresstructidintegertype)
  * [tournaments](#tournaments)
    * [/tournaments/](#tournaments-1)
    * [/tournaments/\{tournamentID:integerType\}/](#tournamentstournamentidintegertype)
    * [/tournaments/\{tournamentID:integerType\}/pilots/\{pilotID:integerType\}/](#tournamentstournamentidintegertypepilotspilotidintegertype)
    * [/tournaments/\{tournamentID:integerType\}/series/](#tournamentstournamentidintegertypeseries)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/](#tournamentstournamentidintegertypeseriesseriesidintegertype)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/](#tournamentstournamentidintegertypeseriesseriesidintegertypematches)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/\{matchID:integerType](#tournamentstournamentidintegertypeseriesseriesidintegertypematchesmatchidintegertype)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/\{matchID:integerType\}/bans/](#tournamentstournamentidintegertypeseriesseriesidintegertypematchesmatchidintegertypebans)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/\{matchID:integerType\}/pilotstats/](#tournamentstournamentidintegertypeseriesseriesidintegertypematchesmatchidintegertypepilotstats)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/\{matchID:integerType\}/realtime/\{frameID:integerType\}/](#tournamentstournamentidintegertypeseriesseriesidintegertypematchesmatchidintegertyperealtimeframeidintegertype)
    * [/tournaments/\{tournamentID:integerType\}/series/\{seriesID:integerType\}/matches/\{matchID:integerType\}/static/](#tournamentstournamentidintegertypeseriesseriesidintegertypematchesmatchidintegertypestatic)
    * [/tournaments/\{tournamentID:integerType\}/teams/\{teamID:integerType\}/](#tournamentstournamentidintegertypeteamsteamidintegertype)
    * [/tournaments/teams/](#tournamentsteams)
    * [/tournaments/teams/\{teamID:integerType\}/](#tournamentsteamsteamidintegertype)
    * [/tournaments/teams/\{teamID:integerType\}/members/](#tournamentsteamsteamidintegertypemembers)
    * [/tournaments/teams/\{teamID:integerType\}/members/\{memberID:integerType\}/](#tournamentsteamsteamidintegertypemembersmemberidintegertype)
  * [universe](#universe)
    * [/constellations/](#constellations)
    * [/constellations/\{constellationID:integerType\}/](#constellationsconstellationidintegertype)
    * [/universe/locations/\{locationID:integerType\}/](#universelocationslocationidintegertype)
    * [/moons/\{moonID:integerType\}/](#moonsmoonidintegertype)
    * [/planets/\{planetID:integerType\}/](#planetsplanetidintegertype)
    * [/regions/](#regions)
    * [/regions/\{regionID:integerType\}/](#regionsregionidintegertype)
    * [/stargates/\{stargateID:integerType\}/](#stargatesstargateidintegertype)
    * [/stations/\{stationID:integerType\}/](#stationsstationidintegertype)
    * [/solarsystems/](#solarsystems)
    * [/solarsystems/\{solarSystemID:integerType\}/](#solarsystemssolarsystemidintegertype)
  * [wars](#wars)
    * [/wars/](#wars-1)
    * [/wars/\{warID:integerType\}/](#warswaridintegertype)
    * [/wars/\{warID:integerType\}/killmails/all/](#warswaridintegertypekillmailsall)


## bloodlines

### /bloodlines/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_bloodlines](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_bloodlines)

### /bloodlines/{bloodlineID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_bloodlines](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_bloodlines)


## decode

### /decode/

Not needed?


## factions

### /factions/{factionID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_factions](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_factions)


## graphicids

### /graphicids/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_graphics](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_graphics)

### /graphicids/{graphicID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_graphics_graphic_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_graphics_graphic_id)


## insurance

### /insuranceprices/

[https://esi.evetech.net/ui/?version=latest#/Insurance/get_insurance_prices](https://esi.evetech.net/ui/?version=latest#/Insurance/get_insurance_prices)


## loyaltypoints

### /loyaltypoints/{corporationID:corporationIdType}/

[https://esi.evetech.net/ui/?version=latest#/Loyalty/get_loyalty_stores_corporation_id_offers](https://esi.evetech.net/ui/?version=latest#/Loyalty/get_loyalty_stores_corporation_id_offers)


## races

### /races/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_races](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_races)

### /races/{raceID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_races](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_races)


## time

### /time/

Not needed?


## alliances

### /alliances/

[https://esi.evetech.net/ui/?version=latest#/Alliance/get_alliances](https://esi.evetech.net/ui/?version=latest#/Alliance/get_alliances)

### /alliances/{allianceID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Alliance/get_alliances_alliance_id](https://esi.evetech.net/ui/?version=latest#/Alliance/get_alliances_alliance_id)


## characters

### /characters/

[https://esi.evetech.net/ui/?version=latest#/Universe/post_universe_names](https://esi.evetech.net/ui/?version=latest#/Universe/post_universe_names)

### /characters/{characterID:characterIdType}/

[https://esi.evetech.net/ui/?version=latest#/Character/get_characters_character_id](https://esi.evetech.net/ui/?version=latest#/Character/get_characters_character_id)

[https://esi.evetech.net/ui/?version=latest#/Character/get_characters_character_id_portrait](https://esi.evetech.net/ui/?version=latest#/Character/get_characters_character_id_portrait)


## contacts

### /characters/{characterID:characterIdType}/contacts/

[https://esi.evetech.net/ui/?version=latest#/Contacts/get_characters_character_id_contacts](https://esi.evetech.net/ui/?version=latest#/Contacts/get_characters_character_id_contacts)

[https://esi.evetech.net/ui/?version=latest#/Contacts/post_characters_character_id_contacts](https://esi.evetech.net/ui/?version=latest#/Contacts/post_characters_character_id_contacts)

### /characters/{characterID:characterIdType}/contacts/{contactID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Contacts/put_characters_character_id_contacts](https://esi.evetech.net/ui/?version=latest#/Contacts/put_characters_character_id_contacts)

[https://esi.evetech.net/ui/?version=latest#/Contacts/delete_characters_character_id_contacts](https://esi.evetech.net/ui/?version=latest#/Contacts/delete_characters_character_id_contacts)


## fittings

### /characters/{characterID:characterIdType}/fittings/

[https://esi.evetech.net/ui/?version=latest#/Fittings/get_characters_character_id_fittings](https://esi.evetech.net/ui/?version=latest#/Fittings/get_characters_character_id_fittings)

[https://esi.evetech.net/ui/?version=latest#/Fittings/post_characters_character_id_fittings](https://esi.evetech.net/ui/?version=latest#/Fittings/post_characters_character_id_fittings)


### /characters/{characterID:characterIdType}/fittings/{fittingID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Fittings/delete_characters_character_id_fittings_fitting_id](https://esi.evetech.net/ui/?version=latest#/Fittings/delete_characters_character_id_fittings_fitting_id)


## location

### /characters/{characterID:characterIdType}/location/

[https://esi.evetech.net/ui/?version=latest#/Location/get_characters_character_id_location](https://esi.evetech.net/ui/?version=latest#/Location/get_characters_character_id_location)


## loyaltypoints

### /characters/{characterID:characterIdType}/loyaltypoints/

[https://esi.evetech.net/ui/?version=latest#/Loyalty/get_characters_character_id_loyalty_points](https://esi.evetech.net/ui/?version=latest#/Loyalty/get_characters_character_id_loyalty_points)


## opportunities

### /characters/{characterID:characterIdType}/opportunities/

[https://esi.evetech.net/ui/?version=latest#/Opportunities/get_characters_character_id_opportunities](https://esi.evetech.net/ui/?version=latest#/Opportunities/get_characters_character_id_opportunities)


## ship

### /characters/{characterID:characterIdType}/ship/

[https://esi.evetech.net/ui/?version=latest#/Location/get_characters_character_id_ship](https://esi.evetech.net/ui/?version=latest#/Location/get_characters_character_id_ship)


## ui

### /characters/{characterID:characterIdType}/ui/openwindow/contract/

[https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_contract](https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_contract)

### /characters/{characterID:characterIdType}/ui/openwindow/marketdetails/

[https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_marketdetails](https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_marketdetails)

### /characters/{characterID:characterIdType}/ui/openwindow/newmail/

[https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_newmail](https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_newmail)

### /characters/{characterID:characterIdType}/ui/openwindow/ownerdetails/

[https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_information](https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_openwindow_information)

###  /characters/{characterID:characterIdType}/ui/autopilot/waypoints/

[https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_autopilot_waypoint](https://esi.evetech.net/ui/?version=latest#/User32Interface/post_ui_autopilot_waypoint)


## corporations

### /corporations/{corporationID:corporationIdType}/

[https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_corporation_id](https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_corporation_id)

### /corporations/{corporationID:corporationIdType}/structures/

[https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_corporation_id_structures](https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_corporation_id_structures)

### /corporations/{corporationID:corporationIdType}/loyaltystore/

[https://esi.evetech.net/ui/?version=latest#/Loyalty/get_loyalty_stores_corporation_id_offers](https://esi.evetech.net/ui/?version=latest#/Loyalty/get_loyalty_stores_corporation_id_offers)

### /corporations/npccorps/

[https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_npccorps](https://esi.evetech.net/ui/?version=latest#/Corporation/get_corporations_npccorps)


## dogma

### /dogma/attributes/

[https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_attributes](https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_attributes)

### /dogma/attributes/{attributeID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_attributes_attribute_id](https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_attributes_attribute_id)

### /dogma/effects/

[https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_effects](https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_effects)

### /dogma/effects/{effectID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_effects_effect_id](https://esi.evetech.net/ui/?version=latest#/Dogma/get_dogma_effects_effect_id)


## fleets

### /fleets/{fleetID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id](https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id)

[https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id](https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id)

### /fleets/{fleetID:integerType}/members/

[https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id_members](https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id_members)

[https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_members](https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_members)

### /fleets/{fleetID:integerType}/members/{memberID:characterIdType}/

[https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_members_member_id](https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_members_member_id)

[https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_members_member_id](https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_members_member_id)

### /fleets/{fleetID:integerType}/wings/

[https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id_wings](https://esi.evetech.net/ui/?version=latest#/Fleets/get_fleets_fleet_id_wings)

[https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_wings](https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_wings)

### /fleets/{fleetID:integerType}/wings/{wingID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_wings_wing_id](https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_wings_wing_id)

[https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_wings_wing_id](https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_wings_wing_id)

### /fleets/{fleetID:integerType}/wings/{wingID:integerType}/squads/

[https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_wings_wing_id_squads](https://esi.evetech.net/ui/?version=latest#/Fleets/post_fleets_fleet_id_wings_wing_id_squads)


### /fleets/{fleetID:integerType}/wings/{wingID:integerType}/squads/{squadID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_squads_squad_id](https://esi.evetech.net/ui/?version=latest#/Fleets/delete_fleets_fleet_id_squads_squad_id)

[https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_squads_squad_id](https://esi.evetech.net/ui/?version=latest#/Fleets/put_fleets_fleet_id_squads_squad_id)


## incursions

### /incursions/

[https://esi.evetech.net/ui/?version=latest#/Incursions/get_incursions](https://esi.evetech.net/ui/?version=latest#/Incursions/get_incursions)


## industry

### /industry/facilities/

[https://esi.evetech.net/ui/?version=latest#/Industry/get_industry_facilities](https://esi.evetech.net/ui/?version=latest#/Industry/get_industry_facilities)

### /industry/systems/

[https://esi.evetech.net/ui/?version=latest#/Industry/get_industry_systems](https://esi.evetech.net/ui/?version=latest#/Industry/get_industry_systems)


## inventory

### /inventory/categories/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_categories](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_categories)

### /inventory/categories/{categoryID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_categories_category_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_categories_category_id)

### /inventory/groups/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_groups](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_groups)

### /inventory/groups/{groupID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_groups_group_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_groups_group_id)

### /inventory/types/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_types](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_types)

### /inventory/types/{typeID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_types_type_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_types_type_id)


## killmails

### /killmails/{killID:integerType}/{killHash:stringType}/

[https://esi.evetech.net/ui/?version=latest#/Killmails/get_killmails_killmail_id_killmail_hash](https://esi.evetech.net/ui/?version=latest#/Killmails/get_killmails_killmail_id_killmail_hash)


## market

### /market/groups/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_groups](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_groups)

### /market/groups/{groupID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_groups_market_group_id](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_groups_market_group_id)

### /market/types/

iterate all the groups and cache

### /market/types/{marketTypeID:integerType}/

iterate all the groups and cache

### /market/{regionID:integerType}/history/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_history](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_history)

### /market/{regionID:integerType}/orders/all/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders)

### /market/{regionID:integerType}/orders/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders) with `order_type=sell` and `type_id`

### /market/{regionID:integerType}/orders/buy/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders) with `order_type=buy` and `type_id`

### /market/{regionID:integerType}/orders/sell/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_region_id_orders) with `order_type=sell` and `type_id`

### /market/prices/

[https://esi.evetech.net/ui/?version=latest#/Market/get_markets_prices](https://esi.evetech.net/ui/?version=latest#/Market/get_markets_prices)


## opportunities

### /opportunities/groups/

[https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_groups](https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_groups)

### /opportunities/groups/{groupID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_groups_group_id](https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_groups_group_id)

### /opportunities/tasks/

[https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_tasks](https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_tasks)

### /opportunities/tasks/{taskID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_tasks_task_id](https://esi.evetech.net/ui/?version=latest#/Opportunities/get_opportunities_tasks_task_id)


## sovereignty

### /sovereignty/campaigns/

[https://esi.evetech.net/ui/?version=latest#/Sovereignty/get_sovereignty_campaigns](https://esi.evetech.net/ui/?version=latest#/Sovereignty/get_sovereignty_campaigns)

### /sovereignty/structures/

[https://esi.evetech.net/ui/?version=latest#/Sovereignty/get_sovereignty_structures](https://esi.evetech.net/ui/?version=latest#/Sovereignty/get_sovereignty_structures)


## structures

### /structures/{structID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Corporation/put_corporations_corporation_id_structures_structure_id](https://esi.evetech.net/ui/?version=latest#/Corporation/put_corporations_corporation_id_structures_structure_id)


## tournaments

**On hold due to possible redesign**

### /tournaments/

### /tournaments/{tournamentID:integerType}/

### /tournaments/{tournamentID:integerType}/pilots/{pilotID:integerType}/

### /tournaments/{tournamentID:integerType}/series/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/bans/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/pilotstats/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/realtime/{frameID:integerType}/

### /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/static/

### /tournaments/{tournamentID:integerType}/teams/{teamID:integerType}/

### /tournaments/teams/

### /tournaments/teams/{teamID:integerType}/

### /tournaments/teams/{teamID:integerType}/members/

### /tournaments/teams/{teamID:integerType}/members/{memberID:integerType}/


## universe

### /constellations/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_constellations](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_constellations)

### /constellations/{constellationID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_constellations_constellation_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_constellations_constellation_id)

### /universe/locations/{locationID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stations_station_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stations_station_id)

### /moons/{moonID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_moons_moon_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_moons_moon_id)

### /planets/{planetID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_planets_planet_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_planets_planet_id)

### /regions/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_regions](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_regions)

### /regions/{regionID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_regions_region_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_regions_region_id)

### /stargates/{stargateID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stargates_stargate_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stargates_stargate_id)

### /stations/{stationID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stations_station_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_stations_station_id)

### /solarsystems/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_systems](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_systems)

### /solarsystems/{solarSystemID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_systems_system_id](https://esi.evetech.net/ui/?version=latest#/Universe/get_universe_systems_system_id)


## wars

### /wars/

[https://esi.evetech.net/ui/?version=latest#/Wars/get_wars](https://esi.evetech.net/ui/?version=latest#/Wars/get_wars)

### /wars/{warID:integerType}/

[https://esi.evetech.net/ui/?version=latest#/Wars/get_wars_war_id](https://esi.evetech.net/ui/?version=latest#/Wars/get_wars_war_id)

### /wars/{warID:integerType}/killmails/all/

[https://esi.evetech.net/ui/?version=latest#/Wars/get_wars_war_id_killmails](https://esi.evetech.net/ui/?version=latest#/Wars/get_wars_war_id_killmails)
