from setuptools import setup
setup(
    name='cli-anything-corner',
    version='1.0.0',
    packages=['cli_anything.corner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-corner=cli_anything.corner:cli']},
)
