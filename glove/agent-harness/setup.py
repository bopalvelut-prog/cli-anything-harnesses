from setuptools import setup
setup(
    name='cli-anything-glove',
    version='1.0.0',
    packages=['cli_anything.glove'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glove=cli_anything.glove:cli']},
)
