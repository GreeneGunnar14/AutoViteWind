#! /usr/bin/env python3
import sys

if __name__ == '__main__':

    # Ensure that a filepath was included
    if len(sys.argv) != 3:
        print('Usage python setup.py <path-to-vite-project>')
        exit()

    # Retrieve filepath from CLI arguments
    filepath = sys.argv[1]
    project_folder = sys.argv[2]

    # Create filenames from filepath
    config_file = filepath + project_folder + '/tailwind.config.js'
    css_file = filepath + project_folder + '/src/index.css'
    
    try:
        # Open tailwind config file, add content
        config_lines = []
        with open(config_file, 'r') as f:
            config_lines = f.readlines()

        config_lines[2] = "  content: ['./src/**/*.{js,ts,jsx,tsx}', './src/index.html'],\n"

        with open(config_file, 'w') as f:
            f.writelines(config_lines)

        # Open index.css, add the following lines
        css_line = '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n'

        with open(css_file, 'w') as f:
            f.write(css_line)

    except FileNotFoundError as e:
        print('Error while trying to setup tailwind config\n', e)