from setuptools import setup

setup(
    name="Serializers",
    version='1.0.4',
    author="Anya",
    packages=['serializers.json', 'serializers.pickle', 'serializers.toml', 'serializers.yaml', 'serializers.abstract_serializer', 'serializers.serializer_factory', 'addition', 'logger'],
    install_requires=['PyYAML==5.3.1', 'pytomlpp==0.3.5'],
    scripts=['serialize'],
    url="https://github.com/alicecoal/python_Lab2/tree/main/serializers",
    tests_require=['pytest']
)
