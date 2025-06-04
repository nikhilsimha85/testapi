from fastapi import APIRouter, Response, Path
from typing import Annotated

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model= str)
def get_tvarv(
              ex_out: Annotated[str, Path(title = "Output which contains the TVARV entries. The type is ZTT_DYN_VAR which is a table type")] = "lt_out"
             
             ) -> str:
    return(
    f'''CALL METHOD zcl_parameters=>get_all_variables
    EXPORTING
    im_param_names  = 
    im_skip_non_buf = 
    IMPORTING
    ex_values       = '''
    )

