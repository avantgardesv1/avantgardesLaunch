document.addEventListener('DOMContentLoaded', function() {



    const labels = [
        'Doob&Derb: Space Veggies',
        'GARGAMEL: Tiger Thugs',
        'RRddraft: Drippy Dinos',
      ];
      const data = {
        labels: labels,
        datasets: [{
          label: 'My First dataset',
          backgroundColor: ["#475140", "#1a2e25", "#324731"],
          borderColor: '#c1cdb8',
          data: [6350, 4541, 4287],
        }]
      };
      
      const config = {
        type: 'pie',
        data,
        options: {
            plugins: {
                title: {
                  display: true,
                  text: 'Week 10',
                },
                legend: {
                    display: false
                }
              }
          
          }
      };

  //  === include 'setup' then 'config' above ===

  var myChart = new Chart(
    document.getElementById('myChart'),
    config
  );


    



    
    load_page()

    window.addEventListener('load', function() { // can also use window.addEventListener('load', (event) => {
        
        load_page2()

        
    });


});



function load_page() {
    //Check if Metamask is installed
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');

        // If it is installed.. Check if user is connected
        let web3 = new Web3(Web3.givenProvider)
        web3.eth.getAccounts(function(err, accounts) {
            if (err != null) {
                console.error("An error occurred: "+err);
            }
            // If the user isn't connected.. Show them the preview
            else if (accounts.length == 0) {
                document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
                document.querySelector("#div2").style.display = 'inline-flex';
                document.querySelector("#p1_2").style.display = "none";

            }
            // If the user is connected and a memeber don't show them the preview
            else {
                member()
            }
        });
      }
    //If the user doesn't have metamask.. show the preview
    else {
        document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
        document.querySelector("#div2").style.display = 'inline-flex';
        document.querySelector("#p1_2").style.display = "none";

    }

    ////////////////////
    // CONTRACT CALL TO SEE IF THE USER HAS A MEMBERSHIP
    ///////////////////
    async function member() {
        // Get the accounts
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0]
        //Initiate web3 instance
        let web3 = new Web3(Web3.givenProvider)
        //await web3.eth.getAccounts(console.log);
        //Connect to the contract
        const abi = [{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"flipSaleState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintAvantGardes","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reserveMemes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reserveOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newProv","type":"string"}],"name":"setProv","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_AVANT_GARDES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPurchase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Prov","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"saleIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
        const address = '0x7E4d0E1b36c375d95FB7282593c7d46864C82ca6'
        const contract = new web3.eth.Contract(abi, address)
        // Determine how many tokens our user has
        const tokenBalance = await contract.methods.balanceOf(account).call()

        if (tokenBalance >= 1) {
            document.querySelector("#p1_1").innerHTML = "";
            document.querySelector("#div2").style.display = 'none';
            document.querySelector("#button1").style.display = "none";
            document.querySelector("#p1_2").style.display = "block";

        }
        else {
            document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
            document.querySelector("#div2").style.display = 'inline-flex';
            document.querySelector("#button1").style.display = "block";
            document.querySelector("#p1_2").style.display = "none";

        }

    }



}

function load_page2() {

    /*////////////////////////////
    ///// This is the Show Guide button
    /////////////////////////////////*/
    var count = 0;

    document.querySelector("#button1").addEventListener("click", () => {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)});
        


        if (count % 2 != 0) {
            window.location.reload();
            
        }
        else {
            document.querySelector("#button1").innerHTML = "Hide Guide";
        }

        count++;
        
    })

    document.querySelector("#button2").addEventListener("click", () => {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)});

        for (const tt of tooltipList) {
            tt.show()
        }
    })

    /*//////////////////////
    //// Determing what should be in the profile
    /////////////////////////*/

    const post_div = document.querySelector("#div2_2")
    var height = document.querySelector("#div2_2").clientHeight + 59;

    // Deteting the scrolling
    post_div.addEventListener("scroll", ()=> {
        // ALways be at the top of the scroll
        document.querySelector("#profile-div").scrollTo(0, 0);

        if (isInViewport(document.querySelector("#h2_2_1"))) {
            // This is Bill Yates
            document.querySelector("#profile-name").innerHTML = "Bill Yates";
            document.querySelector("#description").innerHTML = "Bill Gate's long lost eighth cousin. Internet explorer fanatic.";
            document.querySelector("#profile-img").src = "/static/doge/images/0004.png";
            document.querySelector("#profile-meme1-likes").innerHTML = "4865";
            document.querySelector("#profile-meme1").src = "/static/doge/images/explorer.png";
            document.querySelector("#profile-meme2-likes").innerHTML = "8621";
            document.querySelector("#profile-meme2").src = "/static/doge/images/shrek.png"
        }
        else if (isInViewport(document.querySelector("#h2_2_2"))) {
            // This is Crack Sparrow
            document.querySelector("#profile-name").innerHTML = "Crack Sparrow";
            document.querySelector("#description").innerHTML = "Sailing the seven seas since forever.";
            document.querySelector("#profile-img").src = "/static/doge/images/0002.png";
            document.querySelector("#profile-meme1-likes").innerHTML = "23k";
            document.querySelector("#profile-meme1").src = "/static/doge/images/superbad.png";
            document.querySelector("#profile-meme2-likes").innerHTML = "9234";
            document.querySelector("#profile-meme2").src = "/static/doge/images/stepbrothers.png"
        }
        else if (isInViewport(document.querySelector("#h2_2_3"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "BAYC";
            document.querySelector("#description").innerHTML = "The official BAYC Avant-Gardes account. We love Avant-Gardes!!!";
            document.querySelector("#profile-img").src = "/static/doge/images/0003.png";
            document.querySelector("#profile-meme1-likes").innerHTML = "6798";
            document.querySelector("#profile-meme1").src = "/static/doge/images/nft.png";
            document.querySelector("#profile-meme2-likes").innerHTML = "13k";
            document.querySelector("#profile-meme2").src = "/static/doge/images/bernie.png"
        }
    })

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    /*///////////////
    /// Controling the heights of the scrollables
    /////////////////*/

    // Intializing
    var height = document.querySelector("#myChart").clientHeight + 59;
    document.querySelector("#div2_2").style.height = `${height}px`;
    document.querySelector("#profile-div1").style.height = `${height - 67}px`;

    // Updating
    window.addEventListener("resize", function() {
        var height2 = document.querySelector("#myChart").clientHeight + 59;
        document.querySelector("#div2_2").style.height = `${height2}px`;
        document.querySelector("#profile-div1").style.height = `${height2 - 67}px`;

    })
};