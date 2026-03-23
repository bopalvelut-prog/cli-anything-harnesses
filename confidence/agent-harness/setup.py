from setuptools import setup
setup(
    name='cli-anything-confidence',
    version='1.0.0',
    packages=['cli_anything.confidence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-confidence=cli_anything.confidence:cli']},
)
