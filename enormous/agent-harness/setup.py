from setuptools import setup
setup(
    name='cli-anything-enormous',
    version='1.0.0',
    packages=['cli_anything.enormous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enormous=cli_anything.enormous:cli']},
)
