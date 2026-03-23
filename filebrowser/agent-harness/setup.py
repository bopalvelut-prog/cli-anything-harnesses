from setuptools import setup
setup(
    name='cli-anything-filebrowser',
    version='1.0.0',
    packages=['cli_anything.filebrowser'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-filebrowser=cli_anything.filebrowser:cli']},
)
