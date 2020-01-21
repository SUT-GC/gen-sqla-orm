from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gensqlalorm',
      version='0.0.11',
      description='a generate sqlarchemy models utils',
      url='https://github.com/SUT-GC/gen-sqla-orm',
      author='gouchao',
      author_email='sutgouc@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'PyMySQL>=0.9.3',
          'PyYAML>=5.2',
      ],
      entry_points={
          'console_scripts': [
              'gensqlalorm = gensqlalorm:gen_console',

          ]
      },
      zip_safe=True)
