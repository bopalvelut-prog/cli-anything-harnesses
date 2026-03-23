from setuptools import setup
setup(
    name='cli-anything-plan',
    version='1.0.0',
    packages=['cli_anything.plan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plan=cli_anything.plan:cli']},
)
