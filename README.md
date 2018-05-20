# LN_Donations
Cross Reference Donations
## Unix instructions:

```
$ git clone https://github.com/jkms/LN_Donations.git
$ cd LN_Donations
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ python3 donations.py -h
usage: donations.py [-h] [-l LEADNOW] [-d DONATION] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit

-l LEADNOW, --leadnow LEADNOW
                        the leadnow csv
  -d DONATION, --donation DONATION
                        the donation csv
  -o OUTFILE, --outfile OUTFILE
                        the output csv
$python3 donations.py -l sample.csv -d od_cntrbtn_de_e.csv -o output.csv
```

## Windows Instructions
1. Install Python: https://www.python.org/downloads/release/python-365/ (see recommended settings below)
   1. ![Python Install image](pythoninstall.PNG?raw=true "python install")
1. Install C++ Libraries: https://www.microsoft.com/en-US/download/details.aspx?id=48145
1. Download zip of this repo, and extract
1. Open a command prompt and `cd` into extracted dir
```
>python -m venv venv
>venv\scripts\activate.bat
>pip install -r requirements.txt
>python donations.py -h
usage: donations.py [-h] [-l LEADNOW] [-d DONATION] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -l LEADNOW, --leadnow LEADNOW
                        the leadnow csv
  -d DONATION, --donation DONATION
                        the donation csv
  -o OUTFILE, --outfile OUTFILE
                        the output csv
>python donations.py -l sample.csv -d od_cntrbtn_de_e.csv -o output.csv
```
