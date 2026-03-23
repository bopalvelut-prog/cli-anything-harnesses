from setuptools import setup
setup(
    name='cli-anything-rocks',
    version='1.0.0',
    packages=['cli_anything.rocks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocks=cli_anything.rocks:cli']},
)
