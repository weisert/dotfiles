#!/usr/bin/env python

import os

project_file_content = """
{
  "folders": [{
    "path": "src",
    "name": "src",
    "file_exclude_patterns": [
      "*.vcproj",
      "*.vcxproj",
      "*.sln",
      "*.gitignore",
      "*.gitmodules",
      "*.vcxproj.*"
    ],
    "folder_exclude_patterns": [
      "out",
      ".git",
    ]
  }]
}
"""
cd = os.getcwd()
prj_name = os.path.basename(cd)
with open(os.path.join(cd, prj_name + '.sublime-project'), 'w') as f:
    f.write(project_file_content)
