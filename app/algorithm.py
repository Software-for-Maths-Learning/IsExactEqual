def grading_function(body: dict) -> dict:
    """
    Function used to grade a student response.
    ---
    The handler function passes only one argument to grading_function(),
    which is a dictionary of the structure of the API request body
    deserialised from JSON.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. This is also subject to
    standard response specifications.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that grading_function() is the main function used
    to output the grading response.
    """

    type_dict = {"float": float, "int": int, "str": str, "dict": dict}
    req_type = body["params"]["type"]

    # Try cast each of the inputs to their requested type:
    errors = []
    try:
        res = type_dict[req_type](body["response"])
    except ValueError as e:
        errors += [
            {"description": f"Could not cast `response` parameter to {req_type}"}
        ]

    try:
        ans = type_dict[req_type](body["answer"])
    except ValueError as e:
        errors += [{"description": f"Could not cast `answer` parameter to {req_type}"}]

    if errors:
        return {"error": errors}

    # Are they equaL?
    is_exact_equal = res == ans

    return {"is_correct": is_exact_equal}
