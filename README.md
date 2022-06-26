# abandoned and outdated
last i checked this didnt work anymore. for some reason only deletion works and only when logging in with username and passwd...? no clue why or how or whatever and im not sure if i remember right either. i abandoned it couse the [ruby cli](https://neocities.org/cli) is good enough for me so i dont rly have a reason to fix it or look into it too much

theres an oldish (relative to when im writing this readme) comment in the source abt the issue i think, just check that out if youre curious

oh well

# neocities ~~syncer~~ something
a little script ive thrown together to quickly ~~sync~~(?) multiple local website folders (including subfolders and their respective content) to your neocities websites.

uploading is disabled, its only good for deleting rn

## usage
* install the [neocities py api](https://github.com/neocities/python-neocities)
* make the `websites` file
* `python neosync.py WEBSITE`

you need a file called `websites` in the same folder with the neosync file which keeps the data of your site. [example websites file](websites_example). you can use this one as a template but obviously rename `websites_example` to `websites`.

`python neosync.py -h` for other options