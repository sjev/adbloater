
# Android Debloater



Android debloater with ADB automation

`adbloater` is a simple command line tool that automates package removal with `adb`.

The  general process of removing bloatware is described [here](https://www.droidwin.com/remove-uninstall-bloatware-apps-from-android-via-adb-commands)



## Installation

`pip install -e .`



## Usage

1. save installed packages `adbloater list --save` . The list will be saved to `packages.txt`
2. comment out packages you want to remove by adding `#` at the beginning of the line
3. bulk remove packages with `adbloater uninstall`
4. (optional) Some packages can be restored after removal with `adbloater restore`


For list of commands see

`adbloater --help`


## Development

1. create virtual environment `make venv`
2. activate `source venv/bin/activate`
3. install in editable mode `make install`

