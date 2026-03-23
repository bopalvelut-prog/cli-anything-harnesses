from setuptools import setup
setup(
    name='cli-anything-blog',
    version='1.0.0',
    packages=['cli_anything.blog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blog=cli_anything.blog:cli']},
)
