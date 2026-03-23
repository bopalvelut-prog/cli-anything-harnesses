from setuptools import setup
setup(
    name='cli-anything-kitty',
    version='1.0.0',
    packages=['cli_anything.kitty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kitty=cli_anything.kitty:cli']},
)
