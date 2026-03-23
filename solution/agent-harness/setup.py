from setuptools import setup
setup(
    name='cli-anything-solution',
    version='1.0.0',
    packages=['cli_anything.solution'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solution=cli_anything.solution:cli']},
)
