from setuptools import setup
setup(
    name='cli-anything-syncthing',
    version='1.0.0',
    packages=['cli_anything.syncthing'],
    install_requires=['click', 'requests'],
    entry_points={
        'console_scripts': [
            'cli-anything-syncthing=cli_anything.syncthing:cli',
        ],
    },
)
