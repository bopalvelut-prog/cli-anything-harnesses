from setuptools import setup
setup(
    name='cli-anything-button',
    version='1.0.0',
    packages=['cli_anything.button'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-button=cli_anything.button:cli']},
)
