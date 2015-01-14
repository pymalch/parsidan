<%inherit file="local:templates.master"/>

<%
    col_classes = "col-md-12 "
%>

  <ul class="nav nav-pills">
        <li class="equivalents active"><a href="${tg.url('/contribution/manage/')}">${_('Equivalents')}</a></li>
        <li class="persian "><a href="${tg.url('/contribution/manage/persian')}">${_('Persian words')}</a></li>
        <li class="foreign"><a href="${tg.url('/contribution/manage/foreign')}">${_('Foreign words')}</a></li>
    </ul>

<div class="container contribute-area ${col_classes} manage-words">

    <div class="clearfix"></div>
    % if words:

        % for word in words:
         <div class="col-md-4 col-sm-6 words">
              <span class="word persian box-bordered">${word.persian_word.title}
                  <i class="link glyphicon glyphicon-link"></i></span>

              <span class="word foreign box-bordered">${word.foreign_word.title}</span>
             <i class="remove glyphicon glyphicon-remove"></i>
         </div>
        % endfor

    % endif
</div>




<%def name="scripts()">
    <script type="text/javascript">
        $(document).ready(function () {
            $('#persianInput').contributionEngine({
                onComplete:function(object){
                    this.state.word.$foreignInput().contributionEngine();
                }
            });

        });
    </script>
</%def>