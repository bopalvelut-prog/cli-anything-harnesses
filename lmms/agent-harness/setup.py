from setuptools import setup
setup(
    name='cli-anything-lmms',
    version='1.0.0',
    packages=['cli_anything.lmms'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-lmms=cli_anything.lmms:cli',
        ],
    },
)
