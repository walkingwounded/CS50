# Random Gym Workout Challenge Generator
#### Video Demo: https://youtu.be/c1TrQGizI_g

## Description:

### The Purpose
Exercising can be daunting, moreover, once January is over, the burning resolution wane. Planning for exercise for individuals ~~lack in discipline~~ with busy schedule becomes cumbercent. A workout challenge generator can ease the workout planning, provide goal setting, and make workout fun!

### The Requirement
The requirement of this workout generator to provide a challenge are individual's parameters, such as:
```
1. Age
2. Weight
3. Height
4. Gender
```

### The Program
The gym workout challenge generator generate random workout challenge (currently only support 2 exercises) using the individuals' BMI and recommend a workout challenge.

### The Program Design
This project consist of 1 file, namely *project.py*.
Current design takes input from user and calculate base on a formula. The formula considers the users' gender, and BMI. The program then dispense workout by printing a challenge with 2 random workouts.

The advantage of using a formula is that we can safely dispense challenges cater for the general population. It is also a safe benchmark for beginners to intermediate users for goal settings.

The disavantage of using a formula is that the formula may be underwhelming for fitness enthusiasts and advance users who ~~surpass normal human physical capability~~ requires more intensive workout to attain their next level. However, I'd argue that this problem can be resolved by adding new function to recognize advance users base on their number of successful challenge or user input.

The program is designed to add new gym exercises by adding into existing list of dictionary.

### Considerations
Future upgrade to this generator can consider new type of exercises, such as cardio, yoga, sports, etc. In addition, consider user friendly GUI than text-based entry.

*Thank you to CS50 team 🥰 and to be as cool as Mr. Malan 😎! This was the Random Workout Challenge Generator Project, and **this was CS50P**!*