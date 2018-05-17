# esi-issues

For public ESI issue tracking only. Bring out your dead.

https://esi.evetech.net/

**Please only submit issues related to ESI (not CREST or XMLAPI).**

**[Click here for SSO issues](https://github.com/ccpgames/sso-issues/issues)**

**Please do not open issues for anything security related here, send an email to security@ccpgames.com instead.**


## Opening a new issue

Please use the search function before opening a new issue (be sure to include closed issues as well).

To open a new issue click on one of the following headers (if you think your issue doesn't fit in any of these categories we invite you to [discuss it with us in #esi on tweetfleet slack first](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/)):

### [Report a new bug](https://github.com/esi/esi-issues/issues/new?template=bug.md)

Examples:

- unexpected 500 responses
- incorrect information in the swagger spec
- otherwise invalid or unexpected responses

Note: `502` or `503` errors are not bugs. Retry your request again in the future

### [Request a new feature](https://github.com/esi/esi-issues/issues/new?template=feature_request.md)

Some new features will require game design approval. Do not open duplicate feature requests, if you find something similar to what you're requesting, thumbsup the parent comment and add any addendums as comments.

Examples:

- adding an attribute to an existing route
- exposing other readily available client data
- meta requests, adding some global parameter to the specs (`ETag`, `Accept-Encoding`, etc...)

### [Report an inconsistency](https://github.com/esi/esi-issues/issues/new?template=inconsistency.md)

Examples:

- two endpoints returning slightly different names for the same attribute
- attribute values are returned with different formats for different routes (ie; int32 vs int64)

## Migration Guide

### [CREST -> ESI](https://esi.github.io/esi-issues/CREST_to_ESI)

### [XML -> ESI](https://esi.github.io/esi-issues/XML_to_ESI)


## Issue velocity

[![Waffle.io](https://badge.waffle.io/esi/esi-issues.svg?columns=new,backlog,todo,in+progress,staging)](http://waffle.io/esi/esi-issues)

[![Throughput Graph](https://graphs.waffle.io/esi/esi-issues/throughput.svg)](https://waffle.io/esi/esi-issues/metrics/throughput)


## ESI Members

GitHub User | CCP Dev Name | Tweetfleet Slack | Role
------------|--------------|------------------|-----
[a-tal](https://github.com/a-tal) | CCP SnowedIn | [@ccp_snowedin](https://tweetfleet.slack.com/messages/@ccp_snowedin/) | BDFL
[aquarhead](https://github.com/aquarhead) | CCP AquarHEAD | [@ccp_aquarhead](https://tweetfleet.slack.com/messages/@ccp_aquarhead/) | Developer
[ccpStuart](https://github.com/ccpStuart) | CCP Mephysto | N/A | Project Manager
[ccp-zoetrope](https://github.com/ccp-zoetrope) | CCP Zoetrope | [@ccp_zoetrope](https://tweetfleet.slack.com/messages/@ccp_zoetrope/) | Developer
[gitAskur](https://github.com/gitAskur) | CCP PrismX | [@prismx](https://tweetfleet.slack.com/messages/@prismx/) | Database Wizard
[HakShak](https://github.com/hakshak) | CCP Chimichanga | [@ccpchimichanga](https://tweetfleet.slack.com/messages/@ccpchimichanga/) | Manager
[tsuthers-ccpgames](https://github.com/tsuthers-ccpgames) | CCP Bartender | [@ccp_bartender](https://tweetfleet.slack.com/messages/@ccp_bartender/) | Developer


## ESI Community

The following people are members of the ESI github community. They will be helping to triage issues and guide discussions. Please treat them (and all others) with respect.

GitHub User      | EVE Character     | Tweetfleet Slack
-----------------|-------------------|-----------------
[antihax](https://github.com/antihax) | croakroach | [@antihax](https://tweetfleet.slack.com/messages/@antihax/)
[rawrasaur](https://github.com/rawrasaur) | Aurora Morgan | [@aurora](https://tweetfleet.slack.com/messages/@aurora/)
[itshouldntdothis](https://github.com/itshouldntdothis) | Beryl Slanjava | [@berylslanjava](https://tweetfleet.slack.com/messages/@berylslanjava/)
[Blacksmoke16](https://github.com/Blacksmoke16) | Blacksmoke16 | [@blacksmoke16](https://tweetfleet.slack.com/messages/@blacksmoke16/)
[DianaOlympos](https://github.com/DianaOlympos) | Diana Olympos | [@dianaolympos](https://tweetfleet.slack.com/messages/@dianaolympos/)
[CarbonAlabel](https://github.com/CarbonAlabel) | Carbon Alabel | [@Carbon](https://tweetfleet.slack.com/messages/@Carbon/)
[lukasni](https://github.com/lukasni) | Catherine Solenne | [@catherinesolenne](https://tweetfleet.slack.com/messages/@catherinesolenne/)
[w9jds](https://github.com/w9jds) | Chingy Chonga | [@Chingy Chonga](https://tweetfleet.slack.com/messages/@Chingy_Chonga/)
[NathenSample](https://github.com/NathenSample) | Christy Cloud | [@christycloud](https://tweetfleet.slack.com/messages/@christycloud/)
[ddavaham](https://github.com/ddavaham) | David Davaham | [@DoubleD](https://tweetfleet.slack.com/messages/@DoubleD/)
[fuzzysteve](https://github.com/fuzzysteve) | Steve Ronuken | [@fuzzysteve](https://tweetfleet.slack.com/messages/@fuzzysteve/)
[GoldenGnu](https://github.com/GoldenGnu) | GoldenGnu | [@goldengnu](https://tweetfleet.slack.com/messages/@goldengnu/)
[andimiller](https://github.com/andimiller) | Lucia Denniard | [@luciadenniard](https://tweetfleet.slack.com/messages/@luciadenniard/)
[jowrjowr](https://github.com/jowrjowr) | Saeka Tyr | [@saeka](https://tweetfleet.slack.com/messages/@saeka/)


## FAQ

### How do I make authenticated requests?

ESI uses the same standard oauth2 flow CREST used. [We released a blog detailing the SSO flow for ESI applications](https://developers.eveonline.com/blog/article/sso-to-authenticated-calls), but you can use whatever oauth2 library you're most comfortable with.

### What is the error limit?

ESI is not rate limited, it is however error limited. [Please refer to this blog post detailing the ESI error limit](https://developers.eveonline.com/blog/article/esi-error-limits-go-live).

Keep in mind some endpoints have additional rate limits imposed by game design. If you are limited by the game on some action, ESI will have the same restrictions.

### What are "underscore routes"?

They embed the version in the path, resulting in more stable clients. [Please refer to the blog post on the matter](https://developers.eveonline.com/blog/article/esi-best-practices-using-underscore-routes). Clients taking advantage of underscore routes should use the OperationID instead of path when calling a route, for convenience.

### What constitutes a version increase?

[Please refer to the breaking changes document](breaking_changes.md).

### Where can I see upcoming changes?

[You can use ESI's diff interface](https://esi.evetech.net/diff/latest/dev/) for the exact differences per route. There is also the [ESI changelog](changelog.md) for historical reference and to know when upcoming changes will be promoted.

### Is there an ESI client library in &lt;language_x&gt;?

Probably. Check the [awesome-eve](https://github.com/devfleet/awesome-eve) repository. If you can't find something there for your language, you can try the [swagger open source integrations page](https://swagger.io/open-source-integrations/).

### What happened to CREST and XML API?

After [18 months of notice](https://www.eveonline.com/article/introducing-esi/) both CREST and XML API were [shut down on May 8th, 2018](https://developers.eveonline.com/blog/article/a-eulogy-for-xml-crest). Please see either the [CREST to ESI](https://esi.github.io/esi-issues/CREST_to_ESI) or [XML to ESI](https://esi.github.io/esi-issues/XML_to_ESI) migration guides for assistance in porting your old applications to ESI.


## Further Questions?

Join us on Tweetfleet Slack, in the #esi channel. If you're not on Tweetfleet Slack yet, [get an invite here](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/).
