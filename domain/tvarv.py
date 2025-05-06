from pydantic import BaseModel


class tvarv(BaseModel):
    im_param_names: list[str]
    im_skip_non_buf: bool
    ex_values: list[str] 
