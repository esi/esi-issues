# esi-issues

For public ESI issue tracking only. Bring out your dead.

https://esi.evetech.net/

**Please only submit issues related to ESI, for SSO issues [click here](https://github.com/ccpgames/sso-issues/issues).**

**Please do not open issues for anything security related here, send an email to [security@ccpgames.com](mailto:security@ccpgames.com) instead.**

For a list of past and future ESI endpoint changes, see the [changelog](changelog.md).

This repository is run by a group of CCP developers and members of the EVE third-party dev community. For more details, see [Contributors](contributors.md).

The ESI documentation can be found at [https://docs.esi.evetech.net/](https://docs.esi.evetech.net/). A good place to start is the [FAQ](https://docs.esi.evetech.net/docs/FAQ). It is maintained in a separate repository called [esi-docs](https://github.com/esi/esi-docs) and is open for contributions.

## Opening a new issue

Please use the search function before opening a new issue (be sure to include closed issues as well).

To open a new issue click on one of the following headers (if you think your issue doesn't fit in any of these categories we invite you to [discuss it with us in `#esi` on Tweetfleet Slack first](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/)):

### [Report a new bug](https://github.com/esi/esi-issues/issues/new?template=bug.md)

Examples:

- unexpected 500 responses
- incorrect information in the swagger spec
- otherwise invalid or unexpected responses

Note: `502` or `503` errors are not bugs. Retry your request again in the future.

### [Request a new feature or an enhancement](https://github.com/esi/esi-issues/issues/new?template=feature_request.md)

Some new features will require game design approval. Do not open duplicate feature requests! If you find something similar to what you're requesting, thumbs up the parent comment and add any addendums as comments.

Examples:

- adding an attribute to an existing route
- exposing other readily available client data
- meta requests, adding some global parameter to the specs (`ETag`, `Accept-Encoding`, etc...)

### [Report an inconsistency](https://github.com/esi/esi-issues/issues/new?template=inconsistency.md)

Examples:

- two endpoints returning slightly different names for the same attribute
- attribute values are returned with different formats for different routes (ie; `int32` vs `int64`)
