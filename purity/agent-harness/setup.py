from setuptools import setup
setup(
    name='cli-anything-purity',
    version='1.0.0',
    packages=['cli_anything.purity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purity=cli_anything.purity:cli']},
)
