Building out a repository of Python and C++ coding examples.  This is 100% self-study becuase I really
enjoy solving problems through writing code.

HackerRank, LeetCode, and Meta directories include solutions to programming "challenges".

QuantLib directory includes a sample of a zero coupon yield curve.  Through this example, I was able to
reinforce knowledge of C++ Standard Template Library and learned how to utilize boost tools.

I am also developing a website with Django and apache2 that runs on a Raspberry Pi 4 and updates
data from waveform.com Sense-Hat (B) in real time.
**Project Plan:**
- [x] start with a clean, headless RPi4 (latest Debian disk image)
- [x] install & configure python virtual environment
- [x] install & configure apache2
- [x] install & configure Django
- [x] start a new project/app in Django
- [x] develop python code to read and output sensor data (i.e., temp, humidity, pressure, motion, light, color)
- [ ] integrate sensor data into Django model/views
- [ ] research Websocket and Django Channels for real time updates
- [ ] investigate possibility of running RPi in wireless access bridge mode to create a standalone webserver that can also be accessed through a LAN for making updates
