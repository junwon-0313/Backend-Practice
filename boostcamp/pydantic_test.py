from pydantic import BaseModel, HttpUrl, Field, DirectoryPath

class ModelInput03(BaseModel):
    url: HttpUrl
    rate: int = Field(ge=1, le=10)
    target_dir: DirectoryPath
    
if __name__=='__main__':
    ModelInput03(url="https://www.naver.com", rate=2, target_dir='/' )

    