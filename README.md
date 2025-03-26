<h1 align="center">Cyphered QR Gen&Scan</h1>
<h2 align="center">Hi there, I'm Andrey
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h2>
<h3 align="center">Computer science student from Russia 🇷🇺
<h2 align="center"><img src="https://i.pinimg.com/736x/d6/6b/2e/d66b2efa16fc14ff21dd933f635aef8d.jpg" height="300"/></h2>

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Structure](#repository-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contact](#contact)

## Introduction
* Thanks for checking out this GitHub page.
I made 2 programms in pair: the qr-code scanner for Android and QR generator wich both have encryption mode. The base language for the project is Python. The generator is themed to encode some parameters of notebooks or pc. You can change that by editing display text in *CreatingQR_visual.py* in QR_Gen folder and *main.py* in QR_Scan.
* Both programs have 2 modes: normal and encrypted.
* Normal(Encription OFF) mode provides ability to generate QR-codes which can be scaned by any qr-scanning app. The data in the output is represented with HTML-code which you can copy-paste into your browser search tab.
* Encrypted mode provides ability to generate qrcodes with the data encrypted by the simple encryption method. It can be decoded with the QR_Scan app both on *PC* and *Android*.
## Repository Structure
* This repository is organized into subdirectories, each representing one of the two parts of the project. In QR_Gen you can find base .py files and requirements.txt for running program on PC while in QR_Scan you can find extra **buildozer.spec** for building the app for android.


<!--Installation-->
# Installation
* To get started with this repository, follow these steps
## At first

1. **Clone the Repository**: clone the repository to your local machine
    ```sh
        git clone https://github.com/purt1ch/CypheredQR_Gen-Scan.git
        cd CypheredQR_Gen-Scan
    ```
2. **Navigate to the Project directory**:
    ```sh
        cd QR_gen
    ```
## QR_Gen PC intallation


3. **Create a Virtual Environment**: Ensure you have python and virtualenv installed. Create and activate a virtual environment
    ```sh
        python3 -m venv venv
        source venv/bin/activate
    ```

4. **Install Dependencies**: Install the required dependencies from `requirements.txt`.
    ```sh
         pip install -r requirements.txt
    ```
    
## QR_Scan Android intallation
**Buildozer project build**
1. Install buildozer in the QR_Scan folder:
   ```sh
         pip3 install --user --upgrade buildozer
    ```
   ```sh
        sudo apt update
        sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
        pip3 install --upgrade Cython==0.29.33 virtualenv
    ```
   ```sh
         export PATH=$PATH:~/.local/bin/
    ```
2. Run the build:
    ```sh
         buildozer android debug

    ```
    * The *.apk* file will be saved in */bin* directory
### Remember to give permission for CAMERA or else the app will crash
# Usage
* Each directory is a standalone python project.
### QR_Gen PC:
1. **Run the Application**:

    ```sh
        python3 CreatingQR_visual.py
    ```
3. **Enter the parameters of your device and choose encryption mode**
4. **Press CreateQR** *the image will be saved in the program directory*
### Android 
* If you are scanning normal qr, not encrypted by the programm the botom button should show 'Encryption: OFF'.
* But if you're scanning encrypted by *crypto.py* qr-code, then use 'Encryption: ON' mode.
## Contact
* If you have any questions, feel free to reach out

   **Purtov Andrey**
  
   **Email:** andrey.purtov10@gmail.com



