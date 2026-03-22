from setuptools import setup
setup(
    name='cli-anything-darktable',
    version='1.0.0',
    packages=['cli_anything.darktable'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-darktable=cli_anything.darktable:cli',
        ],
    },
)
