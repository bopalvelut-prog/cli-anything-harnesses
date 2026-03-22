from setuptools import setup
setup(
    name='cli-anything-autopsy',
    version='1.0.0',
    packages=['cli_anything.autopsy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autopsy=cli_anything.autopsy:cli']},
)
