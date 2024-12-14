# Specifications document

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Description](#description)
- [Deliverables](#deliverables)
  - [Scope](#scope)
- [Functional Specifications](#functional-specifications)
  - [User Requirements](#user-requirements)
  - [System Behavior](#system-behavior)
- [Technical Specifications](#technical-specifications)
  - [Hardware Requirements](#hardware-requirements)
  - [Software Requirements](#software-requirements)
  - [Integration and Dependencies](#integration-and-dependencies)
- [Design Specifications](#design-specifications)
  - [Architecture Overview](#architecture-overview)
  - [Component Breakdown](#component-breakdown)
  - [User Interface Design](#user-interface-design)
- [Testing and Validation](#testing-and-validation)
  - [Test Cases](#test-cases)
  - [Success Criteria](#success-criteria)
- [Maintenance and Updates](#maintenance-and-updates)
  - [Documentation](#documentation)
  - [Upgrade Plans](#upgrade-plans)
- [Glossary](#glossary)

## Overview
### Description
I found my GitHub home page to be quite empty. As such, I decided to make it more lively by introducing an interactive game on it.

The game I will be recreating is one of my favorite puzzle games: The Witness by Jonathan Blow.

The game will then be embeded on my home page so everyone can play a new game daily.

## Deliverables
This project can be broken down into multiple deliverables:
1. Puzzle and solution verifyers
2. Interactive interface
3. Generator
4. Polyominos & Negative Polyomino mechanics
5. (Optimized solver)

### Scope
For completeness, every regular maze mechanics in the original game is to be included here as well. Special mechanics such as environmental clues or non-square mazes do not apply here and are out of scope. The polyminos are included but at a later stage of the development process due to their complexity.

The optimized solver is currently out of scope and may be created and worked on once the generator is fully working. In the meantime, considering the small sizes of the puzzles (generally 4x4, rarely more than 8x8), bruteforcing the solution will be sufficient.

A puzzle editor is out of scope. Some already exists such as [The Windmill](https://windmill.thefifthmatt.com/build). Being able to share puzzle from and to those engines is out of scope.

Saving score, sharing results and playing previous puzzles will not be done.

## Functional Specifications
### User Requirements
**Interactivity**: The user should be able to interact by clicking/tapping and holding from the start to the end, tracing the path with their cursor/finger. The system should force the path to start and end on the designated areas as well as follow the walls.

**Responsiveness**: The page, when loaded as a standalone, should be responsive and fit the puzzle (a square) to the smallest size of the screen. This ensures the user can fully see the puzzle without scrolling. See [User Interface Design](#user-interface-design) for the different sizes.

**User Manual**: Unlike the real game, the page should contain a button that shows instructions. These will explain how to play and what are the different mechanics. To have the user think by themself, the button will be disabled for the first two minutes. To prevent cheating and unecessary requests, the instructions should be loaded lazily.

**Error Handling**: In case an error occurs during generation or gameplay, the puzzle should instead show a clear error message explaining what went wrong. A link to a GitHub issue should also be provided for easy reporting.

### System Behavior

## Technical Specifications
### Hardware Requirements
### Software Requirements
### Integration and Dependencies

## Design Specifications
### Architecture Overview
### Component Breakdown
### User Interface Design

## Testing and Validation
### Test Cases
### Success Criteria

## Maintenance and Updates
### Documentation
### Upgrade Plans

## Glossary
