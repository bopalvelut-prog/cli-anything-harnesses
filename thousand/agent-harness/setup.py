from setuptools import setup
setup(
    name='cli-anything-thousand',
    version='1.0.0',
    packages=['cli_anything.thousand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thousand=cli_anything.thousand:cli']},
)
