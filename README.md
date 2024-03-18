# geosite-updater

1. download script
```
git clone https://github.com/fx505/geosite-updater.git ~
```
2. chmod
```
cd geosite-updater && chmod +x main.py
```
3. add to crontab
```
crontab -e
```
```
0 1 * * * python3 ~/geosite-updater/main.py
```
