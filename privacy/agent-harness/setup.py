from setuptools import setup
setup(
    name='cli-anything-privacy',
    version='1.0.0',
    packages=['cli_anything.privacy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-privacy=cli_anything.privacy:cli']},
)
