from fastapi import APIRouter

from domain.tvarv import tvarv

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model=list[str])
def get_tvarv(im_param_names:str,im_skip_non_buf:bool, ex_values:str) -> list[str]:
    res = []
    res.append("CALL METHOD zcl_parameters=>get_all_variables")
    res.append("EXPORTING")
    res.append("im_param_names  = {im_param_names}")
    res.append("im_skip_non_buf = {im_skip_non_buf}")
    res.append("IMPORTING")
    res.append("ex_values       = {ex_values}")
    return res
