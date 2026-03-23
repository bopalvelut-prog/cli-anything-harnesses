from setuptools import setup
setup(
    name='cli-anything-others',
    version='1.0.0',
    packages=['cli_anything.others'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-others=cli_anything.others:cli']},
)
