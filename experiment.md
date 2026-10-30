### Plan
- [ ] Import audio file with `.fileImporter`.
- [ ] Copy them into the app's document folder.
- [ ] Play them with `AVAudioPlayer`.
- [ ] Turn on background audio.

**Step 0: Get songs onto the iPhone**
1. Put the old songs via AirDrop onto iPhone simulator then plays with `AVAudioPlayer`.
**Step 2: Enable background audio**
In Xcode: Target –> Signing & Capabilities –> + Capability –> Background Modes –> check "Audio AirPlay, and Picture in Picture"