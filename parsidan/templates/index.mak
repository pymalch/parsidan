<%inherit file="local:templates.master"/>

<div id="mainParsidan">
    <img src="${tg.url('/img/parsidan.jpg')}">
</div>
<div id="dictWrapper" class="fs1">
    <div id="fromLangWrapper">
        <input id="queryInput" type="text" class="form-control main-persian-input"
               placeholder="${ _('Please enter non persian word') }">

        <div class="messages">

            <div class="loading"><img src="img/preloader.gif"></div>
            <div class="noResult item">${ _('Persian translate for this word did not find!') }</div>
            <div class="wordAdded s1 item"> ${ _('Word stores is database to translate later.') }</div>
            <div class="addedWordBefore s2 item">${ _('Word is already added and is waiting for translation.') }</div>
            <div class="aPersianWord s3 item">${ _('The word you entered is already a persian word!') }</div>
        </div>

    </div>


</div>
<div class="join">${ _("You can %(join)s and help us to improve this dictionary.") % {'join': "JOIN US" } } </div>

<%def name="scripts()">

    <script type="text/javascript">
        $(document).ready(function () {
            parsidan.search.Engine.setUp();
        });
    </script>
</%def>