<%inherit file="local:templates.master"/>

<ul>
%for r in result:
    <li>${r}</li>
%endfor
</ul>
