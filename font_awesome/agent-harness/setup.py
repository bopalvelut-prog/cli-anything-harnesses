from setuptools import setup
setup(
    name='cli-anything-font_awesome',
    version='1.0.0',
    packages=['cli_anything.font_awesome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-font_awesome=cli_anything.font_awesome:cli']},
)
