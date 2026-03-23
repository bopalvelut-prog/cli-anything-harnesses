from setuptools import setup
setup(
    name='cli-anything-rules',
    version='1.0.0',
    packages=['cli_anything.rules'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rules=cli_anything.rules:cli']},
)
