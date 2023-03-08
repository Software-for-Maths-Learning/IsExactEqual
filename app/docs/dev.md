# IsExactEqual
Could be qualified as the simplest form of evaluation function, testing exact equality. This function will use the default python `==` test to compare answer and responses. It doesn't infer any types - meaning it requires a `params.type` to be supplied.

[link](./user.md)

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
  "response" "hydrophobic",
  "params": {
    "type": "str"
  }
}
```

```python
{
  "example": {
    "Something": "something"
  }
}
```
