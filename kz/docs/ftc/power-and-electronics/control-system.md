# Control Systems

The FTC control system is based around a "**Robot Controller**" and a "**Driver Station**". The **Robot Controller** is mounted on the robot. It is either embedded within or connected to special "Hub(s)", which in turn connect to motors, servos, and sensors. The **Robot Controller** is linked to the **Driver Station** through WiFi or WiFi Direct.

REV Robotics is the sole manufacturer of legal FTC control system components. The REV Expansion Hub connects to motors, servos, sensors, and a **Robot Controller**. A REV Control Hub has the same functionality as an Expansion Hub but with a built-in **Robot Controller**.

More information about the FTC Control System can be found below:

- [Official Control System Documentation on FTC Docs](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/control_system_intro/The-FTC-Control-System.html)
- [REV Control System Documentation](https://docs.revrobotics.com/duo-control/)
- [Official troubleshooting guide](https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/control-system-troubleshooting-guide.pdf)

There are two possible control systems that can be run on an FTC robot legally:

- REV Control Hub + REV Expansion Hub
- **RC Phone** + REV Expansion Hub(s)

## REV Control Hub + REV Expansion Hub

!> **Warning**: It is of vital importance to update the firmware on REV Expansion hubs to at least version 1.8.2. It includes better protection against disconnects and improves program performance. See the [REV Expansion Hub firmware update docs](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware).

This is the standard control system for teams starting out in FTC.

The Control Hub connects to the Expansion Hub through either an RS-485 connection or a USB-A (Control Hub side) to mini-USB (Expansion Hub-side) connection. In either case, proper strain relief and cable management should be used.

For more information on setting up the Control Hub and configuring the robot, head to [REV Robotics' Technical Resources Control Hub Guide](https://docs.revrobotics.com/duo-control/control-hub-gs).

![A diagram of the Control Hub + Expansion Hub control system](https://dd8f408.webp.ee/ch-wiring-diagram.jpg)
*Image: Control Hub + Expansion Hub control system diagram*

## RC Phone + REV Expansion Hub(s)

!> **Warning**: It is of vital importance to update the firmware on REV Expansion hubs to at least version 1.8.2. It includes better protection against disconnects and improves program performance. See the [REV Expansion Hub firmware update docs](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware).

The Expansion Hub connects to the **Robot Controller** phone through its mini USB port. The REV Expansion Hub is reliable, as long as proper strain relief and wiring are carried out. This includes the **USB Retention Mount**, as well as 3D printing **XT30** stress relief mounts.

For more information on setting up the Expansion Hub and configuring the robot, head to [REV Robotics' Technical Resources Expansion Hub Guide](https://docs.revrobotics.com/duo-control/legacy/expansion-hub-gs).

- [USB Retention Mount](https://www.revrobotics.com/rev-41-1214/)
- [XT30 Stress Relief](https://www.thingiverse.com/thing:2887045)

![A diagram of the RC Phone + Expansion Hub(s) control system](https://dd8f408.webp.ee/exh-wiring-diagram.jpg)
