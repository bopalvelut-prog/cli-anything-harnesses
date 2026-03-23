from setuptools import setup
setup(
    name='cli-anything-brain',
    version='1.0.0',
    packages=['cli_anything.brain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brain=cli_anything.brain:cli']},
)
