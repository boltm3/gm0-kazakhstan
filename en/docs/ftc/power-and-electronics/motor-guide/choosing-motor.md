# Choosing a Motor

## Legal Motors

12 V motors are strictly controlled by FTC® rules. As of the 2020-2021 season, the only FTC legal motors are the following:

- [TETRIX 12V DC Motor](https://www.pitsco.com/TETRIX-DC-Gear-Motor) (`regular`, `Torquenado`)
- [AndyMark NeveRest series 12V DC Motors](https://www.andymark.com/categories/mechanical-gearboxes-gearmotors)
- Modern Robotics/MATRIX 12V DC Motors (this also includes [goBILDA motors](https://www.gobilda.com/motors/), which are MATRIX motors with a different gearbox)
- [REV Robotics HD Hex 12V DC Motor](https://www.revrobotics.com/rev-41-1301/)
- [REV Robotics Core Hex 12V DC Motor](https://www.revrobotics.com/rev-41-1300/)

With the exception of the **REV Core Hex Motor**, which is discussed separately, all other motors above have very similar structures. They consist of the following components:

- **Bare motor**: In all cases above, this is a 12V motor of the **RS-555 type**, with a free speed around 6,000 RPM and a stall current around 10A. The motor specs posted by different vendors might be slightly different, but the difference is mainly due to different testing methods. In real life, the bare motors used by **AndyMark NeveRest motors**, **REV Robotics HD Hex motors**, and **goBILDA motors** are virtually identical. The most reliable specs can be found in the **motor-data** section.
- **Gearbox**: The gearbox is attached to the front of the motor and reduces the speed while increasing the torque. For example, a 20:1 gearbox reduces the speed by a factor of 20, resulting in a no-load speed of around 300 RPM. A gearbox also contains the output **shaft** (typically 6mm D profile; REV motors use 5mm hex shafts) and mounting holes. The gearbox can also be replaced; this is FTC legal but requires some skill.
- **Encoder**: Attached to the back of the motor and protected by a plastic cap, the **encoder** contains a sensor registering motor **shaft** rotation. It can be connected to REV hubs and used for precise control of motor speed or rotating to a specific position.

Since the bare motor is similar for all motors discussed above, the choice of the right motor is dictated by the gearbox: the **gear ratio**, output **shaft** type, and ease of mounting.

## Gearboxes

There are two kinds of gearboxes: **spur** and **planetary** (also known as **orbital**). Their inner structure and differences are discussed in detail in the **gearbox anatomy** section. For new teams, it suffices to know that planetary gearboxes are slightly more expensive, but more reliable. Spur gearboxes can strip under shock loads (for example, when your robot hits a wall), requiring you to replace the gearbox. For this reason, it is advised to use planetary gearboxes in high-load use cases such as drivetrains.

### Available Spur Gearboxes and Motors

!> **Warning**: Spur gearboxes are **NOT** recommended due to their shorter lifespan and lower mechanical resilience compared to planetary gearboxes. If you are purchasing new motors, it is highly suggested to purchase planetary gearbox motors instead. Care should be taken to not put load on the output shaft of a spur gearbox. In particular, spur gear motors should **NOT** be used in high-load applications, such as a drivetrain.

Motors with spur gearboxes include:

- **AndyMark NeveRest Classic motors** (in 40:1 and 60:1 ratios)
- **REV HD Hex 40:1 Spur motor**
- **goBILDA 5201 Series Yellow Jacket Spur Gear Motors**

All of them offer similar performance and reliability, so your choice is primarily dictated by the convenience of mounting and connecting to the rest of your design (e.g., if you use REV kit, you should probably choose the **REV HD Hex motor**, as it uses the same **5mm hex shaft** as the rest of the REV system).

- goBILDA's 5201 series spur gearboxes are much cheaper than either REV's or Andymark's; whether that's a good or bad thing is up to you. They utilize the rather uncommon (in the FTC world) bullet connection for power. However, these are now discontinued. The output shaft is a 6mm D-shaft.
- **REV HD Hex Planetary 40:1 motor** - This motor comes only in a 40:1 ratio, but does use the same connections (**JST VH**) as the REV Expansion and Control Hub for power, which means no adapter cables. The output **shaft** is a 5mm hex. **REV UltraHex** has a 5mm hex **bore** running through the middle of a 1/2" hex **shaft**, which makes adapting this motor to any length of **UltraHex**, and by extension, 1/2" hex **shaft**, very easy.
- **AndyMark NeveRest Classic motors** come in a few different ratios, which are 40:1 and 60:1. The output shaft is a 6mm D-shaft, and like all **NeveRest motors**, they use the **Anderson PowerPole** to connect to power. This connector is perhaps the most robust of the ones listed here.

### Planetary Gearboxes

Standard planetary gearboxes include:

- **Andymark NeveRest Orbital motors**
- **REV 20:1 Planetary motor**
- **goBILDA's 5202/5203/5204 Series Yellow Jacket Motors**

Any of these "standard" gearboxes are more robust than spur gearboxes. Like the spur gearboxes, the gearboxes from different vendors, while not interchangeable, are very comparable in terms of robustness. Once again, the main thing to consider here is your desired reduction, your desired motor connections, and your desired output **shaft** type.

- **goBILDA Yellow Jacket** has the most varied selection of gearbox ratios with too many to list here, but utilizes the rather uncommon bullet connection for power. The output **shaft** is a **6mm D-shaft** or 8 REX (7 mm hex rounded to 8 mm).
- **REV HD Hex Planetary motor** - This motor comes only in a 20:1 ratio, but uses the same connections (**JST-VH**) as the REV Expansion and Control Hub for power, which means no adapter cables. The output shaft is a **5mm hex shaft**. **REV UltraHex** has a 5mm hex **bore** running through the middle of a **1/2" hex shaft**, which makes adapting this motor to any length of **UltraHex**, and by extension, **1/2" hex shaft** very easy. The ratio of the **HD Hex Motor** is 20:1.
- **Andymark NeveRest Orbital motors** come in two ratios: 3.7:1 and 20:1. The output shaft is a **6mm D-shaft**, and like all **NeveRest motors** they use the **Anderson PowerPole** to connect to power. This connector is perhaps the most robust of the ones listed here.
- [**REV UltraPlanetary**](https://www.revrobotics.com/rev-41-1600/) gearbox - The UltraPlanetary is a customizable planetary gearbox that is designed for FTC. The three gearbox options are 3:1, 4:1, and 5:1, and can be mixed & matched to create a custom ratio. It is possible to use from one to three gearboxes for a minimum ratio of 3:1 and a maximum of 125:1.

  > **Note**: While REV lists the UltraPlanetary stages as 3:1, 4:1, and 5:1, their actual gear ratios are slightly different. Consult the [REV UltraPlanetary User's Manual for the exact gear ratios](https://docs.revrobotics.com/ultraplanetary/ultraplanetary-gearbox/cartridge-details).

  The UltraPlanetary was intended to give teams maximum customization without the typical limiting factor – high cost. The total cost for the three-stage gearbox and motor is *exceptionally* good value for a customizable motor. In addition, the UltraPlanetary has a female 5mm hex output **shaft**, which allows teams to customize the shaft length.

## Choosing The Right Gearbox

For regular use, any of the planetary gearboxes will fit your needs. Planetary gearboxes are just a tiny bit more expensive, but boast better backlash and efficiency, higher load capacity, and better capacity for shock loads than spur gearboxes. The tradeoffs, cost, and mechanical noise are almost never a factor.

> **Tip**: Because both gearbox types are so similar in price for similar ratios, we generally recommend the use of a planetary over a spur gearbox.

If you already own spur gearboxes, try to use them in lower-load situations and use planetary motors on your drivetrain.

For small reductions, it may be more economical to choose a motor you already own and build an external reduction using gears, chain, or belts. It should again come down to your desired output shaft, desired gear ratio, and for the UltraPlanetary, whether you want the ability to swap parts out on the fly.
