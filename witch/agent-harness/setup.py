from setuptools import setup
setup(
    name='cli-anything-witch',
    version='1.0.0',
    packages=['cli_anything.witch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-witch=cli_anything.witch:cli']},
)
