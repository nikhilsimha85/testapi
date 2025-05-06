from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model=str)
def get_tvarv(im_skip_non_buf:str="True", im_param_names:str="lt_params", ex_values:str="lt_values") -> str:
    if im_skip_non_buf == "true" or im_skip_non_buf == "True":
        val = True
    else:
        val = False
    return(
    f'''CALL METHOD zcl_parameters=>get_all_variables
    EXPORTING
    im_param_names  = {im_param_names}
    im_skip_non_buf = {val}
    IMPORTING
    ex_values       = {ex_values}'''
    )

