from setuptools import setup
setup(
    name='cli-anything-cinnamon',
    version='1.0.0',
    packages=['cli_anything.cinnamon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cinnamon=cli_anything.cinnamon:cli']},
)
