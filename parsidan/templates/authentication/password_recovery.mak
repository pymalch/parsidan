<%inherit file="local:templates.master"/>
<%def name="title()">${_('Recover your password')}</%def>

<div class="row">
    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-4 col-md-offset-1">
        ${form.display() | n}
    </div>
</div>