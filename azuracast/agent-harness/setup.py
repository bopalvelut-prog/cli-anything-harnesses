from setuptools import setup
setup(
    name='cli-anything-azuracast',
    version='1.0.0',
    packages=['cli_anything.azuracast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azuracast=cli_anything.azuracast:cli']},
)
