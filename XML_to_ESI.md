category | XML endpoint | ESI parity
-------- | ------------ | ----------
char | |
. | AccountBalance | https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallets
. | AssetList | https://esi.tech.ccp.is/latest/#!/Assets/get_characters_character_id_assets
. | Blueprints | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_blueprints
. | Bookmarks | https://esi.tech.ccp.is/latest/#!/Bookmarks/get_characters_character_id_bookmarks
. | CalendarEventAttendees |
. | CharacterSheet |
. | ChatChannels | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_chat_channels
. | Clones |
. | ContactList | https://esi.tech.ccp.is/latest/#!/Contacts/get_characters_character_id_contacts
. | ContactNotifications |
. | ContractBids | https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_bids
. | ContractItems | https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_items
. | Contracts | https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts
. | FacWarStats |
. | IndustryJobs | https://esi.tech.ccp.is/latest/#!/Industry/get_characters_character_id_industry_jobs
. | IndustryJobsHistory | ^ `included_completed=true`
. | KillLog | Deprecated in XML
. | KillMails | https://esi.tech.ccp.is/latest/#!/Killmails/get_characters_character_id_killmails_recent <br/> -> https://esi.tech.ccp.is/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash
. | Locations |
. | MailBodies | https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_mail_id
. | MailMessages | https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail
. | MailingLists | https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_lists
. | MarketOrders | https://esi.tech.ccp.is/latest/#!/Market/get_characters_character_id_orders
. | Medals | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_medals
. | NotificationTexts |
. | Notifications |
. | PlanetaryColonies | https://esi.tech.ccp.is/latest/#/Planetary32Interaction
. | PlanetaryLinks | ^
. | PlanetaryPins | ^
. | PlanetaryRoutes | ^
. | Research | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_agents_research
. | SkillInTraining | Not needed?
. | SkillQueue | https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue
. | Skills | https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills
. | Standings | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_standings
. | UpcomingCalendarEvents |
. | WalletJournal | https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallets_journal
. | WalletTransactions |
corp | |
. | AccountBalance |
. | AssetList |
. | Blueprints |
. | Bookmarks |
. | ContactList |
. | ContainerLog |
. | ContractBids |
. | ContractItems |
. | Contracts |
. | CorporationSheet |
. | CustomsOffices |
. | FacWarStats |
. | Facilities |
. | IndustryJobs |
. | IndustryJobsHistory |
. | KillLog |
. | KillMails |
. | Locations |
. | MarketOrders |
. | Medals |
. | MemberMedals |
. | MemberSecurity |
. | MemberSecurityLog |
. | MemberTracking |
. | OutpostList |
. | OutpostServiceDetail |
. | Shareholders |
. | Standings |
. | StarbaseDetail |
. | StarbaseList |
. | Titles |
. | WalletJournal |
. | WalletTransactions |
eve | |
. | AllianceList | https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances
. | CertificateTree |
. | CharacterAffiliation | https://esi.tech.ccp.is/latest/#!/Character/post_characters_affiliation
. | CharacterID | https://esi.tech.ccp.is/latest/#!/Search/get_search with `strict=true` and `categories=["character"]`
. | CharacterInfo | https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id <br/> https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallets <br/> https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills <br/> https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue <br/> https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_ship <br/> https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_location <br/> https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_corporationhistory <br/>
. | CharacterName | https://esi.tech.ccp.is/latest/#!/Universe/post_universe_names
. | ConquerableStationList | https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_structures <br/> -> filter outpost types <br/> -> https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stations_station_id
. | ErrorList | Not needed?
. | FacWarStats |
. | FacWarTopStats |
. | OwnerID | Not needed?
. | RefTypes |
. | SkillTree | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_categories_category_id (category_id=16) <br/> -> https://esi.tech.ccp.is/latest/#!/Universe/get_universe_groups_group_id <br/> .> https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id <br/> -> https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_attributes_attribute_id
. | TypeName | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id
map | |
. | FacWarSystems |
. | Jumps | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_jumps
. | Kills | https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_kills
. | Sovereignty | https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_map
