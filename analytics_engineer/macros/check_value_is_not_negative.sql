{% test check_value_is_not_negative(model, column_name) %}
SELECT * FROM {{ model }} 
   WHERE {{ column_name}} < 0
{% endtest %}