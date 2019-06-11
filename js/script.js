var softwarelist = {
    blender: "https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/Blender.png",
    gimp: "https://cdn2.iconfinder.com/data/icons/humano2/128x128/apps/gimp.png",
    krita: "https://img.icons8.com/color/48/000000/krita-squared.png",
    inkscape: "https://cdn3.iconfinder.com/data/icons/humano2/128x128/apps/inkscape.png",
    awesomebump: "https://raw.githubusercontent.com/kmkolasinski/AwesomeBump/Release/Sources/resources/icons/icon.png"
}

var randomNames = ["wilson", "alejandra", "alison", "romero", "peten", "guatemala"]

function hide(key) {
    var artwork = document.getElementsByClassName("art");
    var i = 0;
    console.log(artwork.length)
    showall();
    for (i = 0; i < artwork.length; i++) {
        if (!artwork[i].classList.contains(key)) {
            artwork[i].classList.add("hide");
        }
    }

}

function showall() {
    var artwork = document.getElementsByClassName("art");
    var i = 0;
    for (i = 0; i < artwork.length; i++) {
        artwork[i].classList.remove("hide");
    }
}

function thumbnailer() {
    let url = "https://raw.githubusercontent.com/wilsoft-gt/art/master/data/data.json";

    fetch(url)
        .then(res => res.json())
        .then((out) => {

            for (const x in out["id"]) {
                

                var baseurl = out["id"][x].mainImage
                var imagelst = out["id"][x].extraImages.split(",")
                console.log(baseurl)

                //create the image element
                var thumbnailimage = document.createElement("img");
                thumbnailimage.src = baseurl + "min/"+imagelst[0]+".jpg";
                thumbnailimage.alt = out["id"][x].title;
                var tagsout = out["id"][x].tags.split(",");
                thumbnailimage.classList.add("art",tagsout[0]);
                console.log(tagsout)

                //create the link source
                var alink = document.createElement("a");
                alink.href = "galerydescription.html?image=" + x;
                alink.appendChild(thumbnailimage);

                document.getElementById("artworkcontainer").appendChild(alink);
            }

        })
        .catch(err => {
            throw err;
        });

}

function updateMainImg(url) {
    document.getElementById("mainimg").src = url;    
}


function addinfo() {
    let url = "https://raw.githubusercontent.com/wilsoft-gt/art/master/data/data.json";
    var myParam = location.search.split('image=')[1];
    fetch(url)
        .then(res => res.json())
        .then((out) => {
            console.log(out)

            var baseurl = out["id"][myParam].mainImage
            var imagelst = out["id"][myParam].extraImages.split(",")

            document.getElementById("mainimg").src = baseurl +"fhd/"+ imagelst[0] + ".png";
            /* Define title */
            document.getElementById("title").innerText = out["id"][myParam].title;

            /* define description from json file */
            document.getElementById("descriptionText").innerText = out["id"][myParam].description;

            /* iterate using the leng of items in the software list from json */
            var softwarel = out["id"][myParam].software.split(",")

            for (const x in softwarel) {
                console.log(softwarel)
                /* creting a new img element */
                var insertimg = document.createElement("img");
                /* addng the url of the softwarelist */
                insertimg.src = softwarelist[softwarel[x]];
                /* inserting the necesary classes */
                insertimg.title = softwarel[x];
                insertimg.className = "software";
                /* appending the software logo to the software section */
                document.getElementById("softwarecontainer").appendChild(insertimg)
            }

            var tagslist = out["id"][myParam].tags.split(",");

            for (y in tagslist) {
                /* console.log(y)
                console.log(tagslist[y]) */
                var insertspan = document.createElement("span");
                insertspan.textContent = tagslist[y];
                insertspan.className = "tag";
                document.getElementById("texTags").appendChild(insertspan);
            }

            for (lst in imagelst){
                console.log(baseurl+"fhd"+imagelst[lst]);
                var insertPrev = document.createElement("img");
                insertPrev.alt = imagelst[lst];
                insertPrev.title = imagelst[lst];
                insertPrev.classList.add("preview");
                insertPrev.setAttribute("onclick","updateMainImg('"+ baseurl+ "fhd/"+ imagelst[lst] + ".png"+"')")
                insertPrev.src = baseurl+"min/"+imagelst[lst]+".jpg";
                document.getElementById("otherImgsContainer").appendChild(insertPrev);
            }




        })
        .catch(err => {
            alert("No pudimos encontrar lo que estabas buscando");
            document.getElementById("title").innerText = "Nothing found!";
            document.getElementById("descriptionText").innerText = "Please redefine your search or contact the webmaster to report";
            document.getElementById("mainimg").src = "";
            document.getElementById("mainimg").alt = "Nothing found!";
            throw err;

        });

}

function showprev() {
    var x = event.clientY;
    var ypos = window.innerHeight;
    var porcentaje = (20 * ypos) / 100;
    if (x >= ypos - porcentaje && x <= ypos) {
        document.getElementById("OtherImgs").classList.add("fadeInUp");
        document.getElementById("OtherImgs").classList.remove("fadeOutDown");

    }
    else {
        document.getElementById("OtherImgs").classList.add("fadeOutDown");
        document.getElementById("OtherImgs").classList.remove("fadeInUp");

    }
}
