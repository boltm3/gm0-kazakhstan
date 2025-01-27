```markdown
# Using Android Studio

[Android Studio](https://developer.android.com/studio/intro) is an integrated development environment (IDE) for Android app development based on IntelliJ. It compiles your code to an APK, which is then installed onto the Robot Controller: either the Control Hub or a legal Android phone.

## Downloading Android Studio

If you've already downloaded Android Studio, you can move on to the next step, which is [setting up the SDK](#setting-up-the-sdk).

The steps to download and set up Android Studio are:

1. Check to make sure your system meets the [necessary requirements](https://developer.android.com/studio#Requirements).
2. Install the *latest* version of Android Studio from [here](https://developer.android.com/studio/index.html).
3. Run the executable, follow the setup wizard, and use any and all recommended development kits.

## Setting up the SDK

Now that you have Android Studio installed, you're going to want to use the current season's SDK (software development kit) where you will create your team's code.

### Downloading the SDK

The SDK is publicly released to a GitHub repository every season. The current season's SDK can be found in the [FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) repository.

#### Downloading the ZIP

1. When you're at the repository, click the green "code" button. Then, select "Download ZIP."

   ![Click the Download ZIP option](https://dd8f408.webp.ee/download-zip.jpg)

2. Then, save it to the desired location on your computer.

   ![The ZIP file should be called FtcRobotController-master](https://dd8f408.webp.ee/save-to-computer.jpg)

3. After it is saved, extract the contents of the ZIP and place them into your desired location. You should see the contents of the SDK inside the folder location.

#### Using GitHub Desktop

1. [Install GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop).
2. Open the [SDK repository](https://github.com/FIRST-Tech-Challenge/FTCRobotController) in a browser.
3. Click the green "code" button, and then select "Open with GitHub Desktop."

   ![Click the Open with GitHub Desktop option](https://dd8f408.webp.ee/open-with-gh-desktop.jpg)

4. Clone the project.

   ![Clone the repository to your resource folder](https://dd8f408.webp.ee/clone-github-desktop.jpg)

#### From the Command Line

1. [Install git](https://github.com/git-guides/install-git).
2. Open the terminal (probably bash) in the desired resource location.
3. Use the command: `$ git clone https://github.com/FIRST-Tech-Challenge/FtcRobotController.git`

### Opening the SDK on Android Studio

1. Open Android Studio. If you have another project open, close it.

   ![A screen should appear with an option to configure settings and import a project](https://dd8f408.webp.ee/opening-as.jpg)

2. Check for updates. Click on the "configure" dropdown and select "check for updates." If you do not have the latest version, download the updates.

   ![If you have no new updates, it should say that you have the latest version installed](https://dd8f408.webp.ee/check-for-updates.jpg)

3. Select "Import Project." Navigate to where you have the SDK saved on your computer. Choose the directory that has the Android logo.

   ![Only select the folder with the Android logo](https://dd8f408.webp.ee/select-the-sdk.jpg)

4. Change to project view. In the top left corner should be a dropdown that allows you to change the way you are looking at your project.

   ![Change to project view](https://dd8f408.webp.ee/select-project-view.jpg)

5. Wait for Gradle to complete the build. This indicator should be located at the bottom of the window by default.

   ![An in-progress Gradle build](https://dd8f408.webp.ee/build-gradle.jpg)

## Layout

Android Studio can look intimidating at first glance, but there are only a few features needed to use it properly.

![Android Studio layout](https://dd8f408.webp.ee/as-layout.jpg)

## Creating Classes

The first thing to note in the project view is the dropdown with the name of the project. If you drop that down, you will see all of the Gradle files and directories. Navigate to the TeamCode folder. In the `teamcode` folder you will see an `org.firstinspires.ftc.teamcode` package.

![TeamCode > src > main > java > org.firstinspires.ftc.teamcode](https://dd8f408.webp.ee/code-project-structure.jpg)

This is where you will create your code for the robot. To create a new Java class, right-click on the package, select "New," and then choose "Java Class."

![New > Java Class](https://dd8f408.webp.ee/new-java-class.jpg)

Alternatively, you can select the "Package" option if you want to create a subfolder for organization purposes. Then, you can create classes in those packages.

## Terminal and Logcat

Near the bottom left of the application, you will find tabs for the local terminal and logcat. These are useful tools for working with your program.

![Terminal and logcat tabs near the bottom left](https://dd8f408.webp.ee/terminal-logcat-location.jpg)

Some useful information on using the logcat can be found [here](https://developer.android.com/studio/debug/am-logcat).

> You can build your program through the command line via the local terminal. Click on the terminal tab and then input `gradlew :TeamCode:clean :TeamCode:build`. This will delete the previously compiled files and build your TeamCode module.

## Installing Your Program

To install your program onto the Robot Controller, you will use the play button located near the top right of the application window.

![Play button next to device dropdown](https://dd8f408.webp.ee/build-and-run.jpg)

Next to it, you will see a dropdown for devices. When you connect your Robot Controller to your computer (using the correct cable), the device should appear in the dropdown after some time. Then, click the play button and your program will install onto the device.

> **Tip:** Occasionally, the app will fail to start on the robot controller, leaving the driver station in a disconnected state. If this occurs, you can open the terminal and run the following command to remotely start the Robot Controller app:
> `adb shell am start -n com.qualcomm.ftcrobotcontroller/org.firstinspires.ftc.robotcontroller.internal.PermissionValidatorWrapper`

If you run into any problems with this process, refer to the official [REV documentation](https://docs.revrobotics.com/duo-control/). Some useful pages from the REV site are:

- [Troubleshooting the Control System](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Android-Studio-Tutorial)
- [Deploying Code Wirelessly](https://docs.revrobotics.com/duo-control/programming/android-studio-using-wireless-adb)

If you're still stuck, you can ask for help in the [FTC Discord](https://discord.com/invite/first-tech-challenge).

## Gradle

Gradle is a build tool for software development. In the scope of FTC, it is used to build and manage dependencies for your project.

When you update any of your Gradle files, you will need to perform a Gradle sync, which syncs your project to the changes and rebuilds it. In your `build.common.gradle`, you will find information about how your robot controller application is built.

### Rebuilding

You can rebuild your project easily with the build dropdown.

![The build dropdown at the top of the screen](https://dd8f408.webp.ee/gradle-build.jpg)

To rebuild from a clean project, press the clean project option. This removes old compiled files from your project, ensuring you build from scratch with no old files.

### Invalidate and Restart

Sometimes you can get errors after moving things around, refactoring, etc. The first step is to try cleaning the project and doing a rebuild. If this doesn't work, you might have confused Android Studio, as it caches information about your project structure.

The most common way to fix these errors is to do an invalidate and restart. In the file dropdown, there will be an option for this and then you will choose **Invalidate and Restart**. This clears the cache and restarts Android Studio, performing a Gradle rebuild.

## Adding Dependencies

If you want to add dependencies to your project, you can do so in the `build.gradle` file in the TeamCode directory.

There should be a dependencies block at the bottom of the file:

```groovy
// Include common definitions from above.
apply from: '../build.common.gradle'
apply from: '../build.dependencies.gradle'

dependencies {
    implementation project(':FtcRobotController')
    annotationProcessor files('lib/OpModeAnnotationProcessor.jar')
}
```

Some dependencies require changes to your other Gradle files. Make sure to read the installation instructions for whatever dependency you want to add.

Next, add a line in the dependencies block to implement the dependency:

```groovy
dependencies {
    implementation project(':FtcRobotController')
    annotationProcessor files('lib/OpModeAnnotationProcessor.jar')

    implementation 'com.package.name:name:version'
}
```

Refer to the instructions of whatever library you are using for the correct package name and version.

Finally, perform a Gradle sync.

## Upgrading to Java 8

By default, the SDK's version of Java is set to 7. Java 8 is also supported. You might want to upgrade your version of Java from 7 to 8 to use features like lambdas or generics. Some libraries may also require you to change your Java version.

To upgrade to Java 8, navigate to your `build.common.gradle` file. Scroll down until you find this block:

```groovy
compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_7
    targetCompatibility JavaVersion.VERSION_1_7
}
```

Change the `7` to `8`:

```groovy
compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
}
```

Then, perform a Gradle sync.

## Android Debug Bridge

> **Note:** On macOS, Linux, or using PowerShell, you will have to change any commands that start with `adb` to start with `./adb` if you are in the `platform-tools` directory.

### Logcat

Logcat is extremely useful for debugging issues with your code at runtime or figuring out what went wrong. For example, if your app activity crashes and you pull up the log seeing 5000 lines of the same error, there is probably infinite recursion in your code!

To use logcat, plug in your device (or connect via ADB). Then, select the app you want to view the logs for. Your window should look like this:

![A selected device and app with the error messages](https://dd8f408.webp.ee/adb-screenshot.jpg)

If you have an issue you don't understand, you can take a screenshot of the log or select and copy the error and ask a question in the [FTC discord](https://discord.com/invite/first-tech-challenge).

### Wireless Communication

Android Debug Bridge (ADB) is a command-line tool that allows for wireless communication between the robot controller (phone or Control Hub).

ADB should come with the platform tools in Android Studio. Navigate to your `local.properties` file in the root of your project and you should see a path to the Android SDK on your computer, such as `C:\Users\Woodie\AppData\Local\Android\Sdk`. Then navigate to `platform-tools` and an application called adb should be there. To use it, open CLI (like PowerShell or command prompt) and run either `adb devices` or `./adb devices`.

For more information on ADB, you can look at the [developer's page](https://developer.android.com/studio/command-line/adb).

### Setting Up ADB

1. Ensure USB debugging is enabled on your device and it is in developer mode.
2. Make sure you have ADB installed. If you do not, follow the instructions at [this link](https://www.xda-developers.com/install-adb-windows-macos-linux/).

> **Note:** You can use logcat via ADB with the `adb logcat` command. This is extremely useful for debugging as it allows you to look at the logs wirelessly, saving time. Remember, logcat is the *best* way to debug your software.

### Add ADB To PATH

Adding variables to PATH:

- [Windows](https://docs.alfresco.com/content-services/latest/admin/troubleshoot/)
- [Linux/Unix (bash)](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path)
- [macOS (zsh)](https://koenwoortman.com/zsh-add-directory-to-path/)

If you want to use ADB from any directory, add it to PATH. Follow an online tutorial for adding to PATH and set the PATH to the `platform-tools` directory. Once you do that, you can run ADB commands from anywhere on your system.

### Connecting to a Phone Wirelessly

1. Plug the robot controller phone into your computer.
2. Run the command `adb devices` in the `platform-tools` directory and see if the phone shows up.
3. Run `adb usb` and then `adb tcpip 5555`. You can then unplug the phone.
4. Connect to the same WiFi network the device is either