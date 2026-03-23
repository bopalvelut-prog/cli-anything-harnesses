from setuptools import setup
setup(
    name='cli-anything-odyssey',
    version='1.0.0',
    packages=['cli_anything.odyssey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-odyssey=cli_anything.odyssey:cli']},
)
