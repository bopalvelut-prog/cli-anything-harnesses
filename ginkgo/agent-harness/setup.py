from setuptools import setup
setup(
    name='cli-anything-ginkgo',
    version='1.0.0',
    packages=['cli_anything.ginkgo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ginkgo=cli_anything.ginkgo:cli']},
)
