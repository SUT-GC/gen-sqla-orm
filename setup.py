from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gensqlalorm',
      version='0.0.3',
      description='a generate sqlarchemy models utils',
      url='https://github.com/SUT-GC/gen-sqla-orm',
      author='gouchao',
      author_email='sutgouc@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=["gensqlalorm"],
      install_requires=[
          'PyMySQL>=0.9.3',
          'PyYAML>=5.2',
      ],
      zip_safe=False)
