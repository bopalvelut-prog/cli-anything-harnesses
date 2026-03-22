from setuptools import setup
setup(
    name='cli-anything-excalidraw',
    version='1.0.0',
    packages=['cli_anything.excalidraw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-excalidraw=cli_anything.excalidraw:cli']},
)
