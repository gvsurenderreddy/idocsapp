/**
 * Created by Jales on 23/11/15.
 */
django.jQuery(document).ready(function ($) {
    $('#id_contact_position_0, #id_contact_position_1').attr('readonly', 'readonly');

    $('#id_contact_address, #id_contact_city, #id_contact_state').blur(function (event) {
        /* Act on the event */
        if ($('#id_contact_address').val() != '' && $('#id_contact_city').val() != '' && $('#id_contact_state').val() != '') {
            $('.geoposition-search input').val($('#id_contact_address').val() + ' ' + $('#id_contact_city').val() + ' ' + $('#id_contact_state').val());

            // TRIGGER DO ENTER PARA EXECUTAR A BUSCA
            var e = $.Event("keydown");
            e.which = 50; // # Some key code value
            $(".geoposition-search input").trigger(e);
        }
        ;
    });
});