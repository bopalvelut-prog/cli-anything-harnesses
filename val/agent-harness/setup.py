from setuptools import setup
setup(
    name='cli-anything-val',
    version='1.0.0',
    packages=['cli_anything.val'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-val=cli_anything.val:cli']},
)
