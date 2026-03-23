from setuptools import setup
setup(
    name='cli-anything-mkosi',
    version='1.0.0',
    packages=['cli_anything.mkosi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mkosi=cli_anything.mkosi:cli']},
)
