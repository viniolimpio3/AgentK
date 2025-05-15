from src.services.db.models import file_last_modification as flm
if __name__ == '__main__':
    result = flm.fetch_by({"filename": "test1-pod.yaml"})
    print(result)
    print(result[0]['st_mtime'])
