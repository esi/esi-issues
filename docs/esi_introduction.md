# ESI (EVE Swagger Interface)
The ESI API is the official RESTful API for EVE third party development. It leverages [Swagger](https://swagger.io/) so that documentation
about the API is always up to date and not dependent on documentation websites like this one. You can find all the endpoints
and try them out at [https://esi.evetech.net/ui/](https://esi.evetech.net/ui/).

## Fundamentals
### Multi-tenant to the core

ESI was designed to be a single interface to all information EVE related. As such, if ESI and the cluster agree on configuration,
you can change the datasource query parameter on any route (including /<version>/swagger.json) to the server name of your choice.

You will see this in the ESI UI as a select menu in the header/nav bar, and in the datasource enum in the spec itself.

There are actually three ESI environments running, an esi-dev, esi-test, and the production esi. With esi-dev or esi-test and a
bit of configuration (which will be replaced with tooling), EVE developers can actually query their local development server through ESI.

### Authentication

Auth is still handled by SSO. There are new scopes which ESI uses, you can make new developer keys (or alter your existing)
to make use of the new scopes. If an ESI endpoint requires authentication, you will see a red exclamation mark on the route description in the
Swagger UI. Mouse hovering over this icon will tell you what scope the endpoint requires.

ESI handles redirecting your authentication header to the correct SSO for verification (depending on the datasource query string argument).
SSO is not multi-tenant though, so you will need to create app keys on each SSO backend you intend to use.

### Versioning

ESI itself has an API version (as defined in the spec). That version number is mostly irrelevant to API consumers (it's the version of ESI-lib).
Instead, ESI versions each route individually. This allows us to make much faster changes and avoid the awkward situation of global API versioning.

As an example, let's say you have a route /v1/hello/\<string\>/, and you want to change the path parameter to accepting an integer instead.
With a traditional API, the entire APIs basePath would have to be bumped. This is obviously a little less than ideal, considering there could be hundreds of other unchanged routes.

With ESI, you always (and only) get three complete APIs, /dev/, /latest/ and /legacy/. But each route is also given a numbered path, starting with /v1/.
Alternate routes are mentioned in the route description (until something better comes along in the standards?).

/dev/ can change at any point, changes to /latest/ will be announced. After changes are made the previous /latest/ will be available as /legacy/, until the next version bump.
If you want to avoid the return schema of your request suddenly changing, you can use the versioned alternate route. In that case, prudent developers may want to
create unit tests (watch for the `warning: 199` headers) to notify them when endpoints are moved to legacy.

Additionally, endpoints may be deprecated. When an endpoint is deprecated, a line appears through it on the Swagger UI, and it begins returning the "warning: 299" header.
This is slightly different than a `warning: 199` header, which you will receive if an endpoint was updated and there is now a newer version of it available.
Deprecation is how Tech Co broadcasts an intent to delete a route. Deprecated endpoints may include a recommended alternate source or
other message in the 299 warning, and you should move away from them immediately.

Because endpoints are versioned individually, the concept of an overall /v1/ (or 2 or 5) API is not very relevant, and no swagger-ui is provided for these routes.
Browsing the API's capabilities should be done via /dev/, /latest/ or /legacy/. However, users who wish to indulge their curiosity may feed a
/v1/swagger.json into their own Swagger UI to get an overview, if they wish.

As an aside, all ESI routes end with a /. The only exceptions are the /\<version\>/swagger.json routes and routes used by the swagger-ui, which are passed through ESI.

### Rate limiting

There are no rate limits in place, ESI relies on caching more than rate limiting.

ESI returns standard caching headers if the data is cached. Applications should notice and make use of these headers (expires and last-modified) on routes where they are provided.

ESI is a shared resource and projects should be optimized to have minimum consumption of unnecessary resources. In the case of long running
services, consistent amounts of slow traffic are preferred to spiky, high throughput traffic.

## Important Online Resources
The following is a list of important online resources for ESI development.

* Watch the [third party developer blog](https://developers.eveonline.com/blog) for updates about ESI.
* Make bug or feature requests at our [esi-issues](https://github.com/esi/esi-issues) Github page.
* For real time discussion about ESI join us on our #esi channel in Slack by following [these instructions](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/).
