# Flora

I'm trying to make a pet robot.  I called her Flora, after [Florence Nightingale](https://en.wikipedia.org/wiki/Florence_Nightingale), a heroine of mine.  She lived around 1900 in London.  She worked as a manager and trainer of nurses during the Crimean war.  She was one the first people to collect health care data and aggregating it to gain insight with the goal of improving health care in her own practice.

My robot version of her is clearly not as impressive, but at least she looks happy:

![](media/phase3c_growingup.jpg | width=100)


### Hardware

A very general overview of my development:
1. I was gifted a raspberry pi from a friend.
2. I bought a [Sunfounder Starter Kit](https://www.sunfounder.com/) to get myself going with the raspberry pi and the GPIO, up until the lesson using the motor and the fan.
3. At that point I was ready to develop myself, and I started developing the hardware for Flora.  
  I bought [the cheapest lego technic set](https://shop.lego.com/en-US/Hook-Loader-42084) on the market.  Since I hadn't touched lego in about 20 years, I build the truck to familiarise myself.  Then I redesigned the truck to be able to hold the (1) raspberry pi, (2) the solderless breadboard from the starter kit, (3) a USB-power bank to power the raspberry pi.  First I tried making the truck drive with the motor from the starter kit, but this was not powerful enough.  It would also require me to add an external battery (the one from the kit is wired).

4. I went to the lego store and bought some more bricks to stabilise the robot (less friction --> less power needed).  I also bought a [Lego power functions M-Motor](https://shop.lego.com/en-US/LEGO-Power-Functions-M-Motor-8883) to spin the wheels (using an L293D).  I added a 9V battery to the schema to be sufficiently powered.

**TODO**

- I need to reconnect the motor to the 9V battery.  Currently blocked on my inability to connect a 9V battery without being electrocuted.
- At this point, there is only 1 motor, so Flora can only go forward and backward.  I want to replace the main motor with a L-motor and add the M-motor to the front so that Flora can make turns.
- With the two motors, I'll probably need to rebuild her completely.  I also need more lego to connect lego technic with standard lego.

### Software: backend

I developed a flask app to provide an API to remotely steer the robot.  

To start the backend development for the robot, I'm just playing around with leds.  I have 8 leds connected to GPIO (see `api/api.py` for which ones) and I have 3 endpoints.  To start the server  on the GPIO:

    uwsgi --ini flora.ini

When the raspberry pi is running on eg. IP 192.168.0.191, you can reach the api for example on:

    http://192.168.0.191:9000/api/led/random

To put on/off leds:

    http://192.168.0.191:9000/api/led/1/on

**TODO:**

- Set up remote access.  Figure out how to deal with the router for port forwarding.  Maybe also figure out security in API-requests once it's open.
- Create endpoints.
- Connect the hardware of the robot.

### Software: frontend

**TODO**

Some (underdeveloped) thoughts:
- I could set up a web server (doable given that the api is set up) that could remotely control the robot.

### Software: data science

**TODO**

Some (underdeveloped) thoughts:

- It would be cool to have a few metrics and program the robot to learn by himself where in the apartment she can/should go:
  - Some way of determining the location (from a fixed origin) based on history of events.
  - Some way of determining 'blockedness', i.e. with the accellerometer the robot could technically _test_ if he can go forward/backward.  Still some thoughtwork on this.
- Loss function: Some measure of its distance (in cm) to me.  The loss function should be `abs(100 - distance)` (or square to make it differentiable) to make the robot follow me.
