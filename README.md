<img src="https://raw.githubusercontent.com/segnoda/Coda/master/resources/icon/coda.png"  width="128" height="128"/>

# Coda

**Coda** is a simple, cross-platform, and open source **visual novel game engine** using PyQt5.

## Screenshot

<img src="https://raw.githubusercontent.com/segnoda/Coda/master/screenshot/screenshot-1.png"  width="710"/>\
<img src="https://raw.githubusercontent.com/segnoda/Coda/master/screenshot/screenshot-2.png"  width="710"/>\
<img src="https://raw.githubusercontent.com/segnoda/Coda/master/screenshot/screenshot-3.png"  width="710"/>\
<img src="https://raw.githubusercontent.com/segnoda/Coda/master/screenshot/screenshot-4.png"  width="710"/>\
<img src="https://raw.githubusercontent.com/segnoda/Coda/master/screenshot/screenshot-5.png"  width="710"/>

## Getting Started

Everyone can create your own visual novel games using **Coda** by simply writing XML scripts and importing your resources. Your creation is good to go!

### Installation

First, clone the repo to any target directory.

```
$ git clone https://github.com/segnoda/Coda.git
```

Install dependencies using pip3 (sudo if needed)

```
$ sudo pip3 install -r requirements.txt
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

Use PyInstaller to build a stand alone App.

```
$ sudo pip3 install pyinstaller
$ pyinstaller build_mac.spec    # for macOS
$ pyinstaller build_win.spec    # for Windows
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
