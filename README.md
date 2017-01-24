<img src="https://raw.githubusercontent.com/segnoda/Coda/master/resources/icon/coda.png"  width="128" height="128"/>

# Coda

**Coda** is a simple, cross-platform, and open source **visual novel game engine** using PyQt5.

## Getting Started

Everyone can create your own visual novel games using **Coda** by simply writing XML scripts and importing your resources. Your creation is good to go!

### Installation

First, install PyQt5 using pip3

```
$ pip3 install pyqt5
```

Clone the repo to any target directory.

```
$ git clone git@github.com:segnoda/Coda.git
```

Run the shell script to build resources files.

```
$ ./pyrcc.sh
```

### Usage

Just run main.py to execute **Coda** with example resources.

```
$ python3 main.py
```

### Build

Run the build script to build a stand alone App by PyInstaller.

```
$ ./build.sh
```

## Documentation (under construction)

The guideline below allows you to control and modify your game flow.

### Basic Script Layout

```xml
<script>
    <content id="0">
    ...
    </content>
    <content id="1">
    ...
    </content>
    ...
</script>
```
