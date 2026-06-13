# Vyr

## What is this?
- Vyr is a small indie language
- A sequel to my original language vpp

## Systems
- Vyr does have a module system, however as for now the modules must be written in python and put under the modules folder
- To use a function from a module you must list it in `addInScript` like this:
- ```Vyr
  addInScript -> {
    moduleName
  }
  ```
- And to use it you must call it like:
- ```Vyr
  moduleName.use -> function()
  ```
## How to start
- First, download the `Vyr` folder and the `VyrBackend` folder under `C:\Users\<you>`
- You can acces that folder by opening up terminal and running:
- ```bash
  explorer .
  ```
- Inside this folder, also put `vy.bat`

## Creating a project
- To create a new project, in terminal you must run `vy spawn <projectName>` under `C:\Users\<you>`
- Then run `cd <projectName>`
- Then you can run `explorer .` to go into the folder. There you can edit `TEST.vyr`
- In that folder you can do `vy run` in that folders terminal to run it.

## How to learn
- There are examples given under VyrExamples
  
