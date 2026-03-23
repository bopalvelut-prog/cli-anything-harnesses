from setuptools import setup
setup(
    name='cli-anything-roaring',
    version='1.0.0',
    packages=['cli_anything.roaring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roaring=cli_anything.roaring:cli']},
)
