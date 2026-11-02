# Python Logging Demonstration

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A small modern Python 3 logging example demonstrating DEBUG, INFO, WARNING, ERROR and CRITICAL levels. Importing the module does not write files. A reusable function configures its own handler, closes it properly and uses parameterized logging rather than string interpolation.

```sh
python3 loggin.py
python3 loggin.py --output ./my-example.log
python3 -m unittest discover -s tests -v
```

Original code: [old branch](https://github.com/hamdyaea/logging/tree/old).
