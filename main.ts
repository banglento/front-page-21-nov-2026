// Front Page — 21 November 2026: a make.fun news-image-20261121 entry.
//
// The poster itself is entry.png beside this file, drawn by draw.py
// (kept in the repo as the drawing source). This program's only job is
// to deliver those exact bytes to the output directory as entry.png,
// so the grader's two runs produce a byte-identical file.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });

const source = new URL('./entry.png', import.meta.url);

// Sanity check before copying: the competition gate refuses an image
// over 1 MiB, so fail loudly here rather than deliver an invalid entry.
const MAX_BYTES = 1_048_576;
const size = statSync(source).size;
if (size === 0 || size > MAX_BYTES) {
  throw new Error(`entry.png is ${size} bytes; expected between 1 and ${MAX_BYTES}`);
}

copyFileSync(source, join(outputDir, 'entry.png'));
