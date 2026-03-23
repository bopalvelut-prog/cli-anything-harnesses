from setuptools import setup
setup(
    name='cli-anything-vulture',
    version='1.0.0',
    packages=['cli_anything.vulture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vulture=cli_anything.vulture:cli']},
)
