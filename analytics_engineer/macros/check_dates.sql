{% test check_dates(model, column_name) %}
SELECT * FROM {{ model }} 
   WHERE {{ column_name}} NOT BETWEEN '2010-01-01' AND '2024-12-31'
{% endtest %}