#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Small Python logging demonstration without import-time side effects."""
import argparse
import logging
from pathlib import Path

FORMAT = "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s"

def write_demo(path: Path) -> None:
    logger = logging.getLogger("daylight.logging.demo")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)
    try:
        logger.debug("This message should go to the log file")
        logger.critical("Critical log example")
        logger.info("Informational log example")
        logger.warning("Warning log example")
        logger.error("Error log example")
        logger.info("Variable: %s; Variable 2: %s", "Je suis une variable", "Je suis une autre variable !")
    finally:
        logger.removeHandler(handler)
        handler.close()

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("example.log"))
    args = parser.parse_args()
    write_demo(args.output)
    print(f"Log written to {args.output}")

if __name__ == "__main__":
    main()
