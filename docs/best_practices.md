A few thoughts on Best practices when using SSO and ESI (If you have any recommendations, please add them. Tag with your name)


Fuzzysteve - Steve Ronuken

* Do not have users log into your application using scopes, each and every time they log in (unless you're only using the implicit flow, which does not generate refresh tokens). This will clutter their application page. Instead, have them log in with a scopeless login. When they do that, if you do not have a registered refresh token for them, or require additional scopes, send them to an interstitial page where you explain what you're about to ask them for, and have them log in again with scopes. This additional login should be quick and easy as they're _already_ logged into SSO.

* Do not use character_id as an primary identifier for a character/user link. Instead, use CharacterOwnerHash. This is so, if a character is sold, the new owner doesn't appear to be the same as the old owner. Especially if you allow for different character logins, to reach the same master account on your system.

* Be willing to have multiple tokens for each character, with different scopes on them. This should not be difficult to manage. Your DB structure could look like:

    User Table -> Character Table -> Token Table -> Scope table.

* Where the character table has a primary lookup key of characterownerhash. (use a actual primary key that's a sequence or something. Don't use character id. That's just another bit of data in the table). Token table is where you store your refresh tokens, tied to the character table with the aforementioned sequence value. Scope tables is a list of scopes with a many to one relationship with token table. Your User table carries any data which is for your _user_ not just a single character they have. It might be as simple as a single id which is then referenced in character table. This would let you easily have a user log into their account, with _any_ of the characters they have tied to it. And as you're using characterownerhash as the way to identify the character, if it's sold, you haven't then exposed the user's data.
