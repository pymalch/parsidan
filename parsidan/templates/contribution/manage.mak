<%inherit file="local:templates.master"/>

<%
    col_classes = "col-md-12 "
%>

  <ul class="nav nav-pills">
        <li class="equivalents ${('','active')[type == None]}"><a href="${tg.url('/contribution/manage/')}">${_('Equivalents')}</a></li>
        <li class="persian ${('','active')[type == 'persian']}"><a href="${tg.url('/contribution/manage/persian')}">${_('Persian words')}</a></li>
        <li class="foreign ${('','active')[type == 'foreign']}"><a href="${tg.url('/contribution/manage/foreign')}">${_('Foreign words')}</a></li>
    </ul>

<div class="container contribute-area ${col_classes} manage-words">

    <div class="clearfix"></div>
    % if words:

            % if type == None:
                 % for word in words:
             <div class="col-md-4 col-sm-6 words" id="w_${word.persian_word.id}">
                  <span class="word persian box-bordered">${word.persian_word.title}
                      <i class="link glyphicon glyphicon-link" data-rel="${word.persian_word.id}"></i></span>

                  <span class="word foreign box-bordered">${word.foreign_word.title}</span>

                 <div class="author">${word.user_detail}</div>
                 <i class="remove glyphicon glyphicon-remove"  data-rel="${word.persian_word.id}"></i>
             </div>
            % endfor
        % else:

                 % for word in words:
             <div class="col-md-4 col-sm-6 words"  id="w_${word.id}">
                  <h3 class="word box-bordered">${word.title}
                       </h3>

                  <i class="remove glyphicon glyphicon-remove"  data-rel="${word.id}"></i>
             </div>
            % endfor
        % endif



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