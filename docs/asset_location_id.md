
The Asset endpoints `location_id` can refer to a lot of things.

Here is a quick reference of all the ones I know about: 
- `item_id` of the parent asset (Used to build the assets tree)
- **Item ID of the active ship in space**
If the active ship is in space, the fitting, but, not the ship itself will be returned by the asset endpoint
You can get the active ship by combining data from following endpoints:
  - [ESI location endpoint](https://esi.evetech.net/ui/#/Location/get_characters_character_id_location)
  - [ESI ship endpoint](https://esi.evetech.net/ui/#/Location/get_characters_character_id_ship)
- **Asset Safty** (locationID == 2004)
- **System ID** (Range: 30000000 - 32000000)
- **Abyssal System ID** (Range: 32000000 - 33000000)
- **Station ID** (Range: 60000000 - 64000000)
- **Structure ID**
Resolvable via:
  - The [ESI structure endpoint](https://esi.tech.ccp.is/ui/#/Universe/get_universe_structures_structure_id) (if you have docking rights)
  - The [ESI bookmark endpoint](https://esi.tech.ccp.is/ui/#/Bookmarks/get_characters_character_id_bookmarks) (all structures you have bookmarked, resolve structures regardless of docking rights)
  - The [Hammerti.me 3rd party structure API](https://stop.hammerti.me.uk/api/docs/structure) (all structures regardless of docking rights, but, limited to structures added by the users)
- **Customs Office ID** (Those are not resolvable, see [ESI feature request](https://github.com/ccpgames/esi-issues/issues/685), Note: they share ID range with Item IDs and Structure IDs)
- **Character ID** (when `location_flag` is `wardrobe`)
- **Bugged Assets**
  - **Planet ID** (Range: 40000000 - 50000000) Returned for deleted PI structures. They should probably be ignored. They will be removed from the return when the bug is fixed (See: [ESI bug report](https://github.com/esi/esi-issues/issues/943))



Change Log:

22-06-2018
- Moved to esi wiki (you can now make pull request to improve this document, yay!)
- Added asset safty

2018-05-31
- Added PI bug
- Added Abyssal System info (verified)
- Added note on active ship
- Bug Fixed: Destroyed Assets included in return ([ESI Issue](https://github.com/ccpgames/esi-issues/issues/698))
- Corporation Offices no longer require any math to resolve (To the best of my knowledge)

2018-05-14
- Bug Fixed: 9e18 locations ([ESI Issue](https://github.com/ccpgames/esi-issues/issues/684))
- Bug Fixed: Assets endpoint no longer return trained skills and active boosters ([ESI Issue](https://github.com/ccpgames/esi-issues/issues/911#issuecomment-388436462))

2018-04-15
- Updated comment on locationIDs starting with 9
- Added note about bookmarks to  structureIDs
- Minor layout improvements
