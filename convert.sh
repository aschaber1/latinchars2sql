xq '[.characterSet.characterDescription[] | {codepoint: ."@codepoints", char: ."@theChars" }]' < latinchars.xml > chars.json
