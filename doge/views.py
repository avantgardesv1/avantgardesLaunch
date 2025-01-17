import json
from web3 import Web3

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, ABI

# Create your views here.

@csrf_exempt
def home(request):
    # Authenticated users view their inbox
        '''
        web3 = Web3()
        print(web3)
        
        web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
        

        abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_CRANIUMS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PROV","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"craniumPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"flipSaleState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxCraniumPurchase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintCraniums","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"nof_tokens","type":"uint256"}],"name":"reserveCraniums","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"saleIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
 
        address = web3.toChecksumAddress("0x39Fb7a527164C3D3F39918DE05A6Fe9A6BCb61EB")
        contract = web3.eth.contract(address=address, abi=abi)

        accounts = web3.eth.accounts




        print(contract.functions.setBaseURI("poop").transact({"from" : accounts[0]}))

        print(contract.functions.baseURI().call())

        contract.functions.reserveCraniums(40).transact( {'from': accounts[0]})
        
        print(contract.functions.totalSupply().call())
        '''
        return render(request, "doge/about.html")
        

def about(request):
    return render(request, "doge/about.html")

def join(request):
    if request.method == "GET":
        return render(request, "doge/join.html")

def variations(request):
    if request.method == "GET":

        #################
        ### Just setting up the page
        #################

        previous_selection = "Previous Selection"

        paths = [
            "static/doge/attributes/backgrounds/background_White.png",
            "static/doge/attributes/rick1.png",
            "static/doge/attributes/skins/extras_None.png",
            "static/doge/attributes/eyes/eyes_None.png",
            "static/doge/attributes/bodies/body_None.png",
            "static/doge/attributes/heads/head_None.png",
            "static/doge/attributes/mouths/mouth_None.png"
        ]

        return render(request, "doge/variations.html",
        {"previous_selection" : previous_selection,
        "paths" : paths})

    elif request.method == "POST":

        
        #################
        ###Determining what the attributes are
        #################
        background = str(request.POST["background"]).replace(" ", "_")
        extra = str(request.POST["extra"]).replace(" ", "_")
        eyes = str(request.POST["eyes"]).replace(" ", "_")
        clothes = str(request.POST["clothes"]).replace(" ", "_")
        head = str(request.POST['head']).replace(" ", "_")
        mouth = str(request.POST["mouth"]).replace(" ", "_")

        #These lists determine how much hair the body has
        one = ["Wolverine Hat", "Planet BS", "Dino", "Wax On Wac Off", "Nobody Cares", "Ducks", "None"]
        two = ["King George", "Turds", "Angus Young", "Wildcat", "Santa", "Army", "Wolverine", "Happy Accidents", "Date Mike", "Clark", "Somebody Stop Me", "Sombrero", "Classic Bowler", "Captain", "Watermelon"]
        three = ["Clint Eastwood", "Alright", "Eminem", "Joker", "Tinfoil", "The Best Pirate I Have Ever Seen"]
        four = ["Indiana Jones", "Hulk Hogan"]

        if request.POST['head'] in one:
            body = "rick1"
        elif request.POST['head'] in two:
            body = "rick2"
        elif request.POST['head'] in three:
            body = "rick3"
        elif request.POST['head'] in four:
            body = "rick4"



        #################
        ### Determining what order they should be in
        ################

        glasses = ["Wilder", "Thug Life", "Aviators", "Rocketman", "Wolfie", "Jackass 3d", "What If I Told You"]
        hair = ["Hulk Hogan", "Joker", "Wolverine", "Wax On Wac Off", "Happy Accidents", "Eminem"]
        helmets = ["Wildcat", "Wolverine Hat", "Wolverine", "Joker", "Happy Accidents", "Watermelon", "Angus Young", "Eminem"]
        beards = ["Mutton Chops", "Hunger Games"]


        paths = []

        # This is the lazers order
        if request.POST['eyes'] == "Lazers":
            # This is lazers + a beard and helmet
            if (request.POST['mouth'] in beards and request.POST['head'] in helmets):
                paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
                paths.append(f"static/doge/attributes/{body}.png")
                paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
                paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
                paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
                paths.append(f"static/doge/attributes/heads/head_{head}.png")
                paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
            else:
                paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
                paths.append(f"static/doge/attributes/{body}.png")
                paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
                paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
                paths.append(f"static/doge/attributes/heads/head_{head}.png")
                paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
                paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
        # This is a glasses + hair
        elif (request.POST['eyes'] in glasses) and (request.POST['head'] in hair):
            # This is a glasses + hair + beard + helmet/glasses
            if (request.POST['mouth'] in beards and (request.POST['head'] in helmets or request.POST['eyes'] in glasses)):
                paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
                paths.append(f"static/doge/attributes/{body}.png")
                paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
                paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
                paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
                paths.append(f"static/doge/attributes/heads/head_{head}.png")
                paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
            else:
                paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
                paths.append(f"static/doge/attributes/{body}.png")
                paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
                paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
                paths.append(f"static/doge/attributes/heads/head_{head}.png")
                paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
                paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
        # This is just beard + helmet/glasses
        elif (request.POST['mouth'] in beards and (request.POST['head'] in helmets or request.POST['eyes'] in glasses)):
            paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
            paths.append(f"static/doge/attributes/{body}.png")
            paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
            paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
            paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
            paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
            paths.append(f"static/doge/attributes/heads/head_{head}.png")
        # This is hulk hogan and eyepatch
        elif (request.POST['eyes'] == "Eyepatch" and request.POST['head'] == "Hulk Hogan"):
            paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
            paths.append(f"static/doge/attributes/{body}.png")
            paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
            paths.append(f"static/doge/attributes/eyes/eyes_Eyepatch2.png")
            paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
            paths.append(f"static/doge/attributes/heads/head_{head}.png")
            paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
        # Normal
        else:
            paths.append(f"static/doge/attributes/backgrounds/background_{background}.png")
            paths.append(f"static/doge/attributes/{body}.png")
            paths.append(f"static/doge/attributes/skins/extras_{extra}.png")
            paths.append(f"static/doge/attributes/eyes/eyes_{eyes}.png")
            paths.append(f"static/doge/attributes/bodies/body_{clothes}.png")
            paths.append(f"static/doge/attributes/heads/head_{head}.png")
            paths.append(f"static/doge/attributes/mouths/mouth_{mouth}.png")
        
        
        return render(request, 'doge/variations.html', 
        {'paths': paths, 
        'background': str(request.POST["background"]), 
        'extra' : str(request.POST["extra"]), 
        'eyes' : str(request.POST["eyes"]), 
        'clothes' : str(request.POST["clothes"]), 
        'head' : str(request.POST["head"]),
        'mouth' : str(request.POST["mouth"])
        })

def memes(request):
    if request.method == "GET":
        return render(request, "doge/memes.html")

def cycle(request):
    if request.method == "GET":
        return render(request, "doge/cycle.html")

def atm(request):
    if request.method == "GET":
        return render(request, "doge/atm.html")

def submissions(request):
    if request.method == "GET":
        return render(request, "doge/submissions.html")

def atm_memes(request):
    if request.method == "GET":
        return render(request, "doge/atm_memes.html")
def faqs(request):
    if request.method == "GET":
        return render(request, "doge/faqs.html")
def community(request):
    if request.method == "GET":
        return render(request, "doge/community.html")




def metadata(request, metadata_id):

    metadata_response = "https://youtu.be/dQw4w9WgXcQ"

    if metadata_id < 6969 and metadata_id >= 0:
        web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/bd9a389d10ea4114902f64206071effb"))
        abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"flipSaleState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintAvantGardes","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reserveMemes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reserveOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newProv","type":"string"}],"name":"setProv","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_AVANT_GARDES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPurchase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Prov","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"saleIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
        address = '0x7E4d0E1b36c375d95FB7282593c7d46864C82ca6'
        contract = web3.eth.contract(abi=abi, address=address)

        totalSupply = contract.functions.totalSupply().call()

        if True: #metadata_id < totalSupply:
            print(f"{metadata_id} : post")
            with open('doge/api_list3.json') as json_file:
                metadata_list = json.load(json_file)

            metadata_response = metadata_list[metadata_id]
    
    return JsonResponse(metadata_response, safe=False)


