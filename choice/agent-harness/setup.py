from setuptools import setup
setup(
    name='cli-anything-choice',
    version='1.0.0',
    packages=['cli_anything.choice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-choice=cli_anything.choice:cli']},
)
