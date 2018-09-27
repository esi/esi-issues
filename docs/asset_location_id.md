
## Asset `location_id` quick reference

- `item_id` of the parent asset (Used to build the assets tree)
- **Item ID of the active ship in space**
If the active ship is in space, the fitting, but, not the ship itself will be returned by the asset endpoint
You can get the active ship by combining data from following endpoints:
  - [ESI location endpoint](https://esi.evetech.net/ui/#/Location/get_characters_character_id_location)
  - [ESI ship endpoint](https://esi.evetech.net/ui/#/Location/get_characters_character_id_ship)
- **Asset Safty** (`location_id` == 2004)
- **System ID** (Range: 30000000 - 32000000)
- **Abyssal System ID** (Range: 32000000 - 33000000)
- **Station ID** (Range: 60000000 - 64000000)
- **Structure ID**
Resolvable via:
  - The [ESI structure endpoint](https://esi.evetech.net/ui/#/Universe/get_universe_structures_structure_id) (if you have docking rights)
  - The [ESI bookmark endpoint](https://esi.evetech.net/ui/#/Bookmarks/get_characters_character_id_bookmarks) (all structures you have bookmarked, resolve structures regardless of docking rights)
- **Customs Office ID** (Those are not resolvable, see [ESI feature request](https://github.com/esi/esi-issues/issues/685), Note: they share ID range with Item IDs and Structure IDs)
- **Character ID** (when `location_flag` is `wardrobe`)
- **Bugged Assets**
  - **Planet ID** (Range: 40000000 - 50000000) Returned for deleted PI structures. They should probably be ignored. They will be removed from the return when the bug is fixed (See: [ESI bug report](https://github.com/esi/esi-issues/issues/943))
- **Fixed Bugs** (only relevant for historic data)
  - Destroyed Assets included in return ([ESI Issue](https://github.com/esi/esi-issues/issues/698))
  - 9e18 locations ([ESI Issue](https://github.com/esi/esi-issues/issues/684))
  - Assets endpoint no longer return trained skills and active boosters ([ESI Issue](https://github.com/esi/esi-issues/issues/911#issuecomment-388436462))
