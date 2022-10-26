/* 
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:

    1 <= haystack.length, needle.length <= 10**4
    haystack and needle consist of only lowercase English characters.

*/

//Lazy... but effective
const findFirstOccurence = (haystack, needle) => {

    return haystack.indexOf(needle)
}


let haystack = "sadbutsad"
let needle = "sad"

console.log(findFirstOccurence(haystack, needle))