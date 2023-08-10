from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "HOSTNAME",
        access_key="ACCESS_KEY",
        secret_key="SECRET_KEY",
        secure=False,
        cert_check=False
        
    )

    # Make 'BUCKET_NAME' bucket if not exist.
    found = client.bucket_exists("BUCKET_NAME")
    if not found:
        client.make_bucket("BUCKET_NAME")
    else:
        print("Bucket 'BUCKET_NAME' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'image.png' to bucket 'BUCKET_NAME'.
    client.fput_object(
        "BUCKET_NAME", "image.png", "/home/USER/learn/minio/image.png",
    )
    print(
        "'/home/USER/learn/minio/image.png' is successfully uploaded as "
        "object 'image.png' to bucket 'BUCKET_NAME'."
    )

def func_list_buckets():
    client = Minio('HOSTNAME', access_key='ACCESS_KEY', secret_key='SECRET_KEY', secure=False)
    #buckets = client.list_buckets()
    # for bucket in buckets:
    #     print(bucket.name, bucket.creation_date)
    objects = client.list_objects("BUCKET_NAME",prefix='avatar/')
    for obj in objects:
        print(obj)

if __name__ == "__main__":
    try:
#        main()
        func_list_buckets()
    except S3Error as exc:
        print("error occurred.", exc)