from typing import Union, TypedDict

class ResponseBody(TypedDict):
    body: Union[dict,str]
    message: str