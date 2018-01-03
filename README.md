# esi-issues

For public ESI issue tracking only. Bring out your dead.

https://esi.tech.ccp.is/

**Please only submit issues related to ESI (not CREST or XMLAPI).**

**[Click here for SSO issues](https://github.com/ccpgames/sso-issues/issues)**

**Please do not open issues for anything security related here, send an email to security@ccpgames.com instead.**


## Migration Guide

### [CREST -> ESI](https://ccpgames.github.io/esi-issues/CREST_to_ESI)

### [XML -> ESI](https://ccpgames.github.io/esi-issues/XML_to_ESI)


## Issue velocity

[![New Issues](https://badge.waffle.io/ccpgames/esi-issues.svg?label=new&title=New)](http://waffle.io/ccpgames/esi-issues)
[![Backlog](https://badge.waffle.io/ccpgames/esi-issues.svg?label=backlog&title=Backlog)](http://waffle.io/ccpgames/esi-issues)
[![TODO](https://badge.waffle.io/ccpgames/esi-issues.svg?label=todo&title=TODO)](http://waffle.io/ccpgames/esi-issues)
[![In Progress](https://badge.waffle.io/ccpgames/esi-issues.svg?label=in%20progress&title=In%20Progress)](http://waffle.io/ccpgames/esi-issues)
[![Staging](https://badge.waffle.io/ccpgames/esi-issues.svg?label=staging&title=Staging)](http://waffle.io/ccpgames/esi-issues)

[![Throughput Graph](https://graphs.waffle.io/ccpgames/esi-issues/throughput.svg)](https://waffle.io/ccpgames/esi-issues/metrics/throughput)


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


## FAQ

### How do I make authenticated requests?

ESI uses the same standard oauth2 flow CREST used. [We released a blog detailing the SSO flow for ESI applications](https://developers.eveonline.com/blog/article/sso-to-authenticated-calls), but you can use whatever oauth2 library you're most comfortable with.

### What is the error limit?

ESI is not rate limited, it is however error limited. [Please refer to this blog post detailing the ESI error limit](https://developers.eveonline.com/blog/article/esi-error-limits-go-live).

### What are "underscore routes"?

They embed the version in the path, resulting in more stable clients. [Please refer to the blog post on the matter](https://developers.eveonline.com/blog/article/esi-best-practices-using-underscore-routes). Clients taking advantage of underscore routes should use the OperationID instead of path when calling a route, for convenience.

### What constitutes a version increase?

[Please refer to the breaking changes document](breaking_changes.md).

### Where can I see upcoming changes?

[You can use ESI's diff interface](https://esi.tech.ccp.is/diff/latest/dev/) for the exact differences per route, and the ["ESI Deployment Timeline" GitHub project board](https://github.com/ccpgames/esi-issues/projects/2) for when the upcoming changes will be promoted.

### Is there an ESI client library in &lt;language_x&gt;?

Probably. Check the [awesome-eve](https://github.com/devfleet/awesome-eve) repository. If you can't find something there for your language, you can try the [swagger open source integrations page](https://swagger.io/open-source-integrations/).

### When are CREST and XML API going away?

[May 8th, 2018](https://www.timeanddate.com/countdown/launch?iso=20180508T11&p0=211&msg=CREST+and+XML+API+shutdown&font=slab).


## Further Questions?

Join us on Tweetfleet Slack, in the #esi channel. If you're not on Tweetfleet Slack yet, [get an invite here](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/).
