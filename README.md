# Anitomy-js

[![Build Status](https://travis-ci.org/nevermnd/anitomy-js.svg?branch=master)](https://travis-ci.org/nevermnd/anitomy-js)

*Anitomy-js* is a Node.js wrapper for [Anitomy](https://github.com/erengy/anitomy) - a C++ library for parsing anime video filenames.

## Installation

With [npm](http://npmjs.org) do:

```
npm install anitomy-js
```

## Usage

*Anitomy-js* provides two methods: `parseSync` and `parseAsync`. 
Both methods accept single filename input or, an array of filenames for batch parsing.

Additionally you can pass an object as the last parameter to change Anitomy's original parsing options. The options are the following:

+ `allowed_delimiters` - defaults to `" _.&+,|"`
+ `ignored_strings` - defaults to `[]`
+ `parse_episode_number` - defaults to `true`
+ `parse_episode_title` - defaults to `true`
+ `parse_file_extension` - defaults to `true`
+ `parse_release_group` - defaults to `true`
 
### parseSync()

```js
var anitomy = require('anitomy-js');
anitomy.parseSync("[tlacatlc6] Natsume Yuujinchou Shi Vol. 1v2 & Vol. 2 (BD 1280x720 x264 AAC)");
```
... would be parsed into

```json
{
   "anime_title":"Natsume Yuujinchou Shi",
   "audio_term":"AAC",
   "file_name":"[tlacatlc6] Natsume Yuujinchou Shi Vol. 1v2 & Vol. 2 (BD 1280x720 x264 AAC)",
   "release_group":"tlacatlc6",
   "release_version":"2",
   "source":"BD",
   "video_term":"x264",
   "video_resolution":"1280x720",
   "volume_number":[
      "1",
      "2"
   ]
}
```

### parseAsync()

```js
var anitomy = require('anitomy-js');
var filenames = ["[DmonHiro] Magi - The Labyrinth Of Magic - Vol.1v2 (BD, 720p)", "[KLF]_D.Gray-man_04V2.avi"];
anitomy.parseAsync(filenames, function(data) {
    // ...
});
```

... would be parsed into

```json
[
   {
      "anime_title":"Magi - The Labyrinth Of Magic",
      "file_name":"[DmonHiro] Magi - The Labyrinth Of Magic - Vol.1v2 (BD, 720p)",
      "release_group":"DmonHiro",
      "release_version":"2",
      "source":"BD",
      "video_resolution":"720p",
      "volume_number":"1"
   },
   {
      "anime_title":"D.Gray-man",
      "episode_number":"04",
      "file_extension":"avi",
      "file_name":"[KLF]_D.Gray-man_04V2",
      "release_group":"KLF",
      "release_version":"2"
   }
]
```

## License

Licensed under the incredibly [permissive](http://en.wikipedia.org/wiki/Permissive_free_software_licence) [MIT license](http://creativecommons.org/licenses/MIT/)
