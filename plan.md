**Goal:** Cassette is a personal iPhone app. It plays Sin Sisamuth songs in shuffled order. It has three buttons: play/pause, next, previous. There is no song picking.

**Decisions made:**

- Personal use only, not published
- 20 songs bundled in a blue folder reference
- Files named `0001.m4a`, `0002.m4a`, ...
- Catalog in `songs.json`
- Queue and position saved in UserDefaults

**Session 1: "It plays!"** (the first win)

- Add the 20 songs and `songs.json`, and check that all say `found`
- Turn on Background Modes → Audio and set up the audio session
- Play the first song with one Play/Pause button

**Session 2: "It works like a player"**

- Shuffled queue, Next and Previous, auto-next when a song ends
- Save and restore queue and position
- Test: close the app, open it again, and it continues from the same song

**Session 3: "It works on the lock screen"** (real device)

- Now Playing info, plus play/pause/next/previous controls only
- Turn off the scrubber
- Test with the screen locked and with headphones

**Session 4: "It looks like a cassette"**

- Spinning reels (move on play, stop on pause)
- Mechanical click sound on each button
- Polish the layout and the song title

**Later:** grow to 1000 songs. At 64 kbps mono this is about 1.9 GB, which is fine for personal use.

**Parking lot:** put new ideas here (tapes of 10 songs, sleep timer, and so on). Do not build them until Session 4 is done. This is how hobby projects stay fun and don't die from too many features.

**Done means:** you lock your iPhone, music keeps playing, the lock screen shows play/pause/next/previous, and reopening the app continues where you stopped.

## Common mistake to avoid

Polishing the cassette art before the audio and queue work. The boring parts (audio, queue, saved state) are where bugs hide, and the art can be added in an evening.

Want me to write Session 1 as a single file next?