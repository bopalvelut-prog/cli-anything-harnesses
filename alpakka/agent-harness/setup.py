from setuptools import setup
setup(
    name='cli-anything-alpakka',
    version='1.0.0',
    packages=['cli_anything.alpakka'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alpakka=cli_anything.alpakka:cli']},
)
