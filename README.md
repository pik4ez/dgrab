dgrab
=====

Discography grabber. Creates albums lists compatible with vkapi.


Supported sources
-----------------

* Allmusic (http://allmusic.com)
* Discogs (http://discogs.com)


Usage
-----

```
./dgrab.py http://www.allmusic.com/album/stone-temple-pilots-mw0001975741
```

Result:

```
{"albums":[{"year":2010,"title":"Stone Temple Pilots","tracks":[{"duration":170,"title":"Between the Lines"},{"duration":191,"title":"Take a Load Off"},{"duration":190,"title":"Huckleberry Crumble"},{"duration":202,"title":"Hickory Dichotomy"},{"duration":269,"title":"Dare If You Dare"},{"duration":213,"title":"Cinnamon"},{"duration":179,"title":"Hazy Daze"},{"duration":165,"title":"Bagman"},{"duration":209,"title":"Peacoat"},{"duration":213,"title":"Fast as I Can"},{"duration":183,"title":"First Kiss on Mars"},{"duration":292,"title":"Maver"}],"artist":"Stone Temple Pilots"}]}
```


Extending
---------

* improve sherlock's deduction to return appropriate parser for your uri
* write parser similar to existing one
