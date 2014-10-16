<%inherit file="local:templates.master"/>
<%def name="title()">${_('Verification Success')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3">
        <h2>${_('Verification success!')}</h2>

        <p>
            you can now:
            <ul>
                <li><a href="/login">${_('Login')}</a></li>
                <li><a href="/">${_('Homepage')}</a></li>
            </ul>


        </p>
    </div>
</div>