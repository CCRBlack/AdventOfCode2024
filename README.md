# Advent Of Code 2024
This year I'm going to work in python predominately. See [AdventOfCode2024](https://adventofcode.com/2024).

## Day 1: Historian Hysteria
Part 1 is to simply make two ordered lists and check the difference between each pair of values.

Part 2 is to calculate the so called "similarity score" between the two lists: the sum of each value in list 1 times it's count in line 2.

## Day 2: Red-Nosed Reports
Part 1 is to count the number of lines in which all numbers, separated by a space, are consecutively ascending or descending by a value between 1 and 3 inclusive.

Part 2 calculates how many reports can be made safe if a single number is removed from the sequence.

## Day 3: Mull It Over
Part 1 is to clean up a 'corrupted' file by ony recognising correct terms `mul(000,111)` using simple regex where both terms in the instruction are 1-3 digit integers.

Part 2 requires instructions to be ignored if preceded by a `dont()` instruction, ignore all instructions until a `do()` is detected. The starting state is `do()`. Only the last occurrence counts.

## Day 4: Ceres Search
Part 1 requires finding all instances of a word "XMAS" in a crossword. The word could be horizontal, vertical, diagonal, written backwards, or even overlapping other words.

Part 2 requires finding all instances of the two "MAS" crossing each other.

## Day 5: Print Queue
Part 1 requires ordering numbers according to input logic which defines A before B.