/**
 * Created by Midoki on 27/05/2017.
 */
function show_hide(a , b , c, d){
              if ($(a).is(':checked')){
                $(b).removeClass("hidden")
                $(c).val("")
                $(c).attr("disabled" , true)
                $(d).attr('required', true);
            }
            else {
                $(d).removeAttr("required")
                $(b).addClass("hidden")
                  $(c).removeAttr("disabled")


}}
show_hide('#id_seance1-is_two' , '.supp1' , '#id_seance1-salle' , '#id_prof_supp1');
show_hide('#id_seance2-is_two' , '.supp2' , '#id_seance2-salle' , '#id_prof_supp2');
show_hide('#id_seance3-is_two' , '.supp3' , '#id_seance3-salle' , '#id_prof_supp3');
show_hide('#id_seance4-is_two' , '.supp4' , '#id_seance4-salle' , '#id_prof_supp4');
show_hide('#id_seance5-is_two' , '.supp5' , '#id_seance5-salle' , '#id_prof_supp5');
show_hide('#id_seance6-is_two' , '.supp6' , '#id_seance6-salle' , '#id_prof_supp6');
show_hide('#id_seance7-is_two' , '.supp7' , '#id_seance7-salle' , '#id_prof_supp7');
show_hide('#id_seance8-is_two' , '.supp8' , '#id_seance8-salle' , '#id_prof_supp8');
show_hide('#id_seance9-is_two' , '.supp9' , '#id_seance9-salle' , '#id_prof_supp9');
show_hide('#id_seance10-is_two' , '.supp10' , '#id_seance10-salle' , '#id_prof_supp10');
show_hide('#id_seance11-is_two' , '.supp11' , '#id_seance11-salle' , '#id_prof_supp11');
show_hide('#id_seance12-is_two' , '.supp12' , '#id_seance12-salle' , '#id_prof_supp12');

$(document).on('change','#id_seance1-is_two',function(){
    show_hide('#id_seance1-is_two' , '.supp1' , '#id_seance1-salle' , '#id_prof_supp1');
        });
$(document).on('change','#id_seance2-is_two',function(){
    show_hide('#id_seance2-is_two' , '.supp2' , '#id_seance2-salle' , '#id_prof_supp2');
        });
$(document).on('change','#id_seance3-is_two',function(){
    show_hide('#id_seance3-is_two' , '.supp3' , '#id_seance3-salle' , '#id_prof_supp3');
        });
$(document).on('change','#id_seance4-is_two',function(){
    show_hide('#id_seance4-is_two' , '.supp4' , '#id_seance4-salle' , '#id_prof_supp4');
        });
$(document).on('change','#id_seance5-is_two',function(){
    show_hide('#id_seance5-is_two' , '.supp5' , '#id_seance5-salle' , '#id_prof_supp5');
        });
$(document).on('change','#id_seance6-is_two',function(){
    show_hide('#id_seance6-is_two' , '.supp6' , '#id_seance6-salle' , '#id_prof_supp6');
        });
$(document).on('change','#id_seance7-is_two',function(){
    show_hide('#id_seance7-is_two' , '.supp7' , '#id_seance7-salle' , '#id_prof_supp7');
        });
$(document).on('change','#id_seance8-is_two',function(){
    show_hide('#id_seance8-is_two' , '.supp8' , '#id_seance8-salle' , '#id_prof_supp8');
        });
$(document).on('change','#id_seance9-is_two',function(){
    show_hide('#id_seance9-is_two' , '.supp9' , '#id_seance9-salle' , '#id_prof_supp9');
        });
$(document).on('change','#id_seance10-is_two',function(){
    show_hide('#id_seance10-is_two' , '.supp10' , '#id_seance10-salle' , '#id_prof_supp10');
        });
$(document).on('change','#id_seance11-is_two',function(){
    show_hide('#id_seance11-is_two' , '.supp11' , '#id_seance11-salle' , '#id_prof_supp11');
        });
$(document).on('change','#id_seance12-is_two',function(){
    show_hide('#id_seance12-is_two' , '.supp12' , '#id_seance12-salle' , '#id_prof_supp12');
        });
