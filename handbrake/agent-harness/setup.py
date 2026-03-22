from setuptools import setup
setup(
    name='cli-anything-handbrake',
    version='1.0.0',
    packages=['cli_anything.handbrake'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-handbrake=cli_anything.handbrake:cli',
        ],
    },
)
