# EE250 Final Project

Team Member Names: James Li and Alice Steele

### Running

For the weather data reporting component (the laptop), simply run the `weather.py` script with `python weather.py` using python 3 or above.

For the server, install Node and NPM, and run `npm install` then `node server.js`.

For the Raspberry Pi, run `python rpi_code.py`, which runs both the GrovePi sensors and their data reporting, as well as updating the LCD screen with vibe data.

### External Libraries

In Python:

- Requests (for HTTPS requests)
- GrovePi packages (to interface with the sensors and LCD screen)

In Node:

- Express (for running the web server)
- color-interpolate (for generating the vibe color based on a gradient)
