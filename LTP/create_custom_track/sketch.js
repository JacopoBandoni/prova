function setup() {
  //button to change the color
  change_color_button = createButton('change_cone_color');
  change_color_button.position(0, 0);
  change_color_button.mousePressed(changeColor);
  //button to save
  save_button = createButton('save');
  save_button.position(0 + change_color_button.width, 0);
  save_button.mousePressed(sv)
  
  createCanvas(1000, 1000);
}

let points_yellow = []
let points_green = []
let cur_color = 0 //0 = yellow, 1=green

function draw() {
  background(100);
  
  //color yellow
  fill(color('#EAED11'));
  noStroke();
  points_yellow.forEach((pt, i) => ellipse(pt.x, pt.y, 10, 10));
  
  //color green
  fill(color('#68DF16'));
  noStroke();
  points_green.forEach((pt, i) => ellipse(pt.x, pt.y, 10, 10));
}

function mousePressed() {
  if (cur_color == 0)
    points_yellow.push({x: mouseX, y: mouseY})
  else
    points_green.push({x: mouseX, y: mouseY})
  // prevent default
  return false;
}

function changeColor(){
  cur_color = (cur_color+1) % 2
  // prevent default
  return false;
}

function sv(){
  //creating final result
  const res = {yellow_cones: null, green_cones:null};
  res.yellow_cones = points_yellow;
  res.green_cones = points_green;

  const doc = document.createElement("a");
  const file = new Blob([JSON.stringify(res)], {type: 'text/plain'});
  doc.href = URL.createObjectURL(file);
  doc.download = 'track.json';
  doc.click();
}
