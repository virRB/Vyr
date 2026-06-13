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
  
