from setuptools import setup
setup(
    name='cli-anything-optaplanner',
    version='1.0.0',
    packages=['cli_anything.optaplanner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-optaplanner=cli_anything.optaplanner:cli']},
)
