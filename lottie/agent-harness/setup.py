from setuptools import setup
setup(
    name='cli-anything-lottie',
    version='1.0.0',
    packages=['cli_anything.lottie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lottie=cli_anything.lottie:cli']},
)
