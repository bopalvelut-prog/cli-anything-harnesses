from setuptools import setup
setup(
    name='cli-anything-bubble',
    version='1.0.0',
    packages=['cli_anything.bubble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bubble=cli_anything.bubble:cli']},
)
