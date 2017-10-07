/**
 * Created by Midoki on 08/05/2017.
 */
function two1(a) {
 if ($(a).is(':checked')) {
                $('#id_prof1').removeClass("professeur")
                $('#id_prof1').addClass("prof_supp")
                $('#id_prof_supp1').addClass("prof_supp")
                $('.supp1').removeClass("hidden")
                 $('#id_salle1').val("")
                $('#id_salle1').attr("disabled" , true)
                $("#id_prof_supp1").attr('required', true);
            }
            else {
                $('#id_prof1').addClass("professeur")
                $('#id_prof1').removeClass("prof_supp")
                $('#id_prof_supp1').removeClass("prof_supp")
                $('#id_prof_supp1').removeAttr("required")
                $('.supp1').addClass("hidden")
                $('#id_salle1').removeAttr("disabled")
            }
}
two1($('#is_two1'))
$(document).on('change','#is_two1',function(){
          two1($(this))
        });
$(document).on('change','#is_two2',function(){
            if ($(this).is(':checked')) {
                $('#id_prof2').removeClass("professeur")
                $('#id_prof2').addClass("prof_supp")
                $('#id_prof_supp2').addClass("prof_supp")
                $('.supp2').removeClass("hidden")
                $('#id_salle2').attr("disabled" , true)
                $("#id_prof_supp2").attr('required', true);
            }
            else{
                $('#id_prof2').addClass("professeur")
                $('#id_prof2').removeClass("prof_supp")
                $('#id_prof_supp2').removeClass("prof_supp")
                $('#id_prof_supp2').removeAttr("required")
                $('.supp2').addClass("hidden")
                $('#id_salle2').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two3',function(){
            if ($(this).is(':checked')) {
                $('#id_prof3').removeClass("professeur")
                $('#id_prof3').addClass("prof_supp")
                $('#id_prof_supp3').addClass("prof_supp")
                $('.supp3').removeClass("hidden")
                $('#id_salle3').attr("disabled" , true)
                $("#id_prof_supp3").attr('required', true);
            }
            else{
                $('#id_prof3').addClass("professeur")
                $('#id_prof3').removeClass("prof_supp")
                $('#id_prof_supp3').removeClass("prof_supp")
                $('#id_prof_supp3').removeAttr("required")
                $('.supp3').addClass("hidden")
                $('#id_salle3').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two4',function(){
            if ($(this).is(':checked')) {
                $('#id_prof4').removeClass("professeur")
                $('#id_prof4').addClass("prof_supp")
                $('#id_prof_supp4').addClass("prof_supp")
                $('.supp4').removeClass("hidden")
                $('#id_salle4').attr("disabled" , true)
                $("#id_prof_supp4").attr('required', true);
            }
            else{
                $('#id_prof4').addClass("professeur")
                $('#id_prof4').removeClass("prof_supp")
                $('#id_prof_supp4').removeClass("prof_supp")
                $('#id_prof_supp4').removeAttr("required")
                $('.supp4').addClass("hidden")
                $('#id_salle4').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two5',function(){
            if ($(this).is(':checked')) {
                $('#id_prof5').removeClass("professeur")
                $('#id_prof5').addClass("prof_supp")
                $('#id_prof_supp5').addClass("prof_supp")
                $('.supp5').removeClass("hidden")
                $('#id_salle5').attr("disabled" , true)
                $("#id_prof_supp5").attr('required', true);
            }
            else{
                $('#id_prof5').addClass("professeur")
                $('#id_prof5').removeClass("prof_supp")
                $('#id_prof_supp5').removeClass("prof_supp")
                $('#id_prof_supp5').removeAttr("required")
                $('.supp5').addClass("hidden")
                $('#id_salle5').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two6',function(){
            if ($(this).is(':checked')) {
                $('#id_prof6').removeClass("professeur")
                $('#id_prof6').addClass("prof_supp")
                $('#id_prof_supp6').addClass("prof_supp")
                $('.supp6').removeClass("hidden")
                $('#id_salle6').attr("disabled" , true)
                $("#id_prof_supp6").attr('required', true);
            }
            else{
                $('#id_prof6').addClass("professeur")
                $('#id_prof6').removeClass("prof_supp")
                $('#id_prof_supp6').removeClass("prof_supp")
                $('#id_prof_supp6').removeAttr("required")
                $('.supp6').addClass("hidden")
                $('#id_salle6').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two7',function(){
            if ($(this).is(':checked')) {
                $('#id_prof7').removeClass("professeur")
                $('#id_prof7').addClass("prof_supp")
                $('#id_prof_supp7').addClass("prof_supp")
                $('.supp7').removeClass("hidden")
                $('#id_salle7').attr("disabled" , true)
                $("#id_prof_supp7").attr('required', true);
            }
            else{
                $('#id_prof7').addClass("professeur")
                $('#id_prof7').removeClass("prof_supp")
                $('#id_prof_supp7').removeClass("prof_supp")
                $('#id_prof_supp7').removeAttr("required")
                $('.supp7').addClass("hidden")
                $('#id_salle7').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two8',function(){
            if ($(this).is(':checked')) {
                $('#id_prof8').removeClass("professeur")
                $('#id_prof8').addClass("prof_supp")
                $('#id_prof_supp8').addClass("prof_supp")
                $('.supp8').removeClass("hidden")
                $('#id_salle8').attr("disabled" , true)
                $("#id_prof_supp8").attr('required', true);
            }
            else{
                $('#id_prof8').addClass("professeur")
                $('#id_prof8').removeClass("prof_supp")
                $('#id_prof_supp8').removeClass("prof_supp")
                $('#id_prof_supp8').removeAttr("required")
                $('.supp8').addClass("hidden")
                $('#id_salle8').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two9',function(){
            if ($(this).is(':checked')) {
                $('#id_prof9').removeClass("professeur")
                $('#id_prof9').addClass("prof_supp")
                $('#id_prof_supp9').addClass("prof_supp")
                $('.supp9').removeClass("hidden")
                $('#id_salle9').attr("disabled" , true)
                $("#id_prof_supp9").attr('required', true);
            }
            else{
                $('#id_prof9').addClass("professeur")
                $('#id_prof9').removeClass("prof_supp")
                $('#id_prof_supp9').removeClass("prof_supp")
                $('#id_prof_supp9').removeAttr("required")
                $('.supp9').addClass("hidden")
                $('#id_salle9').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two10',function(){
            if ($(this).is(':checked')) {
                $('#id_prof10').removeClass("professeur")
                $('#id_prof10').addClass("prof_supp")
                $('#id_prof_supp10').addClass("prof_supp")
                $('.supp10').removeClass("hidden")
                $('#id_salle10').attr("disabled" , true)
                $("#id_prof_supp10").attr('required', true);
            }
            else{
                $('#id_prof10').addClass("professeur")
                $('#id_prof10').removeClass("prof_supp")
                $('#id_prof_supp10').removeClass("prof_supp")
                $('#id_prof_supp10').removeAttr("required")
                $('.supp10').addClass("hidden")
                $('#id_salle10').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two11',function(){
            if ($(this).is(':checked')) {
                $('#id_prof11').removeClass("professeur")
                $('#id_prof11').addClass("prof_supp")
                $('#id_prof_supp11').addClass("prof_supp")
                $('.supp11').removeClass("hidden")
                $('#id_salle11').attr("disabled" , true)
                $("#id_prof_supp11").attr('required', true);
            }
            else{
                $('#id_prof11').addClass("professeur")
                $('#id_prof11').removeClass("prof_supp")
                $('#id_prof_supp11').removeClass("prof_supp")
                $('#id_prof_supp11').removeAttr("required")
                $('.supp11').addClass("hidden")
                $('#id_salle11').removeAttr("disabled")
             }
        });
$(document).on('change','#is_two12',function(){
            if ($(this).is(':checked')) {
                $('#id_prof12').removeClass("professeur")
                $('#id_prof12').addClass("prof_supp")
                $('#id_prof_supp12').addClass("prof_supp")
                $('.supp12').removeClass("hidden")
                $('#id_salle12').attr("disabled" , true)
                $("#id_prof_supp12").attr('required', true);
            }
            else{
                $('#id_prof12').addClass("professeur")
                $('#id_prof12').removeClass("prof_supp")
                $('#id_prof_supp12').removeClass("prof_supp")
                $('#id_prof_supp12').removeAttr("required")
                $('.supp12').addClass("hidden")
                $('#id_salle12').removeAttr("disabled")
             }
        });

   if($('#id_salle1').val().length<=0){
        $('#id_salle1').attr('disabled',true);
   }
    if($('#id_salle2').val().length<=0 ){
        $('#id_salle2').attr('disabled',true);
    }
    if($('#id_salle12').val().length<=0 && ($('#id_matiere12 option:selected').text() == "-LIBRE-")){
        $('#id_salle12').attr('disabled',true);
    }
       if($('#id_salle3').val().length<=0){
        $('#id_salle3').attr('disabled',true);
    }
    if($('#id_salle4').val().length<=0){
        $('#id_salle4').attr('disabled',true);
    }
       if($('#id_salle5').val().length<=0){
        $('#id_salle5').attr('disabled',true);
    }
    if($('#id_salle6').val().length<=0){
        $('#id_salle6').attr('disabled',true);
    }
       if($('#id_salle6').val().length<=0){
        $('#id_salle6').attr('disabled',true);
    }
    if($('#id_salle6').val().length<=0){
        $('#id_salle6').attr('disabled',true);
    }

$(document).on('change','#id_matiere1',function(){
            if($(this).val().length<=0 || $('#id_matiere1 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere1 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){

                    $('.activite1').removeClass("hidden");
                }
                else{
                    $('.activite1').addClass("hidden");

                }
                $.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof1').html(resultat);
        			$('select[multiple]#id_prof1').multiselect('reload');
                    $('#id_prof_supp1').html(resultat);
                    $('select[multiple]#id_prof_supp1').multiselect('reload');
    			}
    	        });
                $('#id_salle1').attr('disabled', true);
            }
            else{

                $('.activite1').addClass("hidden");
                $('#id_prof1 > .ms-options-wrap > button:focus, .ms-options-wrap > button').removeAttr('disabled');
                $('#id_prof_supp1').removeAttr('disabled');
                $('#id_prof1').css('background-color' , '#FFF')
                $('#id_prof_supp1').css('background-color' , '#FFF');
                $('#id_salle1').removeAttr('disabled');
            }
            if($(this).val() > 0 && $('#id_matiere1 option:selected').text() != "ACTIVITEE PARASCOLAIRE" ){

			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof1').html(resultat);
        			$('select[multiple]').multiselect('reload');
                    $('#id_prof_supp1').html(resultat);
                    $('select[multiple]#id_prof_supp1').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere2',function(){
            if($(this).val().length<=0 || $('#id_matiere2 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere2 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite2').removeClass("hidden");

                }
                else{
                    $('.activite2').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof2').html(resultat);
        			$('select[multiple]#id_prof2').multiselect('reload');
                    $('#id_prof_supp2').html(resultat);
                    $('select[multiple]#id_prof_supp2').multiselect('reload');

    			}
    	});
                $('#id_salle2').attr('disabled', true);

            }
            else{
                $('.activite2').addClass("hidden");
                $('#id_prof2').removeAttr('disabled');
                $('#id_prof_supp2').removeAttr('disabled');
                $('#id_prof2').css('background-color' , '#FFF')
                $('#id_prof_supp2').css('background-color' , '#FFF');
                $('#id_salle2').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof2').html(resultat);
        			$('select[multiple]#id_prof2').multiselect('reload');
                    $('#id_prof_supp2').html(resultat);
                    $('select[multiple]#id_prof_supp2').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere3',function(){
            if($(this).val().length<=0 ||  $('#id_matiere3 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere3 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite3').removeClass("hidden");

                }
                else{
                    $('.activite3').addClass("hidden");

                }
                			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof3').html(resultat);
        			$('select[multiple]#id_prof3').multiselect('reload');
                    $('#id_prof_supp3').html(resultat);
                    $('select[multiple]#id_prof_supp3').multiselect('reload');

    			}
    	});
                $('#id_salle3').attr('disabled', true);

            }
            else{
                $('.activite3').addClass("hidden");
                $('#id_prof3').removeAttr('disabled');
                $('#id_prof_supp3').removeAttr('disabled');
                $('#id_prof3').css('background-color' , '#FFF')
                $('#id_prof_supp3').css('background-color' , '#FFF');
                $('#id_salle3').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof3').html(resultat);
        			$('select[multiple]#id_prof3').multiselect('reload');

                    $('#id_prof_supp3').html(resultat);
                    $('select[multiple]#id_prof_supp3').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere4',function(){
            if($(this).val().length<=0 || $('#id_matiere4 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere4 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite4').removeClass("hidden");

                }
                else{
                    $('.activite4').addClass("hidden");

                }
                			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof4').html(resultat);
        			$('select[multiple]#id_prof4').multiselect('reload');
                    $('#id_prof_supp4').html(resultat);
                    $('select[multiple]#id_prof_supp4').multiselect('reload');

    			}
    	});
                $('#id_salle4').attr('disabled', true);

            }
            else{
                $('.activite4').addClass("hidden");
                $('#id_prof4').removeAttr('disabled');
                $('#id_prof_supp4').removeAttr('disabled');
                $('#id_prof4').css('background-color' , '#FFF')
                $('#id_prof_supp4').css('background-color' , '#FFF');
                $('#id_salle4').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof4').html(resultat);
        			$('select[multiple]').multiselect('reload');
                    $('#id_prof_supp4').html(resultat);
                    $('select[multiple]#id_prof_supp4').multiselect('reload');
    			}
    	});}
		});
$(document).on('change','#id_matiere5',function(){
            if($(this).val().length<=0 || $('#id_matiere5 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere5 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite5').removeClass("hidden");

                }
                else{
                    $('.activite5').addClass("hidden");

                }
                			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof5').html(resultat);
        			$('select[multiple]#id_prof5').multiselect('reload');
                    $('#id_prof_supp5').html(resultat);
                    $('select[multiple]#id_prof_supp5').multiselect('reload');

    			}
    	});
                $('#id_salle5').attr('disabled', true);

            }
            else{
                $('.activite5').addClass("hidden");
                $('#id_prof5').removeAttr('disabled');
                $('#id_prof_supp5').removeAttr('disabled');
                $('#id_prof5').css('background-color' , '#FFF')
                $('#id_prof_supp5').css('background-color' , '#FFF');
                $('#id_salle5').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof5').html(resultat);
        			$('select[multiple]').multiselect('reload');
                    $('#id_prof_supp5').html(resultat);
                    $('select[multiple]#id_prof_supp5').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere6',function(){
            if($(this).val().length<=0 || $('#id_matiere6 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere6 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite6').removeClass("hidden");

                }
                else{
                    $('.activite6').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof6').html(resultat);
        			$('select[multiple]#id_prof6').multiselect('reload');
                    $('#id_prof_supp6').html(resultat);
                    $('select[multiple]#id_prof_supp6').multiselect('reload');

    			}
    	});
                $('#id_salle6').attr('disabled', true);

            }
            else{
                $('.activite6').addClass("hidden");
                $('#id_prof6').removeAttr('disabled');
                $('#id_prof_supp6').removeAttr('disabled');
                $('#id_prof6').css('background-color' , '#FFF')
                $('#id_prof_supp6').css('background-color' , '#FFF');
                $('#id_salle6').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof6').html(resultat);
        			$('select[multiple]#id_prof6').multiselect('reload');
                    $('#id_prof_supp6').html(resultat);
                    $('select[multiple]#id_prof_supp6').multiselect('reload');
    			}
    	});}
		});
$(document).on('change','#id_matiere7',function(){
            if($(this).val().length<=0 || $('#id_matiere7 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere7 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite7').removeClass("hidden");

                }
                else{
                    $('.activite7').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof7').html(resultat);
        			$('select[multiple]#id_prof7').multiselect('reload');
                    $('#id_prof_supp7').html(resultat);
                    $('select[multiple]#id_prof_supp7').multiselect('reload');
    			}
    	});
                $('#id_salle7').attr('disabled', true);

            }
            else{
                $('.activite7').addClass("hidden");
                $('#id_prof7').removeAttr('disabled');
                $('#id_prof_supp7').removeAttr('disabled');
                $('#id_prof7').css('background-color' , '#FFF')
                $('#id_prof_supp7').css('background-color' , '#FFF');
                $('#id_salle7').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof7').html(resultat);
        			$('select[multiple]#id_prof7').multiselect('reload');
                    $('#id_prof_supp7').html(resultat);
                    $('select[multiple]#id_prof_supp7').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere8',function(){
            if($(this).val().length<=0 ||$('#id_matiere8 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere8 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite8').removeClass("hidden");

                }
                else{
                    $('.activite8').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof8').html(resultat);
        			$('select[multiple]#id_prof8').multiselect('reload');
                    $('#id_prof_supp8').html(resultat);
                    $('select[multiple]#id_prof_supp8').multiselect('reload');

    			}
    	});
                $('#id_salle8').attr('disabled', true);

            }
            else{
                $('.activite8').addClass("hidden");
                $('#id_prof8').removeAttr('disabled');
                $('#id_prof_supp8').removeAttr('disabled');
                $('#id_prof8').css('background-color' , '#FFF')
                $('#id_prof_supp8').css('background-color' , '#FFF');
                $('#id_salle8').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof8').html(resultat);
        			$('select[multiple]#id_prof8').multiselect('reload');
                    $('#id_prof_supp8').html(resultat);
                    $('select[multiple]#id_prof_supp8').multiselect('reload');
    			}
    	});}
		});
$(document).on('change','#id_matiere9',function(){
    if($(this).val().length<=0 || $('#id_matiere9 option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                if($('#id_matiere option:selected').text() == "ACTIVITEE PARASCOLAIRE"){
                    $('.activite9').removeClass("hidden");

                }
                else{
                    $('.activite9').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof9').html(resultat);
        			$('select[multiple]#id_prof9').multiselect('reload');
                    $('#id_prof_supp9').html(resultat);
                    $('select[multiple]#id_prof_supp9').multiselect('reload');

    			}
    	});
                $('#id_salle9').attr('disabled', true);

            }
            else{
                $('.activite9').addClass("hidden");
                $('#id_prof9').removeAttr('disabled');
                $('#id_prof_supp9').removeAttr('disabled');
                $('#id_prof9').css('background-color' , '#FFF')
                $('#id_prof_supp9').css('background-color' , '#FFF');
                $('#id_salle9').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof9').html(resultat);
        			$('select[multiple]#id_prof9').multiselect('reload');
                    $('#id_prof_supp9').html(resultat);
                    $('select[multiple]#id_prof_supp9').multiselect('reload');
    			}
    	});}
		});
$(document).on('change','#id_matiere10',function(){
            if($(this).val().length<=0 ||  $(this).val() <0){
                if($(this).val() <0){
                    $('.activite10').removeClass("hidden");

                }
                else{
                    $('.activite10').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof10').html(resultat);
        			$('select[multiple]#id_prof10').multiselect('reload');
                    $('#id_prof_supp10').html(resultat);
                    $('select[multiple]#id_prof_supp10').multiselect('reload');

    			}
    	});
                $('#id_salle10').attr('disabled', true);

            }
            else{
                $('.activite10').addClass("hidden");
                $('#id_prof10').removeAttr('disabled');
                $('#id_prof_supp10').removeAttr('disabled');
                $('#id_prof10').css('background-color' , '#FFF')
                $('#id_prof_supp10').css('background-color' , '#FFF');
                $('#id_salle10').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof10').html(resultat);
                    $('select[multiple]#id_prof10').multiselect('reload');

                    $('#id_prof_supp10').html(resultat);
                    $('select[multiple]#id_prof_supp10').multiselect('reload');


    			}
    	});}
		});
$(document).on('change','#id_matiere11',function(){
            if($(this).val().length<=0 ||  $(this).val() <0){
                if($(this).val() <0){
                    $('.activite11').removeClass("hidden");

                }
                else{
                    $('.activite11').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof11').html(resultat);
        			$('select[multiple]#id_prof11').multiselect('reload');
                    $('#id_prof_supp11').html(resultat);
                    $('select[multiple]#id_prof_supp11').multiselect('reload');

    			}
    	});
                $('#id_salle11').attr('disabled', true);

            }
            else{
                $('.activite11').addClass("hidden");
                $('#id_prof11').removeAttr('disabled');
                $('#id_prof_supp11').removeAttr('disabled');
                $('#id_prof11').css('background-color' , '#FFF')
                $('#id_prof_supp11').css('background-color' , '#FFF');
                $('#id_salle11').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof11').html(resultat);
        			$('select[multiple]#id_prof11').multiselect('reload');
                    $('#id_prof_supp11').html(resultat);
                    $('select[multiple]#id_prof_supp11').multiselect('reload');

    			}
    	});}
		});
$(document).on('change','#id_matiere12',function(){
            if($(this).val().length<=0 ||  $(this).val() <0){
                if($(this).val() <0){
                    $('.activite12').removeClass("hidden");

                }
                else{
                    $('.activite12').addClass("hidden");

                }
			$.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof12').html(resultat);
        			$('select[multiple]#id_prof12').multiselect('reload');
                    $('#id_prof_supp12').html(resultat);
                    $('select[multiple]#id_prof_supp12').multiselect('reload');

    			}
    	});
                $('#id_salle12').attr('disabled', true);

            }
            else{
                $('.activite12').addClass("hidden");
                $('#id_prof12').removeAttr('disabled');
                $('#id_prof_supp12').removeAttr('disabled');
                $('#id_prof12').css('background-color' , '#FFF')
                $('#id_prof_supp12').css('background-color' , '#FFF');
                $('#id_salle12').removeAttr('disabled', true);
            }
            if($(this).val() > 0){
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(this).val(),
				type: "POST",
				success: function(resultat){
        			$('#id_prof12').html(resultat);
        			$('select[multiple]#id_prof12').multiselect('reload');
                    $('#id_prof_supp12').html(resultat);
                    $('select[multiple]#id_prof_supp12').multiselect('reload');


    			}
    	});}
		});