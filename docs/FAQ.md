## FAQ

### How do I make authenticated requests?

ESI uses the same standard OAuth 2.0 flow CREST used. [We released a blog detailing the SSO flow for ESI applications](https://developers.eveonline.com/blog/article/sso-to-authenticated-calls), but you can use whatever OAuth 2.0 library you're most comfortable with.

### What is the error limit?

ESI is not rate limited, it is however error limited. [Please refer to this blog post detailing the ESI error limit](https://developers.eveonline.com/blog/article/esi-error-limits-go-live).

Keep in mind some endpoints have additional rate limits imposed by game design. If you are limited by the game on some action, ESI will have the same restrictions.

### What are "underscore routes"?

They embed the version in the path, resulting in more stable clients. [Please refer to the blog post on the matter](https://developers.eveonline.com/blog/article/esi-best-practices-using-underscore-routes). Clients taking advantage of underscore routes should use the OperationID instead of path when calling a route, for convenience.

### What constitutes a version increase?

[Please refer to the breaking changes document](https://docs.esi.evetech.net/docs/breaking_changes).

### Where can I see upcoming changes?

[You can use ESI's diff interface](https://esi.evetech.net/diff/latest/dev/) for the exact differences per route. There is also the [ESI changelog](https://docs.esi.evetech.net/changelog) for historical reference and to know when upcoming changes will be promoted.

### Is there an ESI client library in &lt;language_x&gt;?

Probably. Check the [awesome-eve](https://github.com/devfleet/awesome-eve) repository. If you can't find something there for your language, you can try the [Swagger open source integrations page](https://swagger.io/open-source-integrations/).

### What happened to CREST and XML API?

After [18 months of notice](https://www.eveonline.com/article/introducing-esi/) both CREST and XML API were [shut down on May 8th, 2018](https://developers.eveonline.com/blog/article/a-eulogy-for-xml-crest). Please see either the [CREST to ESI](https://docs.esi.evetech.net/docs/CREST_to_ESI) or [XML to ESI](https://docs.esi.evetech.net/docs/XML_to_ESI) migration guides for assistance in porting your old applications to ESI.


## Further Questions?

Join us on Tweetfleet Slack, in the `#esi` channel. If you're not on Tweetfleet Slack yet, [get an invite here](https://www.fuzzwork.co.uk/tweetfleet-slack-invites/).
