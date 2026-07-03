---
Title: Lord Monkey
Date: 2026-07-03
Template: pico8
Status: hidden
Game_js: lordmonkey.js
Game_thumb: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAIAAABMXPacAAABMUlEQVR4Ae3dMW7CMBgGUIh6A0YOQAMDJ+mQgauwRqxchdN0qCoOwMjesUMklzrECkg4kfLeEDlWEkXf799eZwAAAMA/9X5R7xeJcTNoj6OPhCuPpZ8Yd13bryhAl+KhDkg8czhe23UKk9J/sgCH4/U2xMRjId+7off8zgS99dmCmuxCys3t7apPvCJigPQ2G84q1EAN8ipEPywFUACoq5lDeND0KzEAAAAAAAAAAAAAT9puVtvNaiQ/M59U7nfnP7/OFmXu5T+eJiimln6fnuCF6UcdoAaDNYHobUEAAADAi+zK5a5cyqGtyJP++uNn/X5RAx0wOvMM0Uczp++L3DOpq7/lH5qgmSRTB0RNYPkPcwB0bUdk2oW6bgEAAAAAAAAAAAAAAAAAAAAAAABgvH4BXEpoivFTn2QAAAAQdEVYdExvZGVQTkcAMjAxMTAyMjHjWbbBAAAAAElFTkSuQmCC
---

**Lord Monkey** is a small PICO-8 game made by my 8 year old daughter to learn some basic programming. It's a great example of how simple a game can be, while still being entertaining (at least to kids) thanks to a good game loop.

You're a monkey called Lord Monkey, and bananas are dropping on the ground (spawning randomly). Your job is to pick up the bananas and collect them before the spider gets you.

## Development Notes

The spider "logic" is just the spider moving around by adding a random number between 0 and 3 to both the spider's X and Y positions every tick. Zero actual logic or pathing of any kind, and yet it works brilliantly because the randomness gives the spider a "skittering" look as it jumps all over the place.

We spent a few evenings learning each basic function of PICO-8 and what they do, doing test code with print statements to see how things effect each other, and doing lots of mini exercises like making a sprite move around with the keys or move by itself. Then she made this game herself with me just helping spell out functions or correct punctuation/etc.

She has plans to add more such as high scores and the spider getting faster as time progresses, but we need to practice some new functions for those features.
