from setuptools import setup
setup(
    name='cli-anything-strength',
    version='1.0.0',
    packages=['cli_anything.strength'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strength=cli_anything.strength:cli']},
)
