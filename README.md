
# Android Debloater



Android debloater with ADB automation

`adbloater` is a simple command line tool that automates package removal with `adb`.

The  general process of removing bloatware is described [here](https://www.droidwin.com/remove-uninstall-bloatware-apps-from-android-via-adb-commands)



## Installation

`pip install -e .`


## Prepare phone


To connect to an Android device using ADB (Android Debug Bridge) from Linux, you can follow these steps:

1. Install ADB: First, ensure that ADB is installed on your Linux machine. If it is not installed, you can typically install it using your package manager. For example, on Debian-based distributions, you can run the following command:

   ```
   sudo apt-get install adb
   ```

2. Enable USB Debugging on your Android device: On your Android device, go to Settings > Developer options (or Developer settings) and enable USB Debugging. If you don't see Developer options in your device's settings, you may need to enable it first. To do this, go to Settings > About phone (or About device) and tap on the Build number several times until it says you are a developer.

3. Connect your Android device to your Linux machine: Use a USB cable to connect your Android device to your Linux machine. Make sure the device is in MTP (Media Transfer Protocol) or PTP (Picture Transfer Protocol) mode.

4. Verify the device is connected: Open a terminal on your Linux machine and run the following command:

   ```
   adb devices
   ```

   This will list the connected Android devices. If your device is listed, it means it's successfully connected.

5. Grant USB debugging authorization (if prompted): When you connect the Android device to your Linux machine for the first time, you may be prompted on your device to authorize the USB debugging connection. Follow the on-screen instructions to grant the authorization.

6. Start using ADB: Once your device is connected, you can use ADB commands to interact with your Android device. For example, you can use the following command to retrieve the device's serial number:

   ```
   adb devices
   ```

## Usage

1. save installed packages `adbloater list --save` . The list will be saved to `packages.txt`
2. comment out packages you want to remove by adding `#` at the beginning of the line
3. create list to manage `adbloater make-list bloat.txt`
3. bulk remove packages with `adbloater uninstall bloat.txt`
4. (optional) Some packages can be restored after removal with `adbloater restore bloat.txt`


For list of commands see

`adbloater --help`


## Development

1. create virtual environment `make venv`
2. activate `source venv/bin/activate`
3. install in editable mode `make install`

