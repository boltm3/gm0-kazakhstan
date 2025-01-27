# Kinematics

Kinematics is the application of geometry to the control of various robot mechanisms. Kinematics equations are used to control mechanisms by providing specific inputs to achieve a desired output.

Many of the kinematics equations here were taken from [Controls Engineering in the FIRST Robotics Competition (book)](https://file.tavsys.net/control/controls-engineering-in-frc.pdf) and [Mobile Robot Kinematics for FTC (paper)](https://github.com/acmerobotics/road-runner/blob/master/doc/pdf/Mobile_Robot_Kinematics_for_FTC.pdf), which contain the relevant derivations. While only tank (differential drive) and mecanum kinematics equations are shown here, these sources also contain derivations for other mechanisms such as swerve and dead wheel odometry.

## Forward vs Inverse Kinematics

Mechanisms may have different sets of equations for their forward and inverse kinematics. Forward kinematics are the equations used to determine the state of a system given the state of its outputs, whereas inverse kinematics determines the output of a system given the desired state. For example, in a drivetrain, forward kinematics would determine body velocity of the robot based on the individual velocities of the wheels, whereas inverse kinematics would determine the required wheel velocities for a desired body velocity.

## Tank (Differential Drive)

A tank, or differential drive, is a drivetrain consisting of two sets of wheels on either side of the robot that are independently driven. These are described under further detail in the [Tank Drivetrain section](#).

### Variables

The following variables are used in this section:

- $( v_r )$ denotes the linear velocity of the right wheel(s)
- $( v_l )$ denotes the linear velocity of the left wheel(s)
- $( v_f )$ denotes the forward velocity of the robot, relative to itself
- $( \omega )$ denotes the rotational velocity of the robot in radians/second
- $( r_b )$ denotes the base track radius, or the distance between the wheel and center of the robot (half of the distance between wheels)

!>**Warning:** These variables, with the exception of $( \omega )$, represent **linear** velocities, not **rotational** velocities. Wheel rotational velocity in radians/second can be converted to linear velocity by multiplying by the wheel's radius.
 Positive rotational velocity ($( \omega )$) will spin the robot COUNTERCLOCKWISE when viewed from above. 

### Forward Kinematics

The forward kinematics of a tank drive relate the velocity of the wheels to the forward and rotational velocities of the robot, relative to itself. The forward velocity $( v_f )$ and the rotational velocity $( \omega )$ are given by:

$$
v_f = \frac{v_r + v_l}{2}
$$

$$
\omega = \frac{v_r - v_l}{2 r_b}
$$

### Inverse Kinematics

The inverse kinematics of a tank drive relate the desired velocity of the robot to the velocity required of the wheels. These velocities are:

$$
v_r = v_f + r_b \cdot \omega
$$

$$
v_l = v_f - r_b \cdot \omega
$$

## Mecanum Drive

### Variables

Mecanum kinematics uses the same variables as differential drive, except with four wheel velocity variables and an additional robot velocity vector for the left-to-right velocity.

- $( v_{\mathrm{fr}} )$ denotes the linear velocity of the front (leading) right wheel
- $( v_{\mathrm{br}} )$ denotes the linear velocity of the back (trailing) right wheel
- $( v_{\mathrm{fl}} )$ denotes the linear velocity of the front (leading) left wheel(s)
- $( v_{\mathrm{bl}} )$ denotes the linear velocity of the back (trailing) left wheel(s)
- $( v_f )$ denotes the forward velocity of the robot, relative to itself
- $( v_s )$ denotes the strafe (sideways) velocity of the robot, relative to itself
- $( \omega )$ denotes the rotational velocity of the robot in radians/second
- $( r_b )$ represents the base track radius, or the distance between the wheel and center of the robot (half of the distance between wheels)

>**Warning:** These variables, with the exception of $( \omega )$, represent **linear** velocities, not **rotational** velocities. Wheel rotational velocity in radians/second can be converted to linear velocity by multiplying by the wheel's radius.

Positive rotational velocity ($( \omega )$) will spin the robot COUNTERCLOCKWISE when viewed from above.

### Forward Kinematics

The forward kinematics of a mecanum drive relate the velocity of the wheels to the forward, strafe, and rotational velocities of the robot, relative to itself. These are:

$$
v_f = \frac{v_{\mathrm{fr}} + v_{\mathrm{fl}} + v_{\mathrm{br}} + v_{\mathrm{bl}}}{4}
$$

$$
v_s = \frac{v_{\mathrm{bl}} + v_{\mathrm{fr}} - v_{\mathrm{fl}} - v_{\mathrm{br}}}{4}
$$

$$
\omega = \frac{v_{\mathrm{br}} + v_{\mathrm{fr}} - v_{\mathrm{fl}} - v_{\mathrm{bl}}}{4 \cdot 2r_b}
$$

### Inverse Kinematics

The inverse kinematics of a mecanum drive relate the desired velocity of the robot to the velocity required on the wheels. These are:

$$
v_{\mathrm{fl}} = v_f - v_s - (2r_b \cdot \omega)
$$

$$
v_{\mathrm{bl}} = v_f + v_s - (2r_b \cdot \omega)
$$

$$
v_{\mathrm{br}} = v_f - v_s + (2r_b \cdot \omega)
$$

$$
v_{\mathrm{fr}} = v_f + v_s + (2r_b \cdot \omega)
$$

