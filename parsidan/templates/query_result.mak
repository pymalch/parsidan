

<h2>${_('Showing persian equivalent of the word: %s') % word}</h2>
<ul>
%for r in result:
    <li>${r['offer']}</li>
%endfor
</ul>
