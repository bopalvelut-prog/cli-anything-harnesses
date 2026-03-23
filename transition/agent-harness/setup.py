from setuptools import setup
setup(
    name='cli-anything-transition',
    version='1.0.0',
    packages=['cli_anything.transition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transition=cli_anything.transition:cli']},
)
