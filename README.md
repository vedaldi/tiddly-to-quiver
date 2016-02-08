# TiddlyWiki to Quiver

This program is a very basic converter from
[TiddlyWiki](http://tiddlywiki.com) to
[Quiver](https://github.com/HappenApps/Quiver).

## Usage

Export your TiddlyWiki to JSON format (using the corresponding
functionality in TiddlyWiki). Then run:

```bash
$ python tiddly-to-quiver.py tiddly.json
```

to create a `tiddly.qvnotebook` Quiver notebook with all the notes;
the notes contain a single cell in Markdown format. Note that the
notebook is **overwritten** if one with the same name exists.

Once done, double click on the notebook to import in Quiver.

## Notes

* This is provided as is and comes *without support*.

* The program applies some basic text transformation to convert some
  Tiddly Wiki syntax to Markdown, but it is all highly
  heuristic. Hence, you may need to change the source code to adapt to
  your needs.

* This code is based on [this converter](https://gist.github.com/anabranch/09c421e3ff13e1245316).
