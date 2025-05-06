from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/", tags=["tvarv"], response_model=None)
def get_tvarv() -> Response |str:
    return(
    f'''CALL METHOD zcl_parameters=>get_all_variables
    EXPORTING
    im_param_names  = lt_params
    im_skip_non_buf = True
    IMPORTING
    ex_values       = lt_values'''
    )

