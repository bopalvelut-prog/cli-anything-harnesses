from setuptools import setup
setup(
    name='cli-anything-ardour',
    version='1.0.0',
    packages=['cli_anything.ardour'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-ardour=cli_anything.ardour:cli',
        ],
    },
)
