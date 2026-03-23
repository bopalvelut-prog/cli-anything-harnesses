from setuptools import setup
setup(
    name='cli-anything-textgen',
    version='1.0.0',
    packages=['cli_anything.textgen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-textgen=cli_anything.textgen:cli']},
)
