<%inherit file="parsidan.templates.master" />

    <script type=text/javascript>
        var word = Array();
  $(function() {





   $('#fromLangWrapper input').keypress(function (e) {
        var word = $(this).val();
        if (e.which == 13) {
            if (false || 0) {

                return;
            } else {
                $('.messages .loading').slideDown();
                $.ajax({
                    url: '/dictionary/getPersian',
                    type: 'post',
                    data: { 'word': word
                    },
                    success: function (data) {
                       console.log(data);
                        $('.messages .item').slideUp();

                        if(data.words.length){
                            $('<div id="result" class="section"> </div>').appendTo('#dictWrapper');
                            $.each(data.words,function(k,v){
                                $('<span class="item">' + v + '<span class="like"><i class="fa fa-thumbs-up"></i><i class="fa fa-thumbs-down"></i></span></span>').appendTo('#result');
                            });
                        }else{

                            $('.messages .noResult').slideDown();
                            $('.messages .s'+data.status).slideDown();


                        }

                        if(data.relatedWords.length){
                            $('<div id="relatedResult" class="section"> </div>').appendTo('#dictWrapper');
                            $.each(data.relatedWords,function(k,v){
                                $('<span class="item">' + v + '</span>').appendTo('#relatedResult');
                            });
                        }


                    },
                    error: function (xhr, status, error) {
                        alert('${_('Internal server error!')}');
                    },complete:function(){

                        $('.messages .loading').slideUp();
                    }
                });
            }
            e.preventDefault();
            return;
        }
    });

  });




</script>

 <div id="dictWrapper" class="fs1">
     <div id="fromLangWrapper">
         <input type="text" class="form-control mainPersianInput" placeholder="${ _('Please enter non persian word') }" >

         <div class="messages">

             <div class="loading"><img src="img/preloader.gif"> </div>
            <span class="noResult item">${ _('Persian translate for this word did not find!') }</span>
            <span class="wordAdded s1 item"> ${ _('Word stores is database to translate later.') }</span>
            <span class="addedWordBefore s2 item">${ _('Word is already added and is waiting for translation.') }</span>
            <span class="aPersianWord s3 item">${ _('The word you entered is already a persian word!') }</span>
         </div>

     </div>




 </div>
         <div class="join">${ _("You can %(join)s and help us to improve this dictionary.") % {'join': "JOIN US" } } </div>






