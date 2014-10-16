<%inherit file="local:templates.master"/>
<%def name="title()">${_('Verification Error')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3">
        <h2>${_('Verification error!')}</h2>

        <p>
            you can now:
            <ul>
                <li><a href="/authentication/resend_verification_request">${_('Resend verification code')}</a></li>
            </ul>


        </p>
    </div>
</div>