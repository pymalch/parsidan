<div style="direction: ${_("css-direction")}; font: 13px Tahoma;">
   <img src="http://${domain}/img/parsidan.jpg" class="center-block" alt="${_('Parsidan')}"/>
    <h2>${_('Parsidan Email verification')}</h2>

    <p>
        ${_('Please click this url to activate your account')}
        <br/>
        <a href="${self.get_url()}" target="_blank">${self.get_url()}</a>

    </p>

    <%def name="get_url()">http://${domain}${action}?user=${user.email}&activation_code=${activation_code}</%def>
</div>