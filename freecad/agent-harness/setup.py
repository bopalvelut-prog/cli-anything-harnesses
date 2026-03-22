from setuptools import setup
setup(
    name='cli-anything-freecad',
    version='1.0.0',
    packages=['cli_anything.freecad'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-freecad=cli_anything.freecad:cli',
        ],
    },
)
