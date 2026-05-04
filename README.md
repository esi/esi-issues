# esi-issues

Issue tracker for EVE Online's API.

- Direct API: https://esi.evetech.net/
- API Explorer: https://developers.eveonline.com/api-explorer
- Documentation: https://developers.eveonline.com/
- Community Support: https://www.eveonline.com/discord - `#3rd-party-dev-and-esi` channel (here you can also find CCPers helping you with any ESI-related questions)

Notes:
- **Please only submit issues related to ESI. For in-game issues, use the in-game functionality.**
- **Please only submit issues for Tranquility. Use in-game functionality or customer support to report issues for other servers.**
- **Please do not open issues for anything security related here; send an email to [security@ccpgames.com](mailto:security@ccpgames.com) instead.**

This repository is run by CCP and members of the EVE third-party dev community.
For more details, see [Contributors](contributors.md).

## Documentation and changes

The [API Explorer](https://developers.eveonline.com/api-explorer) lists all the changes related to ESI routes.
This information is also available via an ESI route [here](https://developers.eveonline.com/api-explorer#/operations/GetMetaChangelog).

For more information on how to work with ESI, check the [Developers](https://developers.eveonline.com/) website.
It contains both blog-posts about the latest, as documentation, best practices, guides and formulas.
The documentation is maintained in the [esi-docs](https://github.com/esi/esi-docs) repository and is open for contributions.

## Opening a new issue

Please use the search function before opening a new issue (be sure to include closed issues as well).

To open a new issue click on one of the following headers.

### [Report a new bug](https://github.com/esi/esi-issues/issues/new?template=bug.yaml)

Examples:

- unexpected 500 responses.
- incorrect information in the API spec.
- otherwise invalid or unexpected responses.

Note: `429`, `502`, `503`, or `504` errors are not bugs.
Retry your request again at a later moment.

### [Request a new feature](https://github.com/esi/esi-issues/issues/new?template=feature_request.yaml)

Some new features will require game design approval.
Do not open duplicate feature requests!
If you find something similar to what you're requesting, thumbs up the parent comment.
In case you have another use-case, feel free to leave that in a comment.

Examples:

- adding an attribute to an existing route.
- exposing other readily available client data.
- meta requests, adding some global parameter to the specs (`ETag`, `Accept-Encoding`, etc...).
