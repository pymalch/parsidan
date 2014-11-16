<%inherit file="local:templates.master"/>
<%def name="title()">${_('Verification Success')}</%def>

<div class="row verification-success">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-3">
        <h2><span class="glyphicon glyphicon-ok" aria-hidden="true"></span> ${_('Verification success!')}</h2>

        <p>

            <ul class="nav nav-pills">
                <li><a href="/login"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> ${_('Login')}</a></li>
                <li><a href="/"><span class="glyphicon glyphicon-home" aria-hidden="true"></span> ${_('Homepage')}</a></li>
            </ul>


        </p>
    </div>
</div>