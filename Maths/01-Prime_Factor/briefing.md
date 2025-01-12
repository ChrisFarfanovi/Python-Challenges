# 01-Prime-y challenge

## Situation

If you divide one number (`a`) by another number (`b`) and got no remainder, then `b` is considered a factor of `a`

A prime number is any number that is ***only*** divisible by itself and 1.

So a `Prime Factor` is any factor of a number that is only divisible by itself and 1.

In fact all numbers can be made using a set of specific `Prime Factor`s.

Take the number `60`:

`30` can be divided by `2` to give `15`, meaning `2` is a `Prime Factor` of `30`.

```txt
2 * 15 = 30
```

`15` can be divided by `5` to give `3`, meaning `3` and `5` are also `Prime Factor`s of `30`

```txt
2 * (3 * 5) = 30
```

So it can be said that `2`, `3` and `5` are the `Prime Factors` of 30.

## Mission

Given a random number, find its ***largest*** `Prime Factor`.

## Execution

1. Create a new Challenge instance.
2. Access the `.data` attribute which will contain the number you are to check.
3. Find its largest Prime Factor.
4. Check the solution using the `.check_solution` method.

## Conclusion

You may have to try a few different techniques for this one; keep in mind that some will perform better than others.

There is a [`solver_stress_tester.py`](./solver_stress_tester.py) in this challenge for seeing how your solver chocks up against the solutions of others.

You can always check [`community_solutions.py`](./community_solutions.py) for inspiration, and don't be afraid to submit your own solution to be added to the list!
