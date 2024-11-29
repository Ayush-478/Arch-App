//30min+

import {
    sendrequest,
    response
} from './server.js';

window.onload = function(){
    document.getElementById('chat_interface').style.display = 'block';
    const cont = document.getElementById('cont');
    const canvas = new fabric.Canvas('canvas', {
        width :cont.clientWidth,
        height :cont.clientHeight,
        backgroundColor : "black"
    })

    canvas.renderAll();
    var rect = new fabric.Rect({
        left: 100,
        top: 100,
        fill: 'red',
        width: 20,
        height: 20,
        angle : 45
    });
    canvas.add(rect);
    const new_app = new app();
    app.set_canvas(canvas);

    const j1 = {
        "order": "add",
        "shape": "Rectangle",
        "name" : "Reactangle101",
        "id": "r101",
        "position": {
            "x": 150,
            "y": 200
        },
        "dimensions": {
            "width": 100,
            "height": 50
        },
        "style": {
            "fillColor": "green",
            "strokeColor": "red",
            "lineWidth": 2
        }
    }
    new_app.order(j1);
}


window.addEventListener('resize', ()=>{ //could be improved
    cont.clientWidth = window.width;
    cont.clientHeight = window.height;
})


//toggle between chat, help, dev
document.getElementById('help').addEventListener('click', ()=>{
    document.getElementById('dev_interface').style.display = 'none';
    document.getElementById('chat_interface').style.display = 'none';
    document.getElementById('help_interface').style.display = 'block';
})

document.getElementById('chatbutton').addEventListener('click', ()=>{
    document.getElementById('dev_interface').style.display = 'none';
    document.getElementById('chat_interface').style.display = 'block';
    document.getElementById('help_interface').style.display = 'none';
})

class app{
    static id_arr = [];
    static canvas = {};
    static objects = {}; //storing all the shapes in form of json

    static set_canvas(canvas){
        app.canvas = canvas;
    }

    order(j){
        switch (j.order){
            case ("add"):
                this.add(j);
                break;
            case ("delete"):
                this.delete(j);
                break;
            case ("edit"):
                this.edit(j);
                break;
        }
    }

    add(j){
        if (app.id_arr.indexOf(j.id) != -1){
            console.log("item already exists");
            return;
        }
        switch (j.shape){
            case ("Rectangle"):
                let rect = new fabric.Rect({
                    width : j.dimensions.width,
                    height : j.dimensions.height,
                    fill : j.style.fillColor,
                    stroke : j.style.strokeColor,
                    left:j.position.x,
                    top : j.position.y,
                    lineWidth : j.style.lineWidth
                });
                let id = j.id;
                app.id_arr.push(id);
                app.objects.id = rect;
                app.canvas.add(rect);
                break;
        }
    }

    edit(j){ //could be improved
        let id = j.id;
        let ind = app.id_arr.indexOf(id);
        if (ind == -1){
            console.log("Object doesn't exist")
            return;
        }
        this.delete(j);
        this.add(j);
    }

    delete(j){
        let id = j.id;
        let ind = app.id_arr.indexOf(id);
        if (ind == -1){
            console.log("Object doesn't exist")
            return;
        }
        app.canvas.remove(app.objects.id);
        delete app.objects.id;
        app.id_arr.splice(ind, 1);
    }
}

//Chat functionality
let chat_area = document.getElementById('chat_area');
document.getElementById('submit').addEventListener('click', () => {
    sendrequest(chat_area.value);
    chat_area.value = "";
});
chat_area.addEventListener('keydown', (e) =>{
    if (e.key == "Enter"){
        sendrequest(chat_area.value)}});
        chat_area.value = "";
