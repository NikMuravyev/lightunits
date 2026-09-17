{% for annotation in annotations -%}
{%if annotation.comment %}
{{annotation.comment}}:
{%endif%}
{%if annotation.annotatedText %}  
><mark style="background: {{annotation.color}}">{{annotation.annotatedText | nl2br}} </mark> ([p. {{annotation.page}}](file://{{annotation.attachment.path | replace(" ", "%20")}}))  
{%endif%}
{%- if annotation.imageRelativePath %}  
> ![[{{annotation.imageRelativePath}}]]
{%- endif %}
---
{% endfor -%}