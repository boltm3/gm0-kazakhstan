# Fastener Guide

If you want your robot to stay in one piece, you will need fasteners. Fasteners are any pieces of hardware that mechanically join parts. This guide will discuss common types of fasteners, and how to use them on your robot.

## Threaded Fasteners

Bolts, screws and nuts are all threaded fasteners -- meaning they use a helical thread to join parts.

### Thread Basics

To understand threaded fasteners, you will need to know some basic terminology

![Thread Diagram](https://dd8f408.webp.ee/thread-diagram.jpg)
*Diagram displaying thread pitch and the difference between internal/external threads and major/minor diameters.*

- **External Thread**: A thread on an outside surface. For example, bolts have external threads.
- **Internal Thread**: A thread on an inside surface. For example, nuts have internal threads.
- **Thread Pitch**: The distance from one thread to another, measured along the length of the thread. This can also be expressed as the number of threads per unit of length, for example threads per inch.
- **Major Diameter**: The largest diameter of the thread profile.
- **Minor Diameter**: The smallest diameter of the thread profile.

### Thread Standards and Naming

There are two main systems of naming and sizing threads that you will encounter in FTC: UTS imperial sizing and ISO metric sizing.

#### Imperial (UTS)

The universal thread standard (UTS) is based on the imperial system and commonly used to size threads in the US and Canada. A UTS thread is named by a number indicating the major diameter of the thread, followed by the thread's pitch measured in threads per inch.

For major diameters of 1/4" or greater, the first number is simply the major diameter in inches. For those smaller than 1/4", the following code is used:

| No.  | Major Diameter (inches) |
|------|-------------------------|
| #0   | 0.0600                  |
| #1   | 0.0730                  |
| #2   | 0.0860                  |
| #3   | 0.0990                  |
| #4   | 0.1120                  |
| #5   | 0.1250                  |
| #6   | 0.1380                  |
| #8   | 0.1640                  |
| #10  | 0.1900                  |
| #12  | 0.2160                  |

Some common imperial thread sizes in FTC include 1/4-20 (one quarter inch major diameter, 20 threads per inch) and #6-32 (0.138 inch major diameter, 32 threads per inch).

#### Metric (ISO)

The ISO metric thread standard is commonly used worldwide, and for many products sold by FTC vendors.

A metric thread is designated by the letter M followed by the outer diameter in millimeters, for example M4 for a 4 mm major diameter bolt. This is then followed by a "x" and the pitch, also in millimeters. For example, "M4X0.7" means a M4 thread with a 0.7 mm pitch.

### Bolts

Bolts are the most commonly used fastener in FTC.

There are several types of bolts you may encounter, such as:

#### **Socket Head Bolts**

![Socket Head Bolt](https://dd8f408.webp.ee/socket-head.jpg)
*Socket head bolt*

These bolts have a cylindrical head and are tightened and loosened with a hexagonal recess.

#### **Button Head Bolts**

![Button Head Bolt](https://dd8f408.webp.ee/button-head.jpg)
*Button head bolt*

These bolts have a domed head, in contrast to the flat top of a standard socket bolt.

#### **Countersunk Head Bolts**

![Countersunk Head Bolt](https://dd8f408.webp.ee/countersunk-head.jpg)
*Countersunk head bolt*

These bolts have a cone-shaped head, and can be used in countersunk (cone-shaped) holes to achieve a flush surface finish.

#### **Grub Screws**

![Grub Screw](https://dd8f408.webp.ee/grub-screw.jpg)
*Grub screw*

These bolts have no head, the recess is instead embedded within the threads. They are primarily used as set screws.

#### **Hex Bolts**

![Hex Head Bolt](https://dd8f408.webp.ee/hex-head.jpg)
*Hex head bolt*

The bolts are tightened with an external hex-shaped head. When designing for these bolts, it is important to allow clearance on the side of the head for tightening.

Every bolt requires a "drive" -- meaning the geometry which is used to turn and install it. Each of the bolts listed above can have a variety of different types of drives:

![Types of Drives](https://dd8f408.webp.ee/types-of-drives.jpg)
*Diagram showing thread terminology*

### Nuts

A nut is a fastener with an internally threaded hole. Together with a bolt, they're used to join parts together.

Here are some types of nuts you may encounter in FTC:

#### **Hex Nuts**

![Hex Nut](https://dd8f408.webp.ee/hex-nut.jpg)
*Hex nut*

These are the most common type of nut. They can be tightened with a socket hex wrench.

#### **Square Nuts**

![Square Nut](https://dd8f408.webp.ee/square-nut.jpg)
*Square nut*

These are four-sided nuts. They work well in small spaces and can be easily inset into square pockets to keep from rotating.

#### **T-slot Nuts**

![T-slot Nut](https://dd8f408.webp.ee/t-slot-nut.jpg)
*T-slot nut*

These can be inserted into t-slot extrusion to tighten parts onto it.

#### **Wing Nuts**

![Wing Nut](https://dd8f408.webp.ee/wing-nut.jpg)
*Wing nut*

These nuts can be easily tightened without a wrench.

#### **Nyloc Nuts**

![Nyloc Nut](https://dd8f408.webp.ee/nyloc-nut.jpg)
*Nyloc nut*

These nuts contain a nylon ring which prevents loosening by increasing friction on the bolt thread. We recommend using these wherever possible.

### Making Threads

Sometimes, you will want to create new threads. This process is called threading. To create internal threads, you can use a cutting tool called a tap -- essentially a sharper version of a screw.

To create external threads, you use a tool called a die.

![Tap and Die](https://dd8f408.webp.ee/tap-and-die.jpg)
*Diagram showing a tap and die*

### Threadlocker

Bolts on your robot may loosen over time, especially if there are heavy vibrations. To prevent this you may use locking nuts or lock washers, which mechanically press against the thread. Another solution is to use a threadlocker, which is an adhesive compound that -- as its name suggests -- locks threads in place.

#### Loctite

The most popular threadlocker among FTC teams is Loctite. There are two types of Loctite: blue, which is removable, and red, which is permanent (and we mean it). To use Loctite, apply it to the thread of the bolts.

>**Note:** It is highly recommended that teams use Loctite on all motor and [servo](#) mounts, as well as any mechanism prone to vibration.

!>**Danger:** Blue or red Loctite should not be used with brittle plastics such as polycarbonate. This is known to cause the plastic to crack. Instead, either use a [cyanoacrolate-based glue](https://www.loctiteproducts.com/products/central-pdp.html/loctite-super-pro-gel/SAP_0201DGL029Z5.html) or use a [screw with a nylon patch](https://www.mcmaster.com/products/screws/socket-head-screws~/18-8-stainless-steel-thread-locking-socket-head-screws/) as this will not damage the plastic.
Also note: **THE BOTTLE COLOR AND THE FLUID COLOR ARE REVERSED.** When we refer to the "color", we mean the fluid color. Blue Loctite usually comes in a red bottle.

![Loctite](https://dd8f408.webp.ee/loctite.jpg)
*A red bottle containing blue (removable) Loctite, and a blue bottle containing red (permanent) Loctite*
