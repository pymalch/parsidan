<%inherit file="local:templates.master"/>
<%def name="title()">${_('Password recovery success')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3">
        <h2>${_('Password recovery success')}</h2>
        <p>
            ${_('Please check your mailbox: %s') % user.email}
        </p>
    </div>
</div>