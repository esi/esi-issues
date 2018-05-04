# Bug

This template contains an example bug report. Please replace all text except for the checklist and the section headers (they start with \#). Thank you for your contribution to improving ESI.

In this space please provide a short description of the bug you've encountered. E.g.:

When requesting my character ID, I receive an unexpected 418 error.

## Request

Be sure to include the HTTP method, path (including version), and any relevant parameters. Please do not include auth tokens. E.g.:

`GET /latest/characters/{character_id}/?datasource=tranquility`

## Response

### Status Code

`418`

### Headers

Include relevant headers received. Timestamps and request ID is nice, you may not have all these values, fill out what you received (don't worry about headers not listed here, unless pertinent to your issue). E.g.:

```
Date: Fri, 27 Apr 2018 07:22:48 GMT
Expires:
Last-Modified:
X-ESI-Request-ID: dcc736af-a73a-4c99-add5-8d66e197cec6
ETag:
```

### Body

Please provide the response body, feel free to scrub any opsec details you wish. E.g.:

JSON
```
{
    "error": "I'm a teapot"
}
```

## Expected

Please provide either the expected return code, correct response body, header value, or some combination thereof. E.g.:

`200`


# Checklist

Check all boxes that apply to this issue:

- [ ] Bug description is provided
- [ ] Request path is provided
- [ ] Response status code is provided
- [ ] Response headers are provided
- [ ] Response body is provided
- [ ] Expected response is provided
