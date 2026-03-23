from setuptools import setup
setup(
    name='cli-anything-review',
    version='1.0.0',
    packages=['cli_anything.review'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-review=cli_anything.review:cli']},
)
