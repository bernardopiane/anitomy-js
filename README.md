# anitomy-js

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/nevermnd/anitomy-js/master/LICENSE)
[![Dependencies][deps-image]][deps-url]
[![Linux Build][travis-image]][travis-url]
[![Windows Build][appveyor-image]][appveyor-url]


*anitomy-js* is a Node.js wrapper for [Anitomy](https://github.com/erengy/anitomy) - a C++ library for parsing anime video filenames.

## Installation

With [npm](http://npmjs.org) do:

```
npm install anitomy-js
```
*anitomy-js* builds it's dependencies upon installation. Please refer to the [node-gyp documentation](https://github.com/nodejs/node-gyp#installation) if you're having trouble with the build.

Starting with version 2.0, *anitomy-js* requires C++ 14 to build:
+ Linux: GCC/G++ >= 5
+ Windows: Visual Studio >= 2015
+ Mac OS >= 10.9

If you can't update your build tools, all versions from 1.x are compatible with C++ 11.

Starting with version 3.0 the old callback style with a single argument is deprecated. You should switch to either use the Promise API or a node style callback (err, data).

## Usage

*anitomy-js* provides two methods: `parse` and `parseSync`. 
Both methods accept single filename input or, an array of filenames for batch parsing.

Additionally you can pass an object as the last parameter to change Anitomy's original parsing options. The options are the following:

+ `allowed_delimiters` - defaults to `" _.&+,|"`
+ `ignored_strings` - defaults to `[]`
+ `parse_episode_number` - defaults to `true`
+ `parse_episode_title` - defaults to `true`
+ `parse_file_extension` - defaults to `true`
+ `parse_release_group` - defaults to `true`
 
### parse(data, [callback], [options]) -> Promise\<any>

```js
var anitomy = require('anitomy-js');
anitomy.parse("[tlacatlc6] Natsume Yuujinchou Shi Vol. 1v2 & Vol. 2 (BD 1280x720 x264 AAC)")
       .then((data) => console.log(data));
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

### parseSync(data, [options]) -> any

```js
var anitomy = require('anitomy-js');
var filenames = ["[DmonHiro] Magi - The Labyrinth Of Magic - Vol.1v2 (BD, 720p)", "[KLF]_D.Gray-man_04V2.avi"];
console.log(anitomy.parseSync(filenames))
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

[deps-image]:https://david-dm.org/skiptirengu/anitomy-js.svg
[travis-image]:https://api.travis-ci.org/skiptirengu/anitomy-js.svg?branch=master
[appveyor-image]:https://ci.appveyor.com/api/projects/status/eb0oky5iae827p0u/branch/master?svg=true
[deps-url]:https://david-dm.org/skiptirengu/anitomy-js
[appveyor-url]:https://ci.appveyor.com/project/skiptirengu/anitomy-js
[travis-url]: https://travis-ci.org/skiptirengu/anitomy-js
