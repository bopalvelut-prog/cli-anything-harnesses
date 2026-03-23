from setuptools import setup
setup(
    name='cli-anything-affinity',
    version='1.0.0',
    packages=['cli_anything.affinity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-affinity=cli_anything.affinity:cli']},
)
