from setuptools import setup
setup(
    name='cli-anything-scribus',
    version='1.0.0',
    packages=['cli_anything.scribus'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-scribus=cli_anything.scribus:cli',
        ],
    },
)
