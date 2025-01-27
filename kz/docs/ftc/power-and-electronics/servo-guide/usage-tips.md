# Servo Usage Tips

Below are some tips on using servos in FTC.

- **Do not backdrive servos**. Forcibly rotating a powered servo away from its position risks damaging the internal gears.
- **Pay attention to a servo's travel range!** The FTC API, by default, outputs 600-2400 microseconds. `ServoImplEx` can be used to increase the range to a maximum of 500-2500 microseconds.

  ```java
     ServoImplEx servo = hardwareMap.get(ServoImplEx.class, "myservo");
     // ...
     servo.setPwmRange(new PwmRange(500, 2500));
  ```

- **Servo wires usually are black-red-white**. Matching the colors is an easy way to check if the servo is plugged in correctly. Servo connectors provide no protection from plugging them the wrong way: if you rotate it 180 degrees, it will still fit—but the servo would not work. (It wouldn't be damaged, though). Thus, if your servo is not working, first check if they are plugged in correctly. Then check it again.
- When using **servo wire extensions**, use [retaining clips](https://www.gobilda.com/servo-connector-clip-yellow-6-pack/) to prevent the connection from coming apart when someone pulls on the wire. Alternatively, electrical tape will work in a pinch.
- **Do not use socket head screws to attach servos**—when tightened, they will damage the plastic. Use button head screws or socket heads with a washer.
- **Servos break easily** when subjected to lateral loads or bending of the shaft. For example, if you mount an arm or a claw directly on the servo without any additional precautions, it is very likely that you will break the servo the first time you drive into the wall with the arm extended (and this will inevitably happen).

  To avoid that, use additional supports. The easiest way to do it is by using **Servoblocks** from Actobotics or goBILDA. These assemblies act as exoskeletons for the servo, providing additional support. They are expensive, but worth every penny. Additionally, REV offers the inside and outside channel **servo brackets**, which when paired with the aluminum servo shaft adapter and **ball bearing assembly**, fulfill the same function.

  ![A servo in a ServoBlock](https://dd8f408.webp.ee/servoblock.jpg)
  *Image: A servo in a ServoBlock*

There are also some alternative designs of servo supports; one of them, which is not as strong as the original **Servoblock** but much more compact, is shown below. ([CAD](https://myhub.autodesk360.com/ue2801558/g/shares/SH56a43QTfd62c1cd968b8829158db7626b9) is also available):

  ![Alternative servo support block](https://dd8f408.webp.ee/compact_servo_block.jpg)
  *Image: Alternative servo support block*

- **Use linkages.** Instead of mounting some rotating piece directly on a servo, mount it so it can rotate around a pivot point and then connect it to the servo using linkage as shown below:

  ![Linkage example](https://dd8f408.webp.ee/linkage.jpg)
  *Image: Linkage example, courtesy of team 4137 Islandbots. A goBILDA flat beam is used as the link.*

- If you need more power, use a [REV Servo Power Module](https://www.revrobotics.com/rev-11-1144/).

## Term

### Servo Power Module
A Servo Power Module (SPM) is a device made by REV Robotics that boosts the voltage that the Expansion Hub provides to a **servo**. The Expansion Hub's output for servos is 5V at 6 amps, and the SPM boosts the voltage to 6V and up to 15 amps.

**This is important for servos under high load conditions such as the Savox servo.**

![A REV Robotics Servo Power Module](https://dd8f408.webp.ee/servo-power-module.jpg)
*Image: A REV Robotics Servo Power Module*
