# VibeFlow — Dictation That Stays on Your Machine

**Status:** draft
**Domains:** desktop product, accessibility, local AI, privacy-first tooling
**Public proof:** [public repository](https://github.com/PascalAI2024/VibeFlow)

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

## Public proof

The public project record documents the local-first privacy model, on-device
transcription workflow, accessibility posture, dictation controls, and the
current Windows-first pre-release status.

## Outcome or learning

The work demonstrates that privacy is not merely a policy page: it can be an
architectural default that directly improves trust in a personal tool.

## The boundary

No personal transcripts, local dictionaries, microphone data, model settings,
or user activity are published. This remains a pre-release product with
platform limitations stated plainly.
