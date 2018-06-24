# Third Party Libraries

A number of third party libraries are available to speed your app development rather than reinventing the wheel.

## Libraries

| Language   | Library                                                        | OAuth2  | Style   | ETags | h2             |
|------------|----------------------------------------------------------------|---------|---------|-------|----------------|
| go         | [GoESI](https://github.com/antihax/goesi)                      | Yes     | codegen | Yes   | Yes            |
| PHP        | [eseye](https://github.com/eveseat/eseye)                      | Library | dynamic | Yes   | Depends on PHP |
| PowerShell | [POSH](https://github.com/markus-lassfolk/EVE-Online-ESI-Posh) | Yes     | static  | No    | No             |
| Python     | [EsiPy](https://github.com/Kyria/EsiPy)                        | Yes     | dynamic | Yes   | Yes            |
| .NET       | [ESI.NET](https://github.com/seraphx2/ESI.NET)                 | Yes     | static  | No    | No             |
| Ruby       | [EVEOnline ESI API](https://github.com/biow0lf/eve_online)     | Library | static  | No    | No             |
| Java       | [eve-esi](https://github.com/burberius/eve-esi)                | Yes     | codegen | Yes   | No             |

## Features

| Feature | Description                                                                        |
|---------|------------------------------------------------------------------------------------|
| OAuth2  | Supports OAuth2 flows. May be included via a library.                              |
| Style   | See Style table below.                                                             |
| ETags   | Supports ETag based cache to reduce bandwidth consumption.                         |
| h2      | Supports http2 request multiplexing to send concurrent requests over a connection. |

## Styles

| Style   | Description                                |
|---------|--------------------------------------------|
| codegen | Automatically rebuilt as endpoints change. |
| dynamic | Builds model in memory each run.           |
| static  | Built by hand.                             |

## Disclaimer

These libraries are not maintained by CCP Games.