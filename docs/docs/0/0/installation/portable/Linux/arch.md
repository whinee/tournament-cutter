# Portable - Linux - Arch Linux distro and derivatives

- Open your preferred terminal and run the following command:

    ```shell
    sudo pacman -Syyu --noconfirm curl fuse
    sudo modprobe fuse
    sudo groupadd fuse
    sudo usermod -a -G fuse $(whoami)
    curl -s tc.comms.whinyaan.xyz/scripts/0/0/ld | sudo bash
    ```

- You can now use tournament-cutter by running the following command:

    ```shell
    ./tc-x86_64.AppImage
    ```
