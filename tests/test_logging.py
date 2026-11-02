# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from loggin import write_demo

class LoggingTests(unittest.TestCase):
    def test_writes_expected_levels(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "test.log"
            write_demo(path)
            data = path.read_text()
            for level in ("DEBUG", "CRITICAL", "INFO", "WARNING", "ERROR"):
                self.assertIn(level, data)
            self.assertIn("Variable 2:", data)

if __name__ == "__main__":
    unittest.main()
