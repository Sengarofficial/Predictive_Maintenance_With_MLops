import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.Mlflow_Project import logger

class FileOperations:
    @staticmethod
    @ensure_annotations
    def read_yaml(path_to_yaml: Path) -> ConfigBox:
        """reads yaml file and returns ConfigBox type"""
        try:
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"yaml file: {path_to_yaml} loaded successfully")
                return ConfigBox(content)
        except Exception as e:
            raise e

    @staticmethod
    @ensure_annotations
    def create_directories(path_to_directories: list, verbose=True):
        """create list of directories"""
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")

    @staticmethod
    @ensure_annotations
    def save_json(path: Path, data: dict):
        """save json data"""
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

        logger.info(f"json file saved at: {path}")

    @staticmethod
    @ensure_annotations
    def load_json(path: Path) -> ConfigBox:
        """load json files data"""
        with open(path) as f:
            content = json.load(f)

        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)

    @staticmethod
    @ensure_annotations
    def save_bin(data: Any, path: Path):
        """save binary file"""
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at: {path}")

    @staticmethod
    @ensure_annotations
    def load_bin(path: Path) -> Any:
        """load binary data"""
        data = joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data

    @staticmethod
    @ensure_annotations
    def get_size(path: Path) -> str:
        """get size in kb"""
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
 