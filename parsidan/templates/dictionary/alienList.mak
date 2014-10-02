<%inherit file="parsidan.templates.master" />



% if not tg.auth_stack_enabled:
    <script language="JavaScript">
        $(function(){
           $('#words .item').click(function(){
               if(!$(this).find('input').length)
                    $('<span class="input"><input type="text"><span class="fa fa-plus-circle"></span><span>').appendTo($(this));
                    $(this).find('input').slideDown(100);
           });

               $('#words .item input').live('keypress',function (e) {
                var title = $(this).val();
                var div = $(this).parent().parent();

                var item = div.attr('data-rel');
                if (e.which == 13) {
                    alert(item);

                        $.ajax({
                            url: '/translate/addPersian',
                            type: 'post',
                            data: { 'word': title, 'item': item
                            },
                            success: function (data) {

                                if(data.success){
                                    alert('success');
                                    $('<span class="pendingWord">'+ title + '</span>').appendTo(div)
                                    div.find('input').val('');
                                }else{
                                     alert('error adding');

                                }


                                console.log(data);

                            },
                            error: function (xhr, status, error) {
                                alert('error');
                            }
                        });

                    e.preventDefault();
                    return;
                }
            });

        });
    </script>
% endif

% if words:

    <div class="words listStyle1" id="words">
        % for word in words:
            <div class="item" data-rel="${ word.id }"><span class="word">${ word.name }</span></div>
        %endfor
    </div>
% endif