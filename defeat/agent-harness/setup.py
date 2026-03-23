from setuptools import setup
setup(
    name='cli-anything-defeat',
    version='1.0.0',
    packages=['cli_anything.defeat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-defeat=cli_anything.defeat:cli']},
)
