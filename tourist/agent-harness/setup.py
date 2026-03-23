from setuptools import setup
setup(
    name='cli-anything-tourist',
    version='1.0.0',
    packages=['cli_anything.tourist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tourist=cli_anything.tourist:cli']},
)
