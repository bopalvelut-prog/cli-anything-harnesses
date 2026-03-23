from setuptools import setup
setup(
    name='cli-anything-kate',
    version='1.0.0',
    packages=['cli_anything.kate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kate=cli_anything.kate:cli']},
)
