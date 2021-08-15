document.addEventListener('DOMContentLoaded', function() {

    ////////////////////
    ////// The Bottom Information
    ////////////////////



    // initialize
    const tooltipElement = document.querySelector('#contractAddress');
    let bsTooltip = new bootstrap.Tooltip(tooltipElement);

    document.querySelector("#contractAddress").addEventListener('click', () => {
        copyToClipboard("0x7E4d0E1b36c375d95FB7282593c7d46864C82ca6");
        
        // update
        tooltipElement.title = 'Copied';
        bsTooltip.hide()
        bsTooltip = new bootstrap.Tooltip(tooltipElement)
        bsTooltip.show()

        // reset
        setTimeout( () => {
            tooltipElement.title = 'Copy Contract Address';
            bsTooltip.hide()
            bsTooltip = new bootstrap.Tooltip(tooltipElement)
            bsTooltip.show()
        }, 3000)
    })

    // initialize
    const tooltipElement2 = document.querySelector('#email');
    let bsTooltip2 = new bootstrap.Tooltip(tooltipElement2);

    function copyToClipboard(text) {
        var input = document.body.appendChild(document.createElement("input"));
        input.value = text;
        input.focus();
        input.select();
        document.execCommand('copy');
        input.parentNode.removeChild(input);
      }

});