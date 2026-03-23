from setuptools import setup
setup(
    name='cli-anything-axe',
    version='1.0.0',
    packages=['cli_anything.axe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-axe=cli_anything.axe:cli']},
)
