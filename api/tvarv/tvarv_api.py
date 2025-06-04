from fastapi import APIRouter, Response, Path
from typing import Annotated

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model= str)
def get_tvarv(
              im_params: Annotated[str, Path( title = "list of paramater names in TVARV to be fetched. The type of parameter is ZTT_TVARVC_NAME which is a table type of structure ZST_TVARVC_NAME which has one field NAME")] = "lt_values",
              im_skip_buf: Annotated[str, Path(title = "If abap_true skip fetching data from non-buffered tables")] = "abap_true",
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

