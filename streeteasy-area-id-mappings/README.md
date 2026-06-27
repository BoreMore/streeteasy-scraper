# StreetEasy area ID to neighborhood mapping

[`streeteasy-areas.json`](streeteasy-areas.json) is a complete mapping of all 346
StreetEasy **area IDs** to their neighborhoods. StreetEasy search URLs encode
neighborhoods as opaque numeric IDs (e.g. `area:106,117,142,302`), with no
published lookup table. This file maps the area IDs to the names of neighborhoods and boroughs. Feel free to use in your own projects.

## How it was captured

It is a scrape of StreetEasy's public GraphQL endpoint. POST this query to
`https://api-v6.streeteasy.com/`:

```graphql
{
  areas {
    id          # URL slug, e.g. "stuyvesant-town"
    name        # display name, e.g. "Stuyvesant Town/PCV"
    numericId   # numeric area code used in search URLs, e.g. 106
    parentId    # numericId of the parent area (borough/region tree); null at the root
    geometry {
      encodedBoundary   # area outline as a Google-encoded polyline
    }
  }
}
```

## Discovered schema

Introspection is disabled on the endpoint, so these fields were found by probing
(the JSON uses StreetEasy's own field names, unmodified):

### `Area`

| Field | Type | Description |
| --- | --- | --- |
| `id` | `String` | URL slug, e.g. `"stuyvesant-town"` |
| `name` | `String` | Display name, e.g. `"Stuyvesant Town/PCV"` |
| `numericId` | `Int` | The numeric **area code** used in StreetEasy search URLs (e.g. `106`) |
| `parentId` | `Int` (nullable) | `numericId` of the parent area; `null` for the root (`NYC and NJ`) |
| `geometry` | `GeoGeometry` | The area's geometry |

### `GeoGeometry`

| Field | Type | Description |
| --- | --- | --- |
| `encodedBoundary` | `String` | The area outline as a Google-encoded polyline |

## Example entry

```json
{
  "id": "stuyvesant-town",
  "name": "Stuyvesant Town/PCV",
  "numericId": 106,
  "parentId": 102,
  "geometry": { "encodedBoundary": "}irwFbvpbMx\\}eA..." }
}
```

## Notes

- Codes are grouped by borough: `100`s are Manhattan, `200`s are the Bronx, `300`s are Brooklyn,
  `400`s are Queens, `500`s are Staten Island; values above `856000` are Jersey 🤮 (jk, I love Jersey).
- `parentId` lets you reconstruct the full hierarchy and derive each area's borough
  by walking up the parent chain to the borough-level ancestor.
