from setuptools import setup
setup(
    name='cli-anything-ashley',
    version='1.0.0',
    packages=['cli_anything.ashley'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ashley=cli_anything.ashley:cli']},
)
