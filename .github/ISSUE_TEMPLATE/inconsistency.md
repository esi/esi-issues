# Inconsistency

This template contains an example inconsistency report. Please replace all text except for the checklist and the section headers (they start with \#). Thank you for your contribution to improving ESI.

Please provide a short description of the inconsistency you have noticed. E.g.:

Sometimes the corporation ID is returned as `id` and other times as `corporation_id`

## Routes

List the routes (with version and method) that are affected by this inconsistency. Split into groups if appropriate. E.g.:

Corporation ID as `corporation_id`:

- `GET /v1/corporations/{corporation_id}/`
- all other corporation routes

Corporation ID as `id`:

- `GET /v1/characters/{character_id}/medals/`

## Resolution

Propose a solution to resolve the inconsistency. E.g.:

Change the `id` attribute in the return of `GET /v1/characters/{character_id}/medals/` to `corporation_id`

# Checklist

Check all boxes that apply to this issue:

- [ ] Inconsistency description is provided
- [ ] Inconsistent route(s) are provided
- [ ] Resolution [will require a version bump](https://docs.esi.evetech.net/docs/breaking_changes)
- [ ] Resolution [does not require a version bump](https://docs.esi.evetech.net/docs/breaking_changes)
