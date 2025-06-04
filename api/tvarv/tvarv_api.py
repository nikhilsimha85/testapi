from fastapi import APIRouter, Response, Path
from typing import Annotated

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model= str)
def get_tvarv(
              
             
             ) -> str:
    return(
    f'''CALL METHOD zcl_parameters=>get_all_variables
    EXPORTING
    im_param_names  = 
    im_skip_non_buf = 
    IMPORTING
    ex_values       = '''
    )

