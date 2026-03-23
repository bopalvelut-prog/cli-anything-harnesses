from setuptools import setup
setup(
    name='cli-anything-root',
    version='1.0.0',
    packages=['cli_anything.root'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-root=cli_anything.root:cli']},
)
