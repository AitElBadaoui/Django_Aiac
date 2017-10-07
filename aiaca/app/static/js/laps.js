/**
 * Created by Midoki on 28/05/2017.
 */
function liste(a ,b , c , d ,e , dd , ee , s  , av , num){
     if($(a).val().length<=0 || $(b).text() == "ACTIVITEE PARASCOLAIRE"){
                if($(b).text() == "ACTIVITEE PARASCOLAIRE"){

                    $(c).removeClass("hidden");
                }
                else{
                    $(c).addClass("hidden");

                }
                $.ajax({
				url: "/vide/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(a).val(),
				type: "POST",
				success: function(resultat){
        			$(d).html(resultat);
        			$(dd).multiselect('reload');
                    $(e).html(resultat);
                    $(ee).multiselect('reload');
    			}
    	        });
                $(s).attr('disabled', true);
                $(av).attr('disabled', true);
            }
            else{

                $(c).addClass("hidden");
                $(d +  '> .ms-options-wrap > button:focus, .ms-options-wrap > button').removeAttr('disabled');
                $(d).removeAttr('disabled');
                $(d).css('background-color' , '#FFF')
                $(e).css('background-color' , '#FFF');
                $(s).removeAttr('disabled');
                $(av).removeAttr('disabled');
            }
            if($(a).val() > 0 && $(b).text() != "ACTIVITEE PARASCOLAIRE" ){
            values =[$('#id_seance1-matiere').val() , $('#id_seance2-matiere').val(),$('#id_seance3-matiere').val() , $('#id_seance4-matiere').val()]
			$.ajax({
				url: "/getProf/",
				data: "csrfmiddlewaretoken="+$('input[name=csrfmiddlewaretoken]').val()+"&id="+$(a).val(),
				type: "POST",
				success: function(resultat){
        			$(d).html(resultat);
        			$(dd).multiselect('reload');
                    $(e).html(resultat);
                    $(ee).multiselect('reload');

    			}
    	});
            $.ajax({
				url: "/getSeance/",
				data: {csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  , id : $(a).val() , laps :values},
				type: "POST",
				success: function(resultat){
                    $(av).val(resultat)
    			}
    	});
}}

$(document).on('change','#id_seance1-matiere',function() {
    liste('#id_seance1-matiere', '#id_seance1-matiere option:selected', '#id_seance1-activite', '#id_seance1-professeur_firstgroup', '#id_seance1-professeur_secondgroup' , 'select[multiple]#id_seance1-professeur_firstgroup', 'select[multiple]#id_seance1-professeur_secondgroup' ,  '#id_seance1-salle' , '#id_seance1-avancement' , 1);
    $('#id_seance2-matiere').trigger("change");

});
$(document).on('change','#id_seance2-matiere',function() {
    liste('#id_seance1-matiere', '#id_seance1-matiere option:selected', '#id_seance1-activite', '#id_seance1-professeur_firstgroup', '#id_seance1-professeur_secondgroup' , 'select[multiple]#id_seance1-professeur_firstgroup', 'select[multiple]#id_seance1-professeur_secondgroup' ,  '#id_seance1-salle' , '#id_seance1-avancement' , 1);
    $('#id_seance2-matiere').trigger("change");

});
