# Writing your first program in VyScript!

## What is this?
- VyScript is an indie language created by solo developer VirRB during his summer break. How long did it take? Some questions are better left unanswered.
- While writing this, VirRB also does not know why he is referring to himself in the third person.

## Dependencies
- [Python](https://python.org)

## Initial setup
- Open your user folder. to do this you must open terminal and run
```bash
explorer .
```
- This should open your user directory. eg.(`C:\Users\<your name>`)
- Then, in your user folder, add: `vy.bat`, the `Vyr` folder, and the `VyrBackend` folder
- Then, open terminal again and do
```bash
vy start
```

## Creating a new project
- In terminal, run
```bash
vy spawn <project name>
```
- This should create a new project with that name.
- Then run
```bash
cd <project name>
```
- This should set the terminal directory to your project folder
- Then do
```bash
vy run
```
- If all goes well, you should see a parsing message with a fish, and then it should say **Hello World**
- Then, run
```bash
explorer .
```
- This should open up your project folder
- Put all your **VyScript** code inside `TEST.vyr`

# Syntax
- Once you have a project ready, the next thing you would want to do is well... Code!

## Variables
- Creating a variable is very simple.
- Format:
```VyScript
var <name> = <value>
```
- Integers:
```VyScript
var x = 5
```
- Strings:
```VyScript
var name = "Vir"
```
- Function values:
```VyScript
var answer = add(5, 3)
```

## Functions
- Functions are basically reusable chunks of code so you dont have to type the same thing 1 thousand times.
- Format:
```VyScript
func <name>(<parameters>) {
    <body code>
    return <optional return value>
}
```
- Function without params:
```VyScript
func ask_my_name() {
    var name = input("Whats your name: ")
}
```
- Function with params:
```VyScript
func say(guy, text) {
    prnt(Guy + " said: " + text)
}
```
- Function with return value (these can be called as values for a variable):
- The parentheses are needed if you are returning an expression that is meant to be evaluated
```VyScript
func add(a, b) {
    return (a + b)
}
```
- Calling a function is simple
```VyScript
ask_my_name()
say("Bob", "Simple enough?")
var seven = add(5, 2)
```
- Some in built functions include:
```VyScript
@type conversion
var a = "1"
a = int(a)
@output: 1
var b = 2
b = str(b)
@output: "2"
prnt("Hi")
@prnts something in terminal
var name = input("Whats your name?")
@asks for user input and records what the user says as a variable
```
- If a function needs to use variables from outside its body, then they must be listed as public.
- Example:
```VyScript
var a = "Hello"
func say_hi() {
    public a
    prnt(a)
}
say_hi()
```
## Conditionals
- The backbone of many programming languages. `if a then b`
- the format is simple:
```VyScript
if 1 == 1 {
    prnt("Basic maths exists")
}
```
- Though more commonly with variables
```VyScript
var x = 5
if x == 5 {
    prnt("Stuff")
}
var name = "Vir"
if name == "Vir" {
    prnt("Great name!")
}
var thing = True
if thing {
    prnt("thing is correct!")
}
```
- Alterantively, you can use the keyword `not` as an inverter of sorts.
```VyScript
var b = False
if not b {
    @Runs if the value of b is false
    prnt("B is false")
}
```
- VyScript does not support else statements yet, but may support them in future versions.
- For now, long statements of conditionals must be formatted like:
```VyScript
if a == 1 {
    prnt("a is 1")
}
if a == 2 {
    prnt("Nvm, a is 2")
}
```
## Loops
- Loops are basically one piece of code repeated multiple times.
- "For" loops (Loops that loop through every item in an array):
```VyScript
var things = [1, 2, 3]
for thing -> things {
    prnt(thing)
}
@loops through every item in the array "things", aliases it as "thing"
@and lets you use it in the loop body
```
- Or you can loop a certain amount of times using a range
```VyScript
for i -> range(10) {
    prnt("Hi")
}
@repeats a controlled amount of times
```
- while most programming languages use `while` loops, VyScript has `aslongas`
- `aslongas` functions the same as `while`
```VyScript
aslongas True -> {
    prnt("Hi!")
}
```
- Though that has no end. a safer way to use `aslongas` would be:
```VyScript
var RUNNING = True

aslongas RUNNING -> {
    var inp = input("Command?")
    if inp == "exit" {
        RUNNING = False
    }
}
```
## Modules
- Modules are there to make life easier. They add extra features to VyScript and let you do more without writing everything from scratch.
- To see all built-in modules, check `modules.md`.
- You can even create your own modules! For now, custom modules must be written in Python and placed inside the `modules/` folder.
- To import a module, you must list it under your addInScript, or alias it.
```VyScript
addInScript -> {
    cursor
}
@adds the cursor module to your script
```
- To list more than one module, you can place them in the same addInScript
```VyScript
addInScript -> {
    cursor,
    vywin,
    rand
}
@adds 3 modules to your script
```
- To use a function from a module, you must follow the format:
```VyScript
module.use -> function()
```
- Example:
```VyScript
cursor.use -> MOVE(500, 500)
```
- Sometimes the format gets repetetive or you only need to use one function from a module.
- Thats where alias comes in.
- Lets say you only want to use a certain function from the module, but dont wanna keep writing the format. You can use `alias.pull`:
```VyScript
alias.pull -> module -> function
```
example
```VyScript
alias.pull -> rand -> pick

pick(1, 10)
@you can now use the pick function directly without naming the module or following the use format
```
## Arithemtic
- One final thing, unlike most languages, VyScript does not support traditional += or -=
- Instead, you can do:
```VyScript
var a = 1
a = (a + 1)
a = (a - 1)
a = (a * 2)
a = (a / 2)
```
- The parentheses around the values are nessecary for evaluation
