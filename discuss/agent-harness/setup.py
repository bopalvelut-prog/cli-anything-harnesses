from setuptools import setup
setup(
    name='cli-anything-discuss',
    version='1.0.0',
    packages=['cli_anything.discuss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discuss=cli_anything.discuss:cli']},
)
