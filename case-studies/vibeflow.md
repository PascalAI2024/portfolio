# VibeFlow — Dictation That Stays on Your Machine

**Publication status:** public-safe narrative
**Project status:** source-private pre-release work
**Domains:** desktop product, accessibility, local AI, privacy-first tooling
**Evidence posture:** not counted as independently inspectable public proof

## The brief

Make voice dictation useful for developers and power users without sending every
utterance through a remote service or interrupting the application they are
already using.

## Constraints

The product needed to preserve privacy by default, stay responsive during
transcription, work with the active application, and make correction feel less
like post-processing.

## The decisive move

VibeFlow keeps recording, transcription, cleanup, vocabulary help, and optional
history local by default. It prioritises predictable rule-based cleanup, with
heavier local language-model assistance treated as an opt-in path.

## The system shape

An overlay captures speech, a local worker transcribes it, and a guarded output
path returns the cleaned text to the active application. Supporting local data
such as snippets and vocabulary remains under the user's control.

## Evidence posture

The source is currently private. This note preserves the public-safe product
decision and stated pre-release boundary; it is context rather than public
proof.

## Outcome or learning

The work demonstrates that privacy is not merely a policy page: it can be an
architectural default that directly improves trust in a personal tool.

## The boundary

No personal transcripts, local dictionaries, microphone data, model settings,
or user activity are published. This remains a pre-release product with
platform limitations stated plainly.
