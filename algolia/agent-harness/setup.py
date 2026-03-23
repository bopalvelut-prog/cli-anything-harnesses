from setuptools import setup
setup(
    name='cli-anything-algolia',
    version='1.0.0',
    packages=['cli_anything.algolia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-algolia=cli_anything.algolia:cli']},
)
