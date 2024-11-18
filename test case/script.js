// Basic Three.js Setup for 3D Character Animation
let scene, camera, renderer;
function init3D() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('character'), alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Add a simple box as a placeholder
    let geometry = new THREE.BoxGeometry();
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    let cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    animate();
}

init3D();

// SpeechSynthesis API
function speakText(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}

// Trigger speech on button click
document.querySelector('.hover-button').addEventListener('click', () => {
    speakText('Welcome to the 3D animated website!');
});
