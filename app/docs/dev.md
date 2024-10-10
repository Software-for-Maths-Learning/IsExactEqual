# IsExactEqual
Could be qualified as the simplest form of evaluation function, testing exact equality. This function will use the default python `==` test to compare answer and responses. It doesn't infer any types - meaning it requires a `params.type` to be supplied.

## Inputs
This function requires a parameter to function properly:
```json 
{ 
  "params": {
    "type": "<string>" (any of ["int", "float", "str", "dict"])
  }
  "response": <>,
  "answer": <>
}

```

When a student submits a response to a response area the number of previously submitted responses submitted to the same response area byt the same student will be sent to the evaluation function. The following format is used:
```json
{
    "submission_context": {
        "submissions_per_student_per_response_area": # non-negative integer that represent the number of previously processed responses
    }
}
```

The total number of submitted responses (i.e. the number of processed response + 1) can be displayed in the feedback by setting adding a field named `display_submission_count` to `params` and set its value to true.

## Outputs
Outputs to the `grade` command will feature:

```json
{
  "command": "eval",
  "result": {
    "is_correct": "<bool>"
  }
}

```

## Examples

### Simple String Comparison

```python
{
  "answer": "hydrophobic",
  "response": "hydrophobic",
  "params": {
    "type": "str"
  }
}
```

### Displaying number of submitted responses in the feedback

```python
{
  "answer": 1,
  "response": 1,
  "params": {
    "type": "int",
    "display_submission_count": true
  }
}
```
