#! /usr/bin/env python3
import sys
import os
import pathlib

if __name__ == '__main__':

    # Ensure that a filepath was included
    if len(sys.argv) not in [2, 3]:
        raise ValueError('Incorrect argument count')

    if len(sys.argv) == 3:
        # Retrieve filepath from CLI arguments
        filepath_list = pathlib.Path(sys.argv[1]).parts
        print(filepath_list)
        project_folder = sys.argv[2]

        # Create filenames from filepath
        config_file = os.path.join(*filepath_list, project_folder, 'tailwind.config.js')
        css_file = os.path.join(*filepath_list, project_folder, 'src', 'index.css') 
        app_file = os.path.join(*filepath_list, project_folder, 'src', 'App.tsx')

    else:
        filepath_list = list(pathlib.Path(sys.argv[1]).parts)
        config_file = os.path.join(*filepath_list, 'tailwind.config.js')
        css_file = os.path.join(*filepath_list, 'src', 'index.css')
        app_file = os.path.join(*filepath_list, 'src', 'App.tsx')

    
    try:
        # Open tailwind config file, add content
        config_lines = []
        with open(config_file, 'r') as f:
            config_lines = f.readlines()

        config_lines[2] = f"  content: ['{os.path.join('.', 'src', '**', '*.{js,ts,jsx,tsx}')}', '{os.path.join('.', 'src', 'index.html')}',' {os.path.join('.', 'src', 'App.{js,ts,jsx,tsx}')}'],\n"

        with open(config_file, 'w') as f:
            f.writelines(config_lines)

        # Open index.css, add the following lines
        css_line = '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n'

        with open(css_file, 'w') as f:
            f.write(css_line)

        with open(app_file, 'w') as f:
            f.write('function App() {\n  return (\n    <h1 className="text-blue-600 font-black text-3xl">Vite + Tailwindcss</h1>\n  )\n}\n\nexport default App')

    except FileNotFoundError as e:
        print('Error while trying to setup tailwind config\n', e)