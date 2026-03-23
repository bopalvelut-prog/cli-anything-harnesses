from setuptools import setup
setup(
    name='cli-anything-drop',
    version='1.0.0',
    packages=['cli_anything.drop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drop=cli_anything.drop:cli']},
)
