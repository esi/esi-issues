---
title: XML to ESI Migration
---

# XML to ESI Migration

See also [CREST to ESI Migration](https://esi.github.io/esi-issues/CREST_to_ESI)


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

[https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallet](https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallet)

### AssetList

[https://esi.evetech.net/latest/#!/Assets/get_characters_character_id_assets](https://esi.evetech.net/latest/#!/Assets/get_characters_character_id_assets)

### Blueprints

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_blueprints](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_blueprints)

### Bookmarks

[https://esi.evetech.net/latest/#!/Bookmarks/get_characters_character_id_bookmarks](https://esi.evetech.net/latest/#!/Bookmarks/get_characters_character_id_bookmarks)

### CalendarEventAttendees

[https://esi.evetech.net/latest/#!/Calendar/get_characters_character_id_calendar_event_id_attendees](https://esi.evetech.net/latest/#!/Calendar/get_characters_character_id_calendar_event_id_attendees)

### CharacterSheet

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id](https://esi.evetech.net/latest/#!/Character/get_characters_character_id)

[https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_clones](https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_clones)

[https://esi.evetech.net/dev/#!/Skills/get_characters_character_id_skills](https://esi.evetech.net/dev/#!/Skills/get_characters_character_id_skills)

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_attributes](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_attributes)

[https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_implants](https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_implants)

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_fatigue](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_fatigue)

[https://esi.evetech.net/dev/#!/Character/get_characters_character_id_roles](https://esi.evetech.net/dev/#!/Character/get_characters_character_id_roles)

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_titles](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_titles)

[https://esi.evetech.net/ui/#/Universe/get_universe_ancestries](https://esi.evetech.net/ui/#/Universe/get_universe_ancestries)

### ChatChannels

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_chat_channels](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_chat_channels)

### Clones

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id](https://esi.evetech.net/latest/#!/Character/get_characters_character_id)

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_attributes](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_attributes)

[https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_clones](https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_clones)

[https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_implants](https://esi.evetech.net/latest/#!/Clones/get_characters_character_id_implants)

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_fatigue](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_fatigue)

### ContactList

[https://esi.evetech.net/latest/#!/Contacts/get_characters_character_id_contacts](https://esi.evetech.net/latest/#!/Contacts/get_characters_character_id_contacts)

[https://esi.evetech.net/latest/#!/Contacts/get_alliances_alliance_id_contacts](https://esi.evetech.net/latest/#!/Contacts/get_alliances_alliance_id_contacts)

### ContactNotifications

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications_contacts](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications_contacts)

### ContractBids

[https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_bids](https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_bids)

### ContractItems

[https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_items](https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts_contract_id_items)

### Contracts

[https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts](https://esi.evetech.net/latest/#!/Contracts/get_characters_character_id_contracts)

### FacWarStats

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_characters_character_id_fw_stats](https://esi.evetech.net/latest/#!/Faction32Warfare/get_characters_character_id_fw_stats)

### IndustryJobs

[https://esi.evetech.net/latest/#!/Industry/get_characters_character_id_industry_jobs](https://esi.evetech.net/latest/#!/Industry/get_characters_character_id_industry_jobs)

### IndustryJobsHistory

[https://esi.evetech.net/latest/#!/Industry/get_characters_character_id_industry_jobs](https://esi.evetech.net/latest/#!/Industry/get_characters_character_id_industry_jobs) with `included_completed=true`

### KillLog

Deprecated in XML

### KillMails

[https://esi.evetech.net/latest/#!/Killmails/get_characters_character_id_killmails_recent](https://esi.evetech.net/latest/#!/Killmails/get_characters_character_id_killmails_recent)

[https://esi.evetech.net/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash](https://esi.evetech.net/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash)

### Locations

[https://esi.evetech.net/latest/#!/Assets/post_characters_character_id_assets_locations](https://esi.evetech.net/latest/#!/Assets/post_characters_character_id_assets_locations)

[https://esi.evetech.net/latest/#!/Assets/post_characters_character_id_assets_names](https://esi.evetech.net/latest/#!/Assets/post_characters_character_id_assets_names)

### MailBodies

[https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail_mail_id](https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail_mail_id)

### MailMessages

[https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail](https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail)

### MailingLists

[https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail_lists](https://esi.evetech.net/latest/#!/Mail/get_characters_character_id_mail_lists)

### MarketOrders

[https://esi.evetech.net/latest/#!/Market/get_characters_character_id_orders](https://esi.evetech.net/latest/#!/Market/get_characters_character_id_orders)

[https://esi.evetech.net/ui/#/Market/get_characters_character_id_orders_history](https://esi.evetech.net/ui/#/Market/get_characters_character_id_orders_history)

### Medals

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_medals](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_medals)

### NotificationTexts

Notifications and NotificationTexts were rolled into one endpoint:
[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications)

### Notifications

Notifications and NotificationTexts were rolled into one endpoint:
[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_notifications)

### PlanetaryColonies

[https://esi.evetech.net/latest/#/Planetary32Interaction](https://esi.evetech.net/latest/#/Planetary32Interaction)

### PlanetaryLinks

[https://esi.evetech.net/latest/#/Planetary32Interaction](https://esi.evetech.net/latest/#/Planetary32Interaction)

### PlanetaryPins

[https://esi.evetech.net/latest/#/Planetary32Interaction](https://esi.evetech.net/latest/#/Planetary32Interaction)

### PlanetaryRoutes

[https://esi.evetech.net/latest/#/Planetary32Interaction](https://esi.evetech.net/latest/#/Planetary32Interaction)

### Research

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_agents_research](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_agents_research)

### SkillInTraining

Not needed?

### SkillQueue

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skillqueue](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skillqueue)

### Skills

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skills](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skills)

### Standings

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_standings](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_standings)

### UpcomingCalendarEvents

[https://esi.evetech.net/latest/#!/Calendar/get_characters_character_id_calendar](https://esi.evetech.net/latest/#!/Calendar/get_characters_character_id_calendar)

### WalletJournal

[https://esi.evetech.net/dev/#!/Wallet/get_characters_character_id_wallet_journal](https://esi.evetech.net/dev/#!/Wallet/get_characters_character_id_wallet_journal)

### WalletTransactions

[https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallet_transactions](https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallet_transactions)


## corp

### AccountBalance

[https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets](https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets)

### AssetList

[https://esi.evetech.net/latest/#!/Assets/get_corporations_corporation_id_assets](https://esi.evetech.net/latest/#!/Assets/get_corporations_corporation_id_assets)

### Blueprints
[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_blueprints](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_blueprints)

### Bookmarks
[https://esi.evetech.net/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks](https://esi.evetech.net/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks)
[https://esi.evetech.net/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks_folders](https://esi.evetech.net/latest/#!/Bookmarks/get_corporations_corporation_id_bookmarks_folders)

### ContactList

[https://esi.evetech.net/latest/#!/Contacts/get_corporations_corporation_id_contacts](https://esi.evetech.net/latest/#!/Contacts/get_corporations_corporation_id_contacts)

### ContainerLog

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_containers_logs](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_containers_logs)

### ContractBids

[https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts_contract_id_bids](https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts_contract_id_bids)

### ContractItems

[https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts_contract_id_items](https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts_contract_id_items)

### Contracts

[https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts](https://esi.evetech.net/latest/#!/Contracts/get_corporations_corporation_id_contracts)

### CorporationSheet

[https://esi.evetech.net/dev/#!/Corporation/get_corporations_corporation_id](https://esi.evetech.net/dev/#!/Corporation/get_corporations_corporation_id)

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_divisions](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_divisions)

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_members_limit](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_members_limit)

**Removed logos**

### CustomsOffices

[https://esi.evetech.net/latest/#!/Planetary32Interaction/get_corporations_corporation_id_customs_offices](https://esi.evetech.net/latest/#!/Planetary32Interaction/get_corporations_corporation_id_customs_offices)

### FacWarStats

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_corporations_corporation_id_fw_stats](https://esi.evetech.net/latest/#!/Faction32Warfare/get_corporations_corporation_id_fw_stats)

### Facilities

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_facilities](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_facilities)

### IndustryJobs

[https://esi.evetech.net/latest/#!/Industry/get_corporations_corporation_id_industry_jobs](https://esi.evetech.net/latest/#!/Industry/get_corporations_corporation_id_industry_jobs)

### IndustryJobsHistory

[https://esi.evetech.net/latest/#!/Industry/get_corporations_corporation_id_industry_jobs](https://esi.evetech.net/latest/#!/Industry/get_corporations_corporation_id_industry_jobs) with `include_completed=true`

### KillLog

Deprecated in XML

### KillMails

[https://esi.evetech.net/latest/#!/Killmails/get_corporations_corporation_id_killmails_recent](https://esi.evetech.net/latest/#!/Killmails/get_corporations_corporation_id_killmails_recent)

### Locations

[https://esi.evetech.net/latest/#!/Assets/post_corporations_corporation_id_assets_names](https://esi.evetech.net/latest/#!/Assets/post_corporations_corporation_id_assets_names)

[https://esi.evetech.net/latest/#!/Assets/post_corporations_corporation_id_assets_locations](https://esi.evetech.net/latest/#!/Assets/post_corporations_corporation_id_assets_locations)

### MarketOrders

[https://esi.evetech.net/latest/#!/Market/get_corporations_corporation_id_orders](https://esi.evetech.net/latest/#!/Market/get_corporations_corporation_id_orders)

[https://esi.evetech.net/ui/#/Market/get_corporations_corporation_id_orders_history](https://esi.evetech.net/ui/#/Market/get_corporations_corporation_id_orders_history)

### Medals

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_medals](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_medals)

### MemberMedals

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_medals_issued](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_medals_issued)

### MemberSecurity

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_roles](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_roles)

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_titles](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_titles)

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_members_titles](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_members_titles)

### MemberSecurityLog

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_roles_history](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_roles_history)

### MemberTracking

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_membertracking](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_membertracking)

### OutpostList

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_outposts](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_outposts)

### OutpostServiceDetail

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_outposts_outpost_id](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_outposts_outpost_id)

### Shareholders

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_shareholders](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_shareholders)

### Standings

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_standings](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_standings)

### StarbaseDetail

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_starbases_starbase_id](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_starbases_starbase_id)

### StarbaseList

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_starbases](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_starbases)

### Titles

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_titles](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_titles)

### WalletJournal

[https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_journal](https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_journal)

### WalletTransactions

[https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_transactions](https://esi.evetech.net/latest/#!/Wallet/get_corporations_corporation_id_wallets_division_transactions)


## eve

### AllianceList

[https://esi.evetech.net/latest/#!/Alliance/get_alliances](https://esi.evetech.net/latest/#!/Alliance/get_alliances)

[https://esi.evetech.net/latest/#!/Alliance/get_alliances_alliance_id_corporations](https://esi.evetech.net/latest/#!/Alliance/get_alliances_alliance_id_corporations)

[https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_alliancehistory](https://esi.evetech.net/latest/#!/Corporation/get_corporations_corporation_id_alliancehistory)

### CertificateTree

Deprecated

### CharacterAffiliation

[https://esi.evetech.net/latest/#!/Character/post_characters_affiliation](https://esi.evetech.net/latest/#!/Character/post_characters_affiliation)

### CharacterID

[https://esi.evetech.net/ui/#/Universe/post_universe_ids](https://esi.evetech.net/ui/#/Universe/post_universe_ids)

### CharacterInfo

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id](https://esi.evetech.net/latest/#!/Character/get_characters_character_id)

[https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallets](https://esi.evetech.net/latest/#!/Wallet/get_characters_character_id_wallets)

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skills](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skills)

[https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skillqueue](https://esi.evetech.net/latest/#!/Skills/get_characters_character_id_skillqueue)

[https://esi.evetech.net/latest/#!/Location/get_characters_character_id_ship](https://esi.evetech.net/latest/#!/Location/get_characters_character_id_ship)

[https://esi.evetech.net/latest/#!/Location/get_characters_character_id_location](https://esi.evetech.net/latest/#!/Location/get_characters_character_id_location)

[https://esi.evetech.net/latest/#!/Character/get_characters_character_id_corporationhistory](https://esi.evetech.net/latest/#!/Character/get_characters_character_id_corporationhistory)

### CharacterName

[https://esi.evetech.net/latest/#!/Universe/post_universe_names](https://esi.evetech.net/latest/#!/Universe/post_universe_names)

### ConquerableStationList

[https://esi.evetech.net/latest/#!/Sovereignty/get_sovereignty_structures](https://esi.evetech.net/latest/#!/Sovereignty/get_sovereignty_structures)

then filter outpost types into

[https://esi.evetech.net/latest/#!/Universe/get_universe_stations_station_id](https://esi.evetech.net/latest/#!/Universe/get_universe_stations_station_id)

### ErrorList

Not needed?

### FacWarStats

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_wars](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_wars)

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_stats](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_stats)

### FacWarTopStats

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards)

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards_characters](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards_characters)

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards_corporations](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_leaderboards_corporations)

### OwnerID

Not needed?

### RefTypes

All expanded in relevant endpoints

### SkillTree

[https://esi.evetech.net/latest/#!/Universe/get_universe_categories_category_id](https://esi.evetech.net/latest/#!/Universe/get_universe_categories_category_id) (category_id=16)

[https://esi.evetech.net/latest/#!/Universe/get_universe_groups_group_id](https://esi.evetech.net/latest/#!/Universe/get_universe_groups_group_id)

[https://esi.evetech.net/latest/#!/Universe/get_universe_types_type_id](https://esi.evetech.net/latest/#!/Universe/get_universe_types_type_id)

[https://esi.evetech.net/latest/#!/Dogma/get_dogma_attributes_attribute_id](https://esi.evetech.net/latest/#!/Dogma/get_dogma_attributes_attribute_id)

### TypeName

[https://esi.evetech.net/latest/#!/Universe/get_universe_types_type_id](https://esi.evetech.net/latest/#!/Universe/get_universe_types_type_id)


## map

### FacWarSystems

[https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_systems](https://esi.evetech.net/latest/#!/Faction32Warfare/get_fw_systems)

### Jumps

[https://esi.evetech.net/latest/#!/Universe/get_universe_system_jumps](https://esi.evetech.net/latest/#!/Universe/get_universe_system_jumps)

### Kills

[https://esi.evetech.net/latest/#!/Universe/get_universe_system_kills](https://esi.evetech.net/latest/#!/Universe/get_universe_system_kills)

### Sovereignty

[https://esi.evetech.net/latest/#!/Sovereignty/get_sovereignty_map](https://esi.evetech.net/latest/#!/Sovereignty/get_sovereignty_map)
