import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def lista_imagens():
    imagens=[]
    bucket = s3.Bucket('breaking-bad-bucket')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    return imagens

def indexa_colecao(imagens):
    client.create_collection(
        CollectionId='faces-breaking-bad'
    )
    for i in imagens:
        response=client.index_faces(
            CollectionId='faces-breaking-bad',
            DetectionAttributes=[
            ],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'breaking-bad-bucket',
                    'Name': i,
                },
            },
        )

imagens = lista_imagens()
print(imagens)
indexa_colecao(imagens)