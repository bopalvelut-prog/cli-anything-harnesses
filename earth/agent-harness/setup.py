from setuptools import setup
setup(
    name='cli-anything-earth',
    version='1.0.0',
    packages=['cli_anything.earth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-earth=cli_anything.earth:cli']},
)
