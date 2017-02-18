# ieighteen
Speed up your Localization/i18n efforts by automating translation. *You might need to proofread the translated text.* The `translate.py` script translates the file from source-locale folder to target-locale folder. E.g.

`en/strings.txt` --- gets translated to ---> `ur/strings.txt`

The repo contains `ur/strings.txt`, the translated Urdu text as an example. 
![Example](http://i.imgur.com/Q8zgBlx.png)

**Following Folders/Files must exist**

`en` or your source locale folder

`en/strings.txt` or your source locale file

`ur` or your target locale folder

The script creates (overwrites if already exist) the file in target locale folder

**To Run**

*Python 3 and libs used in `translate.py` must be installed*

Change following variables in `translate.py` according to your need

    # Locale code of source and target languages
    sourceLang = 'en'
    targetLang = 'ur'
    # Put file name here
    filename = 'strings.txt'

