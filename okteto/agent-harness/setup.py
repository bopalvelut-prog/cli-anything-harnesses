from setuptools import setup
setup(
    name='cli-anything-okteto',
    version='1.0.0',
    packages=['cli_anything.okteto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-okteto=cli_anything.okteto:cli']},
)
