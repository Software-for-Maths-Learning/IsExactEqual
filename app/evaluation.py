from evaluation_function_utils.errors import EvaluationException


def evaluation_function(response, answer, params) -> dict:
    """
    Function used to grade a student response.
    ---
    The handler function passes only one argument to evaluation_function(),
    which is a dictionary of the structure of the API request body
    deserialised from JSON.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. This is also subject to
    standard response specifications.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that evaluation_function() is the main function used
    to output the grading response.
    """

    type_dict = {"float": float, "int": int, "str": str, "dict": dict}
    req_type = params.get("type", False)

    if not req_type:
        raise EvaluationException(
            "The evaluation function couldn't process this request: missing parameter",
            missing="params.type")

    cast_type = type_dict.get(req_type, False)

    if not cast_type:
        raise EvaluationException(f"Supplied type {req_type} not available",
                                  valid_types=list(type_dict.keys()))

    # Try cast each of the inputs to their requested type:
    errors = []
    try:
        res = cast_type(response)
    except ValueError as e:
        raise EvaluationException(
            f"Could not cast `response` parameter to {req_type}")

    try:
        ans = cast_type(answer)
    except ValueError as e:
        raise EvaluationException(
            f"Could not cast `answer` parameter to {req_type}")

    # Are they equal?
    return {"is_correct": res == ans}
