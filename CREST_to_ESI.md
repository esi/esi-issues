category | CREST route | ESI parity
-------- | ------------ | ----------
/ | 11 | 11
bloodlines | /bloodlines/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_bloodlines
. | /bloodlines/{bloodlineID:integerType}/ | ^
decode | /decode/ | Not needed?
factions | /factions/{factionID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_factions
graphicids | /graphicids/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_graphics
. | /graphicids/{graphicID:integerType}/ |
insurance | /insuranceprices/ | https://esi.tech.ccp.is/latest/#!/Insurance/get_insurance_prices
loyaltypoints | /loyaltypoints/{corporationID:corporationIdType}/ | https://esi.tech.ccp.is/latest/#!/Loyalty/get_loyalty_stores_corporation_id_offers
races | /races/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_races
. | /races/{raceID:integerType}/ | ^
time | /time/ | Not needed?
/alliances | 2 | 2
. | /alliances/ | https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances
. | /alliances/{allianceID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances_alliance_id
/characters | 10 | 10
. | /characters/ | https://esi.tech.ccp.is/latest/#!/Universe/post_universe_names
. | /characters/{characterID:characterIdType}/ | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id <br/> https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_portrait
contacts | /characters/{characterID:characterIdType}/contacts/ | https://esi.tech.ccp.is/latest/#!/Contacts/get_characters_character_id_contacts <br/> https://esi.tech.ccp.is/latest/#!/Contacts/post_characters_character_id_contacts
. | /characters/{characterID:characterIdType}/contacts/{contactID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Contacts/put_characters_character_id_contacts <br/> https://esi.tech.ccp.is/latest/#!/Contacts/delete_characters_character_id_contacts
fittings | /characters/{characterID:characterIdType}/fittings/ | https://esi.tech.ccp.is/latest/#!/Fittings/get_characters_character_id_fittings <br/> https://esi.tech.ccp.is/latest/#!/Fittings/post_characters_character_id_fittings
. | /characters/{characterID:characterIdType}/fittings/{fittingID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Fittings/delete_characters_character_id_fittings_fitting_id
location | /characters/{characterID:characterIdType}/location/ | https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_location
loyaltypoints | /characters/{characterID:characterIdType}/loyaltypoints/ | https://esi.tech.ccp.is/latest/#!/Loyalty/get_characters_character_id_loyalty_points
opportunities | /characters/{characterID:characterIdType}/opportunities/ | https://esi.tech.ccp.is/latest/#!/Opportunities/get_characters_character_id_opportunities
ship | /characters/{characterID:characterIdType}/ship/ | https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_ship
/characters/ui | 5 | 5
. | /characters/{characterID:characterIdType}/ui/openwindow/contract/ | https://esi.tech.ccp.is/latest/#!/User32Interface/post_ui_openwindow_contract
. | /characters/{characterID:characterIdType}/ui/openwindow/marketdetails/ | https://esi.tech.ccp.is/latest/#!/User32Interface/post_ui_openwindow_marketdetails
. | /characters/{characterID:characterIdType}/ui/openwindow/newmail/ | https://esi.tech.ccp.is/latest/#!/User32Interface/post_ui_openwindow_newmail
. | /characters/{characterID:characterIdType}/ui/openwindow/ownerdetails/ | https://esi.tech.ccp.is/latest/#!/User32Interface/post_ui_openwindow_information
. | /characters/{characterID:characterIdType}/ui/autopilot/waypoints/ | https://esi.tech.ccp.is/latest/#!/User32Interface/post_ui_autopilot_waypoint
/corporations | 4 | 4
. | /corporations/{corporationID:corporationIdType}/ | https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id
. | /corporations/{corporationID:corporationIdType}/structures/ | https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_structures
. | /corporations/{corporationID:corporationIdType}/loyaltystore/ | https://esi.tech.ccp.is/latest/#!/Loyalty/get_loyalty_stores_corporation_id_offers
. | /corporations/npccorps/ | https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_npccorps
/dogma | 4 | 4
. | /dogma/attributes/ | https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_attributes
. | /dogma/attributes/{attributeID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_attributes_attribute_id
. | /dogma/effects/ | https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_effects
. | /dogma/effects/{effectID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_effects_effect_id
/fleets | 7 | 7
. | /fleets/{fleetID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Fleets/get_fleets_fleet_id <br/> https://esi.tech.ccp.is/latest/#!/Fleets/put_fleets_fleet_id
. | /fleets/{fleetID:integerType}/members/ | https://esi.tech.ccp.is/latest/#!/Fleets/get_fleets_fleet_id_members <br/> https://esi.tech.ccp.is/latest/#!/Fleets/post_fleets_fleet_id_members
. | /fleets/{fleetID:integerType}/members/{memberID:characterIdType}/ | https://esi.tech.ccp.is/latest/#!/Fleets/delete_fleets_fleet_id_members_member_id <br/> https://esi.tech.ccp.is/latest/#!/Fleets/put_fleets_fleet_id_members_member_id
. | /fleets/{fleetID:integerType}/wings/ | https://esi.tech.ccp.is/latest/#!/Fleets/get_fleets_fleet_id_wings <br/> https://esi.tech.ccp.is/latest/#!/Fleets/post_fleets_fleet_id_wings
. | /fleets/{fleetID:integerType}/wings/{wingID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Fleets/delete_fleets_fleet_id_wings_wing_id <br/> https://esi.tech.ccp.is/latest/#!/Fleets/put_fleets_fleet_id_wings_wing_id
. | /fleets/{fleetID:integerType}/wings/{wingID:integerType}/squads/ | https://esi.tech.ccp.is/latest/#!/Fleets/post_fleets_fleet_id_wings_wing_id_squads
. | /fleets/{fleetID:integerType}/wings/{wingID:integerType}/squads/{squadID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Fleets/delete_fleets_fleet_id_squads_squad_id <br/> https://esi.tech.ccp.is/latest/#!/Fleets/put_fleets_fleet_id_squads_squad_id
/incursions | 1 | 1
. | /incursions/ | https://esi.tech.ccp.is/latest/#!/Incursions/get_incursions
/industry | 2 | 2
. | /industry/facilities/ | https://esi.tech.ccp.is/latest/#!/Industry/get_industry_facilities
. | /industry/systems/ | https://esi.tech.ccp.is/latest/#!/Industry/get_industry_systems
/inventory | 6 | 6
. | /inventory/categories/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_categories
. | /inventory/categories/{categoryID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_categories_category_id
. | /inventory/groups/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_groups
. | /inventory/groups/{groupID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_groups_group_id
. | /inventory/types/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types
. | /inventory/types/{typeID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id
/killmails | 1 | 1
. | /killmails/{killID:integerType}/{killHash:stringType}/ | https://esi.tech.ccp.is/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash
/market | 10 | 10
groups | /market/groups/ | https://esi.tech.ccp.is/latest/#!/Market/get_markets_groups
. | /market/groups/{groupID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Market/get_markets_groups_market_group_id
types | /market/types/ | ^ iterate all the groups and cache
. | /market/types/{marketTypeID:integerType}/ | ^
history | /market/{regionID:integerType}/history/ | https://esi.tech.ccp.is/latest/#!/Market/get_markets_region_id_history
orders | /market/{regionID:integerType}/orders/all/ | https://esi.tech.ccp.is/latest/#!/Market/get_markets_region_id_orders
. | /market/{regionID:integerType}/orders/ | ^ with `order_type=sell` and `type_id`
. | /market/{regionID:integerType}/orders/buy/ | ^ with `order_type=buy` and `type_id`
. | /market/{regionID:integerType}/orders/sell/ | ^ with `order_type=sell` and `type_id`
prices | /market/prices/ | https://esi.tech.ccp.is/latest/#!/Market/get_markets_prices
/opportunities | 4 | 4
. | /opportunities/groups/ | https://esi.tech.ccp.is/latest/#!/Opportunities/get_opportunities_groups
. | /opportunities/groups/{groupID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Opportunities/get_opportunities_groups_group_id
. | /opportunities/tasks/ | https://esi.tech.ccp.is/latest/#!/Opportunities/get_opportunities_tasks
. | /opportunities/tasks/{taskID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Opportunities/get_opportunities_tasks_task_id
/sovereignty | 2 | 2
. | /sovereignty/campaigns/ | https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_campaigns
. | /sovereignty/structures/ | https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_structures
/struct | 1 | 1
. | /structures/{structID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Corporation/put_corporations_corporation_id_structures_structure_id
/tournaments | | **On hold due to possible redesign** <br/> wrong column for formatting
. | | /items/{itemID:integerType}/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/realtime/{frameID:integerType}/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/static/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/pilotstats/
. | | /tournaments/{tournamentID:integerType}/pilots/{pilotID:integerType}/
. | | /tournaments/{tournamentID:integerType}/series/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/
. | | /tournaments/teams/
. | | /tournaments/teams/{teamID:integerType}/members/
. | | /tournaments/teams/{teamID:integerType}/
. | | /tournaments/{tournamentID:integerType}/teams/{teamID:integerType}/
. | | /tournaments/teams/{teamID:integerType}/members/{memberID:integerType}/
. | | /tournaments/
. | | /tournaments/{tournamentID:integerType}/
. | | /tournaments/{tournamentID:integerType}/series/{seriesID:integerType}/matches/{matchID:integerType}/bans/
/universe | 11 | 11
. | /constellations/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_constellations
. | /constellations/{constellationID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_constellations_constellation_id
. | /universe/locations/{locationID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stations_station_id <br/> You should know the type of the id you're looking for.. no??
. | /moons/{moonID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_moons_moon_id
. | /planets/{planetID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_planets_planet_id
. | /regions/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_regions
. | /regions/{regionID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_regions_region_id
. | /stargates/{stargateID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stargates_stargate_id
. | /stations/{stationID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stations_station_id
. | /solarsystems/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_systems
. | /solarsystems/{solarSystemID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_systems_system_id
/wars | 3 | 3
. | /wars/ | https://esi.tech.ccp.is/latest/#!/Wars/get_wars
. | /wars/{warID:integerType}/ | https://esi.tech.ccp.is/latest/#!/Wars/get_wars_war_id
. | /wars/{warID:integerType}/killmails/all/ | https://esi.tech.ccp.is/latest/#!/Wars/get_wars_war_id_killmails
