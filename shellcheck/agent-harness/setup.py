from setuptools import setup
setup(
    name='cli-anything-shellcheck',
    version='1.0.0',
    packages=['cli_anything.shellcheck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shellcheck=cli_anything.shellcheck:cli']},
)
