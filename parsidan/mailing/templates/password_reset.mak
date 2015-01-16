<div style="direction: ${_("css-direction")}; font: 13px Tahoma;">
   <img src="http://${domain}/img/parsidan.jpg" class="center-block" alt="${_('Parsidan')}"/>

    <h2>${_('Your password was changed')}</h2>

    <p>
        ${_('Your new password is:')}
        <br/>
        ${new_password}
    </p>
<br/><br/>
    <p>
        ${_('Please change your password ASAP')}
        <br/>
        <a href="${self.get_url()}" target="_blank">${self.get_url()}</a>

    </p>

    <%def name="get_url()">http://${domain}${action}</%def>
</div>