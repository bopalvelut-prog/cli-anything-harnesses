from setuptools import setup
setup(
    name='cli-anything-audience',
    version='1.0.0',
    packages=['cli_anything.audience'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-audience=cli_anything.audience:cli']},
)
