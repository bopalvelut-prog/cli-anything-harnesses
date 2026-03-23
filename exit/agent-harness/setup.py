from setuptools import setup
setup(
    name='cli-anything-exit',
    version='1.0.0',
    packages=['cli_anything.exit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exit=cli_anything.exit:cli']},
)
