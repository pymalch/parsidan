<%inherit file="parsidan.templates.master" />




    <script type=text/javascript>
        var word = Array();
  $(function() {

   $('#persianInput').keypress(function (e) {
        var title = $(this).val();
        if (e.which == 13) {

                $.ajax({
                    url: '${tg.url('/dictionary/addPersian')}',
                    type: 'post',
                    data: {
                        'word': title
                    },
                    success: function (data) {

                        console.log(data);

                        if(data==0)

                            alert('${ _('Unexpected error') }');
                        else if(data==2)

                            alert('${ _('Persian word added before') }');

                            else{


                            $('<div class="item" data-rel="'+data+'"><span class="word">' + title + '</span></div>').prependTo('#words');

                        }


                    },
                    error: function (xhr, status, error) {
                        alert('${ _('Unexpected error') }');
                    }
                });
            }
    });


   $('#words .item .word').live('click',function(){
       var item =$(this).parent();
       if(!item.find('input').length){

            $('<span class="input"><input type="text" placeholder="${_('Insert alien equivalent')}"><span class="fa fa-plus"></span><span>').appendTo(item);
            var id=item.attr('data-rel');
                $.ajax({
                    url: '/dictionary/getAlien',
                    type: 'post',
                    data: { 'id': id
                    },
                    success: function (data) {
                       console.log(data);

                        if(data.words.length){
                            $('<div class="section"> </div>').appendTo(item);
                            $.each(data.words,function(k,v){
                                $('<span class="subitem" data-rel="' + v[0] + '"><i class="fa fa-times"></i>' + v[1] + '</span>').appendTo(item.find('.section'));
                            });
                        }else{


                        }




                    },
                    error: function (xhr, status, error) {
                        alert('error');
                    }
                });

       }


       if(!item.hasClass('open')){
           item.find('.input,.section').slideDown(100);
           item.addClass('open');

       }else{
           item.find('.input,.section').slideUp(100);
           item.removeClass('open');
       }



       });


  $('#words .item input').live('keydown',function (e) {
        var title = $(this).val();
        var div = $(this).parent().parent();

        var item = div.attr('data-rel');
        if (e.which == 13) {

                $.ajax({
                    url: '${tg.url('/dictionary/assignAlien')}',
                    type: 'post',
                    data: { 'word': title, 'item': item
                    },
                    success: function (data) {

                        if(data.success){
                            alert('success');
                            $('<span class="subitem" data-rel="' + data.success + '"><i class="fa fa-times"></i>'+ title + '</span>').appendTo(div.find('.section'));
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


  $('.subitem .fa-times').live('click',function(){
       var item =$(this).parent();
            var id=item.attr('data-rel');
            var parentId=item.parent().parent().attr('data-rel');

                $.ajax({
                    url: '${tg.url('/dictionary/removeAlien')}',
                    type: 'post',
                    data: { 'id': id , 'parentId':parentId
                    },
                    success: function (data) {


                        if(data.success==1){
                            item.slideUp(500,function(){ $(this).remove(); });
                        }else{


                        }
                    },
                    error: function (xhr, status, error) {
                        alert('error');
                    }
                });


       });


});
</script>
<div id="dictWrapper">
       <div class="fs1">
         <input id="persianInput"  class="form-control main-persian-input" type="text" placeholder="${ _('Insert persian word') }">
     </div>
</div>
    % if words:
        <div class="words listStyle1" id="words">
            % for word in words:
                 <div class="item" data-rel="${ word.id }"><span class="word">${ word.name }</span></div>
            % endfor
        </div>
  % endif
