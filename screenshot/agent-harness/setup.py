from setuptools import setup
setup(
    name='cli-anything-screenshot',
    version='1.0.0',
    packages=['cli_anything.screenshot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-screenshot=cli_anything.screenshot:cli']},
)
