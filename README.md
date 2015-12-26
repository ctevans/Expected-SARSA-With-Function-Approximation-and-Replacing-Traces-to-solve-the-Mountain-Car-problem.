# Expected-SARSA-Tile-Coding-Replacing-Traces-to-solve-Mountain-Car.
I solve the mountain-car problem by implementing onpolicy Expected Sarsa(λ) with tile coding and replacing traces.

Simply put, we have a problem where we have to train an agent (the program) to interact with it's environment through taking three actions.
1: Accelerate.
2: Decelerate
3: Do nothing.

Using the Expected SARSA Reinforcement Learning algorithm it is possible to have the agent learn through it's experience with the environment on what actions it can take to best achieve it's goal.

What is the mountain car's world and goal? What is it attempting to achieve?
As the image below depicts, the car will be in a valley (of sorts) and the ultimate goal of this project is to have the program learn what the most effective combination of actions to take are in the given environment. 

Source: http://library.rl-community.org/images/2/28/MountainCar-Envirornment.png

#Other bonus features, what makes this particularily interesting:

## Lambda:
I stated that we're using Lambda in this equation which may not mean a whole lot to many people. 
In Intelligent Systems, we have many methods that can learn. Of particular interest however is TD learning and MonteCarlo learning methods.
However neither is "perfect" in a sense to be "the best", so a compromise is often necessary. This compromise is obtained through using lambda.

With varying lambda values, the equation can go from a pure TD equation to more of a MonteCarlo equation-- all the way until it IS a MonteCarlo equation.

Avoiding a textbook-eqsue explaination it can be thought of simply as expanding how far we look behind ourselves.

I personally believe this visual representation and comparison may help viewers understand this better:
-Where TD is that single pair, only evaluating the two. The far left.
-Where MC is the long chain, evaluating the entire chain. The far right.
-Where Lambda modifies the amount of evaluation from between the far left and far right.
Source: https://webdocs.cs.ualberta.ca/~sutton/book/ebook/figtmp38.png

## Function Approximation:
This sounds scary but is actually quite simple, this allows me to pin specific points of data into specific regions of "relevant" data points. In other words I take an incredibly large domain (Think like ranges of numbers from 0 to 100000000000) and abstract it to something much easier to work with.
Another perk is that this allows generalization of trail runs ran by the agent into "similar" situations.

I went with "Tile coding" here, as was advised, and as was done earlier on my github repository. This lets me map specific features of the environment to tiles located within a "grid", tiles.
You may think of it quite literally like this, with each region associated with a particular set of values:
http://mathforum.org/alejandre/magic.square/4x4grid.gif
Source: http://mathforum.org/alejandre/magic.square/4x4grid.gif

The SARSA(Lambda) equation will work directly upon this Tile coding modifying the values of the tiles associated with the events that the agent (the program) is experiencing.
Through multiple runs the values within these tiles will be modified and this modification is what is being "learned". This learning in return can be used by the agent in order to actually cause the agent to perform better in accordance to what actions are deemed best in a given state.
