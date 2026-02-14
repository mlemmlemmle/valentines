#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 02:55:09 2026

@author: ruiyang
"""

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body{
      text-align:left;
      font-family:'Courier New', monospace;
      color: rgb(26, 18, 1);
      background-image: url('/static/photos/letterBackground.jpeg');
      background-size: cover;
      background-position: center;
      height: 100vh;
      margin: 0;
    }

    .container{
      position: absolute;
      top: 52%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 40em; /* keeps the block from shifting */
    }

    .letter{
      font-size: 20px;
      line-height: 0.5;
      font-weight: bold;
      white-space: pre-wrap;
    }

    .line{
      display:block;
      min-height: 1.5em; /* reserves vertical space so layout doesn't jump */
    }

    /* The ONE cursor */
    .cursor{
      display:inline-block;
      width: 2px;
      height: 1em;
      background: rgb(26,18,1);
      margin-left: 4px;
      transform: translateY(0.15em);
      animation: blink 0.8s step-end infinite;
      vertical-align: baseline;
    }

    @keyframes blink{
      50% { opacity: 0; }
    }

    button{
      margin-top: 18px;
      background-color: DarkRed;
      color: rgb(26, 18, 1);
      font-family: Georgia, serif;
      border: 4px solid white;
      text-align: center;
      padding: 10px 16px;
      cursor: url('https://cur.cursors-4u.net/symbols/sym-1/sym49.cur'), pointer;
    }

    /* Hide YES until typing finishes (optional but cute) */
    .hidden{ display:none; }
  </style>
</head>

<body>
  <div class="container">
    <div class="letter" id="letter">
      <!-- We store the full line text in data-text and type into the span -->
      <div class="line" data-text="To my Angel,"><span></span></div>
      <div class="line" data-text="I love you to the moon, past the bounds of venus,"><span></span></div>
      <div class="line" data-text="to the stars, and.."><span></span></div>
      <div class="line" data-text="and not back,"><span></span></div>
      <div class="line" data-text="not back down,"><span></span></div>
      <div class="line" data-text="baby let our love bring us around the universe,"><span></span></div>
      <div class="line" data-text="never brought down by gravity."><span></span></div>
      <div class="line" data-text="Be my valentine?"><span></span></div>
    </div>

    <button id="yesBtn" class="hidden" onclick="window.location.href='/yay'">Yes</button>
  </div>

  <script>
    const lines = Array.from(document.querySelectorAll(".line"));
    const cursor = document.createElement("span");
    cursor.className = "cursor";

    const typingSpeedMs = 35;     // slower/faster typing
    const pauseBetweenLinesMs = 450;

    async function typeLine(lineDiv) {
      const span = lineDiv.querySelector("span");
      const fullText = lineDiv.dataset.text;

      // Move the ONE cursor to the active line
      span.after(cursor);

      // Type the line
      span.textContent = "";
      for (let i = 0; i < fullText.length; i++) {
        span.textContent += fullText[i];
        await new Promise(r => setTimeout(r, typingSpeedMs));
      }

      // Pause a bit before next line
      await new Promise(r => setTimeout(r, pauseBetweenLinesMs));
    }

    async function run() {
      for (const line of lines) {
        await typeLine(line);
      }

      // Keep cursor only at the end of the last line (or remove it if you prefer)
      // cursor.remove(); // <- uncomment to remove cursor at the end

      document.getElementById("yesBtn").classList.remove("hidden");
    }

    run();
  </script>
</body>
</html>
