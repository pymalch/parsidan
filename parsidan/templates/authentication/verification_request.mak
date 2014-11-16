<%inherit file="local:templates.master"/>
<%def name="title()">${_('Signup pending')}</%def>

<div class="row verification-request">
    <div class="col-xs-12 col-sm-12 col-sm-offset-1 col-md-8 col-md-offset-3">
        <h2><span class="glyphicon glyphicon-send" aria-hidden="true"></span> ${_('Signup process started successfully.')}</h2>
        <p>
            ${_('For finalize registration please check your mailbox: %s') % user.email}
        </p>
    </div>
</div>