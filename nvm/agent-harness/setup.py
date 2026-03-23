from setuptools import setup
setup(
    name='cli-anything-nvm',
    version='1.0.0',
    packages=['cli_anything.nvm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nvm=cli_anything.nvm:cli']},
)
