# FixThis
*We're making the world a better place here.*

## Set up/Installation
1. Clone the repository
2. Run `python -m SimpleHTTPServer`.
3. Open [http://localhost:8000](http://localhost:8000) in your web browser.
4. If you know your computer's IP address, try accessing it on port 8000 from your phone.

This is probably most definitely going to change as we figure the structure out a bit more.

## Ideas for implementation
1. We use PhoneGap for the native APIs (camera, maps, etc.)
	* this poses a challenge since web apps need to talk to a server
	* templates can't be directly rendered online if we're using PhoneGap
	* we have to use AJAX calls to GET, PUT, and POST data
2. We use JQTouch instead of jQuery mobile for the interface
	* it's a lot more responsive
	* it's more easily themeable with SASS
3. We use Flask for the backend
	* we'd only have to provide JSON from the backend
	* backbone and mustache.js for rendering?
	* how technical do we want to get?