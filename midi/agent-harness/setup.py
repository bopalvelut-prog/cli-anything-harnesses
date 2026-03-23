from setuptools import setup
setup(
    name='cli-anything-midi',
    version='1.0.0',
    packages=['cli_anything.midi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-midi=cli_anything.midi:cli']},
)
