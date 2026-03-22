from setuptools import setup
setup(
    name='cli-anything-tldraw',
    version='1.0.0',
    packages=['cli_anything.tldraw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tldraw=cli_anything.tldraw:cli']},
)
