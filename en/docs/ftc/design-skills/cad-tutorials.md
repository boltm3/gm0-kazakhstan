# CAD Tutorials

## CAD Tutorial Part 1 - Drivetrain in an Hour

### Choosing the Drivetrain

After learning your **CAD** program of choice, determine the necessary requirements for the drivetrain based on the current game. Teams should shoot for the wheelbase that works the best in that specific field's layout.

For instance, in Relic Recovery (2017-2018) a drivetrain required precision to not only grab glyphs from the center pit, but also to line up against the cryptobox. Thus, mecanum wheels and a wide center section of the robot proved an advantage over a 6 wheel tank drive. (However, it should be noted that with sufficient practice and competent drivers, any drive base can be competitive up to a certain extent).

After selecting a drivebase, determine the number of motors. Keep in mind the eight motor limit is a pain that shouldn't be ignored. A good rule of thumb is four motors for driving and four motors for the other mechanisms (e.g. intakes, linear slides, arm, etc.). For most modern FTC |reg| games, you need a minimum of 7 motors to be highly competitive, although 8 is a good rule of thumb.

### Designing the Drivetrain Plates

After learning the CAD software, it's time to start the actual design. Here are some things to figure out before starting:

- Drive Type (mecanum, 6wd, 8wd, etc.)
- Number of Motors (four motors recommended in most cases)
- Type of wheels (**Traction**, **omni**, etc.)
- Drive power (**belt**, **chain**, gear)

To keep it simple, this example uses a 4-wheel tank drive using four motors. The wheels selected are 2 Colson wheels for traction and 2 omni wheels to aid in turning.

First, make the left side of the drivebase. After completing it, all you have to do is mirror the left side to the right, so you don't have to do each side individually. Start with a 2D sketch of everything before trying to extrude and make actual 3D objects.

![Drivetrain Plate Technical Drawing](https://dd8f408.webp.ee/dt-inner-plate-technical-drawing.jpg)
*Drivetrain Plate Technical Drawing*

This is a sketch of the inner plate of the drive base. Everything should be laid out in a 2D sketch to determine the mounting holes, **bore** , **center-to-center distance**, etc. 2D sketches are extremely helpful and are highly recommended in any project. After the sketch is completed, everything else falls into place and becomes pretty simple.

After this, extrude that sketch into the first plate of the drivetrain. Typically, a standard thickness of aluminum plate is 1/8". Thinner plate (3/32") can be used as well, but generally most teams stick to 1/8". Extrude the plate to that thickness. Below is the sketch after extruding.

![Inner Drivetrain Plate](https://dd8f408.webp.ee/dt-inner-plate.jpg)
*Inner Drivetrain Plate*

The next step will be making the outer plate for the drivebase. It is even faster to do than the inner. To do this, simply create a new part. Go back to your inner plate and start a 2D sketch.

![Drivetrain Plate, with entire face selected](https://dd8f408.webp.ee/dt-inner-plate-ui-chrome.jpg)
*Drivetrain Plate, with entire face selected*

After starting the new sketch on the inner plate, hit "Project Geometry" and just click anywhere on the part. It should highlight every outline of the part. (Shown here is a yellow line; yours might be red, blue or some other color.) Now click and drag across the part selecting every line on the screen. Now go hit CTRL + C, then go to the new part and hit create 2D Sketch. Next hit CTRL + V.

![Drivetrain inner plate with the parts specific to the inner plate selected](https://dd8f408.webp.ee/dt-inner-plate-with-parts-to-remove-selected.jpg)
*Drivetrain inner plate with the parts specific to the inner plate selected*

It should look like an exact copy of the inner plate but now as a sketch. Delete your motor mounts out of the middle, then extrude the outer plate.

![Outer Drivetrain Plate](https://dd8f408.webp.ee/dt-outer-plate.jpg)
*Outer Drivetrain Plate*

This is what the outer plate looks like, an almost exact copy of the inner one without the holes for the motors. Now with those two plates made, it's really just time to assemble the rest of the drivetrain, which is by far the most time-consuming. Now, for some info on what to use to attach the two plates together, generally standoffs or churro is highly recommended. To attach the two halves of the drivetrain, use either channel, extrusion, or a custom u-brace. Some teams prefer a custom brace as it is a good way to stiffen up the drivetrain while requiring very little maintenance over the season. It is possible to use peanut extrusion or kit channel, which alternatively works just as well.

Note that when using a custom drivetrain, you can cut out material from your drivetrain plates. This process is called **pocketing**. While not a vital step, pocketing helps you save weight. However, be careful not to remove too much material; if done, the plates become less sturdy. More about pocketing is in the next section.

### Additional Considerations

Powering wheels can be done in a couple of different ways through either belts and pulleys, chains and sprockets, gears, or even powered directly from the motor. Direct drive and chains are the simpler of the options, with direct drive not needing a calculated distance at all just have to set the motor exactly where the center of the wheel is. Chains allow for a little bit of slack, not needing an exact center-to-center distance in the wrap like belts and pulleys do. Finally, gears need to be a certain distance apart from each other to mesh properly and not skip or bind.

Mounting motors is done in a plate style by face mounting the motor into the innermost drivetrain plate. It can also be done by mounting the motors to a 3rd plate, located in between the outside and inside. This allows for the motor to take up less space in the middle of the robot, but adds complexity. Motors should always be as low as possible and depending on where you want the center of mass, either the middle or towards the back of the robot. It is also worth keeping in mind the type of power transmission and the expediency of doing so in light of the motor placement.

Ground clearance is all dependent on if there are any obstacles on the field, as well as what your team wants to do in that game in regards to said obstacles.

For example, in Rover Ruckus some teams with tank drivetrains decided to enter the crater. Therefore, they left enough space to not beach themselves on top of the crater, a common mistake that inexperienced teams often make.

Other teams decided to ignore driving over the crater and decided to reach over with an arm or slide system, which meant they didn't need a lot of ground clearance for their drivebase.

Typically, anywhere from .25 inches of clearance to .5 inches (if you want to be safe) on a completely flat field will allow for the weight of the robot to push into the foam tiles. Nothing else from the robot should touch the ground.

Something you can do is set the robot in CAD onto a field. Set up obstacles such as the crater and simulate driving over the crater by moving it across like you think it would in the real world.

If either of the plates intersect with the obstacle, add some more clearance so you don't get beached like a sad whale.

A general rule of thumb for most teams is the wider the intake, the better the chance of picking up the game piece. However, this is super game-dependent. If you need to pick up a 6" cube like in Relic Recovery, then you would not need 14" of space for your intake.

However, if you need to pick up a ball like in Velocity Vortex, the bigger the intake gives you better chances of grabbing the balls. Keep this in mind when designing drive pods - try to keep them as thin as possible without sacrificing rigidity and strength to maximize space for other mechanisms and wiring.

Connecting your two plates together is really simple. Some standoffs or churro extrusion from AndyMark is a relatively easy way to connect them together with a few bolts. Just make a few 1/4 in. holes in your sketch where you want the churro tube to be. Decide how long the churro needs to be. Remember to leave enough space between the plates for your wheels, pulleys, sprockets, and spacers. You don't need to go overkill on how many standoffs you need in between your plates; however, put them in strategic places where support is needed.

Shown below is a drive pod, which is one half of the drivetrain, including the shafts, bearings, wheels, motors, belts, etc. In short, the drive pod has everything that will be built in real life. This particular one is the left side, but to make the right side, create an offset plane, select the mirror tool, then hit mirror.

![Left side drivetrain pod](https://dd8f408.webp.ee/drive-pod.jpg)
*Left side drivetrain pod*

After mirroring the drive pod to make your opposite side, connect those two halves together and you're done with the drivetrain. Below is a rendering of the complete drivetrain in CAD.

![Complete drivetrain render](https://dd8f408.webp.ee/dt-render.jpg)
*Complete drivetrain render*

## CAD Tutorial Part 2 - Pocketing Guide

### Pocketing

"Pocketing" is a common term in FTC and FRC\ |reg| lingo that refers to cutting out excess material from a CAD-designed part. Pocketing helps to reduce weight and can increase the strength of a part. This may seem counterintuitive (how can removing material strengthen a part?) but pocketing can reduce stress buildup, especially at corners.

Pocketing is often seen on drivetrain sheet metal plates, which will be CNC machined. In FRC, pocketing is often used to reduce the weight of the rectangular aluminum tubes.

There are several ways to machine pockets into material including milling, routing, water jet cutting, laser cutting, and even hand drilling. Depending on your access to tooling, pocketing can be more or less difficult for you.

CNC milling and routing excel at pocketing aluminum box tubing, whereas water jet and laser cutting excel at pocketing plates. Whether pocketing on box tubing or plates, the design is fairly similar.

When designing pockets, **it's important to consider the type of material, thickness, and how much stress will be on the part**. Materials that are weaker, thinner, or under significant stress should have less "aggressive" pocketing and materials that are stronger, thicker, or under less stress can have more "aggressive" pocketing. Aggressive pocketing refers to the amount of material removal from the blank part (more aggressive = more material removal).

Although a bit complex to understand, FEA (finite element analysis) can be used to determine appropriate strut thickness when pocketing. FEA can be used to generate pocketing geometry, but that is an entirely different rabbit hole.

![FEA of inner drivetrain plate](https://dd8f408.webp.ee/fea-on-plate.jpg)
*FEA of inner drivetrain plate*

Designing concise and advantageous pocketing is as simple as drawing circles and tangent lines. Parametric pockets can be defined by one or two offset values. The offset values determine the thickness of
