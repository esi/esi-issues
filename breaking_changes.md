# Breaking changes


The following table describes potential changes and if they require a version bump.

Keep in mind there may be instances where these rules are violated if there is a pressing performance requirement from the monolith. We will try to keep violations to an absolute minimum, and broadcast the changes in advance if possible.

For the purposes of this table, parameter means input parameter, whereas attribute refers to the response object.


Change Description                                 |  Version Bump Required
---------------------------------------------------|-----------------------
Update description/summary/example                 | &#10007;
Adding attribute or parameter                      | &#10007;
Removing optional attribute                        | &#10007;
Removing required attribute                        | &#10003;
Removing parameter                                 | &#10007;
Optional attribute becomes required                | &#10007;
Required attribute becomes optional                | &#10003;
Optional parameter becomes required                | &#10003;
Required parameter becomes optional                | &#10007;
Changing attribute or parameter name               | &#10003;
Changing attribute or parameter type<sup>1</sup>   | &#10003;
Changing attribute format<sup>1</sup>              | &#10007;
Changing parameter format<sup>1</sup>              | &#10003;
Changing values in an Enum                         | &#10003;
Adding values to an Enum                           | &#10007;
Removing values from an Enum                       | &#10003;
Adding pagination<sup>2</sup>                      | &#10007;
Changing attribute maxItems                        | &#10007;
Reducing parameter maxItems                        | &#10003;
Increasing parameter maxItems                      | &#10007;
Changing cache expiry                              | &#10007;
Changing security requirements                     | &#10003;
Changing `x-required-roles`<sup>3</sup>            | &#10007;


<sup>1</sup> Types and formats as described by swagger (https://swagger.io/specification/#dataTypes)  
<sup>2</sup> Pagination can be detected via the response header `x-pages`  
<sup>3</sup> As dictated by game design
