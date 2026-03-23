from setuptools import setup
setup(
    name='cli-anything-minister',
    version='1.0.0',
    packages=['cli_anything.minister'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minister=cli_anything.minister:cli']},
)
