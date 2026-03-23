from setuptools import setup
setup(
    name='cli-anything-recent',
    version='1.0.0',
    packages=['cli_anything.recent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recent=cli_anything.recent:cli']},
)
