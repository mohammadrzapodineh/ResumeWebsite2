


def upload_image_to_gallery(self, instance, **kwargs):
    '''
    This Function Get instance Of image should upload to gallery and Return New Path 
    '''
    upload_path = f'portfolio/gallery/{self.title}/{instance}'
    return upload_path