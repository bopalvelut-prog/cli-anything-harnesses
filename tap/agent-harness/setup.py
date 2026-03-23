from setuptools import setup
setup(
    name='cli-anything-tap',
    version='1.0.0',
    packages=['cli_anything.tap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tap=cli_anything.tap:cli']},
)
