from flask import Flask, send_from_directory

app = Flask(__name__)

# Sirve las imágenes que estén en la misma carpeta que app.py
@app.route('/<path:filename>')
def servir_imagen(filename):
    return send_from_directory('.', filename)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>

<title>MAVIST</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial;
}

body{
    background:#090909;
    color:white;
    display:flex;
}

.sidebar{
    width:220px;
    background:#111;
    height:100vh;
    padding:20px;
}

.logo{
    color:#D4AF37;
    font-size:40px;
    text-align:center;
    margin-bottom:30px;
    font-weight:bold;
}

.category{
    background:#1B1B1B;
    padding:15px;
    margin-bottom:10px;
    border-radius:10px;
    cursor:pointer;
    transition:.3s;
}

.category:hover{
    background:#D4AF37;
    color:black;
}

.content{
    flex:1;
    padding:30px;
}

h1{
    color:#D4AF37;
    margin-bottom:20px;
}

.gallery{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
}

.image{
    width:100%;
    height:250px;
    object-fit:cover;
    border-radius:15px;
    cursor:pointer;
    transition:.3s;
}

.image:hover{
    transform:scale(1.03);
    border:2px solid #D4AF37;
}

.modal{
    display:none;
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,.95);
    justify-content:center;
    align-items:center;
}

.modal img{
    max-width:90%;
    max-height:90%;
    border-radius:20px;
}

</style>

</head>

<body>

<div class="sidebar">

    <div class="logo">
        MAVIST
    </div>

    <div class="category" onclick="mostrar('Anatomía')">
        Anatomía
    </div>

    <div class="category" onclick="mostrar('Poses')">
        Poses
    </div>

    <div class="category" onclick="mostrar('Animales')">
        Animales
    </div>

    <div class="category" onclick="mostrar('Naturaleza')">
        Naturaleza
    </div>

    <div class="category" onclick="mostrar('Arquitectura')">
            Arquitectura
    </div>

    <div class="category" onclick="mostrar('Iluminacion')">
                Iluminacion
    </div>

    <div class="category" onclick="mostrar('Perspectiva')">
                    Perspectiva
    </div>

    <div class="category" onclick="mostrar('Vehículos')">
                    Vehículos
    </div>

    <div class="category" onclick="mostrar('Colores')">
                    Colores
    </div>

    <div class="category" onclick="mostrar('Animacion')">
                    Animacion
    </div>

</div>

<div class="content">

    <h1 id="titulo">Anatomía</h1>

    <div class="gallery" id="galeria"></div>

</div>

<div class="modal" id="modal" onclick="cerrar()">
    <img id="imagenGrande">
</div>

<script>

const referencias = {

    "Anatomía":[
        "/Anatomia/anatomia1.jpg",
        "/Anatomia/anatomia2.jpg",
        "/Anatomia/anatomia3.jpg",
        "/Anatomia/anatomia4.jpg",
        "/Anatomia/anatomia5.jpg",
        "/Anatomia/anatomia6.jpg"
    ],

    "Poses":[
        "/Poses/poses1.jpg",
        "/Poses/poses2.jpg",
        "/Poses/poses3.jpg",
        "/Poses/poses4.jpg",
        "/Poses/poses5.jpg",
        "/Poses/poses6.jpg"
    ],

    "Animales":[
        "/Animales/animales1.jpg",
        "/Animales/animales2.jpg",
        "/Animales/animales3.jpg",
        "/Animales/animales4.jpg",
        "/Animales/animales5.jpg",
        "/Animales/animales6.jpg"
    ],

    "Naturaleza":[
        "/Naturaleza/naturaleza1.jpg",
        "/Naturaleza/naturaleza2.jpg",
        "/Naturaleza/naturaleza3.jpg",
        "/Naturaleza/naturaleza4.jpg",
        "/Naturaleza/naturaleza5.jpg",
        "/Naturaleza/naturaleza6.jpg"
    ],

    "Arquitectura":[
            "/Arquitectura/arquitectura1.jpg",
            "/Arquitectura/arquitectura2.jpg",
            "/Arquitectura/arquitectura3.jpg",
            "/Arquitectura/arquitectura4.jpg",
            "/Arquitectura/arquitectura5.jpg",
            "/Arquitectura/arquitectura6.jpg"
    ],

    "Iluminacion":[
            "/Iluminacion/iluminacion1.jpg",
            "/Iluminacion/iluminacion2.jpg",
            "/Iluminacion/iluminacion3.jpg",
            "/Iluminacion/iluminacion4.jpg",
            "/Iluminacion/iluminacion5.jpg",
            "/Iluminacion/iluminacion6.jpg"
    ],

    "Perspectiva":[
            "/Perspectiva/perspectiva1.jpg",
            "/Perspectiva/perspectiva2.jpg",
            "/Perspectiva/perspectiva3.jpg",
            "/Perspectiva/perspectiva4.jpg",
            "/Perspectiva/perspectiva5.jpg",
            "/Perspectiva/perspectiva6.jpg"
    ],

    "Vehículos":[
            "/Vehiculos/vehiculos1.jpg",
            "/Vehiculos/vehiculos2.jpg",
            "/Vehiculos/vehiculos3.jpg",
            "/Vehiculos/vehiculos4.jpg",
            "/Vehiculos/vehiculos5.jpg",
            "/Vehiculos/vehiculos6.jpg"
    ],

    "Colores":[
            "/Colores/colores1.jpg",
            "/Colores/colores2.jpg",
            "/Colores/colores3.jpg",
            "/Colores/colores4.jpg",
            "/Colores/colores5.jpg",
            "/Colores/colores6.jpg"
    ],

    "Animacion":[
            "/Animacion/animacion1.jpg",
            "/Animacion/animacion2.jpg",
            "/Animacion/animacion3.jpg",
            "/Animacion/animacion4.jpg",
            "/Animacion/animacion5.jpg",
            "/Animacion/animacion6.jpg"
    ],

};

function mostrar(nombre){

    document.getElementById("titulo").innerText = nombre;

    let html = "";

    referencias[nombre].forEach((item)=>{

        html += `
            <img
                src="${item}"
                class="image"
                onclick="abrir('${item}')"
            >
        `;

    });

    document.getElementById("galeria").innerHTML = html;
}

function abrir(imagen){

    document.getElementById("modal").style.display =
        "flex";

    document.getElementById("imagenGrande").src =
        imagen;
}

function cerrar(){

    document.getElementById("modal").style.display =
        "none";
}

mostrar("Anatomía");

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=False,
    use_reloader=False
)