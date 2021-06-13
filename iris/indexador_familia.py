import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def lista_imagens():
    imagens=[]
    bucket = s3.Bucket('familia-bucket')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
        #print(imagem)
    print(imagens)
    return imagens

def indexa_colecao(imagens):
    client.create_collection(
        CollectionId='faces-familia'
    )
    for i in imagens:
        response=client.index_faces(
            CollectionId='faces-familia',
            DetectionAttributes=[
            ],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'familia-bucket',
                    'Name': i,
                },
            },
        )

imagens = lista_imagens()
indexa_colecao(imagens)