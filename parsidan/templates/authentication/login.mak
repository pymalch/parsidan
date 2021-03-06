<%inherit file="local:templates.master"/>
<%def name="title()">${_('Login Form')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-4 col-md-offset-1">
        ${form.display() | n}
    </div>
</div>
<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-4 col-md-offset-1">
        <hr/>
        <a href="/authentication/recover_password_form">${_('Forget password ?')}</a>
        |
        <a href="/authentication/signup_form">${_('SignUp')}</a>
    </div>
</div>
