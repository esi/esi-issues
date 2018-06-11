# Warning Response Header

ESI will sometimes respond with a `Warning` header. You should look for this header in your application(s), as they contain important information.

Generally, you will receive two different types of warnings:

## `299`

Warnings that start with `299` are there to inform you the route you just requested is deprecated. The message may contain a specific date or some other message related to the migration of the route. By default, it will say `299 - This route is deprecated.` If you receive this response header, it means there is a newer version of the route you just requested available and you should update your application as soon as possible. The legacy route you are currently using may disappear, which would result in your application receiving `404` errors and your users being unhappy.

## `199`

Instead of unhappy users, look for `199` warnings ahead of time. These exist in order to tell you the route you have just requested has an update available. This means it's probably a good time to [check the changelog](https://docs.esi.evetech.net/changelog) to see when this new upgrade will be promoted to latest, and/or update your application to take advantage of the new features the change brings.

The typical `199` warning is: `199 - This route has an upgrade available.` You can use the diff page to view the exact details of the upcoming changes. The [v3 ESI webui](https://esi.evetech.net/ui/) will have links in the description to the diff page for any routes with updates available.

# Conclusion

Warning headers are great, they can enable programatic notifications of ESI upgrades to the routes you use every day. You should be logging warning headers when you receive them, and make a note to take action when necessary to ensure the smooth continued operation of your app.
