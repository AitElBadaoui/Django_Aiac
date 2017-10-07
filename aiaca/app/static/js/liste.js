/**
 * Created by Midoki on 27/05/2017.
 */

function liste(a ,b , c , d ,e , dd , ee , s  , av , tok){
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
                $(s).val("").attr('disabled', true)
                $(av).val("").attr('disabled', true);
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
            values =[$('#id_seance1-matiere').val() , $('#id_seance2-matiere').val(),$('#id_seance3-matiere').val() , $('#id_seance4-matiere').val() ,$('#id_seance5-matiere').val() , $('#id_seance6-matiere').val() ,$('#id_seance7-matiere').val() , $('#id_seance8-matiere').val() ,$('#id_seance9-matiere').val() , $('#id_seance10-matiere').val() ,$('#id_seance11-matiere').val() , $('#id_seance12-matiere').val()]
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
				data: {csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  , id : $(a).val() , laps :values  , token : tok},
				type: "POST",
				success: function(resultat){
                    $(av).replaceWith(resultat)
    			}
    	});
}}
function listes(a ,b , c , d ,e , dd , ee , s  , av) {
    if ($(a).val().length <= 0 || $(b).text() == "ACTIVITEE PARASCOLAIRE") {
        if ($(b).text() == "ACTIVITEE PARASCOLAIRE") {

            $(c).removeClass("hidden");
        }
        else {
            $(c).addClass("hidden");

        }
        $.ajax({
            url: "/vide/",
            data: "csrfmiddlewaretoken=" + $('input[name=csrfmiddlewaretoken]').val() + "&id=" + $(a).val(),
            type: "POST",
            success: function (resultat) {
                $(d).html(resultat);
                $(dd).multiselect('reload');
                $(e).html(resultat);
                $(ee).multiselect('reload');
            }
        });
        $(s).attr('disabled', true);
        $(av).attr('disabled', true);
    }
    else {

        $(c).addClass("hidden");
        $(d + '> .ms-options-wrap > button:focus, .ms-options-wrap > button').removeAttr('disabled');
        $(d).removeAttr('disabled');
        $(d).css('background-color', '#FFF')
        $(e).css('background-color', '#FFF');
        $(s).removeAttr('disabled');
        $(av).removeAttr('disabled');
    }
};

    listes('#id_seance1-matiere', '#id_seance1-matiere option:selected', '#id_seance1-activite', '#id_seance1-professeur_firstgroup', '#id_seance1-professeur_secondgroup' , '#id_seance1-professeur_firstgroup', 'select[multiple]#id_seance1-professeur_secondgroup' ,  '#id_seance1-salle' , '#id_seance1-avancement');
    listes('#id_seance2-matiere', '#id_seance2-matiere option:selected', '#id_seance2-activite', '#id_seance2-professeur_firstgroup', '#id_seance2-professeur_secondgroup' , 'select[multiple]#id_seance2-professeur_firstgroup', 'select[multiple]#id_seance2-professeur_secondgroup' ,  '#id_seance2-salle' , '#id_seance2-avancement');
    listes('#id_seance3-matiere', '#id_seance3-matiere option:selected', '#id_seance3-activite', '#id_seance3-professeur_firstgroup', '#id_seance3-professeur_secondgroup' , 'select[multiple]#id_seance3-professeur_firstgroup', 'select[multiple]#id_seance3-professeur_secondgroup' ,  '#id_seance3-salle' , '#id_seance3-avancement');
    listes('#id_seance4-matiere', '#id_seance4-matiere option:selected', '#id_seance4-activite', '#id_seance4-professeur_firstgroup', '#id_seance4-professeur_secondgroup' , 'select[multiple]#id_seance4-professeur_firstgroup', 'select[multiple]#id_seance4-professeur_secondgroup' ,  '#id_seance4-salle' , '#id_seance4-avancement');
    listes('#id_seance5-matiere', '#id_seance5-matiere option:selected', '#id_seance5-activite', '#id_seance5-professeur_firstgroup', '#id_seance5-professeur_secondgroup' , 'select[multiple]#id_seance5-professeur_firstgroup', 'select[multiple]#id_seance5-professeur_secondgroup' ,  '#id_seance5-salle' , '#id_seance5-avancement');
    listes('#id_seance6-matiere', '#id_seance6-matiere option:selected', '#id_seance6-activite', '#id_seance6-professeur_firstgroup', '#id_seance6-professeur_secondgroup' , 'select[multiple]#id_seance6-professeur_firstgroup', 'select[multiple]#id_seance6-professeur_secondgroup' ,  '#id_seance6-salle' , '#id_seance6-avancement');
    listes('#id_seance7-matiere', '#id_seance7-matiere option:selected', '#id_seance7-activite', '#id_seance7-professeur_firstgroup', '#id_seance7-professeur_secondgroup' , 'select[multiple]#id_seance7-professeur_firstgroup', 'select[multiple]#id_seance7-professeur_secondgroup' ,  '#id_seance7-salle' , '#id_seance7-avancement');
    listes('#id_seance8-matiere', '#id_seance8-matiere option:selected', '#id_seance8-activite', '#id_seance8-professeur_firstgroup', '#id_seance8-professeur_secondgroup' , 'select[multiple]#id_seance8-professeur_firstgroup', 'select[multiple]#id_seance8-professeur_secondgroup' ,  '#id_seance8-salle' , '#id_seance8-avancement');
    listes('#id_seance9-matiere', '#id_seance9-matiere option:selected', '#id_seance9-activite', '#id_seance9-professeur_firstgroup', '#id_seance9-professeur_secondgroup' , 'select[multiple]#id_seance9-professeur_firstgroup', 'select[multiple]#id_seance9-professeur_secondgroup' ,  '#id_seance9-salle' , '#id_seance9-avancement');
    listes('#id_seance10-matiere', '#id_seance10-matiere option:selected', '#id_seance10-activite', '#id_seance10-professeur_firstgroup', '#id_seance10-professeur_secondgroup' , 'select[multiple]#id_seance10-professeur_firstgroup', 'select[multiple]#id_seance10-professeur_secondgroup' ,  '#id_seance10-salle' , '#id_seance10-avancement');
    listes('#id_seance11-matiere', '#id_seance11-matiere option:selected', '#id_seance11-activite', '#id_seance11-professeur_firstgroup', '#id_seance11-professeur_secondgroup' , 'select[multiple]#id_seance11-professeur_firstgroup', 'select[multiple]#id_seance11-professeur_secondgroup' ,  '#id_seance11-salle' , '#id_seance11-avancement');
    listes('#id_seance12-matiere', '#id_seance12-matiere option:selected', '#id_seance12-activite', '#id_seance12-professeur_firstgroup', '#id_seance12-professeur_secondgroup' , 'select[multiple]#id_seance12-professeur_firstgroup', 'select[multiple]#id_seance12-professeur_secondgroup' ,  '#id_seance12-salle' , '#id_seance12-avancement');

$(document).on('change','#id_seance1-matiere',function() {
    liste('#id_seance1-matiere', '#id_seance1-matiere option:selected', '#id_seance1-activite', '#id_seance1-professeur_firstgroup', '#id_seance1-professeur_secondgroup' , 'select[multiple]#id_seance1-professeur_firstgroup', 'select[multiple]#id_seance1-professeur_secondgroup' ,  '#id_seance1-salle' , '#id_seance1-avancement' , 'seance1-avancement');


});
$(document).on('change','#id_seance2-matiere',function() {
    liste('#id_seance2-matiere', '#id_seance2-matiere option:selected', '#id_seance2-activite', '#id_seance2-professeur_firstgroup', '#id_seance2-professeur_secondgroup' , 'select[multiple]#id_seance2-professeur_firstgroup', 'select[multiple]#id_seance2-professeur_secondgroup' ,  '#id_seance2-salle' , '#id_seance2-avancement' , 'seance2-avancement');

});
$(document).on('change','#id_seance3-matiere',function() {
    liste('#id_seance3-matiere', '#id_seance3-matiere option:selected', '#id_seance3-activite', '#id_seance3-professeur_firstgroup', '#id_seance3-professeur_secondgroup' , 'select[multiple]#id_seance3-professeur_firstgroup', 'select[multiple]#id_seance3-professeur_secondgroup' ,  '#id_seance3-salle' , '#id_seance3-avancement' , 'seance3-avancement');
});
$(document).on('change','#id_seance4-matiere',function() {
    liste('#id_seance4-matiere', '#id_seance4-matiere option:selected', '#id_seance4-activite', '#id_seance4-professeur_firstgroup', '#id_seance4-professeur_secondgroup' , 'select[multiple]#id_seance4-professeur_firstgroup', 'select[multiple]#id_seance4-professeur_secondgroup' ,  '#id_seance4-salle' , '#id_seance4-avancement' , 'seance4-avancement');
});
$(document).on('change','#id_seance5-matiere',function() {
    liste('#id_seance5-matiere', '#id_seance5-matiere option:selected', '#id_seance5-activite', '#id_seance5-professeur_firstgroup', '#id_seance5-professeur_secondgroup' , 'select[multiple]#id_seance5-professeur_firstgroup', 'select[multiple]#id_seance5-professeur_secondgroup' ,  '#id_seance5-salle' , '#id_seance5-avancement' , 'seance5-avancement');
});
$(document).on('change','#id_seance6-matiere',function() {
    liste('#id_seance6-matiere', '#id_seance6-matiere option:selected', '#id_seance6-activite', '#id_seance6-professeur_firstgroup', '#id_seance6-professeur_secondgroup' , 'select[multiple]#id_seance6-professeur_firstgroup', 'select[multiple]#id_seance6-professeur_secondgroup' ,  '#id_seance6-salle' , '#id_seance6-avancement' , 'seance6-avancement');
});
$(document).on('change','#id_seance7-matiere',function() {
    liste('#id_seance7-matiere', '#id_seance7-matiere option:selected', '#id_seance7-activite', '#id_seance7-professeur_firstgroup', '#id_seance7-professeur_secondgroup' , 'select[multiple]#id_seance7-professeur_firstgroup', 'select[multiple]#id_seance7-professeur_secondgroup' ,  '#id_seance7-salle' , '#id_seance7-avancement' , 'seance7-avancement');
});
$(document).on('change','#id_seance8-matiere',function() {
    liste('#id_seance8-matiere', '#id_seance8-matiere option:selected', '#id_seance8-activite', '#id_seance8-professeur_firstgroup', '#id_seance8-professeur_secondgroup' , 'select[multiple]#id_seance8-professeur_firstgroup', 'select[multiple]#id_seance8-professeur_secondgroup' ,  '#id_seance8-salle' , '#id_seance8-avancement' , 'seance8-avancement');
});
$(document).on('change','#id_seance9-matiere',function() {
    liste('#id_seance9-matiere', '#id_seance9-matiere option:selected', '#id_seance9-activite', '#id_seance9-professeur_firstgroup', '#id_seance9-professeur_secondgroup' , 'select[multiple]#id_seance9-professeur_firstgroup', 'select[multiple]#id_seance9-professeur_secondgroup' ,  '#id_seance9-salle' , '#id_seance9-avancement' , 'seance9-avancement');
});
$(document).on('change','#id_seance10-matiere',function() {
    liste('#id_seance10-matiere', '#id_seance10-matiere option:selected', '#id_seance10-activite', '#id_seance10-professeur_firstgroup', '#id_seance10-professeur_secondgroup' , 'select[multiple]#id_seance10-professeur_firstgroup', 'select[multiple]#id_seance10-professeur_secondgroup' ,  '#id_seance10-salle' , '#id_seance10-avancement' , 'seance10-avancement');
});
$(document).on('change','#id_seance11-matiere',function() {
    liste('#id_seance11-matiere', '#id_seance11-matiere option:selected', '#id_seance11-activite', '#id_seance11-professeur_firstgroup', '#id_seance11-professeur_secondgroup' , 'select[multiple]#id_seance11-professeur_firstgroup', 'select[multiple]#id_seance11-professeur_secondgroup' ,  '#id_seance11-salle' , '#id_seance11-avancement' , 'seance11-avancement');
});
$(document).on('change','#id_seance12-matiere',function() {
    liste('#id_seance12-matiere', '#id_seance12-matiere option:selected', '#id_seance12-activite', '#id_seance12-professeur_firstgroup', '#id_seance12-professeur_secondgroup' , 'select[multiple]#id_seance12-professeur_firstgroup', 'select[multiple]#id_seance12-professeur_secondgroup' ,  '#id_seance12-salle' , '#id_seance12-avancement' , 'seance12-avancement');
});
