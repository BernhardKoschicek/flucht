document.addEventListener("DOMContentLoaded", function(){
    // Enable popovers everywhere
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    const popoverList = popoverTriggerList.map(function(element){
        return new bootstrap.Popover(element, {
            template: '<div class="popover"><div class="popover-arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div><div class="popover-footer"><a class="btn btn-secondary btn-sm close">Close</a></div></div>'
        });
    });
});
// Close popover on button click
document.addEventListener("click", function(e){
    if(e.target && e.target.classList.contains("close")){
        var popover = bootstrap.Popover.getInstance(e.target.closest(".popover"));
        popover.hide();
    }
});

//
// document.addEventListener("DOMContentLoaded", function () {
//     var element = document.getElementById("7424");
//     var geil = getData("7424")
//     var tooltip = new bootstrap.Popover(element, {
//         title: geil['title']
//     });
// });


// const userAction =  (id_) => {
//     var response =  fetch('https://openatlas.orthodoxes-europa.at/api/0.2/entity/' + id_);
//     var json =  response.json(); //extract JSON from the http response
//     return {
//         'title': json['features'][0]['properties']['title'],
//         'description': json['features'][0]['description'] == null ? 'None' : json['features'][0]['description'][0]['value'],
//         'reference': json['features'][0]['links'] == null ? 'None' : json['features'][0]['links'],
//         'geometry_': json['features'][0]['systemClass'] === 'place' ? json['features'][0]['geometry'] : 'None',
//     };
// }

// function getData(id_) {
//     fetch("https://openatlas.orthodoxes-europa.at/api/0.2/entity/" + id_)
//         .then((resp) => resp.json())
//         .then(data => proccessData(data))
//
//         .then(function (json) {
//             return {
//                 'title': json['features'][0]['properties']['title'],
//                 'description': json['features'][0]['description'] == null ? 'None' : json['features'][0]['description'][0]['value'],
//                 'reference': json['features'][0]['links'] == null ? 'None' : json['features'][0]['links'],
//                 'geometry_': json['features'][0]['systemClass'] === 'place' ? json['features'][0]['geometry'] : 'None',
//             };
//
//         })
//         .catch(function (error) {
//             console.log(error);
//         });
// }
//
// function proccessData(json) {
//     console.log(json['features'][0]['properties']['title'])
// }

// async function fetchText(id_) {
//
//     let url = "https://openatlas.orthodoxes-europa.at/api/0.2/entity/" + id_
//     try {
//         let res = await fetch(url);
//         return await res.json()
//     } catch (error) {
//         console.log(error)
//     }
// }
//
// async function getPopoverText(id_) {
//     let json = await fetchText(id_);
//     return {
//         'title': json['features'][0]['properties']['title'],
//         'description': json['features'][0]['description'] == null ? 'None' : json['features'][0]['description'][0]['value'],
//         'reference': json['features'][0]['links'] == null ? 'None' : json['features'][0]['links'],
//         'geometry_': json['features'][0]['systemClass'] === 'place' ? json['features'][0]['geometry'] : 'None',
//     }
// }


