# Breaking changes

The following table describes potential changes and if they require a version bump.

Keep in mind there may be instances where these rules are violated if there is a pressing performance requirement from the monolith. We will try to keep violations to an absolute minimum, and broadcast the changes in advance if possible.

For the purposes of this document, parameter means input, whereas attribute refers to the response.

Change Description                        | Version Bump Required
------------------------------------------|----------------------
Update description/summary/example        | no
Adding optional attribute or parameter    | no
Adding required parameter                 | yes
Adding required attribute                 | no
Removing optional attribute               | no
Removing required attribute               | yes
Removing parameter                        | no
Optional attribute becomes required       | no
Required attribute becomes optional       | yes
Optional parameter becomes required       | yes
Required parameter becomes optional       | no
Changing attribute or parameter name      | yes
Changing values in an Enum                | yes
Adding values to an attribute Enum        | yes
Removing values from an attribute Enum    | no
Adding values to an parameter Enum        | no
Removing values from an parameter Enum    | yes
Adding pagination with `x-pages`          | no
Reducing attribute maxItems               | no
Increasing attribute maxItems             | yes
Reducing parameter maxItems               | yes
Increasing parameter maxItems             | no
Changing cache expiry                     | no
Changing security requirements            | yes
Changing `x-required-roles` (as dictated) | no


## Type changes

For the purposes of this table `*` means all formats of a type.

Reference document: https://swagger.io/specification/#dataTypes

Original type    | New type         | Breaking parameter | Breaking attribute
-----------------|------------------|--------------------|--------------------
integer/int32    | integer/int64    | no                 | yes
integer/int64    | integer/int32    | yes                | no
number/float     | number/double    | no                 | no
number/double    | number/float     | yes                | no
number/*         | integer/*        | yes                | no
integer/*        | number/*         | no                 | yes
string/date      | string/date-time | yes                | no
string/date-time | string/date      | yes                | no

For any parameter or attribute defined with only a type (format is optional according to swagger spec), it is not a breaking change to clarify the definition to add any format within the type.

Any transition not specifically listed is a breaking change for both parameters and attributes.
