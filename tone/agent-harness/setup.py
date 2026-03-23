from setuptools import setup
setup(
    name='cli-anything-tone',
    version='1.0.0',
    packages=['cli_anything.tone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tone=cli_anything.tone:cli']},
)
