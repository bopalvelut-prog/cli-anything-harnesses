from setuptools import setup
setup(
    name='cli-anything-designer',
    version='1.0.0',
    packages=['cli_anything.designer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-designer=cli_anything.designer:cli']},
)
