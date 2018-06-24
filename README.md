# esi-issues

For public ESI issue tracking only. Bring out your dead.

https://esi.evetech.net/

**Please only submit issues related to ESI.**

**[Click here for SSO issues](https://github.com/ccpgames/sso-issues/issues)**

**Please do not open issues for anything security related here, send an email to security@ccpgames.com instead.**


## Staying up-to-date

ESI is a constant work in progress. Here is a list of sources you can use to keep updated:

- Follow [@TeamTechCo](https://twitter.com/TeamTechCo), as well as [@CCP_SnowedIn](https://twitter.com/CCP_SnowedIn) and [@CCP_Zoetrope](https://twitter.com/CCP_Zoetrope) on Twitter.
- Join the [`#esi` channel on Tweetfleet Slack](https://tweetfleet.slack.com/messages/C30KX8UUX/). You can get an invite [here](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/).
- Read the posts on the [Third Party Developer Blog](https://developers.eveonline.com/blog).
- Follow the activity in this repository, particularly the [ESI changelog](changelog.md) and [issues that are in progress](https://github.com/esi/esi-issues/labels/in-progress).


## Opening a new issue

Please use the search function before opening a new issue (be sure to include closed issues as well).

To open a new issue click on one of the following headers (if you think your issue doesn't fit in any of these categories we invite you to [discuss it with us in `#esi` on Tweetfleet Slack first](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/)):

### [Report a new bug](https://github.com/esi/esi-issues/issues/new?template=bug.md)

Examples:

- unexpected 500 responses
- incorrect information in the swagger spec
- otherwise invalid or unexpected responses

Note: `502` or `503` errors are not bugs. Retry your request again in the future.

### [Request a new feature](https://github.com/esi/esi-issues/issues/new?template=feature_request.md)

Some new features will require game design approval. Do not open duplicate feature requests! If you find something similar to what you're requesting, thumbs up the parent comment and add any addendums as comments.

Examples:

- adding an attribute to an existing route
- exposing other readily available client data
- meta requests, adding some global parameter to the specs (`ETag`, `Accept-Encoding`, etc...)

### [Report an inconsistency](https://github.com/esi/esi-issues/issues/new?template=inconsistency.md)

Examples:

- two endpoints returning slightly different names for the same attribute
- attribute values are returned with different formats for different routes (ie; `int32` vs `int64`)

## Migration Guide

### [CREST -> ESI](https://docs.esi.evetech.net/docs/CREST_to_ESI)

### [XML -> ESI](https://docs.esi.evetech.net/docs/XML_to_ESI)


## Issue velocity

[![Waffle.io](https://badge.waffle.io/esi/esi-issues.svg?columns=new,backlog,todo,in+progress,staging)](http://waffle.io/esi/esi-issues)

[![Throughput Graph](https://graphs.waffle.io/esi/esi-issues/throughput.svg)](https://waffle.io/esi/esi-issues/metrics/throughput)


## ESI Members

 GitHub | CCP Dev Name | Tweetfleet Slack | Twitter | Role
--------|--------------|------------------|---------|------
[a-tal](https://github.com/a-tal) | CCP SnowedIn | [@ccp_snowedin](https://tweetfleet.slack.com/messages/@ccp_snowedin/) | [@CCP_SnowedIn](https://twitter.com/CCP_SnowedIn) | BDFL
[aquarhead](https://github.com/aquarhead) | CCP AquarHEAD | [@ccp_aquarhead](https://tweetfleet.slack.com/messages/@ccp_aquarhead/) | [@aquarhead](https://twitter.com/aquarhead) | Developer
[ccpStuart](https://github.com/ccpStuart) | CCP Mephysto | N/A | N/A | Project Manager
[ccp-zoetrope](https://github.com/ccp-zoetrope) | CCP Zoetrope | [@ccp_zoetrope](https://tweetfleet.slack.com/messages/@ccp_zoetrope/) | [@CCP_Zoetrope](https://twitter.com/CCP_Zoetrope) | Developer
[gitAskur](https://github.com/gitAskur) | CCP PrismX | [@prismx](https://tweetfleet.slack.com/messages/@prismx/) | [@CCP_PrismX](https://twitter.com/CCP_PrismX) | Database Wizard
[HakShak](https://github.com/hakshak) | CCP Chimichanga | [@ccpchimichanga](https://tweetfleet.slack.com/messages/@ccpchimichanga/) | [@ccp_chimichanga](https://twitter.com/ccp_chimichanga) | Manager
[tsuthers-ccpgames](https://github.com/tsuthers-ccpgames) | CCP Bartender | [@ccp_bartender](https://tweetfleet.slack.com/messages/@ccp_bartender/) | N/A | Developer


## ESI Community

The following people are members of the ESI GitHub community. They will be helping to triage issues and guide discussions. Please treat them (and all others) with respect.

 GitHub | EVE Character | Tweetfleet Slack | Twitter
--------|---------------|------------------|---------
[antihax](https://github.com/antihax) | croakroach | [@antihax](https://tweetfleet.slack.com/messages/@antihax/) | [@antihax_croak](https://twitter.com/antihax_croak)
[rawrasaur](https://github.com/rawrasaur) | Aurora Morgan | [@aurora](https://tweetfleet.slack.com/messages/@aurora/) | [@rawrafox](https://twitter.com/rawrafox)
[itshouldntdothis](https://github.com/itshouldntdothis) | Beryl Slanjava | [@berylslanjava](https://tweetfleet.slack.com/messages/@berylslanjava/)  | N/A
[Blacksmoke16](https://github.com/Blacksmoke16) | Blacksmoke16 | [@blacksmoke16](https://tweetfleet.slack.com/messages/@blacksmoke16/) | N/A
[DianaOlympos](https://github.com/DianaOlympos) | Diana Olympos | [@dianaolympos](https://tweetfleet.slack.com/messages/@dianaolympos/) | [@DianaOlympos](https://twitter.com/DianaOlympos)
[CarbonAlabel](https://github.com/CarbonAlabel) | Carbon Alabel | [@Carbon](https://tweetfleet.slack.com/messages/@Carbon/) | [@CarbonAlabel](https://twitter.com/CarbonAlabel)
[lukasni](https://github.com/lukasni) | Catherine Solenne | [@catherinesolenne](https://tweetfleet.slack.com/messages/@catherinesolenne/) | N/A
[w9jds](https://github.com/w9jds) | Chingy Chonga | [@Chingy Chonga](https://tweetfleet.slack.com/messages/@Chingy_Chonga/) | [@w9jds_](https://twitter.com/w9jds_)
[NathenSample](https://github.com/NathenSample) | Christy Cloud | [@christycloud](https://tweetfleet.slack.com/messages/@christycloud/) | [@ChristyCloudEve](https://twitter.com/ChristyCloudEve)
[ddavaham](https://github.com/ddavaham) | David Davaham | [@DoubleD](https://tweetfleet.slack.com/messages/@DoubleD/) | N/A
[fuzzysteve](https://github.com/fuzzysteve) | Steve Ronuken | [@fuzzysteve](https://tweetfleet.slack.com/messages/@fuzzysteve/) | [@Fuzzysteve](https://twitter.com/Fuzzysteve)
[GoldenGnu](https://github.com/GoldenGnu) | GoldenGnu | [@goldengnu](https://tweetfleet.slack.com/messages/@goldengnu/) | N/A
[andimiller](https://github.com/andimiller) | Lucia Denniard | [@luciadenniard](https://tweetfleet.slack.com/messages/@luciadenniard/) | N/A
[jowrjowr](https://github.com/jowrjowr) | Saeka Tyr | [@saeka](https://tweetfleet.slack.com/messages/@saeka/) | N/A


## Documentation

Docs are stored in the [docs](docs) subfolder. Please open pull requests if you see anything out of order there.

If you're adding a new document, be sure to include a link here somewhere.

### General

- [ESI Introduction](https://esi.github.io/esi-issues/docs/esi_introduction)
- [Frequently Asked Questions](https://esi.github.io/esi-issues/docs/FAQ)
- [Third Party Libraries](https://esi.github.io/esi-issues/docs/third_party_libraries)
- [Transitioning from XML](https://esi.github.io/esi-issues/docs/XML_to_ESI)
- [Transitioning from CREST](https://esi.github.io/esi-issues/docs/CREST_to_ESI)
- [What defines a breaking change](https://esi.github.io/esi-issues/docs/breaking_changes)
- [Warning headers explained](https://esi.github.io/esi-issues/docs/warning_header)

### Using ESI Data

- [Dogma](https://esi.github.io/esi-issues/docs/dogma)
- [Useful Formulae](https://esi.github.io/esi-issues/docs/useful_formulae)
- [Asset location_id](https://esi.github.io/esi-issues/docs/asset_location_id)

### Static Data Export

- [SDE Introduction](https://esi.github.io/esi-issues/docs/sde_introduction)
- [SDE Conversions](https://esi.github.io/esi-issues/docs/sde_conversions)

### Community FAQs

- [Guidelines](https://esi.github.io/esi-issues/docs/guidelines)
- [Best Practices](https://esi.github.io/esi-issues/docs/best_practices)
- [Quick Reference URLs](https://esi.github.io/esi-issues/docs/quick_reference)
- [Image Server](https://esi.github.io/esi-issues/docs/image_server)
- [Developer License](https://esi.github.io/esi-issues/docs/developer_license)
