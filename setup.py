from setuptools import setup

setup(name='gensqlalorm',
      version='0.0.1',
      description='a generate sqlarchemy models utils',
      url='https://github.com/SUT-GC/gen-sqla-orm',
      author='gouchao',
      author_email='sutgouc@gmail.com',
      license='MIT',
      packages=["config", "db", "gen", "utils"],
      install_requires=[
          'PyMySQL>=0.9.3',
          'PyYAML>=5.2',
      ],
      zip_safe=False)
