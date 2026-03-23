from setuptools import setup
setup(
    name='cli-anything-wrestle',
    version='1.0.0',
    packages=['cli_anything.wrestle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrestle=cli_anything.wrestle:cli']},
)
