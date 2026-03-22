from setuptools import setup
setup(
    name='cli-anything-kicad',
    version='1.0.0',
    packages=['cli_anything.kicad'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-kicad=cli_anything.kicad:cli',
        ],
    },
)
