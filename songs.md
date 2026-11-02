# Research

1. Where to download the audio?
    - Soundcloud

### MVP
1.	Display songs, albums, and artists.
2.	Play, pause, seek, and skip.
3.	Support next and previous tracks.
4.	Create playlists.
5.	Mark songs as favorites.
6.	Remember playback position.
7.	Continue playback with the screen locked.
8.	Work with no internet connection.
9.	Show album artwork when available.

### Interface & UI Design concepts
### Golden Era

### Planning before coding
1. The biggest risk
- Apple rule: We need to proof the recording license to use.
- No legal advice

Conclusion: I do not public the app inside App Store. I need to develop and using myself for purpose learning.

2. Three ways to ship the songs
A. Put all songs inside the app. (20 songs)
B. Apple-hosted background assets.
C. Own server.

Conclusion: Due this is my personal use I prefer to go with option A.

3. How to store the songs
1. Rename files to numbers: 01.m4a, 02.m4a ('m4a' audio-only file formate developed and popularized by Apple)
2. Put them in one folder and drag it into Xcode as folder reference, not an asset catalog.

Conclusion: I need to detail about store the songs into Xcode how will it be.

4. Next and previous with no song picking
1. Shuffle all 20 ids once into an array
2. Keep a number position \
3. Next is position + 1. Previous is position - 1
4. At the end, reshuffled and start again. No songs repeats until all 20 have played.
5. Save queue and position (User Defaults in enough) so the app resumes after closing.

Conclusion: We need to think about UX of user and develop that enough.