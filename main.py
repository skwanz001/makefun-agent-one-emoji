"""Your Agent in One Emoji -- make.fun entry.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.
Standard library only (os, sys) -- the grading sandbox installs nothing.

The pick: DIRECT HIT (target).
  A chatbot answers; an agent is given a target and does not stop until
  it hits it -- read, act, check, retry, ship. The target is the whole
  difference between an LLM and an agent, in one glyph.
  Why this glyph wins its pairwise games:
  - At a glance it IS the agent's character: goal-directed, persistent,
    it keeps working until the job lands -- not a face, not a robot.
  - One bold shape, red on white: reads instantly at small size.
  - Specific about how the agent works: pursue a target until direct hit.
  - Distinctive: not the robot, not the smiley, not the brain or the
    sparkle half the field will send.
"""

import os
import sys

EMOJI = "\U0001F3AF"  # DIRECT HIT -- target


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
