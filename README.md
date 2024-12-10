# Glaucoma Detection Research

<!-- About -->
## About

A collection of jupyter notebooks and python scripts for glaucoma detection research. See [here](https://ieeexplore.ieee.org/document/10436242).

This documentation is work in progress, feel free to add or request more information as needed.

<!-- File Tree -->
## File Tree

```
└── glaucoma-detection-research/
 ├── src/
 │ ├── models/
 │ ├── featureExtraction/
 │ │ ├── 2d/
 │ │ └── 3d/
 │ └── visualizations/
 ├── requirements.txt
 └── README.md
```

<!-- Development Environment -->
## Development Environment - Mac OS

The next steps will show how to setup your computer for local development

### Prerequisites

1. Install [python3](https://docs.python.org/3/using/mac.html)
   
2. Open a terminal and install pip:
   
   ```sh
   python3 -m pip install –upgrade pip
   ```

3. Install [Github CLI](https://cli.github.com/)

4. Install jupyter notebook

   ```sh
   python3 -m pip install jupyter
   ```

### Installation

1. Open a terminal, and navigate to a directory on your machine where you want the project
   
2. Login to GitHub
   
   ```sh
   gh auth login
   ```
   
   Then follow the prompts to login with your browser
   
3. Clone the repo
   
   ```sh
   git clone https://github.com/mcmahonl/glaucoma-detection-research.git && cd glaucoma-detection-research
   ```
   
4. Create a virtual python environment to install dependencies and execute scripts
   
   ```sh
   python3 -m venv .venv
   ```
   
5. Activate the virtual environment. It needs to be activated during development and while running scripts
   
   ```sh
   source .venv/bin/activate
   ```
   
   It can be deactivated with
   
   ```sh
   deactivate
   ```
   
6. Install the scripts' dependencies inside the virtual environment while its activated
   
   ```sh
   pip install -r requirements.txt
   ```

<!-- SCRIPTS -->
## Running scripts
   
- Open a jupyter notebook
   
   ```sh
   jupyter notebook <path-to-notebook.ipynb>
   ```

- Run a python script
   
   ```sh
   python3 <path-to-script.py>
   ```  

<!-- CONTRIBUTING -->
## Contributing - Mac OS terminal CLI

1. Make changes
   
2. Navigate to the root of the repository on your machine
   
   ```sh
   cd <path-to-repo>
   ```

3. Add the directories you made changes in
   
   ```sh
   git add <directory1> <directory2>
   ```

   Or do `git add .` for everything

4. Commit your change locally
    
   ```sh
   git commit -m "<message-about-change>"
   ```
   
5. Upload your change to here
    
   ```sh
   git push origin main
   ```
