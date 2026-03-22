from setuptools import setup
setup(
    name='cli-anything-prismic',
    version='1.0.0',
    packages=['cli_anything.prismic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prismic=cli_anything.prismic:cli']},
)
