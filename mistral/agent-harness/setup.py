from setuptools import setup
setup(
    name='cli-anything-mistral',
    version='1.0.0',
    packages=['cli_anything.mistral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mistral=cli_anything.mistral:cli']},
)
