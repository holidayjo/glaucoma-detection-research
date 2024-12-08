# Glaucoma Detection Research

<!-- About -->
## About

A collection of scripts for glaucoma detection research. See [here](https://ieeexplore.ieee.org/document/10436242)

<!-- Development Environment -->
## Development Environment - Mac OS

The next steps will show how to setup your computer for local development

### Prerequisites

1. Install [python3](https://docs.python.org/3/using/mac.html)
   
3. Open a terminal and install pip:
   
   ```sh
   python3 -m pip install –upgrade pip
   ```

### Installation

1. Open a terminal, and navigate to a directory on your machine where you want the project
   
3. Login to GitHub
   
   ```sh
   gh auth login
   ```
   
   Then follow the prompts to login with your browser
   
4. Clone the repo
   
   ```sh
   git clone https://github.com/mcmahonl/glaucoma-detection-research.git
   ```
   
6. Create a virtual python environment to install dependencies and execute scripts
   
   ```sh
   python3 -m venv .venv
   ```
   
8. Activate the virtual environment
   
   ```sh
   source .venv/bin/activate
   ```
   
   It can be deactivated with
   
   ```sh
   deactivate
   ```
   
10. Install the scripts' dependencies inside the virtual environment while its activated
  ```sh
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing - Mac OS terminal CLI

1. (optional) Make a new issue or resolve an existing one
   
3. Navigate to the root of the repository on your machine
   
   ```sh
   cd <path-to-repo>
   ```
   
5. Make a new branch
   
   ```sh
   git checkout -b <your-new-branch>
   ```

7. Add the directories you want to change
   
   ```sh
   git add <directory1> <directory2>
   ```

9. Commit your changes
    
   ```sh
   git commit -m <message-about-change>
   ```
   
11. Push the changes on your branch to this repo
    
   ```sh
   git push origin <your-new-branch>
   ```

11. Open a pull request to merge your branch to the main branch on Github in the browser
    
13. Merge your pull request to add your changes to this repository

<p align="right">(<a href="#readme-top">back to top</a>)</p>
