# Wiring Guide

## Why does wiring matter?

Have you ever looked inside your robot and thought "what a mess of wires"? Wiring is extremely important in FTC® but is often overlooked or hastily done the hour before competition starts. However, time spent in wiring the robot properly is crucial to the performance and maintenance of the robot.

**Attention**: It is highly discouraged for teams to overlook wiring, but many new teams seem to disregard it or put little thought into wiring the robot properly.

While tedious and often no fun, wiring can mean the difference between a win and a loss. The best robot in the world won't be able to work if a wire is loose or gets tangled up in the middle of a match. Thus, it is imperative that wiring is purposefully thought out when designing and building a robot.

## *FIRST* FTC Wiring Guide

*FIRST* has created a wiring guide to help teams with tasks like crimping cables, soldering connections, and ESD mitigation that won't be covered in this guide. Once you read up on electronics and wiring here, look at the [`FTC Wiring Guide`](https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/robot-wiring-guide.pdf) for the best practices and more tips & tricks. In addition, *FIRST* has written an [`ESD Mitigation Whitepaper`](https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/analysis-esd-mitigation-echin.pdf) that is worth taking a look at.

## General Advice

- **Always label wires!** When bunched up, you may not know which wire goes into which port.
- Tie together loose wires, and better yet, tie that bunch of wires to a structural component. This will ensure that wires don't interfere with your mechanisms.
- **Pay attention to port numbers!** The REV hub will often have multiple ports per connector on the REV hub. [`REV has a pinout guide to avoid confusion`](https://docs.revrobotics.com/duo-control/control-system-overview/port-pinouts).
- **Treat every wire connection as a point of failure.** Therefore, use electrical tape to tape up and insulate connections and utilize strain relief as much as possible.
- **Strain relief** should be used everywhere possible. It is highly recommended for teams to use products like the [REV USB Retention Mount](USB%20Retention%20Mount), as well as 3D printing strain relief methods for devices such as the Expansion Hub and robot controller phones.
- **DO NOT solder a wire before crimping it.** Solder can "creep" and lose connection, possibly leading to fire.
- **Keep all wire runs as short as possible** to prevent entanglement and improve wire management.
- **When using data/sensor cables, keep them away from motors.** This will reduce electromagnetic interference (EMI). Add a ferrite bead if possible.
- **Crimped connectors are generally better than soldered connectors,** as solder joints can break easier than a crimped connection.
- **Keep wires tucked away from moving mechanisms,** and ensure that you will not be at risk of a mechanism snagging a wire. This is a proper application of materials such as acrylic, which allows drivers to see inside the robot while keeping wires out of the way of other robots/game pieces. It is advised for teams to purchase removable velcro ties or cable ties to aid with cable management.
- **For power wires, lower** `gauge` **(larger size) wires are preferable.** This means a lower resistance across the wire and higher power throughput. This is negligible for data wires, however.
- **Small wires and cables are fragile.** Treat them as such, and don't put them in an area where they will constantly be hit by another object. Larger power cables can take much more abuse.
- **Ensure that your wires are kept out of pinch points** where another mechanism could sandwich the wire. This is especially important in arms or mechanisms that are hinged.

![Bad Wiring](https://dd8f408.webp.ee/bad-wiring.jpg)  
*Figure: An example of poor wiring*

![Good Wiring by 731](https://dd8f408.webp.ee/731-wiring-1.jpg)  
*Figure: An example of good wiring by 731*

![Good Wiring by 731](https://dd8f408.webp.ee/731-wiring-2.jpg)  
*Figure: An example of good wiring by 731 Wannabee Strange, Rover Ruckus*

![Good Wiring by 8417](https://dd8f408.webp.ee/8417-wiring.jpg)  
*Figure: An example of good wiring by 8417 'Lectric Legends*

![Good Wiring by 7244](https://dd8f408.webp.ee/7244-wiring.jpg)  
*Figure: An example of good wiring by 7244 Out of the Box Robotics*

When wiring, also take the time to plan out a specific layout for your wires and how they will run throughout the robot. Take the time to lay out something like an electronics panel if necessary! When building the robot, devote adequate space to wiring. This could mean mounting a PVC pipe and running wires from the back end of the robot through it, or simply using velcro or zipties.

**Tip:** Make sure that wires are as short as possible to reduce the risk of entanglement.

However, as components move out of the robot, the wires move with it. Tying down every loose inch will result in wire disconnecting. Wiring is the art of finding the perfect balance between shortest length and allowing enough freedom as mechanisms need.

**It is also recommended for electronics to be mounted on a nonconductive material such as wood to prevent ESD.**

![Good Wiring on Non-Conductive Surface](https://dd8f408.webp.ee/3736-electronics-on-plastic.jpg)  
*Figure: An example of good wiring on a non-conductive surface by 3736 Serious Business*

## Specific Recommendations

### Module Power

Be aware, `XT30` connectors can wear out significantly faster than `PowerPole` connectors. Additionally, because `XT30` connectors are soldered, they can break much easier than `PowerPole` connections.

Cabling for module power should be at least 14awg, if not 12awg. Keep in mind that it must be stranded, not solid wire.

### Motor Power

Cabling for motor power should be between 16awg and 12awg. Again, stranded, not solid wire.

Some motors (like the `REV HD Hex` and `Core Hex`) will have removable power connectors on the back, while other motors (like the `Andymark NeveRests`) will have a cable permanently soldered on the back. It is much more convenient to have a connector on the back, or failing that, have a very short plug on the back of the motor. Once your wires are run and secured, taking them out won't be fun.

### Servo Wires

Using heavy-duty extension wires is recommended.

Tape the connections between extension wires and servo wires with electrical tape, as the connections can become loose over time and are easy to pull out.

The VEX Motor Controller 29 has the wrong gender connector on the 3-pin end. You are required to either use an adapter cable or add the right connector to the wires (recommended). **Be sure to protect the MC29, as it is fragile and prone to failure if it takes impact from another object.**

### USB

USB is generally a strong connector but is prone to wearing out over time. Refrain from plugging/unplugging these cables more than necessary, especially on the RC/DS phones.

USB loves strain relief. To keep disconnects low, tie down cables to leave as little loose cabling on the robot as possible.

### Sensor Wires/Encoder Wires

Sensor wires and their connectors can be incredibly fragile. Use caution when routing, and keep slack on the connector end when adding strain relief to the cable.

The JST data connectors on the REV Expansion Hub and Control Hub have +5v, GND, and two data pins. If you are using a digital or analog sensor that does not use I2C, you can use a Y cable that gives two sensors off of one port.

## Miscellaneous

### REV Grounding Strap

The `REV Grounding Strap` is currently the only legal way to ground your robot. Attach the end to the metal part of your robot frame, and plug the `XT30` connector end into a free `XT30` port on your robot.

### Power Distribution Blocks/Panels

The REV Power Distribution Block allows teams to have more than four `XT30` connectors (2 on each Expansion Hub). The block can be connected to the Servo Power Module to boost voltage for servos.

### Dryer Sheets

Dryer sheets can be used to wipe down the robot after every match to reduce static buildup. This is not directly recommended by *FIRST* or any vendor, but our empirical evidence throughout the years suggests that it helps, or at the very least, can't hurt to do so. However, dryer sheets may or may not be on the boundary of legality, as grounding the robot to the ground is illegal.

### Staticide/Static Spray

Staticide is a spray that helps to keep static off of the robot. Please be sure to spray your robot before an event and not during the event.

### Common Causes of Static

- Every single contact point of your robot to the floor will increase the amount of static buildup.
- Too much turning scrub (or traction when wheels try to turn). This is possible if a 4WD or 6WD (no center drop) with all traction wheels is used.
- A conductive part dragging along the ground. For example, try not to have an intake touch the ground when the robot is moving as much as possible. Foam wheels and foam rollers are a common culprit.
