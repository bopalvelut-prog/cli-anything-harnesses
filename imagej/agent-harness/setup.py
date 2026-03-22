from setuptools import setup
setup(
    name='cli-anything-imagej',
    version='1.0.0',
    packages=['cli_anything.imagej'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-imagej=cli_anything.imagej:cli',
        ],
    },
)
