from setuptools import setup
setup(
    name='cli-anything-heat',
    version='1.0.0',
    packages=['cli_anything.heat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-heat=cli_anything.heat:cli']},
)
