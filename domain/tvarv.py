from pydantic import BaseModel


class tvarv(BaseModel):
    im_param_names: str
    im_skip_non_buf: bool
    ex_values: str 
