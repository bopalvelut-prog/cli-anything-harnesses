from setuptools import setup
setup(
    name='cli-anything-recipe',
    version='1.0.0',
    packages=['cli_anything.recipe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recipe=cli_anything.recipe:cli']},
)
