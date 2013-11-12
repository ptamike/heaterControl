heaterControl
=============

As my programmable heating control has failed I thought I'd make something better using the Raspberry Pi!

The design uses a 1-wire digital thermometer sensor to measure the room temperature and cheap RF modules
and encoders from RF Solutions to handle the radio link.

The initial software will have a fixed programme that keeps the temperature at 18C between 8am and 8pm
and 5C outside those times. It will also include two override buttons. One for holidays where the
unit acts as a frost stat and stops the temperature falling below 5C. The other is a boost button
that will switch the heater on for 2 hours and then fall back to the stored program.
The software will also keep a log of on times and calculate the daily cost.
For a future development I might add a second temp sensor to record the outside temperature and track cost against
temperature differential.

Once this basic unit is working it would be relatively simple to expand the peripherals to control other devices.

The initial software on this repo will comprise small python modules that are being used to test each section of the software.

