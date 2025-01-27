# Choosing a Servo

Choosing a **servo** can seem daunting at first, given the number of options to consider. This guide is intended to provide a starting point to compare different servo options, and also has some hand-picked recommendations at the end.

> **Important:**  
> It is very important to keep the reliability of a given vendor in mind when choosing servos. It is not uncommon for manufacturers and resellers on Amazon and other similar sites to exaggerate their servos' specs or pick unrealistic best-case scenarios for measuring the specs. We have limited our recommendation only to vendors who historically have been reliable with publishing servo specifications.  
> As a rule of thumb, established manufacturers (e.g., HiTech, Savox, ServoCity, Gobilda, Andymark, etc.) will usually publish accurate numbers, and servos from marketplaces (e.g., Amazon, AliExpress, etc.) should be viewed with some skepticism.

## Servo Type: Regular or Continuous

**Servos** that can rotate to a given position based on PWM input signal are called **regular servos**. In addition, there are also **continuous rotation servos**, which are effectively just small motors in a **servo** form factor. They have no position control; instead, PWM signal is used to control their rotation speed.

Many servos from FTC vendors are **Dual Mode**, meaning they can switch between continuous and regular modes (often requiring the use of a sold-separately servo programmer). These servos can be used as either continuous or regular servos.

## Servo Torque And Speed

**Servo** output power is measured in both **speed** and **torque**. Speed (normally in seconds per 60°) refers to how fast the **servo** turns 60 degrees in Standard Rotation mode.

> **Why seconds per 60 degrees?**  
> Historically, the servos commonly used in FTC were created for RC (Radio Controlled) car setups. These cars often had steering linkages with a maximum side-to-side travel of 60 degrees, so manufacturers would often advertise their servos using seconds for 60 degrees.

Torque (usually measured in oz-in or in kg-cm) refers to the amount of force the **servo** can apply to a lever. For reference, if you put a 1" bar on a servo, then put a force gauge on the end, the torque rating of the servo (in oz-in) will be measured.

As you may know, speed and torque will generally have an inverse relationship. You can find some insanely powerful servos that are pretty slow (slower than 0.20 s/60°) or some less powerful ones with faster ratios (anything faster than 0.12 s/60° is considered very fast).

Finding the right **servo** for your application can be tough, but a good way is trying to decide if you need more speed or torque, and if your **servo** will experience shock loads or not.

## Durability and Servo Gear Material

The two things that threaten a **servo's** longevity are the internal motor burning out and, more commonly, the **gears** stripping inside the **servo**. A motor burning out is pretty uncommon, but it can happen under large loads for a prolonged amount of time.

!> **Caution:** You should **never** stall a servo against an immovable object.

Gear stripping is a very common problem which occurs when the torque needed to actuate a component exceeds that of the **servo's** maximum torque. There are two main cases when this can occur:

1. Shock load from external force can strip the **gears** easily, regardless of which material the **gears** are made from. An example could be the component slamming into the field wall or another robot.
2. Shock load from reversing directions on an object that is too heavy can strip the **gears**. Torque increases with mass and also distance from the center of rotation. If the component being actuated is far from the **servo**, the long lever arm means larger torque. Furthermore, if the component is moving, reversing direction also will require more torque. Thus, the principle is that components should be light and not reverse direction suddenly to prolong **servo** life.

Shock load resistance is impacted directly by the material the **gears** are made from. This ranges from plastic to titanium, so let's go down the list, starting from the weakest:

- **Plastic**: Used with low power **servos**, these are generally okay. Normally used for applications in model airplanes such as ailerons. FTC applications include light load mechanisms which will not have direct contact with any game elements or the field, such as a servo that opens a trapdoor or moves game elements within the robot.
- **Karbonite**: Hitec's **gear** plastic is a very durable and long-lasting plastic that is very good under long use and low load. Be aware that it can strip easily under the shock loads found in FTC. Karbonite is more durable than plastic but still suffers from shock loads.
- **Brass**: Brass **gears** are stronger than plastic but also suffer greatly when faced with shock loads in FTC, such as intake wrists and deposit buckets. Found in slightly higher-end servos like the REV Smart Servo.
- **Steel**: Steel **gears** are very durable, and you'll have a tough time stripping these. In general, expect to pay a premium. The goBILDA Dual Mode servos (v2) is an example of steel **gear** **servo**.
- **Titanium**: Titanium is the high-end, virtually unbreakable material for **servos**. Starting from $75, they can reach over $150. A common misconception is that titanium is stronger than steel; however, its advantage is in strength-to-weight ratio (titanium gearboxes are often lighter than steel ones).

## Servo Size

**Servos** come in different sizes. Fortunately, almost all manufacturers use the same standard set of **servo** sizes, ranging from sub-micro to large. The two sizes commonly used in FTC are **standard size** (which includes REV Smart Servo and goBILDA Dual Mode Servos) and **large size** (also known as quarter-scale) **servos**. However, large **servos** are quite uncommon.

Note that while in general, the larger the size, the more powerful the **servo**, it is not a strict rule. You can buy very powerful standard size **servos** — just expect to pay more for them.

## Servo Spline

The output shaft of the **servo** is commonly called the **spline**. Most servos have industry standard 25-tooth spline (also known as F3); in particular, this is the spline used by REV Smart Servo and goBILDA Dual Mode servos. However, Hitec servos use a 24-tooth spline.

Andymark servos are an exception, as they use a 5mm hex shaft instead of a 24 or 25 tooth **servo spline**.

!> **Attention:** Please check the spline type before you buy the **servo** — otherwise, your **servo** attachments will not fit.  
> For more info about servo splines, please check [ServoCity](https://www.servocity.com/servo-spline-info/).

## Servo Range

The angle over which a non-continuous **servo** can rotate while retaining position feedback is called the range. When choosing a **servo**, it is important to make sure you have enough range for the movement you need.

By default, the FTC Control Hub and FTC Expansion Hub output 600-2400 microsecond signals. However, this range can be expanded to 500-2500 microseconds. When choosing a **servo**, ensure that its range will be usable for your application inside of 500-2500 microseconds.

> **Note:**  
> The default 600-2400 range of the FTC Expansion Hub and FTC Control Hub can make it appear that popular servos like the goBILDA Dual Mode servos and REV Smart Robot Servo have less range than advertised. You can use the following code to expand the range to 500-2500 microseconds.
>
  >```java
  ServoImplEx servo = hardwareMap.get(ServoImplEx.class, "myservo");
  ...
  servo.setPwmRange(new PwmRange(500, 2500));
 >```

## Cost

**Servos** range from cheap $7 **servos** for light applications, all the way up to some Hitec or Savox **servos** for close to $200.

The best **bang for your buck** **servos** are the **goBILDA dual mode** and **REV SRS** servos. In addition, the **Andymark High Torque/Speed** servos are promising, but have not been released or tested at the time of writing.

The biggest downside to the REV SRS are their brass **gears**. Coupled with high output power, this meant that stripping **gears** with any shock load was commonplace.

Hitec is a big name in the servo market, offering inexpensive but easily broken low-end **servos**. Their mid-range servos, like the HS 485-HB/488-HB, use Karbonite **gears** and are suitable for general use, such as claws or trapdoors.

For budgets over $100, Hitec offers very powerful **servos**, most of which feature titanium **gears** and are programmable for fine-tuning.

Savox produces high-performance servos with titanium **gears** that are fast and brushless, although they can be noisy under load.

## Recommended Servos

### Bang for Your Buck

- [goBILDA Dual Mode Servo (Torque) (25-2-torque)](https://www.gobilda.com/2000-series-dual-mode-servo-25-2-torque/)
  - A very good price to performance servo. It is dual mode, has a higher than average output torque (and correspondingly lower speed), and steel gearbox.
- [goBILDA Dual Mode Servo (Speed) (25-3)](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/)
  - A very good price to performance servo. It is dual mode, has a higher than average output speed (and correspondingly lower torque), and steel gearbox.
- [REV Smart Servo](https://www.revrobotics.com/rev-41-1097/)
  - While very good price to performance, its brass gearbox makes it less recommended than goBILDA Dual Mode Servos.
- [Andymark High Speed/Torque Servo](https://www.andymark.com/products/programmable-servos/)
  - A newcomer to the market, this servo is promising as a price-to-performance servo with a unique 5mm hex output and imperial half-inch mounting pattern. The high speed variant has more power output than the commonly used goBILDA Dual Mode servo. The high torque servo has a higher efficiency than the goBILDA Dual Mode servo.

### Premium Options

- [Axon Robotics MAX+](https://axon-robotics.com/products/max/)
  - The best price-to-performance high-performance servo. It has high efficiency and high power output, and can track its absolute position via an analog output wire.
- Hitec titanium servos  
  - A reliable choice, Hitec offers a variety of servos, making it a good option for specific needs, such as high speed or very high torque.

### Specialty Servos

- [goBILDA 5 Turn Servo](https://www.gobilda.com/2000-series-5-turn-dual-mode-servo-25-2-torque/)
  - goBILDA manufactures all three of their Dual Mode servos in 5-turn variants, which can rotate 5 turns while still tracking position. These servos have high range, making them ideal for use with external gearboxes.

**REV** and **goBILDA** **servos** can be purchased from their respective websites. For other servos, sources like [ServoCity](https://www.servocity.com/) or [Amazon](https://www.amazon.com/) are good options.
