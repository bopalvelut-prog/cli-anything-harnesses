from setuptools import setup
setup(
    name='cli-anything-hate',
    version='1.0.0',
    packages=['cli_anything.hate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hate=cli_anything.hate:cli']},
)
