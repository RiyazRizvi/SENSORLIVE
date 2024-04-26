from dataclasses import dataclass

@dataclass
# decorator --> to store the data

class DataIngestionArtifacts:
    trained_file_path: str
    test_file_path: str