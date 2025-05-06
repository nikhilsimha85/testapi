from fastapi import APIRouter

from domain.tvarv import tvarv

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model=str)
def get_tvarv(im_skip_non_buf:bool=True, im_param_names:str="lt_params", ex_values:str="lt_values") -> str:
    return(
    f'''CALL METHOD zcl_parameters=>get_all_variables
    EXPORTING
    im_param_names  = {im_param_names}
    im_skip_non_buf = {im_skip_non_buf}
    IMPORTING
    ex_values       = {ex_values}'''
    )

