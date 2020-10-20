# speech2Code

speech2Code is a project in the accessibility of programming software. The initial idea was formed out of a motivation to make programming as widely available to people who may have dexterity issues or cannot use standard computer input devices(Keyboard/Mouse). This was ideated from the idea of disabled people's ability to code.

Project Statement:
We believe everyone should have access to the world of programming and that things such as bodily disabilities should not hinder someones ability to be able to do so. This project is solely a project of accessibility.

The initial idea was that the application would take speech as the input and parse it to make usable code files as well as the ability to run and debug using only speech. This presents a few challenges that may come up during development. Some of the major ones are:

1. How will the IDE(Integrated Development Environment) know to run the code without keyboard/mouse input?
2. How will they save the files after they are done working on them?
3. If the idea is for people with disabilities to use this, how will they be able to access it initially to download/setup.

Proposed Technology:
We will be initially making this in python due to the simplicity of the language and the inferred typecasing that it allows. This will allow us to not worry about having to learn a complex languages syntax and rather tackle the main goals of the project which is the speech plug-in. That being said we are going to be writing a plug-in for IntelliJ, because that is the IDE which PyCharm is based off of and it should be easier to create new features instead of building out a whole separate IDE.

