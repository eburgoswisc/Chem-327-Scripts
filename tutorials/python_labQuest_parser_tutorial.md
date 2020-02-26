# Tutorial for using parse_LabQuest Script

## Requirements

* You need python3 for this one. Just download it from [here](https://www.python.org/downloads/) and install any version that is above 3.

## Usage

- Its simple. Open up a **Terminal** if using a MacOS machine or the equivalent on windows. Mine looks like this:

```bash
markmandel@Marks-iMac:~/Dropbox/UW Classes/Chem 327/Lab$ 
```

- Using the command `cd`, you change move direcrtories into the one where your files are located.

```bash
markmandel@Marks-iMac:~/Dropbox/UW Classes/Chem 327/Lab$ cd where/my/stuff/is/located
```

- To run the program, just type `python3 parse_labQuest.py -i <text_file_from_labquest> -o <output_name_you_want.csv>`. Make sure to replace the carots with the actual names you want! Mine looks like this:

Note: Make the script and the input files are in the **same directory**.

```bash
markmandel@Marks-iMac:~/Dropbox/UW Classes/Chem 327/Lab$ python3 parse_LabQuest.py -i Spike\ Recovery/mdl-with-e.txt -o mdl-spect-formatted.csv
markmandel@Marks-iMac:~/Dropbox/UW Classes/Chem 327/Lab$ head mdl-spect-formatted.csv 
Blank Time,Blank Trans @ 879.6 nm,MDL 1 Time,MDL 1 Trans @ 879.6 nm,MDL2 Time,MDL2 Trans @ 879.6 nm,MDL 3 Time,MDL 3 Trans @ 879.6 nm,MDL 4 Time,MDL 4 Trans @ 879.6 nm,MDL 5 Time,MDL 5 Trans @ 879.6 nm,MDL 6 Time,MDL 6 Trans @ 879.6 nm,MDL 7 Time,MDL 7 Trans @ 879.6 nm
60,99.9,60,95.6,60,95.5,60,96.0,60,95.9,60,96.0,60,95.2,60,92.9
60,99.9,60,95.6,60,95.5,60,96.0,60,95.9,60,96.0,60,95.2,60,92.9
```


