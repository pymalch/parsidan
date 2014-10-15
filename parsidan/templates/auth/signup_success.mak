<%inherit file="local:templates.master"/>
<%def name="title()">${_('Sign Up Success')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3">
        <h2>${_('Registration success!')}</h2>
        <p>
            Please check your mailbox(${user.email}).
        </p>
    </div>
</div>