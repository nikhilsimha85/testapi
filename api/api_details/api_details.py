from fastapi import APIRouter, Response, Path, Query
from typing import Annotated
import json

router = APIRouter()

@router.get("/{class_name}/{method_name}", tags=["class_method"], response_model= str)
def get_method_details(
              class_name: Annotated[str, Path( title = "A string representing the class name for which the signature needs to be retrieved")] ,
              method_name: Annotated[str, Path(title = "A string representing the method name for which the signature needs to be retrieved")] 
             ) -> str:
    if( class_name =="ZCL_ROVER_SEND_EMAIL" and method_name == "SEND_EMAIL"):
        return(json.dumps({
    "class_name": "ZCL_ROVER_SEND_EMAIL",
    "method_name": "SEND_EMAIL",
    "description": "Send Email through Rover to end user",
    "import_parameters": [
        {
            "name": "IM_APPID",
            "direction": "Importing",
            "type": "ZDS_APPID",
            "default_value": "90",
            "required": false,
            "description": "DS ID of the Application"
        },
        {
            "name": "IM_MESSAGE_HDR",
            "direction": "Importing",
            "type": {
                "Structure": "ZROVER_MSG_HDR",
                "fields": {
                    "SUBJECT": "string",
                    "COLLATERAL": "string",
                    "COLLATERAL_SUB_TYPE": "string"
                }
            },
            "required": false,
            "description": "Message header containing subject and other details"
        },
        {
            "name": "IM_PAYLOAD",
            "direction": "Importing",
            "type": "ANY",
            "required": false,
            "description": "Custom payload with information of field values to be sent in the email"
        },
        {
            "name": "IM_ATTACH",
            "direction": "Importing",
            "type": {
                "Structure": "TT_ATTACH",
                "fields": {
                    "NAME": "string",
                    "OTF_CONTENT": "string"
                }
            },
            "required": false,
            "description": "Attachments to be included in the email"
        },
        {
            "name": "IM_EMAIL_HDR",
            "direction": "Importing",
            "type": {
                "Structure": "ZROVER_EMAIL_HDR",
                "fields": {
                    "TO": {
                        "TABLE": "ZSCBX_TO_EMAIL",
                        "fields": {
                            "ZCBX_TO_EMAIL": "CHAR(80)"
                        }
                    },
                    "CC": {
                        "TABLE": "ZSCBX_CC_EMAIL",
                        "fields": {
                            "ZCBX_CC_EMAIL": "CHAR(80)"
                        }
                    },
                    "BCC": {
                        "TABLE": "ZSCBX_BCC_EMAIL",
                        "fields": {
                            "ZCBX_BCC_EMAIL": "CHAR(80)"
                        }
                    }
                }
            },
            "required": false,
            "description": "Email address to which the email will be sent"
        }
    ],
    "export_parameters": [
        {
            "name": "EX_RESPONSE_HDR",
            "direction": "Exporting",
            "type": "ZSESP_RESPONSE_HDR",
            "required": false,
            "description": "Response header containing status and message"
        }
    ]
}))
    else:
        return("No such method found")


@router.get("/{class_name}", tags=["class"], response_model= str)
def get_all_method_details(
              class_name: Annotated[str, Path( title = "A string representing the class name for which the signature needs to be retrieved")]
              
             ) -> str:
    if( class_name =="ZCL_PARAMETERS"):
        return(
            json.dumps([
    {
        "class_name": "ZCL_PARAMETERS",
        "method_name": "GET_ALL_VARIABLES",
        "description": "Get all variables from TVARVC",
        "import_parameters": [
            {
                "name": "IM_PARAM_NAMES",
                "direction": "Importing",
                "type": {
                    "Table": "ZTT_TVARVC_NAME",
                    "fields": {
                        "NAME": "CHAR(50)"
                    }
                },
                "required": true,
                "description": "Variable names to be retrieved from TVARVC"
            },
            {
                "name": "IM_SKIP_NON_BUF",
                "direction": "Importing",
                "type": "BOOLE_D",
                "default_value": "abap_true",
                "required": false,
                "description": "Whether to Skip Non Buffered Table"
            }
        ],
        "export_parameters": [
            {
                "name": "EX_VALUES",
                "direction": "Exporting",
                "type": {
                    "Table": "ZTT_DYN_VAR",
                    "fields": {
                        "NAME": "CHAR(50)",
                        "TYPE": "CHAR(1)",
                        "SIGN": "CHAR(1)",
                        "OPTION": "CHAR(2)",
                        "LOW": "CHAR(80)",
                        "HIGH": "CHAR(80)"
                    }
                },
                "required": true,
                "description": "Table containing the variable names and their values"
            }
        ]
    },
    {
        "class_name": "ZCL_PARAMETERS",
        "method_name": "GET_PARAMETER",
        "description": "Get single paramater variables from TVARVC",
        "import_parameters": [
            {
                "name": "IM_PARAM_NAME",
                "direction": "Importing",
                "type": "CHAR(50)",
                "required": true,
                "description": "Variable name to be retrieved from TVARVC"
            }
        ],
        "export_parameters": [
            {
                "name": "EX_VALUES",
                "direction": "Exporting",
                "type": {
                    "Table": "ZTT_DYN_VAR",
                    "fields": {
                        "NAME": "CHAR(50)",
                        "TYPE": "CHAR(1)",
                        "SIGN": "CHAR(1)",
                        "OPTION": "CHAR(2)",
                        "LOW": "CHAR(80)",
                        "HIGH": "CHAR(80)"
                    }
                },
                "required": true,
                "description": "Table containing the variable names and their values"
            }
        ]
    }
]
        ))
    else:
        return("No such class found")

@router.get("/{function_module_name}", tags=["function_module"], response_model= str)
def get_method_details(
              function_module_name: Annotated[str, Path( title = "A string representing the Function module name for which the signature needs to be retrieved")]
              
             ) -> str:
    return("Function module not found")
