# Brain Games

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AgarkovRoman/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AgarkovRoman/python-project-49/actions)

«Brain Games» is a collection of five console games for brain training,
inspired by popular mobile apps. Each game asks the player a series of
questions. Three correct answers in a row win the round; a single wrong
answer ends it.

## Games

| Command              | Game                                             |
|----------------------|--------------------------------------------------|
| `brain-even`         | Is the number even?                               |
| `brain-calc`         | Calculate an arithmetic expression                |
| `brain-gcd`          | Find the greatest common divisor of two numbers   |
| `brain-progression`  | Find the missing number in a progression          |
| `brain-prime`        | Is the number prime?                              |

## Requirements

* Python >= 3.12
* [uv](https://docs.astral.sh/uv/)

## Installation

```bash
git clone git@github.com:AgarkovRoman/python-project-49.git
cd python-project-49
make install
make build
make package-install
```

## Usage

Once installed with `uv tool install`, every command works directly,
without `uv run`:

```bash
brain-games
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Demo

### brain-even
[![asciicast](https://asciinema.org/a/Amag31kBeeETxveX.svg)](https://asciinema.org/a/Amag31kBeeETxveX)

### brain-calc
[![asciicast](https://asciinema.org/a/B59OCHm9zVP77sAt.svg)](https://asciinema.org/a/B59OCHm9zVP77sAt)

### brain-gcd
[![asciicast](https://asciinema.org/a/AF8bTfAhDGPj4y65.svg)](https://asciinema.org/a/AF8bTfAhDGPj4y65)

### brain-progression
[![asciicast](https://asciinema.org/a/jFwUAPxxLZBbLkHY.svg)](https://asciinema.org/a/jFwUAPxxLZBbLkHY)

### brain-prime
[![asciicast](https://asciinema.org/a/ibDkH9HNmE4wPquM.svg)](https://asciinema.org/a/ibDkH9HNmE4wPquM)
