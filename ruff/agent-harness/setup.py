from setuptools import setup
setup(
    name='cli-anything-ruff',
    version='1.0.0',
    packages=['cli_anything.ruff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ruff=cli_anything.ruff:cli']},
)
