from setuptools import setup
setup(
    name='cli-anything-sea',
    version='1.0.0',
    packages=['cli_anything.sea'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sea=cli_anything.sea:cli']},
)
