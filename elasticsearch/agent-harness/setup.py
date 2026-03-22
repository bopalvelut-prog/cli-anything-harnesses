from setuptools import setup
setup(
    name='cli-anything-elasticsearch',
    version='1.0.0',
    packages=['cli_anything.elasticsearch'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-elasticsearch=cli_anything.elasticsearch:cli']},
)
