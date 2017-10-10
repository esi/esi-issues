---
title: XML to ESI Migration
---

# XML to ESI Migration

See also [CREST to ESI Migration](https://ccpgames.github.io/esi-issues/CREST_to_ESI)


# Table of Contents

  * [char](#char)
    * [AccountBalance](#accountbalance)
    * [AssetList](#assetlist)
    * [Blueprints](#blueprints)
    * [Bookmarks](#bookmarks)
    * [CalendarEventAttendees](#calendareventattendees)
    * [CharacterSheet](#charactersheet)
    * [ChatChannels](#chatchannels)
    * [Clones](#clones)
    * [ContactList](#contactlist)
    * [ContactNotifications](#contactnotifications)
    * [ContractBids](#contractbids)
    * [ContractItems](#contractitems)
    * [Contracts](#contracts)
    * [FacWarStats](#facwarstats)
    * [IndustryJobs](#industryjobs)
    * [IndustryJobsHistory](#industryjobshistory)
    * [KillLog](#killlog)
    * [KillMails](#killmails)
    * [Locations](#locations)
    * [MailBodies](#mailbodies)
    * [MailMessages](#mailmessages)
    * [MailingLists](#mailinglists)
    * [MarketOrders](#marketorders)
    * [Medals](#medals)
    * [NotificationTexts](#notificationtexts)
    * [Notifications](#notifications)
    * [PlanetaryColonies](#planetarycolonies)
    * [PlanetaryLinks](#planetarylinks)
    * [PlanetaryPins](#planetarypins)
    * [PlanetaryRoutes](#planetaryroutes)
    * [Research](#research)
    * [SkillInTraining](#skillintraining)
    * [SkillQueue](#skillqueue)
    * [Skills](#skills)
    * [Standings](#standings)
    * [UpcomingCalendarEvents](#upcomingcalendarevents)
    * [WalletJournal](#walletjournal)
    * [WalletTransactions](#wallettransactions)
  * [corp](#corp)
    * [AccountBalance](#accountbalance-1)
    * [AssetList](#assetlist-1)
    * [Blueprints](#blueprints-1)
    * [Bookmarks](#bookmarks-1)
    * [ContactList](#contactlist-1)
    * [ContainerLog](#containerlog)
    * [ContractBids](#contractbids-1)
    * [ContractItems](#contractitems-1)
    * [Contracts](#contracts-1)
    * [CorporationSheet](#corporationsheet)
    * [CustomsOffices](#customsoffices)
    * [FacWarStats](#facwarstats-1)
    * [Facilities](#facilities)
    * [IndustryJobs](#industryjobs-1)
    * [IndustryJobsHistory](#industryjobshistory-1)
    * [KillLog](#killlog-1)
    * [KillMails](#killmails-1)
    * [Locations](#locations-1)
    * [MarketOrders](#marketorders-1)
    * [Medals](#medals-1)
    * [MemberMedals](#membermedals)
    * [MemberSecurity](#membersecurity)
    * [MemberSecurityLog](#membersecuritylog)
    * [MemberTracking](#membertracking)
    * [OutpostList](#outpostlist)
    * [OutpostServiceDetail](#outpostservicedetail)
    * [Shareholders](#shareholders)
    * [Standings](#standings-1)
    * [StarbaseDetail](#starbasedetail)
    * [StarbaseList](#starbaselist)
    * [Titles](#titles)
    * [WalletJournal](#walletjournal-1)
    * [WalletTransactions](#wallettransactions-1)
  * [eve](#eve)
    * [AllianceList](#alliancelist)
    * [CertificateTree](#certificatetree)
    * [CharacterAffiliation](#characteraffiliation)
    * [CharacterID](#characterid)
    * [CharacterInfo](#characterinfo)
    * [CharacterName](#charactername)
    * [ConquerableStationList](#conquerablestationlist)
    * [ErrorList](#errorlist)
    * [FacWarStats](#facwarstats-2)
    * [FacWarTopStats](#facwartopstats)
    * [OwnerID](#ownerid)
    * [RefTypes](#reftypes)
    * [SkillTree](#skilltree)
    * [TypeName](#typename)
  * [map](#map)
    * [FacWarSystems](#facwarsystems)
    * [Jumps](#jumps)
    * [Kills](#kills)
    * [Sovereignty](#sovereignty)


## char

### AccountBalance

[https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallet](https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallet)

### AssetList

[https://esi.tech.ccp.is/latest/#!/Assets/get_characters_character_id_assets](https://esi.tech.ccp.is/latest/#!/Assets/get_characters_character_id_assets)

### Blueprints

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_blueprints](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_blueprints)

### Bookmarks

[https://esi.tech.ccp.is/latest/#!/Bookmarks/get_characters_character_id_bookmarks](https://esi.tech.ccp.is/latest/#!/Bookmarks/get_characters_character_id_bookmarks)

### CalendarEventAttendees

[https://esi.tech.ccp.is/latest/#!/Calendar/get_characters_character_id_calendar_event_id_attendees](https://esi.tech.ccp.is/latest/#!/Calendar/get_characters_character_id_calendar_event_id_attendees)

### CharacterSheet

**WIP** (titles, faction_id)

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id)

[https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_clones](https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_clones)

[https://esi.tech.ccp.is/dev/#!/Skills/get_characters_character_id_skills](https://esi.tech.ccp.is/dev/#!/Skills/get_characters_character_id_skills)

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_attributes](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_attributes)

[https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_implants](https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_implants)

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_fatigue](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_fatigue)

[https://esi.tech.ccp.is/dev/#!/Character/get_characters_character_id_roles](https://esi.tech.ccp.is/dev/#!/Character/get_characters_character_id_roles)

### ChatChannels

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_chat_channels](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_chat_channels)

### Clones

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id)

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_attributes](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_attributes)

[https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_clones](https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_clones)

[https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_implants](https://esi.tech.ccp.is/latest/#!/Clones/get_characters_character_id_implants)

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_fatigue](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_fatigue)

### ContactList

[https://esi.tech.ccp.is/latest/#!/Contacts/get_characters_character_id_contacts](https://esi.tech.ccp.is/latest/#!/Contacts/get_characters_character_id_contacts)

### ContactNotifications

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_notifications_contacts](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_notifications_contacts)

### ContractBids

[https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_bids](https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_bids)

### ContractItems

[https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_items](https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_items)

### Contracts

[https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts](https://esi.tech.ccp.is/latest/#!/Contracts/get_characters_character_id_contracts)

### FacWarStats

### IndustryJobs

[https://esi.tech.ccp.is/latest/#!/Industry/get_characters_character_id_industry_jobs](https://esi.tech.ccp.is/latest/#!/Industry/get_characters_character_id_industry_jobs)

### IndustryJobsHistory

[https://esi.tech.ccp.is/latest/#!/Industry/get_characters_character_id_industry_jobs](https://esi.tech.ccp.is/latest/#!/Industry/get_characters_character_id_industry_jobs) with `included_completed=true`

### KillLog

Deprecated in XML

### KillMails

[https://esi.tech.ccp.is/latest/#!/Killmails/get_characters_character_id_killmails_recent](https://esi.tech.ccp.is/latest/#!/Killmails/get_characters_character_id_killmails_recent)

[https://esi.tech.ccp.is/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash](https://esi.tech.ccp.is/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash)

### Locations

### MailBodies

[https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_mail_id](https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_mail_id)

### MailMessages

[https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail](https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail)

### MailingLists

[https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_lists](https://esi.tech.ccp.is/latest/#!/Mail/get_characters_character_id_mail_lists)

### MarketOrders

[https://esi.tech.ccp.is/latest/#!/Market/get_characters_character_id_orders](https://esi.tech.ccp.is/latest/#!/Market/get_characters_character_id_orders)

### Medals

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_medals](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_medals)

### NotificationTexts

### Notifications

### PlanetaryColonies

[https://esi.tech.ccp.is/latest/#/Planetary32Interaction](https://esi.tech.ccp.is/latest/#/Planetary32Interaction)

### PlanetaryLinks

[https://esi.tech.ccp.is/latest/#/Planetary32Interaction](https://esi.tech.ccp.is/latest/#/Planetary32Interaction)

### PlanetaryPins

[https://esi.tech.ccp.is/latest/#/Planetary32Interaction](https://esi.tech.ccp.is/latest/#/Planetary32Interaction)

### PlanetaryRoutes

[https://esi.tech.ccp.is/latest/#/Planetary32Interaction](https://esi.tech.ccp.is/latest/#/Planetary32Interaction)

### Research

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_agents_research](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_agents_research)

### SkillInTraining

Not needed?

### SkillQueue

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue)

### Skills

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills)

### Standings

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_standings](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_standings)

### UpcomingCalendarEvents

[https://esi.tech.ccp.is/latest/#!/Calendar/get_characters_character_id_calendar](https://esi.tech.ccp.is/latest/#!/Calendar/get_characters_character_id_calendar)

### WalletJournal

[https://esi.tech.ccp.is/dev/#!/Wallet/get_characters_character_id_wallet_journal](https://esi.tech.ccp.is/dev/#!/Wallet/get_characters_character_id_wallet_journal)

### WalletTransactions

[https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallet_transactions](https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallet_transactions)


## corp

### AccountBalance

[https://esi.tech.ccp.is/latest/#!/Wallet/get_corporations_corporation_id_wallets](https://esi.tech.ccp.is/latest/#!/Wallet/get_corporations_corporation_id_wallets)

### AssetList

### Blueprints
[https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_blueprints](https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_blueprints)

### Bookmarks
[https://esi.tech.ccp.is/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks](https://esi.tech.ccp.is/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks)
[https://esi.tech.ccp.is/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks_folders](https://esi.tech.ccp.is/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks_folders)

### ContactList

[https://esi.tech.ccp.is/latest/#!/Contacts/get_corporations_corporation_id_contacts](https://esi.tech.ccp.is/latest/#!/Contacts/get_corporations_corporation_id_contacts)

### ContainerLog

### ContractBids

### ContractItems

### Contracts

### CorporationSheet

[https://esi.tech.ccp.is/dev/#!/Corporation/get_corporations_corporation_id](https://esi.tech.ccp.is/dev/#!/Corporation/get_corporations_corporation_id)

[https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_divisions](https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_divisions)

[https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_members_limit](https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_members_limit)

**Removed logos**

### CustomsOffices

### FacWarStats

### Facilities

### IndustryJobs

### IndustryJobsHistory

### KillLog

Deprecated in XML

### KillMails

[https://esi.tech.ccp.is/latest/#!/Killmails/get_corporations_corporation_id_killmails_recent](https://esi.tech.ccp.is/latest/#!/Killmails/get_corporations_corporation_id_killmails_recent)

### Locations

### MarketOrders

### Medals

### MemberMedals

### MemberSecurity

### MemberSecurityLog

### MemberTracking

[https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_membertracking](https://esi.tech.ccp.is/latest/#!/Corporation/get_corporations_corporation_id_membertracking)

### OutpostList

### OutpostServiceDetail

### Shareholders

### Standings

### StarbaseDetail

### StarbaseList

### Titles

### WalletJournal

[https://esi.tech.ccp.is/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_journal](https://esi.tech.ccp.is/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_journal)

### WalletTransactions


## eve

### AllianceList

[https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances](https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances)

[https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances_alliance_id_corporations](https://esi.tech.ccp.is/latest/#!/Alliance/get_alliances_alliance_id_corporations)

### CertificateTree

Deprecated

### CharacterAffiliation

[https://esi.tech.ccp.is/latest/#!/Character/post_characters_affiliation](https://esi.tech.ccp.is/latest/#!/Character/post_characters_affiliation)

### CharacterID

[https://esi.tech.ccp.is/latest/#!/Search/get_search](https://esi.tech.ccp.is/latest/#!/Search/get_search) with `strict=true` and `categories=["character"]`

### CharacterInfo

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id)

[https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallets](https://esi.tech.ccp.is/latest/#!/Wallet/get_characters_character_id_wallets)

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skills)

[https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue](https://esi.tech.ccp.is/latest/#!/Skills/get_characters_character_id_skillqueue)

[https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_ship](https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_ship)

[https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_location](https://esi.tech.ccp.is/latest/#!/Location/get_characters_character_id_location)

[https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_corporationhistory](https://esi.tech.ccp.is/latest/#!/Character/get_characters_character_id_corporationhistory)

### CharacterName

[https://esi.tech.ccp.is/latest/#!/Universe/post_universe_names](https://esi.tech.ccp.is/latest/#!/Universe/post_universe_names)

### ConquerableStationList

[https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_structures](https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_structures)

then filter outpost types into

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stations_station_id](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_stations_station_id)

### ErrorList

Not needed?

### FacWarStats

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_wars](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_wars)

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_stats](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_stats)

### FacWarTopStats

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards)

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards_characters](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards_characters)

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards_corporations](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_leaderboards_corporations)

### OwnerID

Not needed?

### RefTypes

All expanded in relevant endpoints

### SkillTree

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_categories_category_id](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_categories_category_id) (category_id=16)

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_groups_group_id](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_groups_group_id)

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id)

[https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_attributes_attribute_id](https://esi.tech.ccp.is/latest/#!/Dogma/get_dogma_attributes_attribute_id)

### TypeName

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_types_type_id)


## map

### FacWarSystems

[https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_systems](https://esi.tech.ccp.is/latest/#!/Faction32Warfare/get_fw_systems)

### Jumps

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_jumps](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_jumps)

### Kills

[https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_kills](https://esi.tech.ccp.is/latest/#!/Universe/get_universe_system_kills)

### Sovereignty

[https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_map](https://esi.tech.ccp.is/latest/#!/Sovereignty/get_sovereignty_map)
