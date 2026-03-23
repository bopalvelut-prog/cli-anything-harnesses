from setuptools import setup
setup(
    name='cli-anything-tyr',
    version='1.0.0',
    packages=['cli_anything.tyr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tyr=cli_anything.tyr:cli']},
)
