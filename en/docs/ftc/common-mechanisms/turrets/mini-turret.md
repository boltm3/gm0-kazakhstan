# Mini Turrets

Mini turrets are turrets that pivot something small, typically an end effector. These are often at the end of a linear extension or arm. These are much simpler than full turrets, because they are physically smaller and deal with much smaller loads. There are many ways to implement a mini turret, and generally any of the methods mentioned on the [full-turret](en/docs/ftc/common-mechanisms/turrets/full-turret) page will work, but the center-bearing technique is the most common, as it is the simplest.

## Advantages

- Allows for accurate mechanism rotation, without drivetrain movement.
- Much simpler than a full turret.

## Disadvantages

- Heavier than just an end effector, which is especially important on the end of slides/arms because of mechanism speed and center of gravity.
- More complex than no turret.
- Provide fairly limited range compared to full turrets.

![12518 Almond Robotics' Mini Turret](https://dd8f408.webp.ee/12518-turret.jpg)

*12518 Almond Robotics, Freight Frenzy, a **center-bearing mini turret** on the end of slides used to rotate a scoring mechanism with a servo*
